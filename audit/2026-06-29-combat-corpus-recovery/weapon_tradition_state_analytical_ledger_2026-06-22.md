# Valoria — Weapon × Martial-Tradition × State-Graph Analytical Ledger
**2026-06-22 · scope `design` · status: PROPOSED (mechanical-tier; Jordan-vetoable) · single consolidated surface**

Consolidates the full personal-combat corpus into one analytical ledger: (1) every collected weapon parameter, (2) the combinatorial weapon-matrix logic + its disqualified/valid split, (3) the flattened martial traditions with weapon-category assignment, (4) the combat state graph + all combat parameters, (5) the dual gap register — weapon classes missing tradition, and state-graph points missing tradition.

---

## §0 — PROVENANCE / HONESTY

`[SELF-AUTHORED — bias risk: this ledger synthesises Claude-authored design docs and the Claude-authored combat engine. Inherited verdicts (NERS, loop-safety, sim win-rates) are carried from their source audits, labelled, not re-run. The combinatorial-matrix logic and the weapon-category / gap assignments are new mechanical-tier work this session — bottom-up from the engine vectors, top-down from the project's own historical research; Jordan-vetoable.]`

**as_of** the live `main` of `jordanelias/ttrpg`, bootstrapped this session (token-verified). **CONFIRMED LIVE** content is read from `designs/scene/combat_engine_v1/` (`combatant.py`, `config.py`, `tradition.py`) + the canonical state map (`2026-06-09-personal-combat-comprehensive/combat_engine_flow_and_state_map.md`). **PROPOSED / NOT-LIVE** content (the Valoria-native traditions, the imposition-gate, the ability library, the weapon_axes_v2 substrate beyond what the engine already bakes) is labelled as such at each use.

**Sources read this session (full):**
`[READ: designs/scene/combat_engine_v1/combatant.py — WEAPONS+GEOMETRY tables, Combatant build]`
`[READ: designs/scene/combat_engine_v1/config.py — all Class-C tunables]`
`[READ: designs/scene/combat_engine_v1/tradition.py — 8 traditions, abilities, familiarity]`
`[READ: designs/scene/combat_engine_v1/ability_armature.md — armature, lever map, grounding discipline]`
`[READ: designs/audit/2026-06-22-combat-analysis/combat_attribute_weapon_state_analysis.md — 28-point state graph + impact sims]`
`[READ: designs/audit/2026-06-09-personal-combat-comprehensive/combat_engine_flow_and_state_map.md — canonical 23-step closed-exchange + state diagram]`
`[READ: designs/audit/2026-05-29-combat-armature/{weapon_axes_v2,weapon_rebalance_data.json,martial_traditions_synthesis,martial_traditions_mapping} — substrate, weapon data, native traditions, weapon×tradition census]`
`[READ: designs/audit/2026-06-13-combat-bottomup/{combat_tradition_state_graph_gates,combat_traditions_classes_ability_library} — imposition gate + ability library]`
`[READ: designs/audit/2026-05-28-combat-reframe/historical-precedents/{manual-vs-combat-v32-bridge,combat-manuals-seven-axes-throughlines,blunt-weapon-martial-traditions-completed} — primary historical research]`
`[READ: conversation history — combat-engine audit, weapon-physics (mass+pob), the binary→curvature→hands lineage, weapon-permutation precedent, ranged-physics]`
`[CONFIDENCE: high on all CONFIRMED-LIVE structure/values (engine re-read, line-cited in source docs); medium on the marginal/unattested matrix cells and the native-tradition weapon assignments (proposal, Jordan's creative+structural call).]`

---

## §1 — COLLECTED WEAPON PARAMETERS

### 1.1 The full parameter set (engine `combatant.py` weapon-vector + `geometry`)

Every quantity a weapon carries, with consumption status. The task's requested parameters (reach, head shape, grip length, guard, weight, point of balance, number of hands) all map here.

| Parameter | Type | Values / range | Engine role | Status |
|---|---|---|---|---|
| `reach` | categorical | short / long | measure, phase-dependent reach | **LIVE** |
| `wt` (weight) | categorical | light / heavy | mass → STR-mult, speed, handling | **LIVE** |
| `hands` | categorical | 1 / 2 | bind leverage, off-hand slot, grip-reach | **LIVE** |
| `head` (head shape) | categorical | point / cut_thrust / straight_cut / curved_cut / blunt | armour interaction, tempo, bind behaviour, legibility | **LIVE** |
| `spd` (speed) | scalar | −0.5 … 3.0 | tempo channel | **LIVE** |
| `hand` (handling) | categorical | Forgiving / Standard / Demanding (rank 0/1/2) | skill-demand curve | **LIVE** |
| `grip_len` (grip length) | scalar | ~0.4 … 2.8 | lever-arm → `leverage()` (bind redirect/winding) | **LIVE** |
| `head_len` | scalar | ~0.7 … 5.5 | lever-arm (with grip_len) | **LIVE** |
| `hand_guard` (guard) | scalar | 0 … 1 | passive hand/forearm protection (commit forward + parry safely) | **LIVE** |
| `blade_guard` (guard) | scalar | 0 … 1 | active blade-catching/winding utility of cross/quillons/rings | **LIVE** |
| `gap` | scalar (geometry-baked) | 0 … 1 | gap-thrust precision vs armour | **LIVE** |
| `percussion` | scalar | 0 … 8 | blunt/percussive damage transmission | **LIVE** |
| `reach_adj` | scalar | −0.9 … 1.4 | reach fine-tune | **LIVE** |
| `clinch` | scalar | 2 … 10 | (close-range descriptor) | **UNCONSUMED** (no traced path) |
| `closes_poorly` | flag | spear, staff | pole close-penalty | **LIVE** |
| `mass` | scalar (kg) | 0.3 … 2.7 | intended MoI/heft physics | **DEAD** (committed e414098, not consumed — audit F5) |
| `pob_frac` (point of balance) | scalar | 0.05 … 0.6 | intended MoI/heft physics | **DEAD** (committed e414098, not consumed — audit F5) |
| GEOMETRY: `curvature` | scalar | 0 … 0.55 | bakes `gap`/thrust/cut at import | build-input (baked) |
| GEOMETRY: `point_concentration` | scalar | 0.02 … 0.95 | thrust geometry | build-input (baked) |
| GEOMETRY: `cross_section` | scalar | 0.4 … 0.97 | blade geometry | build-input (baked) |
| GEOMETRY: `edge_keenness` | scalar | 0 … 0.9 | cut geometry | build-input (baked) |
| GEOMETRY: `strike_concentration` | scalar | 0 … 0.85 | percussion geometry | build-input (baked) |

