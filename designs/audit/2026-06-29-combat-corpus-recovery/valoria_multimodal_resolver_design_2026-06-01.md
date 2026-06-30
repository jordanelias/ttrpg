# Valoria — Multimodal Cross-Tradition Resolver (design)
**2026-06-01 · grounds the modular engine's tradition layer in the repo's existing throughlines work**

> Jordan's ask: a resolver that translates each martial tradition's vocabulary into a **common practical language
> grounded in physics/material realities** — the actual combat abstracted from the manuals — so multivariate
> cross-tradition matchups resolve (e.g. German longsword vs Japanese yari). KEY FINDING: **the repo already
> contains the substrate** (`designs/audit/2026-05-28-combat-reframe/historical-precedents/`). This design extends
> it, it does not reinvent it.
> `[READ: combat-manuals-seven-axes-throughlines.md (187 ln, full); combat_mechanical_armature.md (79 ln, full);
> manual-vs-combat-v32-bridge.md (headers)]`
> `[CONFIDENCE: high — design follows the repo's own T1-T9 throughlines + A1-A7 armature; not new claims]`

## The core insight (Jordan's, confirmed by the repo's throughlines)
A tradition is an **ontology** (its own vocabulary, its own theory of the collision, partial knowledge of others).
The **fight is physics** (masses, edges, points, momentum colliding in space — indifferent to vocabulary). The
resolver must therefore: **translate every tradition's concepts DOWN to a physical substrate, resolve THERE, surface
outcomes back UP.** Not "pick the German model vs the Italian model" — both are *readings* of one physical reality.

This is the repo's **T2** stated as architecture: `weapon → option-set; cognitive-mode → selection rule` (T7). The
weapon constrains the physical options; the tradition is a *cognitive mode* that reads/selects among them.

## The universal substrate — the THREE load-bearing primitives (repo's T3)
The throughlines doc identifies three things that recur **independently across traditions with no documented
contact** — the strongest "physical universal" candidates, load-bearing in any combat resolution:

1. **MEASURE** — distance as the governing relation. Named everywhere: German (implicit), Italian *misura*
   (larga/stretta), Spanish *círculo* (diameter = opponent's reach), Japanese *maai* (tōma/uchima/chikama),
   Filipino largo/medio/corto, English *true place*. → Substrate primitive: **continuous distance + who controls it**
   (already in the engine: `reach_base` + measure-state).
2. **INITIATIVE** — *when* initiative transfers relative to commitment. German *Vor/Indes/Nach*, Japanese *sen*
   tiers (go/sen/sen-sen-no-sen), Italian *tempo/mezzo tempo/contratempo*, English *true times*. → Substrate
   primitive: **the commitment-window** — the instant one fighter's commitment opens an exploitable window. (The
   Japanese scheme is *finer at the leading edge*: sen-sen-no-sen = pre-commitment read, no clean German/Italian
   equivalent → the substrate needs a pre-commitment tier, not just on-contact.)
3. **CONTACT-AS-INFORMATION** — the bind as a sensing channel. German *Fühlen*, Italian *sentimento del ferro*,
   Chinese *ting jin*, Wing Chun *chi sao*, Filipino *hubud-lubud*. → Substrate primitive: **tactile read in the
   bind** — DISTINCT from visual anticipation (resolves my fidelity finding #2: Reading=visual/pre-contact;
   Fühlen=tactile/in-bind are two different substrate channels, both real).

## How a tradition maps onto the substrate (T2 cognitive modes)
Each tradition is a **cognitive mode** that reads the same physical axes differently (repo's seven modes: tactile,
temporal-spatial, intentional, geometric, consciousness-theoretical, cosmological, kinetic-rhythmic). The seven
physical axes (reach/speed/stance/initiation/footwork/grip/technique) are largely the *output* of the
temporal-spatial + tactile + biomechanical modes; the other modes are alternate readings. A tradition therefore
provides: (a) a **vocabulary→substrate translation** (its named concepts mapped to the 3 primitives + 7 axes), and
(b) a **selection rule** (which substrate options its mode prioritizes — e.g. German prioritizes the in-bind tactile
channel + indes; Italian prioritizes the temporal commitment-window + measure; Spanish prioritizes geometry/measure).

## RESOLVER ARCHITECTURE (extends the modular engine)
A new module `tradition.py` + a resolver that operates ENTIRELY on the substrate:

```
Combatant gains a `tradition` (a cognitive-mode profile), NOT a separate rule-set.
A tradition = { vocabulary→substrate map, selection-rule weights over the 3 primitives + 7 axes, knowledge-of-others }
```
- **Resolution always happens in the substrate** (measure + commitment-window + tactile/visual read + the physics
  of the collision: mass, edge/point, momentum, leverage). The engine ALREADY resolves here — this is why a
  German-vs-Japanese matchup works: both reduce to the same substrate.
- **The tradition biases HOW its fighter reads/selects**, not WHAT physics applies. German longsword vs Japanese
  yari: the yari's reach + the longsword's bind-game both resolve via measure + commitment-window + contact-channel
  — the traditions only change each fighter's *selection weights* and *what they can read* of the other.
