# The Civic Weave — vectorized settlement identity + generative cast (v1 proposal)

**Status:** PROPOSAL — 2026-06-23. Intensifies settlement + NPC richness; resolves the NERS-audit findings S0 (flat stat-bag), S5 (linear NPC tick), S6 (hand-authored content won't scale to 37 settlements) in one model.
**Binds to (does not replace):** the Armature (`Conviction × Personality × Project × Scar → Agency/Intent/Mechanism → Concerns`), the 7-Conviction axis matrix (opposing pole-pairs), faction ethics frames (Crown=Virtue Ethics … Niflhel=Amoral Consequentialism; α/β conduct-weighting), Knot/resonance, the ambition engine (`governance_play_redesign §3`), the Einhir caste/TS gradient + the Forgetting, and the Settlement registry (`registry.py`).

---

## 0. The brief, decoded

A settlement is not a handful of scalars; it is a **vector across many civic-identity domains, each a continuum** (never a binary). Threaded through that stack is a **noisy throughline** — a single "civic strand" the domains *mostly* express but never *purely*: it is **frayed**, pulled toward one pole or re-woven toward another by a **cast of characters** whose community role is **generated** from a trait stack (ethics / resonances / virtues / ambitions / conviction), **weighted randomly**, then **unified for coherency** by projecting them back through the domain stack. The settlement's identity *is* the running tension between its strand and its fray, and the cast is the hand that frays or weaves.

This replaces "Goldenfurt is a Town with Prosperity 3 / Defense 1 / Order 2" with "Goldenfurt is a *Hierarchy-Orthodox breadbasket strand, frayed hard along its economic-governance, caste, and confessional seams toward Southern leveling-heterodoxy* — and here is the cast pulling each seam."

---

## 0.1 The high-level shape — the four-faction field (and why it is scale-coherent)

The apex framework — the "shape at a high level" that conditions every shape below it — is the peninsula's **four-faction field**, and its structure is **asymmetric**. The asymmetry is the point.

**THREE geographic factions tile the map by ethnicity / caste / territory (exogenous ownership):**
- **Crown / Valorsmark** — Solmundic-Latinate, orthodox, agrarian — the northern **Hierarchy** pole.
- **Hafenmark** — Hanseatic-commercial, oligarchic-parliamentary (Gransol) — the **mercantile** pole.
- **Varfell** — Old-Einhir / Norse, kin/martial, southern (Vaynard is himself southern Einhir) — the **Leveling/heterodox** pole.

These three **partition geography.** A settlement's duchy is *given* (Layer 0); it sets the settlement's ethnic/caste/governance priors.

**ONE confessional faction overlays the map by piety (endogenous valence):**
- **Church / Himmelenger** — its hold on a settlement is **not** a geographic conquest but the **accumulation of piety, and piety is a function of the settlement's own demographics** (caste D6, social-org D5, confessional D7). The Church is therefore **the only faction whose territorial position is *derived from the civic-weave itself*** — it grows where the demographics make it grow (the Geneva / Papal-States vacuum-fill pattern), **cross-cutting all three duchies.**

So the field has **two orthogonal partitions: geography (3 factions, given) × piety (Church, derived).** Every settlement sits at the intersection — it has a **duchy** (exogenous) *and* a **Church-valence** (endogenous), and the tension between them **is** the dual-authority engine (§3) lifted to the faction scale.

**The scale-coherent chain.** This apex shape is **self-similar** — the same field-logic conditions, and aggregates from, every scale:

```
peninsula  (4-faction field)
  ↓ conditions          faction blocs            (the coalesced graph, §6)
  ↓ conditions          settlement Strand + domains   (§0.5, §1–2)
  ↓ conditions          which guilds/orgs hold footholds + their stance  (meso-layer)
  ↓ conditions          the generated character cast  (§3)
  ↑ composes      …and bottom-up the reverse: characters → org-thrusts →
                   settlement-Thrusts → faction-blocs → the peninsula field.
```

Top-down **conditions**; bottom-up **composes**; the link is coherent at every rung because **the same tensions recur at each scale** — `Hierarchy ↔ Leveling` (geography/caste) **×** `Orthodox ↔ Heterodox` (piety) — conditioned by the scale above and expressed by the scale below.

**The meso-layer — associations / guilds / organizations — is the connective tissue the chain runs through, and it is *cross-settlement*.** A Guild, the Löwenritter, the RM, and the Church are each a **Thrust that spans many settlements** — a node-*set* / hyperedge in the coalesced graph, not a single node. The Church is the exemplar: a cross-cutting bloc present in every settlement whose demographics support it. So the graph (§6) is **multi-scale** — settlement-nodes wired by geography, **org-hyperedges** wired by membership/piety, coalescing together into one field.

---

## 0.5 Grounding — geography and faction come FIRST

Nothing in §1–§5 is generated freely. Every settlement is grounded, first and foremost, in two **immovable, canon-given** facts that are never sampled: its **geographic location** and its **initial faction belonging**. These are **Layer 0** — the ground truth that ripples down and *conditions* everything below, so the world is coherent rather than 37 independent dice rolls.

**Layer 0 — immovable ground truth (given, never generated):**
- **Geography:** latitude (the N→S Einhir caste cline), terrain (mountain / plain / coast / fjord / forest), Thread Proximity, Forgetting Proximity (southern maritime boundary + Askeheim), the march-adjacency graph, water/ford/port (trade affordance), Calamity-adjacency.
- **Faction belonging:** the initial owner (Crown / Church / Hafenmark / Varfell / …), the **duchy** (Valorsmark / Hafenmark / Varfell), and special-case status (Himmelenger city-state, Schoenland foreign, Askeheim wilderness).

**Layer 1 — conditioned priors.** Each domain's `(position, grip)` is a **prior computed from Layer 0**, not a free parameter:

| Domain | conditioned by (geography ⊕ faction) |
|--------|--------------------------------------|
| D1 econ output | terrain — mountain→extractive · plain→agrarian · ford/coast→mercantile |
| D2 econ governance | faction culture — Crown→monopoly · Hafenmark→guild/market — ⊕ trade affordance |
| D3/D4 political | faction governance culture — Crown autocratic · Hafenmark oligarchic-parliamentary (Gransol) · Varfell martial-kin — ⊕ caste |
| D5 social org | **duchy** — Valorsmark estate · Hafenmark corporate · Varfell kin/clan |
| D6 caste | **latitude directly** — the gradient *is* geographic (N rigid → S broken) |
| D7 confessional | Church-proximity (distance to Himmelenger, CI) ⊕ latitude |
| D8 mnemonic | Forgetting Proximity ⊕ Thread Proximity |
| D9 martial | frontier / chokepoint / Calamity-gate vs interior |
| D10 cosmopolitan | adjacency degree ⊕ port ⊕ foreign-edge (Schoenland) |

The stochastic generation (§3) then samples **within** these priors — the top-down constraints bound the tail, so identity stays believable for the place.

**Layer 2 — ripple for world-coherence.** Geographic fields (caste, Forgetting, Thread) vary **smoothly** by location, so adjacent settlements share D6/D8 *unless a real geographic boundary intervenes* — and where there **is** a discontinuity, it is a **designed fault line**, not noise. The **duchy is a regional prior** between world and settlement (Hafenmark band = commercial/oligarchic · Varfell band = Norse/kin/martial · Valorsmark band = Crown/orthodox/agrarian). This is the "ripple through and guide for a coherent world."

**Order of operations:** `Geography + Faction (given)` → `conditioned domain priors (L1)` → `smoothed for coherence (L2)` → `per-settlement Strand + generated cast (§1–§4)` → `node thrust + the coalesced graph (§6)`.

---

## 1. The Domain Stack

Each settlement carries a vector over **civic-identity domains** — **seeded by the Layer-1 priors above, not free**. Each domain `d` is a **continuum** between two poles, with:
- **position** `p_d ∈ [−1, +1]` — where the settlement sits on the domain's own axis,
- **grip** `g_d ∈ [0, 1]` — how *pervasively* the domain binds identity (a high-grip domain dominates the settlement's character; a low-grip one is loose, contested, or vestigial).

Each domain also carries a **master-alignment** `a_d(p_d) ∈ [−1,+1]` — its projection onto the settlement's spine axis (§2), where **− = Hierarchy/Orthodoxy** and **+ = Leveling/Heterodoxy** (Valoria's central political tension: Crown–Church–Northern-caste establishment ↔ Einhir–RM–Southern leveling).

| # | Domain | − pole · · · + pole | canon anchor |
|---|--------|---------------------|--------------|
| D1 | **Economic output / bias** | Extractive (raw/mine) · Productive (agrarian/artisan) · Mercantile (trade/rentier) | settlement Prosperity + `stype` + `economic_base` |
| D2 | **Economic governance mode** | Crown-monopoly · Guild-corporate · Free-market · Commons/communal | `subnational` Guild/Crown footholds |
| D3 | **Political input / bias** | Quietist/deferential · Consultative · Contestatory/insurgent | L/PS (§1.8) + RM presence |
| D4 | **Political governance mode** | Autocratic · Oligarchic/council · Assembly/communal · (Theocratic cross-axis) | governor + dual-authority (§3) + Church-Governor |
| D5 | **Demographic / social organization** | Kin/clan · Estate/corporate · Class · Atomized/civic | Einhir kinship ↔ Hanseatic corporate |
| D6 | **Caste pervasiveness (Einhir)** | Caste-rigid (Northern, Church-enforced, Forgetting-suppressed, low-TS) · fluid (Central) · broken/anti-caste (Southern, high-TS, Forgetting-resistant) | Einhir caste / TS gradient; Forgetting-as-enforcement |
| D7 | **Confessional texture** | Orthodox-pious (Church/PT) · syncretic · heterodox/old-rite (RM/Einhir revival) | PT/CI + RM cultural presence |
| D8 | **Mnemonic / temporal orientation** | Forgetting-suppressed (no past) · living-memory · ancestral-haunted (high RS / Thread Proximity) | the Forgetting + Thread Proximity |
| D9 | **Martial posture** | Civilian/defenseless · militia/levy · garrison/martial-caste (Löwenritter) | Defense + garrison + Löwenritter |
| D10 | **Cosmopolitanism** | Insular/parochial · connected · cosmopolitan/foreign-mixed | adjacency degree + Port + Schoenland trade |

*(D1–D6 are the brief's named domains; D7–D10 are the invited "other civic-identity domains that resist binary." The count is an owner ruling — the model is domain-agnostic.)*

**Grip is the texture knob the flat model lacked.** A Cathedral-city runs D7 (confessional) at grip ~1.0; a free-port runs D2/D10 at high grip and D6 (caste) near 0. The *same* position on a domain means different things at different grips — a caste-rigid position at grip 0.2 is vestigial; at grip 0.9 it is the air people breathe (Northern Einhir under the Forgetting).

---

## 2. The Strand — the noisy throughline

The settlement's identity is **not** the flat profile of D1…D10 (that would be ten unrelated dials). It is a **latent throughline** — the spine the domains mostly project onto, plus the deviations that fray it.

**Spine axis (canon-anchored):** Hierarchy-Orthodoxy `(−)` ↔ Leveling-Heterodoxy `(+)`. *(Alternative, per-settlement: derive the spine as the settlement's dominant Conviction-pair tension — e.g. Order↔Autonomy or Continuity↔Equity from the 7-Conviction axis matrix. Owner ruling; the math is identical.)*

```
Strand        s  = Σ_d g_d · a_d(p_d) / Σ_d g_d          # grip-weighted spine projection
Fray (domain) φ_d = a_d(p_d) − s                          # each domain's deviation from the strand
Coherency     C  = 1 − Σ_d g_d·|φ_d| / Σ_d g_d           # 1 = univocal/legible · low = contradictory powder-keg
```

- `s` is the settlement's **civic temperament**: e.g. `s = −0.35` → "a Crown-orthodox Hierarchy town."
- `C` is **how pure the strand is.** `C → 1`: a settlement that means one thing in every domain (stable, legible, *dull*). Low `C`: a settlement at war with itself across domains (alive, dangerous, *dramatic*). **The design wants most settlements mid-`C` — a clear strand, conspicuously frayed.** A pure settlement is a problem (no internal engine); a fully-frayed one is a crisis.
- `φ_d` is **where the settlement contradicts itself.** The domains with the largest `|φ_d|` are the **active seams** — and they are exactly where the event deck should draw (§4). The strand is *noisy by construction*: it is the common strand, and every domain frays from it, and **the fray is the drama.**

This is the brief's "common strand … not pure and univocal, but frayed and pulled in tension or weaved again."

---

## 3. The Cast — generated, as fray/weave agents

NPCs are **generated** from a trait stack, **projected** onto the domain stack to *derive* their community role, and each then applies a **fray** or **weave** force to specific domains. The Armature is the engine; this adds the settlement-projection layer.

### 3.1 The trait stack (the brief's "ethics / resonances / virtues / ambitions" — + conviction)

| Trait | Canon binding | What it sets |
|-------|---------------|--------------|
| **Conviction** | the 7-Conviction axis matrix (Faith/Reason/Order/Autonomy/Equity/Continuity/…, opposing pairs) — the primary Armature axis | the core drive; which *pole* of which domains the NPC instinctively pulls toward |
| **Ethic** | faction meta-ethical frame + α/β (Crown=Virtue/principled · Varfell=Consequentialist · Niflhel=Amoral-Consequentialist; public↔covert) | the *register and legitimacy* of how they pull — open principled pressure vs covert expedient |
| **Virtue** | cardinal-virtue orientation (Temperance/Justice/Courage/Prudence/Faith/Fortitude — cf. the Himmelenger Cardinals) | the *quality* they embody or fail; colours their role's tone and their Conviction-Scar fault line |
| **Resonance** | Knot emotional resonance + History/temporal resonance + resonant style (Evidence/Authority/Emotion/Kinship) | **force magnitude** — high resonance = a keystone connector who moves a domain a lot; low = an isolate. Style = the channel they pull through |
| **Ambition** | the Project/Concern engine (`governance_play_redesign §3`) | **target + direction** — which domain(s) they are actively trying to move, and toward which pole |

### 3.2 Generation — weighted-random, *biased by the domain stack*

For each NPC slot, sample the trait-vector with probability **weighted by the settlement's domain-vector**: a caste-rigid, pious, high-grip town biases draws toward Faith-conviction / Virtue-ethic / Temperance-virtue / Strand-conforming ambition. **But the draw is stochastic, not deterministic** — so the town *also* produces outliers (a Reason-conviction, Justice-virtue dissident born under the orthodoxy). **The conformists become weave agents; the outliers become fray agents.** This is the crux: a single stochastic generator yields *both* the settlement's defenders and its dissidents, in believable proportion, because identity-biased sampling with a fat tail is how real communities reproduce themselves *and* breed their own opposition.

### 3.3 Projection — trait-vector → **role** (derived, never assigned)

Project the NPC onto the domain stack. Their **role is the function they occupy in the settlement's domain-tensions**:

```
role(npc)   = the seam(s) they sit on  ×  the pole they pull toward  ×  resonance magnitude
force_d(npc)= direction(Conviction, Virtue, d) · ambition_target(d) · resonance · ethic_register(d)
```

A high-resonance, Reason+Equity, Justice-virtue, principled NPC dropped into a caste-rigid town does not get *assigned* "Magistrate" — "the magistrate who frays the political and caste seams toward leveling" **falls out** of (their traits × the town's position). Change the town and the *same traits* yield a different role (in a free-port, that NPC is a reform-minded guild arbiter, not a caste-breaker).

### 3.4 Coherency unification — "weighted randomly **then** unified"

After sampling K NPCs, run the Armature's Meta-Armature reconciliation as a **two-pass** generator:
1. **Seam coverage.** Every high-`|φ_d|` seam must have ≥1 **weave** and ≥1 **fray** agent — otherwise the tension is dead. Gaps are filled by re-rolling a slot's *ambition target* (cheap) before re-rolling the whole NPC.
2. **Aggregate-Strand match.** The cast's resonance-weighted mean pull must reproduce the settlement's seed Strand **within a tolerance band** — i.e. the cast *collectively expresses the settlement*, with a deliberate residual of dissent (the fray) preserved. Too-pure (all weave) → inject a dissident; too-chaotic → flag a powder-keg (a valid, dramatic state).

Outliers are **kept** — they are the drama. Only the *distribution* is balanced. That is the brief's "weighted randomly then unified for coherency through the stack of domains."

---

## 4. The runtime weave (the churn, generalized)

Each season:
1. **Cast acts.** Each NPC applies `force_d(npc)` to its target domains; `p_d` drifts by the net force. (This is the S5 ambition tick, generalized: an NPC "advancing its ambition" *is* it pulling a seam.)
2. **Strand re-computes.** `s`, `C`, and the fray vector `φ` update. A settlement can slowly **cross the spine** — a Crown-orthodox breadbasket, frayed season after season by a Southern-Einhir cast + a tolerant player, drifts `s` from `−0.35` toward `+`, and at the crossing its **whole profile, cast-generation bias, and deck re-key** — emergent settlement *evolution*, the thing the NERS audit said the genre's best deliver and Valoria lacked.
3. **Deck draws from the seams.** Cards are weighted by `|φ_d|` — the active tensions *are* the event sources. (This replaces hand-authored per-card triggers with domain-tension-derived ones; see §6.)
4. **Player governance re-weaves or frays.** Every governance verb is a fray/weave force on specific domains: `Keep Order: Clergy` weaves D7 toward orthodoxy (−); `Treat` with the Guild frays D2 toward corporate (+); a `Hold Court` ruling re-weaves D3/D6. **The player-governor is the single largest weave/fray agent** — governing *is* deciding which seams to pull.

---

## 5. Goldenfurt, **derived** (proof the model reproduces the hand-authored slice)

Seed domain-vector for S-006 Goldenfurt (Crown breadbasket on a toll-ford, Southern-Einhir-descended hamlets):

| Domain | position | grip | master-align `a_d` | note |
|--------|:-------:|:----:|:----:|------|
| D1 econ output | Productive-agrarian | 0.6 | −0.2 | breadbasket, traditional |
| **D2 econ governance** | Crown-monopoly⇄Guild | 0.5 | **+0.1 (high fray)** | ford toll contested (Orsk vs Crown) |
| D3 political input | Quietist | 0.5 | −0.4 | deferential, RM undercurrent |
| D4 political mode | Autocratic+chapel | 0.7 | −0.6 | Crown governor, Church-leaning |
| D5 social org | Kin/clan (hamlets) | 0.5 | −0.3 | rural kinship |
| **D6 caste** | rigid(town)⇄broken(hamlets) | 0.6 | **+0.0 (high fray)** | Northern town vs Southern hamlets (Greta) |
| **D7 confessional** | Orthodox⇄old-rite | 0.6 | **−0.1 (high fray)** | chapel/Wessel vs RM circle/Greta |
| D8 mnemonic | suppressed⇄circle | 0.3 | +0.0 | the stone circle pocket |
| D9 martial | militia | 0.3 | 0.0 | Defense 1, no garrison |
| D10 cosmopolitan | connected (ford) | 0.4 | +0.2 | trade + smuggling |

**Strand `s ≈ −0.35`** (a Crown-orthodox Hierarchy town), **but low `C`** — the big fray seams are **D2 (economic governance), D6 (caste), D7 (confessional)**, all straining toward the Leveling/Southern pole. *That is the slice's central tension, now read off the vector instead of hand-authored.*

The six NPCs **fall out of generation** as the agents on those seams:

| NPC | sampled traits (biased + outlier) | derived role | pull |
|-----|-----------------------------------|--------------|------|
| **Konrad** | Order-conviction · Virtue-ethic(Crown) · high resonance | Crown bailiff / strand-keeper | **weave** D3/D4 → − |
| **Wessel** | Faith · Temperance · Virtue · high resonance | curate / orthodoxy-deepener (Geneva trap) | **weave** D7/D6 → − |
| **Orsk** | Reason+Ambition · Prudence · Consequentialist · mid res | grain-factor / corporatiser | **fray** D2 → + |
| **Hedda** | Reason+Equity · Justice · Virtue(principled) · **high res outlier** | magistrate / leveler | **fray** D3/D6 → + |
| **Greta** | Autonomy+Continuity · Faith-in-old-rite · principled · covert kin-resonance | RM elder / heterodox root | **fray** D6/D7/D8 → + |
| **Tomas** | Autonomy · Courage · Amoral-Consequentialist · covert low-res | smuggler / commons-fixer | **fray** D2/D8 → + |

Coverage check passes: every high-fray seam has a weave **and** a fray agent (**D2**: Crown/Konrad weave, Orsk+Tomas fray · **D6**: Wessel weave, Hedda+Greta fray · **D7**: Wessel weave, Greta fray). The aggregate pull reproduces `s ≈ −0.35` with the fray preserved. **The generator produces the slice — so it scales to 37 settlements** without hand-authoring each (S6 Design-Fail resolved).

---

## 6. The Coalesced Graph — settlements as a world-political field

The top-down-conditioned, bottom-up-generated settlements do not sit in isolation. Each settlement **+ its cast** aggregates into a **node**, the nodes wire into a **graph**, and the graph **coalesces** into the peninsula's political field — the macro-layer where "what each settlement wants from the world" becomes a coherent world.

### 6.1 Node = settlement + cast → a **Thrust**

Each settlement aggregates (resonance-weighted over its cast, ⊕ its own deficits) into a **Thrust** — *what it wants from the world and how it puts itself into it*:

| Component | = | source |
|-----------|---|--------|
| **position** | where on the Strand / domains | `s` and the domain-vector (§2) |
| **ambition** | the goal the cast is collectively pursuing | resonance-weighted sum of NPC ambition vectors |
| **need** | what it lacks and must draw from the world | domain deficits — a grain-importer needs grain, a frontier needs defense, a heterodox town needs tolerance |
| **care** | its non-negotiables, what it will defend | the dominant Convictions/Virtues of the cast |
| **disposition** | its stance toward each neighbour/faction | caste/faction/confessional alignment ⊕ the Knot/relational graph |

`Thrust = ⟨position, ambition, need, care, disposition⟩`.

### 6.2 Edges = geography ⊕ faction ⊕ caste ⊕ trade ⊕ Thread

| Edge type | coupling | from |
|-----------|----------|------|
| **march** | physical reachability | adjacency graph (geography) |
| **allegiance** | shared faction/duchy | faction belonging |
| **caste-cline** | latitude continuity (or discontinuity = fault) | the Einhir gradient |
| **flow** | economic coupling | ford / port / road trade |
| **resonance** | metaphysical coupling | RS bleed / Forgetting boundary / Thread |

Edge **weight** = coupling strength; edge **sign** = whether the two Thrusts **align (+)** or **oppose (−)**.

### 6.3 Coalescence — what the graph settles into

Propagating Thrusts along signed edges, the graph self-organizes into:
- **Blocs** — connected regions of aligned Thrust (a duchy that *means one thing*; the Crown-orthodox core).
- **Fault lines** — edges where adjacent Thrusts oppose (a Hierarchy town bordering a Leveling one; a caste-cline cliff) — **the world's conflict-ignition points**.
- **Gradients** — smooth transitions (the N→S caste/Forgetting cline, now *visible* as a Thrust-gradient across the map).
- **Flows** — directed propagation of need/ambition/care along flow edges (RM cell-export south→north; grain breadbasket→cities; Forgetting-bleed at the boundary).

The peninsula's **central fault line — Hierarchy-Orthodox core (Crown/Church/Valorsmark/North) ↔ Leveling-Heterodox periphery (Einhir/RM/South)** — **emerges from the graph** rather than being asserted. The map's politics *is* the coalesced field, not a painted backdrop.

### 6.4 Feedback — the graph is load-bearing, both ways

- **UP:** the graph is the substrate the **faction layer reads** — faction **Mandate** (§1.8), province **fracturing** (§2.3), and **political value** (§2.4) become *derived from* the Thrust-graph (a faction's strength = the bloc it holds; a fracture = a fault line activating inside a province; a movement = a flow coalescing).
- **DOWN:** world/faction events ripple back to settlement domains (a Crown crackdown raises D4 grip toward autocratic across its bloc; an RM surge frays D6/D7 along the southern flow) — re-keying casts and decks.
- **PLAYER:** governing one settlement perturbs its node-Thrust, which **propagates along edges** — a player who frays Goldenfurt toward Leveling shifts the Kronmark bloc and strengthens the southern flow. **Settlement-scale play gains world-scale consequence; world events land at the settlement.** The churn is now peninsula-wide.

### 6.5 Full pipeline (top-down grounded → bottom-up emergent → coalesced)

```
1. Geography + faction            (Layer 0 — given, immovable)
2. Conditioned domain priors      (Layer 1) + coherence ripple (Layer 2)
3. Per-settlement Strand + cast    (§1–§4 — generated within the priors)
4. Aggregate each → node Thrust    (§6.1)
5. Wire edges, propagate, coalesce (§6.2–6.3 — the world-political field)
6. Runtime: cast frays/weaves → Thrusts drift → graph re-coalesces →
   faction layer + decks read the field → player perturbs → repeat
```

---

## 7. NERS self-check (does it earn its complexity?)

- **N (Necessary):** Yes — one model discharges three audit findings (S0 texture, S5 living-NPC, S6 scale). It removes the flat stat-bag *and* the per-town hand-authoring burden.
- **E (Elegant):** Core rule restatable: *"a settlement is a noisy strand across domains; the cast is generated to fray and weave it; governing is choosing which seams to pull."* Second-order consequences are predictable (high-fray seam → events there; sustained one-sided fray → the strand crosses the spine → the town evolves).
- **R (Robust):** Generates variety, conformists *and* dissidents from one stochastic pass, and emergent settlement evolution; scales to the full map. **Friction:** generation-weight tuning is unvalidated (needs a sim sweep — does identity-biased sampling actually produce believable casts, or clichés?).
- **S (Smooth):** Composes with every named system (Armature, Convictions, ethics frames, α/β, Knot/resonance, ambition, caste/TS, the Forgetting, the registry, the deck). **The one real risk is legibility** — a D-dimensional vector per settlement × 37 is a lot of hidden state.
  - **Legibility answer:** the player/GM never sees the vector. They see **(1) the Strand** as one sentence ("a Crown-orthodox breadbasket fraying toward leveling") and **(2) the top-2 active seams** ("the toll and the old rites are what's in play here"). The D-dimensional model is backstage; the Strand + top seams is the readable face — the same "warning-signal / legible trend" pattern the NERS matrix already prescribes.

**Verdict:** N pass · E pass · R Friction (tuning) · S Friction (legibility, mitigated). No Design-Fail. It *earns* its complexity because it is not additive — it **subsumes** the stat-bag, the ambition tick, and the content pack into one generative substrate.

---

## 8. Integration & open questions

- **Grounding is primary:** the seed pipeline is `Geography + Faction → conditioned priors (§0.5) → Strand + cast → Thrust → graph (§6)`. Geography and faction are inputs to world-gen, never outputs.
- **Registry:** `Settlement` gains `domains: dict[str,(position,grip)]` + cached `strand`/`coherency` + a `thrust`; `World` gains a `civic_graph` (nodes = Thrusts, edges = §6.2) that the faction layer reads for Mandate/fracturing/political-value (§6.4). All derived from the Layer-0 seed, not authored per-town.
- **Deck (S4):** card triggers move from hand-written predicates to `|φ_d|`-weighted seam draws; the Goldenfurt deck becomes the *archetype* deck for "Hierarchy-orthodox agrarian, frayed on caste/confession/econ-gov."
- **Ambition tick (S5):** an NPC's ambition *is* a sustained `force_d`; the punctuated/opportunistic upgrade (NERS S5 patch) = forces spike when a seam's `|φ_d|` crosses a threshold (an opening).
- **Generation:** runs once at settlement seed (or world-gen) + light re-coherency when the strand crosses the spine.
- **Open rulings:** the domain count and poles; single canon spine vs per-settlement dominant Conviction-pair; K (cast size) per settlement-type; coherency tolerance band; how much of the seed is authored (geography/faction/type) vs generated.

> The model's claim in one line: **geography and faction ground each settlement; a noisy strand frays across its domains; a generated cast is the hands on the seams; and every settlement's Thrust wires into a graph that coalesces into the peninsula's politics — top-down coherent and bottom-up alive at once.**
