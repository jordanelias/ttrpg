# Character Stats, Faction Stats, and Progression — a design proposal

## Status: PROPOSED — DESIGN-ONLY, HELD FOR JORDAN. Nothing here is built, ratified, or scheduled. No constant is changed, no default flipped, no golden re-recorded, no `.py` touched. §11 states the calls that are Jordan's; §9 states what would falsify the recommendation.

**Date:** 2026-08-15 · **Lane:** IN (cross-cutting: characters + factions + every resolution subsystem)
**IDs:** none allocated (design-only, following the `2026-07-26-personal-combat-player-agency-and-tradition-curriculum.md` precedent)
**Subject:** the working tree at `94ac02f`
**Bears on:** `OPT-AV-1` (attribute roster, Jordan-SKIPPED 2026-07-08, still open) · `OPT-AV-18` Renown-cap sub-item (no default stated) · `repo_state_armature_v1.md` P5 (hard-gated on OPT-AV-1) · `valoria_fork_plan_of_record_v1.md` C4 · workplan v6 M1 juncture 6 (season close / Accounting)

---

## §0 What this document is, and what it is not

It is three things: a **measurement** of what the tree actually contains today on stats and
progression (§1), a set of **alternatives** for each of the three design axes the question opens
(§3 characters, §4 factions, §5 progression), and **one recommended composition** with its numbers,
its calibration debt, and its falsifiers (§7–§9).

It is **not** a ratification. It does not resolve OPT-AV-1 — it supplies the evidence and the
option set that OPT-AV-1 has been waiting on since 2026-07-08, and states a recommendation Jordan
can correct rather than author.

It deliberately does **not** propose a new primitive where an existing one composes. Every
mechanism recommended in §7 is either already in the tree, already proposed in the tree, or a
rule *about* things already in the tree. Where this proposal does introduce something genuinely
new (one faction stat, one Conviction channel), it says so and gives the alternative of not doing it.

### 0.1 Is this premature? — the strongest objection, answered up front

M1 ("one playable season") stands at 0/7 junctures closed. Fieldwork's sim is `stub_resolve`
throughout; the social-contest kernel does not read attributes at all; `combat_engine_v1` is not
campaign-dispatched; no production caller reaches any threadwork entry point. **A reasonable
reviewer will ask why a progression proposal now, rather than after the subsystems resolve.**

Three answers, in decreasing strength:

1. **The roster question (§3, §4) is not premature — it is overdue and it is blocking.**
   `repo_state_armature_v1.md` Phase 5 is *hard-gated* on OPT-AV-1 and has been since 2026-07-20.
   The fork plan's C4 records that the `Character` dataclass **cannot be built** until the roster's
   contents are ruled. The SessionStart banner says it every session: *"schema: descriptor roster IN
   FLUX — do not bind Godot fields yet."* Four surfaces are waiting on one skipped ruling.
2. **Progression is already inside M1 juncture 6, and nobody noticed.** Juncture 6 is *"Season close
   (Accounting + propagation)"*, and `campaign_modes_v30:27` defines Accounting as *"Apply Domain
   Echoes, advance clocks, **assign CP**."* The season loop cannot be closed while the thing
   Accounting is specified to do has no rules. This is not adjacent to the critical path; it is on it.
3. **§10 sequences around the gap honestly.** Step 6 — extending the Craft clock into fieldwork and
   social contest — is explicitly *blocked* until those subsystems resolve. Nothing here proposes
   writing pacing numbers for a stub.

What *is* premature and is therefore not attempted: any pacing number for fieldwork or contest, and
any claim that the recommended composition is balanced across subsystems. §8 marks that debt and
§9 F5 states plainly that the no-exchange rule is an assumption, not a result.

---

## §1 THE MEASUREMENT

### 1.1 The substrate every stat must serve

| Layer | Spec | Source |
|---|---|---|
| Die rule | d10; face 1 = −1, 2–6 = 0, 7–9 = +1, 10 = +2, no chain. Net may be negative. | `engine/engine_params/params_tables.yaml` → `engine/params/core.md` §Die Rule |
| TN | 6 controlled / 7 standard / 8 desperate | ibid. §TN Values |
| Ob | 1 routine … 20 foundational (cap); min 1 | ibid. §Obstacle Scale |
| Degrees | Overwhelming (net ≥ 2·Ob **and** ≥ 3) / Success (≥ Ob) / Partial (>0, <Ob) / Failure (≤0) | ibid. §Degrees of Success |
| Continuous mode (Godot-canonical) | `net ~ Normal(0.4·N, 0.8·√N)` at TN 7, resolved against `net − (Ob − 0.5)` | ibid. §Continuous Engine |
| Universal Ob | `floor(opponent Attribute / 2) + 1` | `canonical_registry.md:148` |

**Every derived value is `attribute × multiplier`** (`derived_stats_v30.md` §1), which is why +1 on
an attribute is not a small change: End 4→5 moves Health 40→45, Stamina 20→23, and Wound Interval;
any Primary 4→5 moves a `(Primary×2)+History+3` pool by +2D, which at TN 7 is roughly +0.8 expected
net. **This is the single most important constraint on progression design in this game** and it is
developed in §2.1.

**The "universal pool" is universal in exactly one subsystem.** Measured:

| Subsystem | Pool actually used | Attribute-driven? |
|---|---|---|
| Fieldwork | `(Primary × 2) + History + 3` | yes |
| Personal combat (live engine) | `max(5, History + 6)` — `core.py:47-52`, Agility-independent by ratified design (ED-901) | **no** |
| Threadwork (live sim) | `Spirit×2 + min(3, history+3) + TPS` — `operations.py:145-157` | Spirit only |
| Social contest (live kernel) | abstract `faculty` integer; `primitives.py:128` states *"Charisma is NOT kernel state… faculty is an abstract pool-size parameter"* | **no** |
| Mass battle (live engine) | `eff_power × eff_size × POOL_QUALITY_SCALE` (or legacy `min(Size,Command)+Command`) | unit stats only |
| Faction domain action | bare stat, 1–7D | yes |

Two further substrate splits worth recording because they bear on any cross-subsystem stat rule:
combat's `core.degree()` is **deliberately held on the pre-2026-08-14 ladder** while threadwork
routes through the unified `dice_engine.degree_label` (ED-IN-0187) — the two subsystems do not
presently share degree math; and combat carries a 5% `UPSET_FLOOR` that is self-labelled
*"non-emergent designer fiat"* (`config.py:294-304`).

### 1.2 The attribute roster: four incompatible declarations, one skipped ruling