- **Partial knowledge of others (Jordan's point):** a tradition has a `knowledge-of-others` factor — fighting an
  unfamiliar tradition degrades your *read* (you mis-time their commitment-window, mis-anticipate their tradition's
  characteristic openings). This is a substrate penalty on the read channels vs an unfamiliar opponent — and it is
  the mechanic that makes cross-tradition matchups interesting rather than just stat-vs-stat.

## What this FIXES from the module fidelity audit (the 4 findings)
1. **Bind over-weights Strength** → bind resolves on the substrate's **leverage** primitive (measure quality + blade
   contact position), with Fühlen (tactile read) as the in-bind information channel — NOT raw Strength. (Repo
   confirms: bind is *tactile-mode* + leverage; "winding asks you to be clever rather than strong.")
2. **Reading vs Fühlen conflation** → TWO substrate channels: visual anticipation (pre-contact, Cog/Att) and tactile
   read (in-bind). Different traditions weight them differently (German → tactile-heavy; Italian → temporal/visual).
3. **Measure is one-shot** → measure is a continuously-maintained substrate variable (repo T5: measure is
   relational and per-action; "maintaining measure on each follow-up is as critical as the initial close").
4. **Tempo is Italian, not universal** → RESOLVED: tempo is the *Italian vocabulary* for the universal
   **commitment-window** primitive; German *Indes* and Japanese *sen* are other vocabularies for it. The engine
   resolves the commitment-window in the substrate; each tradition's tempo/indes/sen is a translation onto it. The
   engine should NOT impose an "Italian tempo clock" — it should resolve the commitment-window, which all three
   describe.

## Build plan (next session — substantial, sequenced)
1. **Read `manual-vs-combat-v32-bridge.md` in full** (how the substrate maps to the engine's mechanisms; it
   reportedly finds v32 "unusually well-aligned with the manual's cross-cultural universals" — confirm the mapping
   before coding). Also `modifier_system_spec.md` (state-gating: tactile-read only in-bind, stance-counter only at
   closing — directly relevant to channel-gating).
2. **`tradition.py` module:** a tradition = (vocab→substrate map, selection weights over the 3 primitives + 7 axes,
   knowledge-of-others matrix). Seed the traditions already scoped (German/Italian/Spanish/Japanese/Chinese/Filipino/
   English) from the master cross-reference table in the throughlines doc.
3. **Split the read channel** in `systems.py`: `visual_read` (pre-contact, Cog/Att) vs `tactile_read` (in-bind,
   the Fühlen primitive) — tradition weights pick the mix.
4. **Make the bind leverage-based:** substrate leverage (measure quality + contact position) + tactile read, not Str.
5. **Commitment-window primitive:** generalize the current tempo gate to a substrate commitment-window that
   German/Italian/Japanese vocabularies all translate onto (with the Japanese pre-commitment tier).
6. **Cross-tradition penalty:** unfamiliar-opponent degrades the read channels (knowledge-of-others).
7. Validate: German longsword vs Japanese yari resolves sensibly; same-tradition mirror unaffected; the T3 universals
   hold across all weapon/tradition pairs.

## Jordan decisions flagged
- **Context-apex (repo T6):** the manual's load-bearing result is that *combat context* decides the apex —
  dueling contexts make counterattack the apex; multi-opponent/formation contexts do not. Valoria personal combat
  is dueling-centric → counterattack-apex is appropriate HERE, but the engine should not bake it as universal if
  battlefield/mass combat is ever in scope. (Matches the earlier C1 duel/battlefield split.)
- **In-world tradition names** (still open from the martial-traditions mapping) — the cognitive-mode profiles can be
  given Valoria culture names once Jordan sets them.

## Not committed
Lanes ignored per directive; all staged. This is a design doc; no engine code written yet for the resolver — the
build is sequenced above and starts from reading the bridge doc in full.

---
# ADDENDUM (2026-06-01) — bridge doc read in full; design confirmed & grounded

`[READ: manual-vs-combat-v32-bridge.md — 107 lines, full, via blob SHA (path was under historical-precedents/)]`

## The bridge CONFIRMS the resolver architecture (not my invention — the repo's own finding)
The bridge analyzes the v32 reframe against the manual and finds **the named-set taxonomy already maps onto the
cognitive modes / traditions**, explicitly:
- **Thrust Duelist ≈ Italian rapier** (temporal-spatial mode)
- **Bind Fighter ≈ German Liechtenauer** (tactile / *Fühlen* / the bind)
- **Counter-time ≈ contratempo / sen** (the counterattack-prestige cluster)
- **Continuous-flow ≈ Filipino FMA** (kinetic-rhythmic *flow*)
- **Burst ≈ Chinese *fa jin*** (explosive committed opening)