**Point-of-balance note (conversation-history-grounded).** The weapon-physics model (`weapon_physics_and_concentration_model.md`, v2) settled the primitives as **mass + point-of-balance (`pob_frac`) + lengths** (the earlier invented head-mass fraction `f` was retired). MoI ≈ `mass × pob_frac × head_len²` for hilt-swung blades, but **must branch by three regimes** — (a) hilt-swung blade, (b) polearm thrust/pivot, (c) centre-grip strike — because the universal sword formula blows up for poles (spear ≈ 25× a sword) and understates the centre-gripped staff. `mass`/`pob_frac` are committed to all 12 weapons but **behaviour-neutral**: the consuming physics is the not-yet-built next stage. **POB is therefore a recorded-but-inert parameter.**

### 1.2 The 12 live weapon vectors (authoritative — `combatant.py`)

| Weapon | reach | wt | hands | head | spd | handling | grip_len | hand_g | blade_g | perc | mass | pob_frac |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rapier | long | light | 1 | point | 1.5 | Demanding | 0.6 | 0.90 | 0.45 | 0 | 1.3 | 0.10 |
| arming | long | light | 1 | cut_thrust | 1.5 | Standard | 0.8 | 0.40 | 0.55 | 2 | 1.2 | 0.12 |
| longsword | long | heavy | 2 | cut_thrust | 0.5 | Standard | 1.6 | 0.45 | 0.85 | 4 | 1.4 | 0.14 |
| greatsword | long | heavy | 2 | straight_cut | 0.0 | Demanding | 1.8 | 0.55 | 0.70 | 3 | 2.7 | 0.22 |
| sabre | long | light | 1 | curved_cut | 2.0 | Standard | 0.7 | 0.70 | 0.45 | 1 | 0.9 | 0.18 |
| dagger | short | light | 1 | cut_thrust | 3.0 | Forgiving | 0.4 | 0.30 | 0.40 | 1 | 0.3 | 0.25 |
| paired_short | short | light | 1 | cut_thrust | 2.5 | Demanding | 0.5 | 0.55 | 0.50 | 2 | 0.7 | 0.22 |
| spear | long | light | 2 | point | 0.0 | Forgiving | 1.2 | 0.10 | 0.20 | 1 | 2.0 | 0.42 |
| staff | long | light | 2 | blunt | 0.0 | Forgiving | 2.8 | 0.15 | 0.30 | 4 | 1.5 | 0.05 |
| mace | long | heavy | 1 | blunt | 0.0 | Forgiving | 0.7 | 0.45 | 0.30 | 8 | 1.2 | 0.60 |
| poleaxe | long | heavy | 2 | blunt | −0.5 | Demanding | 2.2 | 0.30 | 0.60 | 8 | 2.5 | 0.45 |
| longsword_halfsword | short | heavy | 2 | point | −0.5 | Demanding | 2.6 | 0.35 | 0.25 | 4 | 1.4 | 0.12 |
| *(half-sword is the auto-switched form of `longsword` vs medium/heavy armour, not a separately-wielded weapon)* | | | | | | | | | | | | |

### 1.3 The axis substrate (the parameter model — `weapon_axes_v2`, PROPOSED beyond what the engine bakes)

The engine already implements the 6-axis substrate. The proposal's encoding discipline: **one new free axis (`hands`) + one refined axis (`type`→`head`)** absorbs curvature + cut/thrust + blade/blunt into one five-value axis, instead of a six-axis explosion. Curvature is explicit; cut↔thrust carries the armour interaction; blunt stays clean. The remaining parameters (handling, guard, POB, grip, speed) are **determined**, not free — Elegance lives in the substrate, expressiveness in the instantiation.

---

## §2 — THE COMBINATORIAL WEAPON MATRIX

### 2.1 Logic

**Free combinatorial axes** (the only independent ones; the rest are computed): `reach{2} × weight{2} × hands{2} × head{5} = 40 cells`. This is exactly the canonical count (`weapon_axes_v2 §7`: "5 heads × 2 hands × 2 reach × 2 weight = 40 cells, but only ~15 are real"). **Key scheme:** `{reach}.{weight}.{hands}.{head}` (e.g. `long.heavy.2H.blunt` = poleaxe).