| Source | Count | Roster |
|---|---|---|
| `engine/params/core.md` §Attributes + `canonical_registry.md:138-142` | **10** | Agility · Endurance · Strength / **Cognition · Recall · Focus** / Attunement · Bonds · **Charisma** / **Spirit** |
| `references/descriptor_registry.yaml:39-53` | **9** | Strength · Endurance · Agility / Focus · **Acuity** · **Will** / Attunement · Charisma · Bonds — **no Recall at all** |
| `references/glossary.md:53-64` | **7** | Agility · Attunement · Cognition · Endurance · **Presence** · Spirit · Strength — no Focus, Bonds, Recall |
| `proposals/valoria_fork_plan_of_record_v1.md:439` (C4) | **10** | "3/3/3 plus Spirit… stays reversible" |

`glossary.md:53` flags the conflict itself and records *why nothing catches it*: `names_index.yaml`'s
MIRRORS block omits the glossary, so `ci_names_consistency.py` never fires. Jordan explicitly
**skipped** OPT-AV-1 on 2026-07-08 (`editorial_ledger_in_archive.jsonl` ED-IN-0029). It is still the
hard gate on `repo_state_armature_v1.md` Phase 5.

Creation rule (the one place all sources agree): **31 points across the roster, min 1 each,
max 5 for one attribute and 4 for the rest, advancement ceiling 7.**

### 1.3 Attribute load-bearing, measured — and why the naive reading is a confound

Read counts in the live combat package (`grep -c '\.<attr>\b'` over `systems/combat/combat_engine_v1/*.py`)
plus presence in each other subsystem's live code:

| Attribute | Combat (live) | Threadwork (live) | Social contest (live) | Fieldwork (live) | Faction / mass battle |
|---|---|---|---|---|---|
| Strength | **15** — damage, footwork, bind, Health buffer | — | — | — | — |
| Agility | **8** — tempo, reflex, footwork, initiative | — | — | — | — |
| Endurance | 4 — Health, Stamina, fatigue | — | — | — | — |
| Cognition | 2 — `reading()` | 1 — collective helper `floor(Cog/2)` | label only | — | Command `⌈(2Cha+Cog)/3⌉` |
| Attunement | 3 — `reading()`, `reflex()` | — | label only | — | — |
| Spirit | 7 — Health/Stamina/Concentration derivation | **primary** — `Spirit×2` pool, fatigue threshold | label only | — | — |
| Focus | 4 — Concentration, `disrupt_resist_p`, `poise_regen` | **0** (claimed in docstring, never read) | label only | — | — |
| **Recall** | **0** | 0 | **absent** | — | — |
| **Bonds** | **0** | 0 | — | Knots only (`knots.py`, the one built fieldwork module) | — |
| **Charisma** | **0** | 0 | display-only `FaceScale.face_max` | — | Command |

**The naive reading of this table is wrong, and the error is the exact class §0.1 of `CLAUDE.md`
was written to prevent.** "Recall, Bonds and Charisma have no executable presence, therefore cut
them" is a **confounded measurement**: it does not measure attribute quality, it measures *which
subsystems have engines*. `systems/fieldwork/sim/fieldwork.py` and `investigation.py` are pure
`stubwire.stub_resolve` no-ops; the social-contest kernel abandoned the doc's named-attribute pool
construction entirely for an abstract `faculty` int. Recall, Bonds and Charisma are precisely the
attributes whose demand lives in fieldwork and social contest — i.e. **the entire non-combat half
of the game**. Cutting on this evidence would delete the attributes that carry investigation and
politics because investigation and politics are the parts that have not been built yet.

The *sound* reading of the table is different and sharper: **`History` — not any attribute — is the
dominant progression input in the one subsystem that is fully built.** `pool = max(5, History + 6)`
makes History worth +1D per point with no attribute involvement at all, across a 5→12D range.

And in threadwork, the same identifier is **inert**: `history_contrib = min(3, history + 3)` means
any `history ≥ 0` yields the cap of 3, so History has **zero** marginal value in every Thread
operation (`operations.py:153-157`). The canon comment at that line describes a "+3 constant plus up
to +3D from level" that the formula does not express. That is a live defect in the single most
load-bearing progression quantity in the game, and it is worth fixing whatever else is decided.

### 1.4 Faction stats: canon versus the live schema

| | Canon (`descriptor_registry.yaml`, `faction_canon_v30 §5.1`) | Live (`engine/autoload/game_state.py:97-110`) |
|---|---|---|
| Base stats | Influence 1–7 · Wealth 0–7 · Military 0–7 · **Intel 0–7** · Stability 0–7 | `{L, Sta, W, I, Mil}` |
| Mandate | **DERIVED** — size-weighted aggregate of per-settlement Legitimacy/Popular Support (LPS-2e, Jordan 2026-05-30) | `Faction.L` **is** the scalar Mandate (the pre-LPS-1 convention its own header calls superseded) |
| Intel | declared, floor ratified 2026-07-08 | field exists, *"currently unread/unwritten by live code"* |

Derived buffers, each independently calibrated with **no master scale** (`derived_stats_v30` §3, §8):
Legitimacy = Mandate×20 · Treasury = Wealth×100 · Reputation = Influence×15 · Faction Discipline =
Stability×10 · Levies = Military×2 (ceiling).

Settlement stats: Legitimacy · Popular Support (0–7) · Prosperity · Defense · Order (0–5) ·
Facility Tier (0–3). Territory: Fort Level (0–4).

Three structural observations:

1. **Intel is a stat with no consumers.** Six declared faction stats, five wired, one dead.
2. **Mandate collapses two different legitimacies.** Settlement scale correctly separates
   *Legitimacy* (elite/institutional) from *Popular Support* (popular); faction scale aggregates
   both into one number. The most interesting political stories in this setting — Crown versus
   Parliament, a governor beloved locally and distrusted at court — need both at faction scale.
3. **Administrative reach is unmodelled and keeps being re-invented.** `Clerk Capacity`
   (ED-SE-0022, PROPOSED, Ming-Qing thin-bureaucracy), `Haushalt Competence` 0–3 (ED-663), and the
   "network" half of Intel are three names for one missing quantity: *how far and how reliably does
   policy actually execute at distance.*

Faction *Discipline* (Stability×10, 0–70) and unit *Discipline* (1–7) are a live name collision,
already flagged and display-labelled but not renamed (OPT-AV-18).

### 1.5 Progression today: a complete loss engine, and no gain engine

**What exists and is well-specified — all of it downward:**