→ **`weapon-class (option-set) × named-set (selection-frame)` IS the manual's T6+T7** ("weapon constrains the
option-set; the cognitive mode selects from it"). The resolver's "tradition = selection-frame over a shared physical
substrate" is therefore the **repo's confirmed model**, validated cross-culturally — I build on it, I don't invent it.

## Substrate confirmations (each resolves a fidelity finding, all repo-grounded)
- **Measure ≠ contact (confirmed):** v32 "cleanly separates distance (weapon reach mod) from contact (the In-bind
  state)" — the manual's *misura* (distance) vs *the bind* (tactile channel). My engine has this split. ✓
- **Bind = leverage + tactile, NOT strength (confirmed):** the bridge's N1 lens — "a stance-edge does not disappear
  at contact; it *transforms* into a bind relationship (*Stark/Schwach* leverage, *Winden*)." Bind is leverage
  (*Stark/Schwach*) + Fühlen, exactly fidelity-finding #1. The bind sub-loop must resolve on leverage, not Str.
- **Initiative tiers map to substrate (confirmed):** "v32's Reaction (after/simultaneous, depth-scaled) covers
  *go-no-sen* and *sen-no-sen*; Predictive-Anticipation/Intent-Reading is the closest to pre-commitment
  *sen-sen-no-sen*." → the commitment-window substrate with a pre-commitment (anticipation) tier is correct, and the
  Italian *tempo* / German *Indes* / Japanese *sen* are vocabularies onto it (fidelity-finding #4 resolved).
- **Commit-depth × reaction-slope = Silver's true-times (confirmed):** over-commit → exposed is already the
  commit-depth mechanic. My engine's `overcommit_exposure` is the same primitive.

## Per-weapon tradition grounding (bridge Part C) — for `tradition.py` seeding
The bridge maps which traditions apply to each weapon class (at-depth + documented weapon). Directly usable for the
cross-tradition matchups Jordan named:
- **German longsword** = `long_cut_and_thrust` — German/Italian/Japanese(ōdachi)/Chinese(wodao)/Korean apply.
- **Japanese yari** = `long_pole_spear` — Chinese(qiang, deepest)/Japanese/Korean/Indian apply.
- **Both resolve on the SAME substrate** (measure + commitment-window + contact-channel + the collision physics) —
  which is *why* the cross-tradition matchup is computable. The traditions differ only in selection-weights + what
  each can read of the other (the knowledge-of-others penalty).
- Richest weapon-tradition spreads: spear (7–8), sabre (6), staff (6), longsword (5–6). Leanest: rapier (2–3),
  paired-short (3), heavy-blunt (3). (Matches T7: the sabre is the canonical "one weapon, many cognitive frames.")

## Caveats carried from the bridge (load-bearing for the build)
1. v32 weapon classes are **draft Class B, not canon** — the resolver seeds traditions onto a proposal layer; flag
   any value as Class-B/Class-C, Jordan-vetoable.
2. v32 classes are **coarse** (reach×weight×type; no curvature, no 1- vs 2-hand axis) — the one-handed arming/
   sidesword straddles classes; East-Asian curved two-handers (ōdachi, wodao) straddle cut-and-thrust vs curved.
   My engine's 11-weapon roster is finer than the 8 classes — keep the finer roster, map classes onto it.
3. v32 is a **1v1 dueling-paradigm** system — counterattack-apex is correct HERE (context licenses it, per T6/§15.5),
   but the resolver must NOT bake counterattack as universal if mass/battlefield combat ever enters scope.
4. The bridge "makes no design decisions" — neither does this design until Jordan rules; the build is Class-C.

## BUILD — now fully specified (next session, sequenced; all grounding read)
All prerequisite reading is DONE (seven-axes throughlines, mechanical armature, bridge — all full). Remaining:
1. **`tradition.py`:** a tradition = (vocab→substrate map, selection-weights over the 3 primitives + 7 axes,
   knowledge-of-others matrix). Seed German/Italian/Spanish/Japanese/Chinese/Filipino/English from the bridge's
   set↔tradition mapping + the throughlines master cross-reference table.
2. **Split read channels** (`systems.py`): `visual_read` (pre-contact, Cog/Att) vs `tactile_read` (in-bind, Fühlen).
   Tradition weights pick the mix (German tactile-heavy; Italian temporal/visual).
3. **Bind → leverage-based** (`Stark/Schwach` = measure-quality + contact-position + tactile read, not Str).
4. **Generalize tempo → commitment-window** substrate primitive, with the pre-commitment (sen-sen-no-sen) tier;
   Italian/German/Japanese vocabularies translate onto it.
5. **Cross-tradition penalty:** unfamiliar opponent degrades read channels (knowledge-of-others).
6. **Validate:** German longsword vs Japanese yari resolves sensibly; mirror unaffected; T3 universals hold across
   all weapon/tradition pairs; the named sets reproduce their tradition's characteristic edge.

## Status
Design fully grounded in the repo's framework; build is specified and ready. No resolver code written yet (was
reading the bridge this turn). The modular engine (`combat_engine/`) is the substrate the resolver plugs into.
Nothing committed; all staged. Lanes ignored per directive.