**Derived parameters** computed per cell (not enumerated as free axes — they fall out of the four): `handling` (str-demand proxy: reach+mass+2H), `guard` band (head+hands), `point-of-balance` band (head+weight+reach push forward; hilt/pommel pull back), `grip-length` band (hands+reach), `speed` band (weight+hands+head).

**Disqualification rules** (each cell tested; reason logged; three verdicts — VALID / FLAG / DISQ):
- **D1 — short + 2H + non-point → DISQ.** A two-handed grip on a short weapon has no leverage/reach justification. The *only* coherent short-2H weapon is the half-sword: a shortened long blade gripped on the blade for a **point/thrust**. So short+2H+point survives; short+2H+{cut/blunt} is incoherent.
- **D2 — short + heavy + blade (non-blunt) → DISQ.** Short blades are intrinsically light; a short heavy blade has no referent.
- **D3 — long + heavy + 1H + straight_cut → DISQ.** Greatsword/montante mass needs two hands; one-handed is nonsensical.
- **D4 — short + heavy + 1H + blunt → FLAG (the short-blunt gap).** Attested (shillelagh / canne / tonfa / sap) but THIN — no deep transmissible corpus.
- **D5 — long + light + 1H + blunt → FLAG.** A light baton/rod — marginal; the real one-handed blunt is the short-blunt class.
- **D6 — long + heavy + 1H + {point/cut_thrust/curved_cut} → FLAG.** A heavy blade used one-handed (hand-and-a-half-used-1H / heavy chopper); thin referent.
- **Historical-verification gate (HV).** A cell surviving D1–D6 is **VALID** only if it maps to a documented weapon (the 12 live weapons + the `weapon_axes_v2 §5` roster + attested archetypes). Surviving-but-unreferenced cells are **FLAG: UNATTESTED** — invent or exclude (Jordan).

### 2.2 Result — 40 cells → 19 VALID · 8 FLAG · 13 DISQ

**VALID (19) — documented referent:**

| Key | handling | speed | POB | guard | Referent |
|---|---|---|---|---|---|
| short.light.1H.point | Forgiving | fast | hilt-balanced | high (rings/cup) | stiletto / rondel |
| short.light.1H.cut_thrust | Forgiving | fast | hilt-balanced | mid (cross) | **dagger (live)**, paired_short |
| short.light.1H.curved_cut | Forgiving | fast | hilt-balanced | mid (cross) | kukri / karambit |
| short.heavy.2H.point | Demanding | slow | hilt-balanced | mid | **longsword_halfsword (live)** |
| long.light.1H.point | Forgiving | fast | hilt-balanced | high (rings/cup) | **rapier (live)** / estoc-1H |
| long.light.1H.cut_thrust | Forgiving | fast | hilt-balanced | mid (cross) | **arming (live)** / sidesword |
| long.light.1H.straight_cut | Forgiving | fast | hilt-balanced | mid (cross) | messer / falchion |
| long.light.1H.curved_cut | Forgiving | fast | hilt-balanced | mid (cross) | **sabre (live)** |
| long.light.2H.point | Standard | medium | hilt-balanced | mid | **spear (live)** |
| long.light.2H.cut_thrust | Standard | fast | neutral | high (long cross) | glaive / naginata-style pole-blade |
| long.light.2H.straight_cut | Standard | medium | neutral | high (long cross) | bardiche-light pole-blade |
| long.light.2H.curved_cut | Standard | fast | neutral | high (long cross) | naginata / curved pole-glaive |
| long.light.2H.blunt | Standard | medium | head-heavy | none/low | **staff (live)** |
| long.heavy.1H.blunt | Demanding | medium | head-heavy | none/low | **mace (live)** — 1H levy weapon |
| long.heavy.2H.point | Demanding | slow | hilt-balanced | mid | estoc/tuck-2H / half-sword form |
| long.heavy.2H.cut_thrust | Demanding | slow | neutral | high (long cross) | **longsword (live)** |
| long.heavy.2H.straight_cut | Demanding | slow | head-heavy | high (long cross) | **greatsword (live)** / montante |
| long.heavy.2H.curved_cut | Demanding | slow | head-heavy | high (long cross) | curved two-hander (ōdachi / wodao) |
| long.heavy.2H.blunt | Demanding | slow | head-heavy | none/low | **poleaxe (live)** / war-hammer |