| Mechanism | Spec quality |
|---|---|
| Coherence 10→0, banded (Stable/Dissonant/Fragmented/Fractured/Severed/Crisis), escalating +Ob on all Thread rolls, −1D/−2D social and memory, **effective Recall −1/−2** (skill-loadout loss), NPC conversion at 0 | complete, numeric, with recovery paths (Anchoring Scene, Rendering Crisis Resolution) |
| Conviction Scars, per-Conviction: 1 destabilised → 2 weight shift + Resonant Style permanently exposed → 3+ crisis (d6 table) | complete |
| Knot strain −5..+5, rupture at +5 (Disposition→−3, 4 Composure, +1 Scar both sides), five bypass triggers | complete |
| Disposition decay −1/season above +2 without contact | complete |
| Standing demotion ladder: default 1 rank / severe 2–3 / total → Standing −1 dismissal | complete, per-faction |
| Renown governance penalties −1 each, cap −2/season | complete |
| Exposure → Cover bands → Church Attention Pool | complete |
| Faction: five Stability triggers, collapse at 0, six-step collapse procedure, reconstitution check, deterministic anti-death-spiral floor at Stability ≤2 | complete and unusually disciplined |

**What is supposed to exist and does not:**

| Mechanism | Status |
|---|---|
| **CP (Character Points)** — named as *the* advancement currency in `campaign_modes_v30`, `hybrid_gaps_v30`, `glossary`, and 14 subsystem glossaries | The spending menu is cited as `valoria_ttrpg_complete.md §10.2`. **That file has never existed in this repository.** Verified across all commits on all refs (`git log --all --name-only \| grep ttrpg_complete` → 0 hits; positive control on `derived_stats_v30` → hits). The only CP cost anywhere in the tree is *4 CP for one Inspiration* (G-053). |
| **Attribute advancement** | `"Advancement max 7"` states a ceiling. No trigger, no cost, no currency, no per-season cap exists anywhere. |
| **History growth** | **Two incompatible models of what a History even is.** (a) `canonical_registry.md:144-150`: a History is a **level** 1/2/3, each worth +1D, capped by Recall; the Universal Pool row reads `History (0–3D)`. (b) `character_histories_v30.md:14,33-35`: a History has a `dice_bonus` **points** score capped by Recall (so 1–7), *and separately* a depth Level 1–3 gated at `dice_bonus ≥ 3` (L2) and `≥ 5` (L3), with SaGa sparking (Spirit + `floor(Recall/2)` after any Ob ≥ 2 roll) as the acquisition trigger. Model (b) is internally coherent as a two-axis system; model (a) collapses the two axes into one, and **under (a)'s reading the L3 gate is unreachable** because the level ladder tops out at 3. `dice_bonus`'s own growth rule is defined in neither. Meanwhile the live combat engine treats `history` as a **single scalar** (`max(5, history+6)`, default 3), i.e. a third model. |
| **Beliefs** — the stated CP driver | `add_belief` has zero callers. The flow-skeleton's verdict: *"A live campaign can therefore never contain a Belief."* |
| **Conviction (13-set)** | Code runs a **superseded 9-set** (`sim/conviction.py:42-49`); a live caller passes `'Loyalty'`, a member of neither set, and silently no-ops. |
| **Standing range** | 0–5 (`clock_registry_v30`, self-declared single source of truth for tracks) vs 0–7 (`faction_politics_v30`, CANONICAL, explicitly *"replace the 0–5 Standing track"*) vs `player_agency_v30` using 0–5 in §5.4 and 6–7 in §6.2. |
| **Renown cap** | 0–10 implied by its own effects table; OPT-AV-18 records *no default stated*; `clock_registry_v30` has **no Renown row at all**. |
| **Aging / generational arc** | absent corpus-wide, despite 10–15+ season campaigns and Portrait Retirement. |

### 1.6 The finding, stated once

> **Valoria has built a rigorous, numerate, thematically-committed engine for characters and
> factions getting *worse*, and has never built the matching engine for them getting *better*.
> The gain side is not under-tuned; it is absent — a currency with no menu, a ceiling with no
> ladder, a skill system with two incompatible growth rules, and a Belief mechanic no live
> campaign can instantiate.**

This asymmetry was never a decision. It is the residue of building combat first (where progression
is a build-time input, not a loop), evacuating the document that held the CP menu, and never
closing OPT-AV-1. It has to be decided deliberately now, because it determines the game's feel more
than any single subsystem does. **It is also an opportunity**: a complete, well-specified decline
engine is the rarest and hardest half to build, and Valoria already owns it. The design question is
not "how do we add progression" but "what kind of *rise* does this particular *fall* deserve."

---

## §2 CONSTRAINTS THIS PROPOSAL MUST RESPECT

These are not preferences. Each is a ruling or a measurement already in the tree.

**2.1 — The balance envelope is small, and it is measured.** `combat_engine_v1` is calibrated at
attributes ≈3–4, `disp` 4, `history` 3. The U9/U10 ablation work established that the noise floor on
`workbench/balance.py` at n∈{350,500} is **≈±4pp**, and that the *correct instrument* for a
situational lever is per-fight texture with outcome preservation, not aggregate win-rate
(ED-PC-0022/0023, after a 4-critic pass retracted a confounded "+2.8pp"). A single +1 attribute is
far outside ±4pp. **Therefore any progression system that grants more than a handful of attribute
points across a campaign invalidates the most expensive calibration work in the repository.**
§7 sizes the budget to this.

**2.2 — "Efficacy from INVESTMENT/EXPERTISE, not membership; no fiat"** (Jordan, 2026-07-23,
`fiat_audit_v1.md`). The `IMPOSITION_GATE` was retired for forcing a tradition's preferred node.
A progression system that grants power for *belonging* to something rather than *doing* something
is the same defect wearing a different hat.

**2.3 — Both poles must cost.** D3 of the combat balance-state report: *"any new player-facing axis
that is not explicitly bound to both of its ends will become another monotone stat"*, and the
engine must charge the cost **in the same commit** that grants the benefit, never in a follow-up.

**2.4 — No GM.** Every award must be adjudicable by the engine from data it already produces.
Anything requiring a human to judge "was that a genuine step toward your Conviction" is unshippable
as written.

**2.5 — Triage is the gameplay.** 3–5 scene actions per season against 4–9 opportunities
(`player_agency_v30` §6). This is the structural anti-farm defence that Elder Scrolls-style
use-based advancement has always lacked, and it is free.

**2.6 — The campaign has a chosen ending.** Portrait Retirement unlocks after 2 of 3 starting
Convictions resolve. A campaign is a *chapter of a life*, not a rags-to-riches arc. Progression
should deepen an identity set at creation, not replace it.

**2.7 — Build bottom-up; never re-implement a rule that already lives once** (`CLAUDE.md` §0, §8).

---

## §3 CHARACTER ATTRIBUTE SPREAD — ALTERNATIVES