**FLAG (8) — marginal / gap / unattested (Jordan's call to instantiate or exclude):**
- `short.heavy.1H.blunt` — **the short-blunt gap** (shillelagh/canne/tonfa/sap): attested, thin, no deep corpus.
- `long.light.1H.blunt` — light baton/rod: marginal.
- `long.heavy.1H.point` / `long.heavy.1H.cut_thrust` / `long.heavy.1H.curved_cut` — heavy blade used one-handed: thin referent.
- `short.light.1H.straight_cut` / `short.light.1H.blunt` / `short.light.2H.point` — UNATTESTED: physically coherent, no documented referent.

**DISQ (13) — physically incoherent:** all short+2H+non-point (8 cells, D1), all short+heavy+blade (4 cells, D2), long+heavy+1H+straight_cut (1 cell, D3).

### 2.3 The broad weapon classifications (for the gap register, §5)

Collapsing the 19 VALID + the FLAG-but-real cells into the classifications the traditions are assigned against:

1. **Point / thrust blade** (rapier, estoc, half-sword) — `*.point`
2. **Cut-and-thrust blade** (arming, sidesword, longsword) — `*.cut_thrust`
3. **Straight-cut blade** (messer/falchion, greatsword) — `*.straight_cut`
4. **Curved-cut blade** (sabre, ōdachi/wodao) — `*.curved_cut`
5. **Spear / point-pole** (`long.light.2H.point`)
6. **Cutting pole-blade** (glaive / naginata / bardiche — `long.light.2H.{cut/curved/straight}`)
7. **Staff / blunt-pole** (`long.light.2H.blunt`)
8. **Hafted blunt 2H** (poleaxe / war-hammer — `long.heavy.2H.blunt`)
9. **Bare mace 1H** (`long.heavy.1H.blunt`)
10. **Short blade** (dagger, paired-short, stiletto, kukri — `short.light.1H.*`)
11. **Short blunt** (club / sap / shillelagh — `short.heavy.1H.blunt`) — *the documented missing class*

---

## §3 — FLATTENED MARTIAL TRADITIONS + WEAPON-CATEGORY ASSIGNMENT

The corpus carries **two tradition layers**. This section flattens both into one normalized table, then assigns weapon categories (the §2.3 broad classes) to each. **Structural-ontology decision is Jordan's** (synthesis D-α): whether the native layer **replaces** the historical-named scaffold or **coexists** (coexistence → 14 traditions, fails NERS-E; author default is replace). The flatten holds both pending that call.

### 3.1 Flattened tradition table

A tradition = a **cognitive-mode bias-vector over the shared substrate** (channels: visual `v`, tactile `ta`, precommit `pc`, leverage `lev`, tempo `te`, measure `me`, balance `ba`; neutral 1.0), a `set`+`mode` label, equipped ability levers, and familiarity edges.

**LAYER A — historical-named (LIVE in `tradition.py`):**

| Tradition | v | ta | pc | lev | te | me | ba | set | mode | live ability levers | adjacent (reads better) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **german** | .95 | 1.35 | 1.00 | 1.30 | 1.10 | 1.05 | 1.00 | Bind Fighter | tactile | indes (+counter_succ), vorschlag (seize — *cut*), staerke_schwaeche (leverage — *pending*) | italian, english |
| **italian** | 1.20 | 1.00 | 1.00 | .95 | 1.30 | 1.25 | 1.05 | Thrust Duelist | temporal-spatial | mezzo_tempo (×counter_sel), misura (measure — *pending*) | german, spanish, english |
| **spanish** | 1.15 | .95 | 1.00 | .95 | 1.05 | 1.35 | 1.30 | Thrust Duelist | geometric | atajo (measure — *pending, S2/S3*) | italian |
| **japanese** | 1.05 | 1.15 | **1.35** | 1.05 | 1.20 | 1.10 | 1.10 | Counter-time | intentional | sen_no_sen (seize — *cut*) | chinese, filipino |
| **chinese** | 1.05 | 1.20 | 1.05 | 1.15 | 1.05 | 1.20 | 1.15 | Burst | kinetic-rhythmic | **none** (priority-gap; grade-M fill only) | japanese, filipino |
| **filipino** | 1.00 | 1.25 | 1.05 | 1.00 | 1.15 | 1.05 | 1.25 | Continuous-flow | kinetic-rhythmic | **none** (NOT S1/S2-anchored per armature) | chinese, japanese |
| **english** | 1.10 | 1.05 | 1.00 | 1.05 | 1.15 | 1.15 | 1.10 | Counter-time | biomechanical | true_times (+anti_overcommit) | german, italian |
| **none** | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | — | — | — (neutral baseline; mirror-fair) | — |

**LAYER B — Valoria-native (PROPOSED, `martial_traditions_synthesis.md`; provisional vectors; only Constraint fully grounded):**

| Tradition (working label) | v | ta | pc | lev | te | me | ba | set | mode | intended levers | structural weakness |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **Constraint** | .88 | 1.35 | .95 | 1.30 | .95 | 1.25 | 1.30 | Constraint Fighter | tactile-geometric *(fusion)* | measure(V), leverage(V) | the approach (no seize, low visual) |
| **Tempo-read** | 1.15 | 1.00 | 1.00 | .95 | 1.30 | 1.20 | 1.10 | — | temporal-spatial/biomech | anti_overcommit, counter_select | the bind (low tactile/leverage) |
| **Intent-seize** | 1.05 | 1.15 | 1.35 | 1.05 | 1.20 | 1.10 | 1.05 | — | intentional | seize, counter_success | high-variance — read-dependent |
| **Flow** | 1.00 | 1.25 | 1.05 | 1.00 | 1.15 | 1.05 | 1.25 | — | kinetic-rhythmic | counter_select, tempo(V) | a hard tempo-break disrupts it |
| **Root** | 1.00 | 1.20 | 1.00 | 1.35 | .92 | 1.10 | 1.05 | — | structural-leverage *(new)* | leverage(V), strike(V) | slow, low tempo — out-paced in the open |
| **Reach** | 1.20 | .90 | 1.00 | .90 | 1.15 | 1.35 | 1.05 | — | measure-spatial *(fusion)* | measure(V), reopen* | the bind/grapple (reach-inversion) |

`*` `reopen` is the not-yet-built separation lever — Reach is partly blocked on it. The native layer also needs the proposed `grade='V'` (Valoria-synthetic) ability gate (synthesis §2, Jordan-ratify) since native traditions have no single historical anchor.

**Named-set ↔ tradition 1:1 mapping (the bridge keystone, conversation-confirmed):** Bind Fighter = German · Thrust Duelist = Italian/Spanish · Counter-time = Italian-counter / Japanese / English · Burst = Chinese (≈ fa jin) · Continuous-flow = Filipino.

### 3.2 Weapon-category assignment

Each tradition assigned its appropriate weapon categories (§2.3 broad classes). **Layer A grounded top-down in the historical census** (`martial_traditions_mapping.md` MAP 2 — at-depth count, manual treats the weapon per-tradition AND documents it as central). **Layer B grounded bottom-up in the niche/channel-vector** (mechanical-tier; in-world cultural naming is Jordan's).

**LAYER A — historical (from MAP 2's at-depth count):**

| Tradition | Assigned weapon categories | Grounding (historical exemplars) |
|---|---|---|
| **german** | cut-and-thrust blade (longsword), short blade (dagger), hafted blunt 2H (poleaxe) | Liechtenauer *langes Schwert*; Fiore/German *degen*; *Le Jeu de la Hache* / Talhoffer *azza*. Bind-centric → also drives the half-sword form. |
| **italian** | point blade (rapier), cut-and-thrust blade (longsword), short blade (dagger) | Fiore *spada*, *spada da doi mani*; Capoferro/Fabris rapier; Fiore foundational dagger. |
| **spanish** | point blade (rapier) + short blade off-hand (daga) | La Verdadera Destreza; *daga de mano izquierda*. The narrowest weapon footprint (geometric rapier specialist). |
| **japanese** | curved-cut blade (katana), curved/cut-thrust 2H (ōdachi), short blade (tantō), staff (bō/jō) | koryū kenjutsu; *ōdachi*; *tantō*; Shintō Musō-ryū *jō*. |
| **chinese** | spear / point-pole (qiang), staff (gùn), curved-cut blade (dao) | Wu Shu *qiang* (deepest spear corpus); Shaolin *gùn*; *dao*. |
| **filipino** | short blade ×2 (paired-short), short blade (daga), staff | *doble baston* / *espada y daga* / *sinawali*; *balisong*; *sibat*. |
| **english** | staff / blunt-pole (short staff), cut-and-thrust blade (backsword), short blade (sword-and-dagger) | Silver's favoured short staff; backsword; sword-and-dagger. |

**LAYER B — native (niche-derived, mechanical-tier):**

| Tradition | Assigned weapon categories | Grounding (niche → weapon physics) |
|---|---|---|
| **Constraint** | cut-and-thrust blade + half-sword (bind), hafted blunt 2H (leverage), short blade off-hand | `leverage 1.30 / measure 1.25 / tactile 1.35` → wants weapons that win the bind (high blade_guard, 2H grip leverage) after a calculated entry. |
| **Tempo-read** | point blade (stop-hit), cut-and-thrust blade, spear (stop-hit at reach) | `tempo 1.30 / measure 1.20` + anti_overcommit → measure/point weapons that punish the commit; low `lev` keeps it out of the bind. |
| **Intent-seize** | point + cut-and-thrust + curved-cut duel blades | `precommit 1.35` (seize before the blade moves) → the reading duel weapons; weapon-agnostic but spikes on single-time-counter blades. |
| **Flow** | curved-cut blade, short blade ×2 (paired), staff | `balance 1.25 / tactile 1.25 / tempo 1.15` → fast-recovery flow weapons (the moulinet, paired weaving, staff spins). |
| **Root** | hafted blunt 2H (poleaxe), bare mace 1H, straight-cut heavy (greatsword), half-sword | `leverage 1.35` + strike → heavy/percussive/armour-defeat weapons; the battlefield/clinch apex (context-flip C1). |
| **Reach** | spear / point-pole, point blade (rapier), staff, straight-cut heavy 2H (greatsword) | `measure 1.35 / visual 1.20`, low `lev` → own the approach with the longest weapons; dies in the bind (reach-inversion). |

---

## §4 — COMBAT STATE GRAPH + ALL COMBAT PARAMETERS

### 4.1 The canonical state graph (CONFIRMED-LIVE — `combat_engine_flow_and_state_map.md`)

**Phase machine:** `Out-of-contact → Closing → In-bind → Breaking → [Disengaged | Wounded | Felled]`. The game calls **one engagement per turn** (`fight()` is the multi-turn sim harness only). One engagement = one ~10 s turn: **approach → emergent burst of exchanges → separation or felling**.

**Outer loop:** `fight()` → reset wounds, init live state → per turn (≤12): coin-flip first mover → `engagement()` → if felled, decide (±1) + 5% `UPSET_FLOOR` flip; else inter-turn recovery (stamina/conc partial, **wounds persist**) → repeat → 12 turns exhausted = **0 / unresolved** (no tiebreak, Jordan 2026-06-02).

**Engagement state diagram (terminals on the right):**
```
Approach  ──gap≤0.3──►  AwaitTempo ──ready≥2.5──►  Exchange ──┬─wind──►  Bind ──won──►  HitLanded ──► AwaitTempo (burst continues)
   │ stop-hit fells          ▲ reopen (≤.6)              │           └─lost─► Riposte ──role flip─► AwaitTempo
   ▼                         └──────────────────── Riposte / displace-inside ┘
 Felled                  Closed ──clean defence | exchanges≥BURST_MAX(4) | stamina≤−4──► None (separation)
                         Closed ──wound total > MW+1──► Felled
```

### 4.2 The 28-point per-beat state-graph map (CONFIRMED-LIVE — `2026-06-22` analysis §3)

Every mechanic point a beat walks, with its attribute and weapon drivers. **This is the surface the gap register (§5b) checks for tradition coverage.** [Full table in source; the points, grouped:]

- **Pre-exchange:** (1) reach/measure · (2) Vor decay · (3) disposition Vor drift · (4) poise/structure recovery · (5) tempo/cadence · (6) reach re-opening.
- **Approach:** (7) closing · (8) stop-hit.
- **Closed exchange:** (9) aggressor selection · (10) half-sword auto-switch · (11) commit depth (2–5) · (12) OOB · (13) visual read · (14) defence mode · (15) defender σ · (16) attacker σ · (17) initiative term · (18) armour-defeat σ · (19) Vor edge · (20) resolution roll · (21) Indes/sen-no-sen steal + counter · (22) overcommit exposure · (23) outcome mapping · (24) displace-step-inside.
- **Post-strike:** (25) hit application · (26) bind · (27) riposte · (28) burst / turn end.

### 4.3 All combat parameters (CONFIRMED-LIVE — `config.py` + derived)

**Attributes (1–7; combatant build):** Strength, Agility, Endurance, Cognition, Attunement, Spirit, Focus, History (0–7), Disposition (4=neutral). + weapon, armor (none/light/medium/heavy), tradition, skills, equipped abilities, grip-state (normal/choke/lunge).

**Attribute impact on win (vs uniform-4 baseline, N=500, mirror-fair):** History 96.2 · Agility 95.8 · Cognition 95.6 (three dominant levers — pool/tempo/reading) · Endurance 93.8 · Strength 93.2 · Attunement 93.0 (second tier) · Spirit 82.4 (derived-stat contributor) · Focus 66.0 (protective) · Disposition 50.8 (**~neutral by design** — both poles cost).

**Weapon impact on win (vs arming, uniform-4):** reach dominates (Pearson **r = +0.83**); delivery secondary (point/thrust 86.5% mean — thrusts are hard to read); weight not primary. Roster sorts ~monotonically by reach.

**Derived-value formulas:** Combat Pool `max(5, History+6) − wounds` · Wound Interval `End+6`, Max Wounds `min(⌊End/2⌋+1, 3)`, **−1D per wound (aggressor pool, offence-only)** · stamina_max `3·End + 2·Spirit` · conc_max `3·Focus + 2·Spirit` · reading `(2·Cog+Att)/3 + .2·(History−3)` · reflex `(2·Agi+Att)/3` · reach_base `4.0 + 2·long + .8·2H + HEAD_REACH[head] + reach_adj` · str_demand `1 + .35·reach + 1·heavy + .6·HANDLE_RANK + .4·2H` · handling_penalty `.10·max(0, demand−Str) + .20·fatigue` · leverage `2.2·(grip/(grip+head) − .30) + .20·2H` · weapon_tempo (speed/heft/fatigue/poise) · legibility (thrust .80 / swing·blunt 1.25).

**Config tunable groups (Class-C, all live — `config.py`):** core/damage · reach (L0/LONG/HANDS2/HEAD_REACH/REACH_FRAC/REACH_W…) · tempo (BASE_TEMPO/SPEED_K/AGI_TEMPO_K/WEIGHT_PEN/BURST_MAX…) · approach/reopen · stamina/conc · read/init (INIT_K/READ_K/REFLEX…) · legibility/feint · defence modes (PARRY/DODGE/WIND_K/guard terms) · outcome probs · handling/balance · lever/displace · armour-defeat (ADEF_W/BLUNT/POINT/CUT/THRESHOLD) · bind (TECH/TACTILE/STR_K) · **initiative Vor** (INIT_SIGMA_K/DECAY/CAP/STEAL_INDES… — damped+capped per NERS) · **poise/kuzushi** (FLOOR/RECOVER/BREAK…) · counter/disp · UPSET_FLOOR=.05 (95% videogame cap). *(Full literal values in `config.py` / state-map §4A5 — consolidated by reference, not re-transcribed.)*

**Damage chain:** `damage = round(QUAL[deg] · 12 · tanh(Impact · Coupling · 4.0 / 12))` where Impact `= HEFT[wt] + clamp(−1,2,(Str−3)//2)` (blunt heft continuous from percussion), Coupling = best-mode transmit vs armour (blunt percussion / point gap-find / cut shear / cut_thrust = max(cut,point)); cumulative damage ÷ (End+6) → wounds → felled at > MW.

---

## §5 — GAP REGISTER (the analytical core)

**Verdict.** Two coverage surfaces are checked against the live tradition set (`tradition.py`, 8 traditions): (a) the broad weapon classifications from §2, and (b) the 28 state-graph beats from §4.2. **Both have structural holes.** The single worst finding spans both: tradition multipliers are flat scalars applied at ~21 consumption sites and *never route the exchange path* — so even "covered" beats are only tuned, not branched. Within that, the most severe point-gap is **pt21 pre-commit seizure**, where the Japanese tradition's defining channel (`precommit`) has zero consumption sites and the `seize` ability was CUT — a signature mechanic that is structurally unexpressible today.

`[SOURCE: T0 — tradition.py + combat_engine_flow_and_state_map.md A2/A5]` `[CONFIDENCE: high — for what IS/IS-NOT wired; medium — for proposed fills, which are unvalidated]`

### 5a — Broad weapon classifications missing / thin tradition assignment

Ranked worst-first. "Thin" = a live tradition nominally touches it but lacks abilities or historical anchor.

| # | Classification | Live weapon? | Live tradition? | Gap type | Evidence |
|---|---|---|---|---|---|
| 1 | **Short-blunt** (1H mace/hammer, short reach) | **NO** (matrix `short.heavy.1H.blunt` → FLAG; no engine row) | **NO** | **HARD — double absence.** No class instantiated *and* no tradition. Recurs across audits as the standing hole. | matrix D4 FLAG; combatant.py has no short-blunt row; §2 census |
| 2 | **Bare 1H mace** (long-reach, `mace` row exists) | YES (`mace`) | **NO transmissible** | **Orphaned technique.** Weapon is live but no tradition carries its method; percussion/armour-defeat skill survives only inside the `poleaxe` corpus (→ proposed *Root*). | combatant.py `mace`; tradition.py has no mace-anchored set |
| 3 | **2H cutting pole-blade** (glaive / naginata / bardiche) | Partial — matrix VALID (`long.heavy.2H.{straight_cut,curved_cut}`), no dedicated engine row | **NO dedicated** | **Family absence.** VALID, historically attested combinations with no live tradition; Japanese set is sword-anchored, not naginata-anchored. | matrix VALID cells; tradition.py japanese set/abilities |
| 4 | **Messer / falchion straight-cut 1H** | Partial (`sabre` covers curved; straight-cut single-edge unrepresented) | **NO** | **Historical tradition exists, unencoded.** German *Messerfechten* is documented primary research but absent from `tradition.py`. | blunt/straight-cut historical doc; tradition.py enum |
| 5 | **Paired-short** (`paired_short`, off-hand pair) | YES | **THIN** (`filipino` only) | **Single thin anchor.** Filipino is the lone tradition, but it carries **no abilities** and is **not S1/S2-anchored** — grade-M mechanical fill, weak transmission. | tradition.py filipino (empty ability list); martial_traditions_mapping MAP 2 |

`[AGGREGATOR-ONLY: none — all from repo T0]` `[CONFIDENCE: high — items 1,2,5 are unambiguous absences; medium — items 3,4 depend on whether Jordan wants those families instantiated at all]`

### 5b — State-graph beats missing tradition assignment

Of the 28 beats (§4.2), the following carry **no tradition modulation** — the path is decided by attributes/geometry alone, or by a channel/ability that is registered but inert. Ranked worst-first.

| Rank | Beat | What decides it now | Tradition that *should* shape it | Why it's a gap |
|---|---|---|---|---|
| **1** | **pt21 — pre-commit seizure** (Indes / sen-no-sen steal) | `counter_success`/`counter_select` only | **Japanese** (sen-no-sen); German *Indes* | **MOST SEVERE.** `precommit` channel has **0 consumption sites** (audit F2) and `seize` ability **CUT 2026-06-05**. The defining mechanic of a flagship tradition cannot fire. |
| 2 | **pt10 — half-sword auto-switch** | geometry only (`halfsword` auto-form) | **German** *Harnischfechten* | `halfsword_target` is keyed but **neutral**; the armoured-half-sword tradition is unexpressed — switch is pure geometry, no school flavour. |
| 3 | **pt18 — armour-defeat σ** | **Strength only** | **Root / Breacher** (proposed) | No tradition touches the armour-defeat term; percussion/point-gap method is attribute-gated, not school-gated. |
| 4 | **pt24 — displace-step-inside (leverage)** | `leverage` term | **leverage-channel traditions** (Spanish *atajo*, Chinese) | `leverage` channel is **registered but INERT** pending `eff_cw` wiring — the inside-displacement beat reads no school. |
| 5 | **pt8 — stop-hit** | reach/measure geometry | **Italian** *tempo* / **English** | Stop-hit is an Italian/English signature; no tradition modulates it — only the *proposed* imposition gate would. |
| 6 | **pt28 — burst / turn-end continuation** | `BURST_MAX` config | **Chinese** (Burst) / **Filipino** (Flow) | No **live** tradition extends the burst; the two sets that should (Chinese, Filipino) **have no abilities**. |
| 7 | **pt4 — poise / structure recovery** | poise/`kuzushi` config | **Kuzushi** (proposed) | Recovery curve is uniform; no tradition imposes a balance-break or structure-recovery preference. |
| 8 | **pt14 — defence-mode selection** (parry/dodge/wind) | reading-driven | (any defensive school) | Mode is chosen by `reading` value; no tradition biases toward parry vs. void vs. winding. |

**Plus the structural finding (spans all transitions):** every state-graph **transition** currently lacks tradition assignment. Traditions apply flat σ-multipliers at consumption sites; **none imposes its preferred node onto the path.** The proposed imposition gate (`combat_tradition_state_graph_gates_2026-06-13.md`) would add path-routing at only **4** transitions (closing, defence-select, resolution, burst) — a partial fix, not full coverage.

**Inert-lever census (why so many beats read no school):** 5 of 8 ability levers are CUT or pending — `seize` CUT; `leverage`/`measure`/`visual`/`tactile`/`precommit`/`balance` pending `eff_cw` wiring; only `counter_success`/`counter_select`/`anti_overcommit` are live. Reviving the gaps in 5b is therefore **mostly one wiring task** (`eff_cw` + `precommit` consumption), not eight separate builds.

`[CONFIDENCE: high — live/inert status is read directly from source; medium — the "should shape it" column is design proposal, severity is mine]` `[SELF-AUTHORED — bias risk: I built the matrix and ranked these; an independent reviewer should challenge whether pt8/pt14 are true gaps or acceptable attribute-driven beats, and whether the 2H pole-blade family is wanted at all.]`

---

## §6 — CONSOLIDATED FINDINGS & DECISIONS FOR JORDAN

### 6.1 What this ledger establishes (settled, evidence-backed)

1. **Weapon parameters are fully collected** (§1): the live engine vector is reach · weight · hands · head · speed · handling · grip_len · head_len · hand_guard · blade_guard · gap · percussion · reach_adj, plus the geometry build-inputs (curvature · point_concentration · cross_section · edge_keenness · strike_concentration). Two fields — `mass` + `pob_frac` — are committed but **DEAD** (audit F5).
2. **The combinatorial matrix resolves to 40 → 19 VALID + 8 FLAG + 13 DISQ** (§2). The 19 VALID align with the canonical "~15 real weapons" plus attested variants; disqualification is by physical incoherence (D1–D3) and historical non-attestation.
3. **Traditions are flattened across two layers** (§3): 8 LIVE (`tradition.py`, channel-vector form) + 6 PROPOSED Valoria-native (synthesis). Weapon-category assignment per tradition is tabulated.
4. **The state graph is fully pulled** (§4): the 5-phase machine, 28 beats, every config group, and the derived-formula/damage chain.
5. **Both coverage surfaces have structural gaps** (§5): 5 weapon-class gaps and 8 beat-gaps, over a substrate where **traditions tune but never route**.

### 6.2 Decisions required (ranked by leverage)

| # | Decision | Options | Author default | Blocks |
|---|---|---|---|---|
| **D-1** | **Wire `eff_cw` + a `precommit` consumption site** | (a) do it — revives `leverage`/`measure`/`visual`/`tactile`/`precommit`/`balance` and unblocks beats pt21/pt24 (and most of 5b) in one task · (b) leave inert | **(a)** — highest leverage; 5b is *mostly this one fix* | pt21, pt24, pt10, Japanese signature |
| **D-2 (D-α)** | **Native traditions: replace or coexist** with the 8 live? | replace · coexist | **replace** | §3 Layer-B status; all naming |
| **D-3 (D-β)** | **Native tradition count** | 6 (as proposed) · other | 6 | scope of Layer-B build |
| **D-4** | **Instantiate short-blunt class?** (the HARD gap, §5a#1) | (a) add `short_mace`/`warhammer` engine row + anchor a tradition · (b) leave as documented hole | **(a)** if short-blunt is wanted in-world; else close as WONTFIX | 5a#1, 5a#2 (Root) |
| **D-5** | **Adopt the imposition gate** (path-routing at 4 transitions)? | adopt · defer | **adopt** — converts traditions from tuners to routers at the 4 highest-value beats | the structural finding |
| **D-6 (D-γ)** | **Grade-V amendment** for the native-tradition schema change | apply · hold | apply | schema versioning |
| **D-7 (D-δ)** | **In-world naming** (Constraint/Tempo-read/Intent-seize/Flow/Root/Reach → Valorian names) | Jordan authors | — | **Jordan's creative layer — I do not name** |
| **D-8** | **Fill empty ability lists** for Chinese + Filipino (priority-gap; unblocks pt28) | fill · leave | fill (grade-M) | pt28, 5a#5 |

### 6.3 Honest limitations

- **The native-tradition weapon assignments (§3 Layer B) and the marginal/unattested matrix FLAG cells (§2) are medium-confidence proposals**, not ratified design. The 2H pole-blade family (5a#3) and messer/falchion (5a#4) may not be wanted in Valoria at all — that is a creative call, not a defect.
- **No win-rate / balance simulation was re-run for any proposed wiring.** The attribute/weapon impact numbers in §4.3 are carried from the source audits (N=500 / N=300 sims already in the repo); any new lever (eff_cw, imposition gate, short-blunt) is **unvalidated** and would need a fresh sim pass before ratification. `[GAP: balance-of-proposed-wiring — not simulated this session]`
- **Severity rankings in §5 are mine** `[SELF-AUTHORED — bias risk]`. The IS/IS-NOT-wired facts are read directly from source and are high-confidence; the "should shape it" and worst-first ordering are design judgement open to challenge.

`[CONFIDENCE: high — collection, matrix logic, state-graph pull, and live-gap identification; medium — proposed fills and their priority ordering]`

---

*End of ledger. Source of truth: `jordanelias/ttrpg` @ live `main`. This document consolidates by reference — literal config values and full per-beat tables live in `config.py` and the cited audit docs; they are not re-transcribed here to avoid drift.*