| | Option | Roster | Verdict |
|---|---|---|---|
| **C-A** | **Ratify the 10** (3/3/3 + Spirit) | Agi·End·Str / Cog·Rec·Foc / Att·Bon·Cha / Spirit | **RECOMMENDED** (with §3.6's two amendments) |
| **C-B** | Adopt the registry's 9 (drop Recall; Acuity/Will renames) | as `descriptor_registry.yaml` | **REJECT** |
| **C-C** | Adopt the glossary's 7 | Agi·Att·Cog·End·Presence·Spirit·Str | **REJECT** |
| **C-D** | 8 — fold Attunement into Cognition, keep Recall | Agi·End·Str / Cog·Rec·Foc / Bon·Cha / Spirit | Defensible; **not recommended** |
| **C-E** | 12 — split Spirit into Spirit (Thread) and Resolve (will) | — | **REJECT** |

**C-A — ratify the 10.** Every one of the ten is demanded by at least one subsystem's design
(§1.3), the creation rule (31 points) is already written against ten, it is what
`engine/params/core.md` and `canonical_registry.md` both say, and it is the fork plan's stated
default. It costs zero migration. Its weaknesses are real and addressed in §3.6.

**C-B — the registry's 9. Reject.** Dropping Recall deletes the attribute that the *entire skill
system's capacity rules* hang on: `max_equipped = Recall`, learning speed `floor(Recall/2)`, History
cap, plus the elegant Coherence coupling (Fragmented ⇒ effective Recall −1 ⇒ you lose access to
equipped skills). Nothing in the tree proposes a replacement home for any of those. The `Acuity` and
`Will` renames additionally have **zero live consumers** while `Cognition` and `Spirit` are named
engine constants — the rename runs against the traffic.

**C-C — the glossary's 7. Reject.** Loses Focus, Bonds *and* Recall. Losing Focus destroys the one
worked design example threadwork gives for the shape of a practitioner build (*"Spirit 6 / Focus 2:
high threshold, sustained contact, but only 1 operation — endurance without skill. Spirit 2 /
Focus 6: the reverse"* — `derived_stats_v30` §6.1). Losing Bonds destroys the Knot gate (Bonds ≥ 5)
and Knot count (`floor(Bonds/2)+1`), which is the mechanical spine of the relationship system.
This roster is a stale table, not a design.

**C-D — 8, folding Attunement into Cognition.** The honest case: `reading(c) = (2·cog + att)/3` already
blends them, and both are "primary" candidates in contest and fieldwork. The case against, which I
find stronger: fieldwork's split is *things versus people* — Cognition drives Examine, Surveil,
Cover, Concealment; Attunement drives Interview, Read, Negotiate, and Thread-adjacent sensing. That
is a real and playable distinction (the Investigation/Insight split every good investigation game
makes), and collapsing it makes one attribute mandatory for the entire fieldwork subsystem.
**Present to Jordan as the live alternative; do not adopt by default.**

**C-E — 12. Reject.** Roster inflation against a 31-point budget; Spirit's Thread and will roles are
already coherent as one thing (*"internal coherence, resolve, and Thread operation capacity"*).

### 3.6 Two amendments to C-A

**Amendment 1 — un-double-gate Recall.** Today Recall caps *both* how many skills you can hold
(`max_equipped = Recall`) *and* how deep any one goes (`Recall caps dice_bonus`), plus it sets
learning speed. Three roles on one attribute makes Recall a mandatory tax stat every build must
buy — the classic Constitution problem. Proposal: **Recall governs breadth and learning rate only**
(`max_equipped = Recall`; `floor(Recall/2)` spark dice). **Depth is governed by accumulated practice
in that History** (§5, P3), with no attribute cap at all. The attribute already gates power
multiplicatively through `(Primary × 2)`; capping depth as well is double-dipping.
It also forces the §1.5 choice between the two History models to be made explicitly: **adopt (b),
the two-axis points-and-level system**, and retire `canonical_registry`'s one-axis restatement —
which is the collapse that makes the L3 gate unreachable. One quantity, one owner.

**Amendment 2 — sharpen creation, keep growth slow.** Current creation (31 points, min 1, one at 5
and the rest ≤4) produces a flat character: e.g. `5,4,4,4,4,3,3,2,1,1`. Flat start **plus** slow
growth (which §2.1 forces) means the character is never a specialist. Since Valoria's identity is
set by lifepath (Origin → Formation → Vocation → Catalyst) and the campaign is a chapter rather than
an ascent (§2.6), the specificity belongs at creation. **Proposal: raise the single-attribute
creation cap from 5 to 6, keep 31 points and the ≤4 rule for the rest.**
⚠️ This touches the combat calibration envelope directly and **must not be adopted without an
ablation run** — see §9 falsifier F2. The alternative, if the ablation says no, is to keep the cap
at 5 and accept flatness, which is the safer default.

### 3.7 What is *not* an attribute, and should stay that way

`Thread Sensitivity` (0–100, perceptual depth), `Coherence` (10→0), `Truth` (0–5), `Standing`,
`Renown`, `Momentum` (0–4), `Disposition` (−5..+5) are **tracks**, not attributes: they move on
their own rules, several are engine-internal, and none is bought at creation. `derived_stats_v30`
§14.2 has this right. Nothing in this proposal changes it.

---

## §4 FACTION STAT SPREAD — ALTERNATIVES

| | Option | Shape | Verdict |
|---|---|---|---|
| **F-A** | Ratify canon as-is | W · Mil · I · Sta · Intel + derived Mandate | Safe; leaves the dead stat and the collapsed legitimacy |
| **F-B** | Cut Intel, fold into Influence | W · Mil · I · Sta + derived Mandate | Cheapest honest fix |
| **F-C** | **Replace Intel with Administration; split Mandate into Mandate + Support** | W · Mil · I · Sta · **Adm** + derived **Mandate** & **Support** | **RECOMMENDED** |
| **F-D** | Explicit capacity/cohesion split (CK3/EU4 shape) | spendable {W, Mil, I, Adm} vs losable {Sta, Mandate, Support} | Adopt as *presentation*, on top of F-C |

**F-A.** Zero migration, and it is what `descriptor_registry.yaml` says. But it ratifies a stat
nothing reads and preserves the Mandate collapse. Choose it only if the appetite for faction-layer
change is zero.

**F-B.** Intel's actual gameplay is *knowing specific things about specific factions*, which is a
ledger, not a scalar — and `derived_stats_v30` §14.1 already lists **Intelligence Holdings** as
PENDING for exactly this. Folding the scalar into Influence and re-homing the content as a
per-target holdings ledger is defensible and cheap (the scalar is unwired, so nothing breaks).

**F-C — recommended.** Three moves:

1. **Intel (scalar) → Intelligence Holdings (ledger).** As F-B. What you know about whom, with
   provenance and decay — reusing the Record primitive that already exists single-owner at
   `systems/settlements/sim/ledger.py` (which the SC three-lens audit independently identified as
   the missing record spine, ED-SC-0017). That module already ships five tag kinds —
   Precedent · Grudge · Debt · Reputation · **Leverage** (*"a hook the player holds"*) — with
   dedupe, TTL and a season-boundary sweep. **Leverage is intelligence.** Re-homing Intel here is
   composition onto an existing primitive, not a new subsystem.
2. **New stat: Administration (0–7).** *Consolidation, not invention* — it absorbs three quantities
   the tree keeps re-deriving: `Clerk Capacity` (ED-SE-0022, PROPOSED), `Haushalt Competence` 0–3
   (ED-663), and the "network reach" half of Intel. It answers the question none of the other five
   answer: **how far from the capital does an order actually arrive, and how much leaks on the
   way.** Mechanically it gates *how many* Domain Actions a faction may take and at what distance,
   rather than adding dice to any of them — a capacity stat, not a power stat.
   Derived buffer: **Chancery** = Administration × 10.
3. **Split Mandate into two derived aggregates.** `Mandate` = size-weighted settlement *Legitimacy*
   (elite/institutional consent — what Parliament counts). `Support` = size-weighted settlement
   *Popular Support* (what revolts, musters, and pays). Both already exist per-settlement at 0–7
   (LPS-2e). Today they are averaged into one faction number, which makes the Crown-versus-crowd
   story mechanically inexpressible. Parliament votes on Mandate; Muster, Turmoil and Revolt read
   Support.

**F-D — presentation, not a fifth option.** Whichever roster is chosen, present it as two families:
**capacity** (Wealth, Military, Influence, Administration — things you spend and rebuild) and
**cohesion** (Stability, Mandate, Support — things you lose and cannot buy back directly). Valoria
already behaves this way; naming it makes the faction sheet legible and makes §5's asymmetry rule
obvious at a glance. Precedent: CK3's gold/levies versus prestige/piety/legitimacy; EU4's monarch
points versus stability/legitimacy.

**Also settle, in the same pass:** rename faction Discipline → **Cohesion** (Stability×10), retiring
the collision with the unit-scale Discipline stat that OPT-AV-18 could only paper over with a display
label. One name, one thing (`CLAUDE.md` §4 word-choice rule).

---

## §5 PROGRESSION ARCHITECTURES — ALTERNATIVES

Seven genuinely different answers, each judged against §2.

### P1 — Ledger (one currency, one shop)
CP earned at Accounting from a closed rubric; spent from a published menu.
*Precedent:* most tabletop RPGs; CK3 lifestyle XP → perks.
**For:** one number, one pacing dial, trivially engine-adjudicable, and it is what the tree already
half-says. **Against:** it is a shop. Growth decouples from fiction — you become stronger in an
accounting screen. It invites optimal-build convergence, which contradicts the U10 finding that the
game's interest lives in *texture*, not aggregate advantage. And the menu is the hard part: it is a
balance surface with no oracle outside combat. The repo has had six months to write the menu and
has not, which is evidence about difficulty, not about diligence.
**Verdict: not as the spine. Keep CP as a *minor* currency (§7.5).**

### P2 — Use-based (SaGa sparking; already half-designed in-tree)
Skills spark from use at difficulty; no currency.
*Precedent:* SaGa/Romancing SaGa (explicitly cited by `character_histories_v30`), Elder Scrolls,
RuneQuest, Darklands, Dungeon Master.
**For:** fiction and growth are the same act; zero fiat; the engine already produces `(pool, Ob,
degree)` for every roll, so adjudication is free (§2.4 satisfied); it is already written.
**Against:** the Oblivion pathology — players farm the trigger, and Oblivion's leveling became a
system players used third-party trackers to plan around. Valoria has an unusually strong structural
answer (§2.5: 3–5 contested scene actions per season — you cannot grind what you cannot repeat), but
use-based growth still couples advancement to *what happened to you*, which can strand a build.
**Verdict: adopt the trigger; do not adopt it bare.**

### P3 — Test-marking (Burning Wheel)
Each skill records tests by difficulty (routine/difficult/challenging, in BW's terms Ob 1/2/3);
advancement requires a *mix*, so routine work stops counting once you are good.
*Precedent:* Burning Wheel; artha → Epiphany for the slow shade shift.
**For:** it is the anti-farm fix P2 needs, and it is nearly free here because Valoria already
computes an Ob for every roll. The curve is self-flattening by construction. Crucially, BW marks
tests **whether they succeed or fail**, which breaks the rich-get-richer trap where you only improve
where you are already strong — and thematically, failing hard *is* how people learn.
**Against:** bookkeeping — but this is a videogame with an engine, so the ledger is invisible and
the UI shows a bar. **Verdict: this is the mechanism. Recommended.**

### P4 — Traits and passions (Pendragon)
Growth is in *character*: traits and passions strengthen through expression, weaken through
betrayal; at 16+ they become **controlling** — you must roll to act against them. Glory accrues from
dramatic behaviour and buys a point of anything per 1000.
*Precedent:* King Arthur Pendragon, 4th/5th ed.
**For:** Valoria's 13-Conviction system with per-Conviction Scars **is a Pendragon trait system that
was built with only its downward half**. Adding the upward channel is not an import, it is a
completion. And Pendragon's controlling-trait rule is the perfect expression of §2.3 (both poles
cost) in a no-GM engine: a strong Conviction *takes actions for you*, which is a real cost
denominated in agency rather than numbers.
**Verdict: adopt the symmetry and the controlling rule. Do not adopt Glory-buys-anything (it
collapses to P1).**

### P5 — Position, not power (Crusader Kings, Romance of the Three Kingdoms)
Capability barely moves; title, office, holdings and the *verbs* they unlock move a great deal.
**For:** already designed — `settlement_layer_v30` §6.1's stature ladder maps Renown × Standing to
governance scope with explicit ROTK and CK3 parallels; the scene-action budget already scales with
Standing. Costs nothing to adopt because it exists. **Against:** as the *whole* answer it leaves
personal-scale play static — a Standing-7 character fights exactly as well as a Standing-0 one,
which is unsatisfying in a game with a combat engine this good.
**Verdict: adopt as one of the clocks, not as the system.**

### P6 — Entropy budget (Pathologic, Sunless Sea, Darkest Dungeon)
The character only degrades; "progression" is the accumulation of permanent marks that are
simultaneously capability and liability.
**For:** maximally consonant with Valoria's thesis. `campaign_modes_v30` §12.7 already says it out
loud: *"An active practitioner working at Relational+ scale through a full campaign will enter
Dissonant by mid-campaign and approach Fragmented by the end. This is the game's structural
statement about the cost of sustained Thread work."*
**Against:** as the whole system it gives no build agency, contradicting the ratified *"every build
AVAILABLE"* principle. **Verdict: it is already the decline half; keep it, do not extend it.**

### P7 — Three clocks, no exchange (the synthesis)
Split progression into three tracks that move at different rates, in different currencies, and
**cannot be exchanged for one another**:

| Clock | What moves | Rate | Mechanism | Losable? |
|---|---|---|---|---|
| **Craft** | Histories (breadth + depth), techniques | slow, capped | P3 test-marking + P2 spark trigger | only via Coherence (effective Recall) |
| **Standing** | Standing, Renown, Resources, office, holdings, Knots | fast | P5 deed-driven | **yes**, sharply |
| **Character** | Conviction weights, Truth, Self-Other, Coherence, TS | lateral | P4 expression/betrayal + P6 marks | not "lost" — transformed |

**The no-exchange rule is the load-bearing part**: you cannot grind fights into political rank, and
you cannot buy skill with reputation. It is what prevents a single dominant strategy from
collapsing the three halves of the game into one, and it is why this is not just P1 with three
wallets.

**This is not an invention.** All three clocks already exist in the tree (History/techniques;
Standing/Renown/Resources; Convictions/Truth/Coherence/TS). P7 names them, gives the one that has
no rules a set of rules, and states the invariant between them.

**Verdict: RECOMMENDED, staged (§10) — because only the Craft clock has an oracle today.**

---

## §6 DECLINE, SYSTEMATISED

Valoria's decline mechanisms are individually excellent and collectively unclassified. Four tiers,
distinguished by *what it takes to undo them*:

| Tier | Name | Undone by | Instances in tree |
|---|---|---|---|
| 1 | **Drain** | rest, scene change | Stamina, Concentration, Composure/Face, Poise, Initiative, Wounds (clear at session end) |
| 2 | **Debt** | seasons of deliberate work | Disposition decay, Knot strain, Exposure, Deniability Debt, Treasury 0, Faction Cohesion |
| 3 | **Scar** | never fully — it becomes part of you | Conviction Scars, Coherence bands, Infamy, Compacts, unit Discipline |
| 4 | **Fall** | a new arc, or not at all | demotion/dismissal, faction collapse, Coherence 0 → NPC, Portrait Retirement |

**The rule this makes visible: every tier of rise should have a matched tier of fall, and today
tiers 1, 2, 3 and 4 all exist going down while only tier 2 exists going up.** §7 fills tiers 1
(momentum), 3 (marks that are also capabilities) and 4 (the arc-ending transformation).

**And the governing principle, on which four independent parts of this repo have already
converged:**

> **Every increment of capability creates a specific, named, exploitable vulnerability — charged in
> the same commit that grants the benefit.**

- Combat lane: D3's binding rule and the retirement of `IMPOSITION_GATE` (ED-PC-0023).
- Settlement lane: the Ascendancy Ω-d downfall table — *"every rise pays a structurally matched
  fall"* — independently NERS-validated as the strongest claim in its cluster.
- Threadwork: Coherence *is* this rule, expressed as cosmology.
- Precedent: Pendragon's traits becoming controlling at 16+.

Four independent derivations of one rule is the evidence standard `decision_policy_v1` asks for.

---

## §7 THE RECOMMENDED COMPOSITION (R)

### 7.1 Stats
- **Characters: C-A + both §3.6 amendments** — 10 attributes (3/3/3 + Spirit); Recall governs
  breadth and learning rate only; depth governed by practice; creation cap 5→6 **pending the F2
  ablation**.
- **Factions: F-C, presented as F-D** — Wealth · Military · Influence · Stability ·
  **Administration**; derived **Mandate** (elite) and **Support** (popular); Intel → Intelligence
  Holdings ledger; faction Discipline renamed **Cohesion**.

### 7.2 The Craft clock — test-marking with a directed-practice valve
- Every roll marks the History it used, tagged by the Ob it was made against, **regardless of
  degree** (Burning Wheel's rule; failing hard teaches).
- A mark counts toward advancement only if `Ob ≥ current History level + 1`. Routine work stops
  counting once you are good — this is the anti-farm invariant, and it is structural, not a cap.
- Advancement fires when the required mark set fills. `[SEED]` shape, uncalibrated:
  L1→L2 requires 3 marks at Ob ≥ 2; L2→L3 requires 5 marks at Ob ≥ 3 including at least one failure.
- **Directed practice valve** (the fix for P2's stranding problem): one scene action per season may
  be spent on *instruction* — a mark at the instructor's History level, from an NPC or an
  institution. This is what the tradition-curriculum proposal is already reaching for, and it costs
  the scarcest resource in the game (§2.5), so it self-limits.
- **Techniques** (`equipped`, graded levels — already built and invariant-safe) unlock from
  History level + tradition access + one instruction scene. **Hand these out generously**: the
  morphology-lever layer measures at ~0 aggregate win-rate edge, with a per-fight event-divergence
  rate of **~12–13%** (`test_levers_add_texture_without_shifting_balance`, n=200, katana/arming
  25/200 and dagger/arming 26/200) under a guard that fails if outcome flips exceed 20%.
  ⚠️ **Correction, made during this document's own adversarial pass:** an earlier draft cited
  "16–28% diverged / 3–8% flipped". The 16–28% figure is **explicitly retracted in the test's own
  docstring** (ED-PC-0034: *"never reproducible at n=60"*), and the 3–8% flip rate has no source at
  all — the test bounds flips at ≤20% and does not publish a measured rate.
  The signature that matters — *plays out differently, does not shift balance* — is real and is
  already the ratified instrument (ED-PC-0022/0023); the specific numbers were not.
- Fix `history_contrib = min(3, history + 3)` in threadwork so History is not inert there (§1.3).

**Why test-marking and not a deed rubric: fidelity-invariance.** `auto_manual_resolution_duality_v1.md`
(RULED 2026-07-08) requires the same conflict class to resolve at two fidelities — auto-resolved at
faction scale, played out at personal scale — and `hybrid_gaps_v30` G-089 already rules that
*"Board game successes generate CP and personal advancement. The character performed those actions;
the zoom level does not affect whether the experience counts."* A **deed rubric** (P1) must be
re-adjudicated at every fidelity and in every mode, and `campaign_modes_v30` §Advancement shows what
happens when it is not: CP is *"Not applicable"* in Board Game mode and Renown is *"Not tracked"*,
so a character who spends a season zoomed out simply does not advance. **A mark falls out of the
resolution record itself** — every resolver at every fidelity already emits `(pool, Ob, degree)` —
so the Craft clock is fidelity-invariant by construction rather than by a rule someone has to
remember to apply. That is a design argument for P3 that has nothing to do with tabletop taste.

### 7.3 Attribute points — the rarest currency, tied to the campaign's own spine
**Attributes are not bought.** One attribute point is awarded when a **Conviction resolves
Fulfilled or Transformed** — not Failed, not Unresolved — at most one per season, and it must go to
an attribute the engine observed being used in pursuit of that Conviction.

Why this is the right shape:
- **It sizes correctly.** Portrait Retirement unlocks after 2 of 3 Convictions resolve. A normal
  campaign yields **2–4 points**; a long one perhaps 6. That lands inside the envelope §2.1 forces,
  where a CP shop does not.
- **It is engine-adjudicable** (§2.4). Conviction resolution states already exist and are already
  mechanised; scene actions already carry which attribute they rolled. Nothing is invented.
- **It composes rather than adds.** Conviction resolution already grants +2 Momentum and +1 Renown.
  This makes it the most important event in a character's life, which is what the Portrait system
  already says it is.
- **It cannot be farmed**, because Convictions are player-authored and resolution is gated on
  Sufficient Scope (≥2 scene actions).

### 7.4 The Character clock — give Convictions their upward half
Symmetric to Scars, and Pendragon-shaped:
- Acting on a Conviction **at cost** raises that Conviction's weight; acting against it under no
  duress lowers it, and is what produces a Scar today.
  **"At cost" must be computable without a GM (§2.4), so define it from data the engine already
  emits, not from a counterfactual it cannot evaluate:** the Scene Slate already tags every
  opportunity with *"which Conviction/Duty/game-state condition generated this entry"*
  (`player_agency_v30` §4.2b, Step 4 = Conviction-Aligned), and every action already reports its
  stat deltas. **A Conviction-tagged action whose resolution produced a net negative delta on any
  quantity the player owns** — Renown, Standing, Resources, Disposition with a named NPC, Composure,
  Coherence, Exposure — **acted at cost.** No counterfactual, no judgement call, no GM.
- **At high weight the Conviction becomes controlling**: when it is engaged, the engine takes the
  aligned action unless the player spends Momentum to resist. This is the matched liability, it is
  denominated in *agency* rather than numbers, and it is the cleanest possible fit for a no-GM
  engine — the world starts acting through your character's convictions, which is what conviction
  actually is.
- Prerequisite: reconcile the **three-to-four things named "Conviction"** (13-vector · player's
  3 sentences · territory Piety Track "Conviction (PT)" · retired character Piety Track → Truth) and
  fix `sim/conviction.py`'s superseded 9-set and the silently-no-op `'Loyalty'` call. **This is a
  blocker, not a nicety** — the mechanic cannot be built on a name that means four things.

### 7.5 CP — demoted, not deleted
Keep CP as a **minor, fast-cycling** currency for exactly what it already buys in the live tree:
Inspirations, Belief revisions, a re-roll of a spark check, an extra instruction scene. Not
attributes, not History levels. This retires the dangling `§10.2` reference without pretending the
menu that never existed can be reconstructed, and it keeps CP's 14 existing citations valid.

### 7.6 Renown — close OPT-AV-18 by making it symmetric
Cap at **10** — matching Shadow Renown, which is explicitly 0–10 and *"spills into Deniability Debt
at 1:1"* above the cap (`faction_politics_v30` §2.2b.i). Reverse *"Renown does not decay
naturally"*: **−1 per season at Renown ≥ 5 with no qualifying deed.** Reputation that is not
renewed fades, and asymmetric-up is the exact monotone-stat shape §2.3 forbids.
In-repo precedent: **Disposition already decays −1/season above +2 without contact** — the same
rule, on the same kind of quantity, one scale down. External precedent: CK3's dread decay (the
`Forever Infamous` perk exists precisely to *stop* it).
⚠️ Apply the same rule to **Shadow Renown**, which carries the identical *"does not decay
naturally"* clause — fixing one and not the other creates the asymmetry it was meant to remove.
(Deniability Debt's *"−1 per clean season"* is **not** the precedent here: that is a *debt* falling,
which helps the player. It is a precedent for idle seasons moving a track, not for reputation
fading.) Add the missing Renown row to `clock_registry_v30`.

### 7.7 Faction progression
- **Substrate: keep what is ratified.** Derived-buffer income/drain, the five Stability triggers,
  §11's CONVERT/KEEP registry, and the deterministic anti-death-spiral floor at Stability ≤ 2. This
  is the best-disciplined progression machinery in the repository; do not touch it.
- **Add the faction's equivalent of Histories: Institutions.** Durable, purchased, rule-changing,
  and *lateral* — they unlock verbs and change Obs rather than adding stat points. The tree already
  holds the raw material: Charters, Compacts, Facility Tier, Ministries, guild ladders, Entry Terms.
  Each Institution carries a **named liability** in the same entry that grants it (a Charter grants
  revenue *and* opens a Quo-Warranto attack surface; a standing army grants Military *and* creates a
  payroll that collapses on Treasury 0 — both already in the tree).
- **Make Stability's rise as disciplined as its fall.** Five triggers down and passive regeneration
  up is asymmetric. Recommend a mirror set of five rise triggers, so Cohesion is earned, not idled
  into.
- **Extend Ascendancy to the player.** `power_base` + `consolidation_progress` (0–5) + a
  structurally-matched downfall liability is already the strongest in-repo faction-progression
  proposal and is already NERS-validated for NPCs. The player's climb through the Standing ladder
  and into faction emergence is the same shape; running the player on the NPC mechanism is the
  emergence-over-scripting answer.

### 7.8 Resolve Standing, once
**Standing 0–7** (`faction_politics_v30`, CANONICAL, explicitly supersedes the 0–5 track). Correct
`clock_registry_v30`'s 0–5 rows and `player_agency_v30` §5.4's internal contradiction with its own
§6.2. This is a currency correction, not a design change — but leaving three ranges live guarantees
that whoever builds the ladder builds the wrong one.

---

## §8 NUMBERS, AND WHICH OF THEM ARE DEBT

| Quantity | Value | Grade |
|---|---|---|
| Attribute points per campaign | 2–6 | **Derived** from Portrait Retirement's own gate + §2.1's envelope. Defensible. |
| Attribute points per season | ≤ 1 | `[SEED]` — chosen to prevent a burst; untested |
| Creation single-attribute cap | 5 → 6 | **`[BLOCKED]` on falsifier F2.** Do not adopt before the ablation. |
| L1→L2 marks | 3 at Ob ≥ 2 | `[SEED]` — no oracle exists for non-combat pacing |
| L2→L3 marks | 5 at Ob ≥ 3, ≥1 a failure | `[SEED]` |
| Mark eligibility | `Ob ≥ level + 1` | **Structural, not tuned** — the anti-farm invariant |
| Instruction | 1 scene action / season | **Derived** from the 3–5 action budget; self-limiting |
| Renown cap / decay | 10 / −1 per idle season at ≥5 | `[SEED]` on the decay rate; the cap follows Shadow Renown |
| Administration scale / buffer | 0–7 / ×10 | `[SEED]` — matches Stability's shape, no independent basis |

**Honest statement of the oracle problem, since §0.1 point 4 requires it:** `workbench/balance.py`
can measure the Craft clock's effect on personal combat and nothing else. There is **no oracle for
fieldwork** (its sim is pure stub), **none for social contest pacing** (the kernel does not consume
attributes at all), and none for the Standing or Character clocks. Every `[SEED]` above is a number
without a control, and per §0.1 point 4 that means it is not a measurement in either direction —
including the ones that look conservative. §10 sequences the work so the measurable clock lands
first.

---

## §9 FALSIFIERS

Per §0.1 point 3, each claim that gates a decision carries the specific test that would show it
wrong.

- **F1 — "History is inert in threadwork." RUN 2026-08-15. CONFIRMED.** `_actor_pool` with `spirit=3, ts=30` and `history ∈ {0, 3, 7}` returns **pool = 12 in all three cases**; `history = −2` returns 10. History has exactly zero marginal value in every Thread operation for any non-negative score. The formula is a defect, and it is independent of every design decision in this document — fix it either way (§10 step 0).
- **F2 — "Creation cap 5→6 is safe."** `workbench/balance.py all N` with the top-attribute build at 5 versus 6, multi-seed, n ∈ {350, 500}. If the win-rate delta exceeds the established ±4pp noise floor, **the amendment fails and the cap stays at 5.** This is a blocking gate, not advice.
- **F3 — "2–6 attribute points fit the envelope."** Same harness, a baseline build versus that build +4 points distributed to combat-relevant attributes. If the delta exceeds ±4pp — which it very likely will — then the *per-point* effect must be re-examined, and the correct response is to lower the budget, not to widen the envelope.
- **F4 — "Techniques are safe to hand out generously."** Already measured: `test_levers_add_texture_without_shifting_balance` (ED-PC-0022). Re-run it with a larger equipped kit; if aggregate win-rate departs from ~0, the generosity claim fails.
- **F5 — "The no-exchange rule prevents strategy collapse."** Not testable today. There is no multi-subsystem oracle. **Stated as an assumption, not a result.**
- **F6 — "The CP menu never existed."** `git log --all --name-only | grep -c ttrpg_complete` → 0, with a positive control on a file known to exist (`derived_stats_v30` → non-zero). *Run; both results as stated.*

---

## §10 SEQUENCING

Ordered so that each step is either measurable or a pure currency correction.

| # | Step | Gate |
|---|---|---|
| 0 | **Currency corrections** — Standing 0–7 everywhere; Renown row into `clock_registry`; the `history_contrib` defect (F1); the `sim/conviction.py` 9-vs-13 set and the no-op `'Loyalty'` call | none — these are repairs, not design |
| 1 | **Rule OPT-AV-1** (§3). Everything downstream is gated on it; `repo_state_armature_v1` P5 has been blocked on it since 2026-07-20 | Jordan |
| 2 | **Craft clock, combat only** — marks + technique unlocks, measured on `workbench/balance.py` | F2, F3, F4 |
| 3 | **Attribute-point award** wired to Conviction resolution | step 1 + the §7.4 Conviction reconciliation |
| 4 | **Renown symmetry + Standing ladder** | step 0 |
| 5 | **Faction Institutions + Administration** | F-C ruling; SE lane's governance consolidation |
| 6 | **Craft clock extended to fieldwork / contest** | **blocked until those subsystems have engines** — do not extend a progression system into a stub |

Step 6's blocker is the honest one: **you cannot design progression for a subsystem that does not
resolve.** Fieldwork's sim is `stub_resolve` throughout; the social-contest kernel does not read
attributes. Any pacing number written for them today is fiction.

---

## §11 THE CALLS THAT ARE JORDAN'S

1. **OPT-AV-1 — the roster.** Recommended: **C-A, ten attributes.** The live alternative worth your
   eye is **C-D** (fold Attunement into Cognition, 9 attributes). Both §3.6 amendments are separable
   from the roster choice.
2. **Creation cap 5 → 6?** Recommended yes, **blocked on F2**. If the ablation fails, the answer is
   no and the character stays flat.
3. **Attribute points from Conviction resolution — or a CP shop after all?** This is the single
   largest feel decision in the document. The recommendation makes advancement *narrative and rare*;
   the alternative (P1) makes it *legible and player-controlled*. Both are defensible games. They
   are not compatible.
4. **Do Convictions become controlling at high weight?** This deliberately takes agency away from
   the player at the moment they are most invested. It is the most Valorian mechanic in the
   document and the most likely to annoy a player. Your call, not mine.
5. **F-C's Administration stat and the Mandate/Support split** — a real addition to the faction
   sheet, justified in §4 but adding a sixth quantity to a layer whose sim currently reads five.
6. **Renown decay** — reverses an existing explicit rule (*"does not decay naturally"*).
7. **Aging.** Absent corpus-wide. A campaign is 10–15+ seasons and Portrait Retirement is a
   *chosen* ending; whether the body should also impose one is a design question this document
   raises and does not answer.

---

## Appendix — precedent register

| Game | Mechanism taken | Where used here |
|---|---|---|
| **Burning Wheel** | Tests marked by difficulty, success *or* failure; routine work stops counting; artha → slow Epiphany shift | §5 P3 — the Craft clock's mechanism |
| **SaGa / Romancing SaGa** | Sparking: skills emerge from use at difficulty, not from a shop | §5 P2 — the trigger; already cited by `character_histories_v30` |
| **King Arthur Pendragon** | Opposed trait pairs; passions; traits at 16+ become *controlling*; Glory as the headline number | §5 P4, §7.4 — the Conviction upward channel and its agency cost |
| **Crusader Kings III** | Position over power; prestige/piety/legitimacy as losable cohesion vs gold/levies as spendable capacity; dread decay | §4 F-D, §5 P5, §7.6 |
| **Romance of the Three Kingdoms** | Officer rank → governance scope | §5 P5; already cited in `settlement_layer_v30` §6.1 |
| **The Elder Scrolls (Oblivion → Skyrim)** | Use-based advancement and its farming pathology; Skyrim's fix via bounded scaling | §5 P2 — the cautionary case; §7.2's `Ob ≥ level + 1` invariant |
| **Disco Elysium** | Skills as antagonists with a voice; the character is already a specific ruin at hour zero | §3.6 Amendment 2 (sharp creation); §7.4 (Convictions that act on you) |
| **Battle Brothers** | Armour as per-action fatigue cost rather than a max reduction | already adopted at `derived_stats_v30` §4.2 |
| **Darkest Dungeon / Pathologic / Sunless Sea** | Permanent marks that are simultaneously capability and liability | §5 P6, §6 tier 3 |
| **Final Fantasy Tactics / FF VII materia** | Loadout capacity as a stat; equip slots as the scarce resource | §3.6 Amendment 1 — Recall as breadth |
| **EU4 / Victoria** | Institutions that change rules rather than numbers | §7.7 — faction Institutions |

---

*End proposal. PROPOSED — design-only, held for Jordan. Nothing ratified.*
