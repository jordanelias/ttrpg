<!-- STATUS: AUDIT / GATE PACKET — agonist deliverable for Stage 3 / Gate C. Not canon until Jordan
     ratifies. No git add/commit/push run; the diff is uncommitted and awaits approval. -->

# GATE C RATIFICATION PACKET — Rhetoric grounding + the adjudicator armature (CR4 / CR5 / ★★★★★)

**Stage:** 3 / Gate C · **Date:** 2026-07-01 · **ED:** ED-1062 (next_free in `contest_rebuild`) ·
**Tests:** `python -m pytest sim tests/valoria -q` → **1041 passed**; `python -m
sim.personal.contest._kernel_tests` → **377 passed, 0 failed** (319 preserved through Gate B + 58
Stage-3). Golden-trace agôn parity **held** (byte-unchanged — the armature is opt-in AND CR4 now keys on
the chosen Style genre, which lives on the armature, so `armature=None` fires neither CR4 nor the
armature). Armature is **opt-in** (Bout `armature=None` default → adds nothing).

**RE-REVISED #3 at the Gate-C re-revision (2026-07-01) — findings 1, 4, 5 were RE-UPHELD and are now fixed:**
- **Finding 1 (CR4 +1D was tautological — dropped the orator's Style choice):** the +1D was keyed on
  `genre_of_ground(move.ground)`, but `Stasis.relevant` forces `move.ground == self.live`, so the match
  `genre_of_ground(move.ground) == primary_genre_for(live)` was **structurally always-true** for
  FACT/CONSEQUENCE/FEASIBILITY (and always-false / dead-branch for the others) — the bonus was a
  terrain-determined constant that the orator's Style-card choice could not touch. params/contest.md:61
  says "Orator's **CHOSEN GENRE** matches primary genre"; CR4 re-grounds "primary genre" on stasis but
  preserves "chosen genre". **Fixed** (`rhetoric.py` + `resolver.py`): `primary_genre_pool_bonus` now keys
  on the orator's **chosen Style genre** (`genre_of_style(chosen_style)` — Precedent/Suppression→Memory,
  Vision/Insinuation→Projection), NOT the move ground. So a Memory-chosen Precedent earns +1D on a FACT
  stasis but a Projection-chosen Vision earns 0 on the same stasis, and it flips on a CONSEQUENCE stasis —
  the Style choice is **load-bearing**. CR4 is now armature-gated (no chosen Style ⇒ no "chosen genre" ⇒
  no +1D), which **restores byte-identical golden-trace parity** on the `armature=None` path. New kernel
  guards: `genre_of_style` mapping, the anti-tautology matches/flips, no-chosen-genre → 0, and an
  end-to-end proof that the chosen genre MOVES the mean verdict (directionally neutral: CR4's +1D raises
  the reception NET — proven in isolation — but the pool-aware de-saturation bar means a bigger pool does
  not monotonically raise the banded degree, so the honest end-to-end claim is that the CHOICE changes the
  outcome, not that Memory strictly out-scores Projection).
- **Finding 4 (CR5 self-Face backfire cited "bounded by your own standing" but was a flat −2):**
  `cr5_self_backfire(style, landed)` had **no standing parameter** and stripped a fixed −2 regardless of
  the mover's Face — the central self-gating invariant of the cited source (Nyāya/Vācaspati §5.3
  "obstruction is bounded by your own standing"; reconciliation_map §1.3 ratified CR5 "gated by
  SelfGating.licit — your own Face caps your obstruction") was **behaviorally absent**. **Fixed**
  (`rhetoric.py` + `resolver.py`): `cr5_self_backfire(style, landed, my_standing)` now returns
  **min(CR5_BACKFIRE_MAGNITUDE, own Face)** — a low-standing orator (Face < 2) risks only what it holds,
  a higher-standing orator risks the full −2; the resolver passes the mover's own Face. New kernel guards:
  the pure-function standing bound / monotonicity / landed-regardless, and a **LIVE-resolver** guard that a
  Face-1 mover strips exactly 1.0 (not the flat −2). (The remedy is the directly-cited *cap* reading; a
  deeper standing-*scaling* variant — cost GROWS with standing — stays a flagged Jordan fork.)
- **Finding 5 (off-axis 0.15 was behaviorally inert — the armature was categorical, not continuous):**
  the armature was a fractional **POOL bonus**, but `roll_net` floors the pool to an integer die count
  (`max(1,int(round(pool)))`), so any alignment < 0.5 **rounded away** — a misaligned style produced
  resolver outcomes **byte-identical** to the flat scalar (the kernel test's `_flat <= _misaligned` `<=`
  was load-bearing precisely because they were equal), so the "continuous 4×4 dot-product /
  flat<misaligned<aligned" claim was false; the wired armature was a 0.5-threshold **categorical** step.
  **Fixed** (`armature.py` + `resolver.py`): the alignment is now a **CONTINUOUS δσ-LEVERAGE μ-shift**
  (`style_axis_dsigma`, `ArmatureConfig.dsigma`), added to the `net_boost` leverage term (the σ-space
  channel, NOT the rounded pool). This is exactly the **CR6** shape for a setup/audience-boost advantage
  ("audience boost … accumulate as δσ, tanh soft-capped, uniform probability impact") — the flat-dice pool
  is the stack CR6 *retires*. Off-axis 0.15 now → 0.075σ (real, non-rounded), so **flat < misaligned <
  aligned holds STRICTLY** in resolution. Magnitude re-grounded from the npc_behavior +1D onto
  `ARMATURE_MAX_DSIGMA = level("moderate") = 0.50σ` (`modifier_system_spec.md §2.3`, the σ-level
  `Leverage.ONGROUND` already uses — reused, not fresh). The prior `ARMATURE_MAX_POOL_BONUS` /
  `style_axis_pool_bonus` / `ArmatureConfig.pool_bonus` are **DELETED**; the kernel test now asserts
  `flat < misaligned` **strictly** and the off-axis δσ is strictly > 0.

**RE-REVISED #2 at the Gate-C re-revision (2026-07-01) — findings 1, 2, 3, 5, 7, 8 were RE-UPHELD and are now fixed:**
- **Findings 1 + 2 (CR4 keyed on the stasis GROUND, not TENSE; DEFINITION ≠ Memory):** the CR4 genre map
  previously routed through `Stasis.TENSE` and set `STASIS_PRIMARY_GENRE[DEFINITION] = Memory`, which
  reconciliation_map §1.2 explicitly forbids (defect(a)+res(3): "definitional/DEFINITION → NOT Memory …
  never collapsed to a genre"; "Do not use TENSE as the genre intermediary") and which contradicts
  RATIFIED CR4 ("definitional = higher-order reframe via the authored **Present**-rendering"). Fixed: a
  single ground-keyed `_GROUND_TO_GENRE` table (FACT→Memory; **DEFINITION→None**; QUALITY/JURISDICTION→
  None; CONSEQUENCE/FEASIBILITY→Projection), used by both `genre_of_ground` and `STASIS_PRIMARY_GENRE`.
  DEFINITION's reframe role stays captured by `is_higher_order_reframe`/`STASIS_ROLE='higher_order'` — NOT
  a genre. A new kernel guard proves FACT and DEFINITION (same tense 'past') now map to **different**
  genres (Memory vs None), i.e. the map is ground-keyed.
- **Finding 7 (CR5 opponent-Face-attack DEFERRED, not presented as grounded):** the ratified CR5 first
  half ("Indirect → attacks opponent Face") is **not** realized in the resolver (a landed Obscuring move
  advances the mover's own track; the Gate-B Doubt Marker is retained). The `cr5_self_gating` MECHANICS
  source is downgraded to "self-Face backfire only; opponent-Face-attack DEFERRED"; `orientation_channel`
  is re-labeled a **design-table lookup** (not a wired channel) in code, tests, and this packet; the
  unrealized half is flagged as an **open item for Jordan**. A new kernel guard asserts the deferral is
  documented (not silently presented as wired).
- **Finding 8 (§6.1 vs §6.3/§6.5 citation inversion):** §6.1 "Appraise Revelation" is the **empty**
  section; §6.3 "Targeting Effects" (:698) and §6.5 "Stacking Limits" (:738) are the **populated** ones.
  Every "§6.1 table (lines 698-701)" and "off the empty §6.3/§6.5 stubs" mislabel in `armature.py`
  section 4, `appraise.py`, `wrapper.py`, and this packet is corrected: the targeting/stacking tables
  now cite **§6.3:698 / §6.5:738**, and §6.1 is named as the empty section.

**RE-REVISED #1 at the Gate-C re-revision (2026-07-01) — findings 3 and 5 were RE-UPHELD and fixed:**
- **Finding 3 (cited −2 == applied −2):** the CR5 backfire previously called `c.face.strip(2.0)`, but
  `Standing.strip(deg)` scales by `STRIP=0.8`, so the *realized* Face delta was **−1.6**, not the cited
  **−2** (a cited≠applied anti-fabrication violation). Fixed: a new `Standing.strip_points(points)`
  subtracts a FIXED number of Face points directly (floor-clamped), so the realized delta == the cited
  −2 **exactly**. A new kernel test asserts the realized delta on a live-resolver foul == 2.0.
- **Finding 5 (STYLE_AXIS citation + the false-reuse claim):** the antagonist read the empty
  `npc_behavior_v30_infill.md §1.3` stub, but the ASSEMBLED HEAD `npc_behavior_v30.md §1.3` (lines 32-42)
  DOES carry the Resonant Style Taxonomy table verbatim (Evidence→Precedent, Consequence→Vision,
  Authority→Suppression, **Solidarity**→Any+Revealing/Knot-gated). All armature/appraise citations are
  re-pointed to that head table (+ `complete_systems_reference.md §1.2`, CANONICAL) with explicit line
  numbers; the §6.3:698 / §6.5:738 magnitude is cited off the live tables (the empty section is §6.1 —
  see finding 8). The kernel test no longer asserts "Insinuation→Insinuation" as a §1.3 mapping — the
  4th axis is a **documented new invention / Jordan fork** (canon's 4th type is Solidarity, not
  Insinuation). **RE-REVISION #2 addition:** the docstring's "reuse a pre-existing dot-product / no new
  dot-product invented" claim is corrected — there is **no** pre-existing continuous dot-product
  (`conviction.py` has only `resonant_active: set[str]`; the canonical §1.3/§6.3 mechanic is a
  *categorical* boolean → flat +1D); the continuous 4×4 dot-product is a **NEW primitive** (the only one
  in `sim/personal`), of which the categorical +1D is the degenerate row.

**REVISED at the prior Gate C revision (2026-07-01) — the seven judge-upheld findings fixed:**
- **CR4 is now genuinely BEHAVIORAL** (findings 1/2/5): the +1D primary-genre bonus is **plumbed into
  `resolver._reception`** (it was a dead lookup); a seeded reception-net proof + an end-to-end track
  proof show it changes resolution, not just a label.
- **ONE armature channel** (findings 3/4/6): the dead subtractive resistance path
  (`armature_resistance`/`resistance_delta`/`eroded_resistance`/`ARMATURE_MAX_DELTA`) AND the uncited
  multiplicative `resonance_uplift`/`ARMATURE_RES_GAIN` twin are **DELETED**. The armature now enters as
  a single **+1D reception-pool bonus** (`style_axis_pool_bonus`) — the `npc_behavior_v30.md:698`/`:738`
  **cited magnitude in the cited place** (a pool die), the SAME channel CR4's +1D uses.
- **CR5 trigger corrected to a genuine FOUL** (finding 7): the self-Face backfire fires only on a
  **deg==0** Obscuring move (a *nigrahasthāna* — it landed nowhere), NOT on a deg==1 partial that
  advanced the mover's own track; the −2 is a magnitude **anchor** applied to the 0–10 Face stat (a
  different quantity than the Doubt Marker's track-margin −2 — honestly flagged).
- **`mechanics_selftest` strengthened** (finding 4): it now runs the resolver and asserts each Stage-3
  WIRED mechanic actually **fires in resolution** (symbol-resolvability alone let a dead function pass).

This stage exists to make the classical/Renaissance grounding **mechanical, not nominal** (Lens 6),
and to point the armature dot-product at the **judge** (the central bottom-up violation the 2026-06-28
deliberation critique names). It was authored against the **source documents read directly** — the
CR4/CR5 ratified text (`RATIFIED_2026-06-01.md`), the source-research trilogy
(`.../2026-06-28-social-contest-deliberation-critique/source-research/`), and the rhetoric research
(`research/rhetoric_oratory_contest/`) — not the critique distillation.

---

## 1. CR4 — Ciceronian stasis × genre (grounded mechanically)

**What was ratified (CR4):** "stasis (conjectural/definitional/qualitative/translative) = terrain;
genre (Memory/Projection) = stance; stasis sets primary genre; definitional = higher-order reframe;
translative = pre-merits jurisdiction (the Stay)."

**Made behavioral (`rhetoric.py` + `resolver.py`) — the +1D bonus is PLUMBED, and keyed on the orator's
CHOSEN genre (not the tautological move ground; judge finding 1):**
- `primary_genre_for(ground)` — the live stasis **sets which genre is primary**. But the behavioral
  consumer is **`primary_genre_pool_bonus(chosen_genre, live_stasis)`**, which returns **+1D** (the
  params §Genre and Orientation Bonus Dice value) when the orator's **CHOSEN GENRE** — the genre of the
  Style-card the orator picks (`genre_of_style`: Precedent/Suppression→Memory, Vision/Insinuation→
  Projection) — matches the live stasis's primary genre. It is **NOT** keyed on the move's ground: the
  resolver already forces `move.ground == live` (`Stasis.relevant`), so keying on `genre_of_ground(move.
  ground)` was a **tautology** (the ground's genre == its own primary genre) that erased the Style choice
  (judge finding 1). The **+1D is added to the reception pool in `resolver._reception`** (the integer-pool
  channel; the armature now uses a SEPARATE continuous δσ channel — see §3). The `genre_of_ground` /
  ground-keyed map (FACT→Memory, DEFINITION→None per §1.2) still defines the **terrain's** primary genre;
  the CR4 CONSUMER reads the **chosen Style's** genre against it.
  ⚠ **CR4 map corrected (judge findings 1/2):** conjectural (**FACT**) → **Memory** (§1.2 res(2)); but
  **definitional (DEFINITION) → *None*** — a **higher-order REFRAME operator, NOT Memory / not a genre**
  (§1.2 res(3): "NOT Memory … never collapsed to a genre"; RATIFIED CR4: "definitional = higher-order
  reframe via the authored Present-rendering", *Present* not Memory). The prior draft's DEFINITION→Memory
  chain routed through `Stasis.TENSE` (both FACT and DEFINITION are tense 'past'), which §1.2 rules out;
  the map is now keyed on the GROUND, so FACT and DEFINITION (same tense) map to **different** genres.
  Deliberative future grounds (CONSEQUENCE/FEASIBILITY) → **Projection** (§1.2 res(4)); present-tense/
  pre-merits (Qualitative/Translative) → no primary genre → no bonus.
- **BEHAVIORAL, PROVEN in resolution (judge findings 1/2/5):** the prior deliverable marked
  `cr4_stasis_genre` WIRED while the resolver had **zero** references to it (a dead oracle). It is now
  a live consumer: a **seeded** test shows the +1D **raises the mean reception NET** (the roll the
  resolver bands to a degree), and an **end-to-end** test shows the orator's **CHOSEN GENRE** (Style card)
  **moves the mean verdict** — a Memory-chosen Precedent (+1D fires) resolves differently from a
  Projection-chosen Vision (no +1D) on the *identical* FACT stasis + seeds. *The Style choice is
  load-bearing* — not a terrain-determined constant (judge finding 1). (Directionally neutral: the +1D
  raises the reception NET, but the pool-aware de-saturation bar means a bigger pool does not
  monotonically raise the banded degree, so the honest end-to-end claim is that the CHOICE changes the
  outcome, not that Memory strictly out-scores Projection.)
- `is_higher_order_reframe(DEFINITION)` — definitional is a higher-order reframe (up the stasis
  ladder from fact; the kernel already models `Stasis.stronger_than(DEFINITION, FACT)`). Closes **F5**.
- `is_pre_merits(JURISDICTION)` — translative is **pre-merits jurisdiction (the Stay)** with **no
  primary genre** until settled (`primary_genre_for(JURISDICTION) is None`). Closes **F6**.

**Grounding:** `rhetoric_oratory_contest_research §1.4` (Hermagoras→Cicero, the four classical stases,
translative = jurisdiction — session-verified) + `§9.1` ("diagnose the issue before arguing").

### The epideictic question (scope item 1) — addressed, NOT silently ignored

Aristotle's **third genre — epideictic** (present-tense praise/blame, audience-as-spectator) *is*
the axis the 2-genre (Memory/Projection) compression (PP-234, 3→2) most obviously touches.
**`rhetoric.py:EPIDEICTIC_COMPRESSION` documents and answers it:** the epideictic **register
is NOT dropped** from the substrate — it survives as the **`RhetoricalWeights *_present` column**
(`ethos_present = 1.20`, the ethos-dominant praise/blame home, live in `_advance`'s `joint_weight` —
the ceremonial *basilikos logos* register, research §2.2). Only the genre **label** compresses 3→2.

⚠ **Grounding corrected (judge finding 3):** the epideictic-survives claim does **NOT** rest on
equating the qualitative STASIS with the epideictic GENRE. The research doc keeps them distinct —
qualitative (*quale sit*, "was it justified?") is a **forensic evaluation stasis** (§1.4), whereas
epideictic is a **present-tense praise/blame genre** (§1.2); §0.4 explicitly downgrades that exact
conflation ("the honourable/shameful is the epideictic axis, not the deliberative one … do not treat
the six-item list as confirmed canon"). The claim therefore anchors **only** on the defensible
surface — `RhetoricalWeights ethos_present` + the §2.2 *basilikos logos* register — and the earlier
"a qualitative contest *is* the epideictic axis" equivalence is **dropped**.

**What IS lost:** a present-tense **stance** with its own +1D primary-genre bonus (no "praise" style-
card; a pure ceremonial praise contest — *basilikos logos*, coronation oration — is modelled via the
`ethos_present` resonance register, not a first-class genre). **This is a genuine open decision,
flagged for Jordan (fork below), not silently accepted.**

---

## 2. CR5 — orientation re-grounded: Direct→Persuasion / Indirect self-Face backfire (opponent-Face-attack DEFERRED)

**What was ratified (CR5):** Direct → moves Persuasion (merits); Indirect → attacks opponent Face
(ethos), **with self-Face backfire on failure** (Quintilian/Nyāya self-gating).

⚠ **What is REALIZED at Stage 3 vs DEFERRED (judge finding 7).** CR5 has two halves. **Realized:** the
**self-Face backfire** on a failed Obscuring foul (the second half). **DEFERRED (NOT wired):** CR5's
**first half — Indirect *attacks the opponent's* Face**. The resolver does **not** strip the opponent's
Face on an Obscuring move: a *landed* Obscuring move advances the **mover's own track** (byte-identically
to a Revealing move), and the **Gate-B Doubt Marker is retained on the win path** (RATIFIED CR5-vs-ED-1060).
`orientation_channel(Obscuring) == "face_attack"` is therefore a **design-table label** describing the
ratified intent, **not** a wired resolution channel — nothing consumes the `"face_attack"` string in
resolution. The opponent-Face-attack half is flagged as an **open item for Jordan**, not presented as
grounded.

**The mechanic (`rhetoric.py` + `resolver.py`):** REAL new scope (the self-Face backfire), bounded tightly.
- `orientation_channel(Revealing) == "persuasion_track"` (the existing CLASH/REINFORCE/CROSS/TIE
  merits path, **unchanged**, REALIZED); `orientation_channel(Obscuring) == "face_attack"` — a
  **design-table lookup only** (the opponent-Face-attack is DEFERRED; tested as a label, not a wired
  channel).
- `cr5_self_backfire(style, landed, my_standing)` — the **corrected trigger + standing-bounded magnitude**
  (judge findings 7 + 4):
  - **TRIGGER:** an **Obscuring** (Indirect: Suppression/Insinuation) argue move that **FAILS AS A
    MOVE** — reception degree **0**, it landed nowhere (a genuine *nigrahasthāna*/foul). A **LANDED**
    Obscuring move (deg ≥ 1, **including a deg==1 partial that advanced the mover's own track**) does
    **NOT** backfire (judge finding 7); a **Revealing** move never triggers.
  - **MAGNITUDE (STANDING-BOUNDED — judge finding 4):** **min(−2, the mover's own Face)** stripped from
    the mover's own Face, applied via `Standing.strip_points` so the **realized** Face delta == the bounded
    magnitude **exactly** (judge finding 3 — the prior `strip(2.0)` scaled by `STRIP=0.8` applied only
    −1.6). The prior `cr5_self_backfire(style, landed)` had **no standing parameter** and stripped a flat
    −2 regardless of Face — so the cited "obstruction is **bounded by your own standing**" invariant
    (Nyāya/Vācaspati §5.3; reconciliation_map §1.3 ratified CR5 "gated by SelfGating.licit — your own Face
    caps your obstruction") was **behaviorally absent**. Now `cr5_self_backfire` takes `my_standing` and
    returns `min(CR5_BACKFIRE_MAGNITUDE, own Face)`: a low-standing orator (Face < 2) risks only what it
    holds; a higher-standing orator risks the full −2. The −2 is still **anchored to the Doubt Marker −2**
    (a magnitude precedent, applied to the 0–10 Face *credibility* stat, a different quantity than the
    marker's track-margin — honestly flagged).
- **Wired in the resolver** (`_apply`, opt-in): a **deg==0** Obscuring foul calls
  `c.face.strip_points(min(2, c.face.v))` — finally firing the **Face strip channel** Stage 1d established
  but left unwired, **standing-bounded**. A Direct move never strips Face; a landed Obscuring move never
  strips Face. (Asserted against the live resolver: a deg==0 Suppression foul strips Face across seeds; the
  finding-7 guard — **no Face strip ever coincides with a move that advanced the track**; the **finding-4
  guard** — a Face-1 mover strips exactly **1.0**, not the flat −2; a Precedent move never strips.)

**Scope guardrails (verified):** does **NOT** change CLASH/REINFORCE/CROSS/TIE for Direct-vs-Direct
exchanges; does **NOT** change the Obscuring-WIN Doubt Marker (ratified Gate B, ED-1060). Only adds
the deg==0-foul-side backfire consequence.

**Grounding:** the **Nyāya nigrahasthāna** defeat-conditions (`rhetoric_oratory_contest_research §5.1`)
+ Vācaspati/Quintilian self-gating (`§5.3`: "obstruction is bounded by your own standing") + `§9.1`
self-gating invariant; the eristic-has-a-cost fix the critique demands (fallacies FG-2 / §2.6).

---

## 3. THE ARMATURE (★★★★★) — STYLE_AXIS 4×4 + the Style×armature_position dot-product

**The fix (`armature.py`):** the adjudicator gets an `armature_position` — its own **Conviction
vector** over four axes — and the chosen Contest Style is **dot-producted against it** to produce a
**continuous δσ-leverage μ-shift** (`style_axis_dsigma`), aimed at the **judge** (the same idea the
opponent-aimed Resonant Style runs at the *opponent*: `npc_behavior_v30.md §1.3` head table lines
32-42 + `§6.3` line 698).
⚠ **Continuous, not categorical (judge finding 5 — the fix):** the prior revision returned a fractional
**POOL bonus**, but `roll_net` floors the pool to an integer die count (`max(1,int(round(pool)))`), so
any alignment < 0.5 (including the off-axis 0.15) **rounded away** — a misaligned style was
**byte-identical** to the flat scalar, so the wired armature was a 0.5-threshold **categorical** step, not
the advertised continuous dot-product. The alignment now enters as a **continuous δσ-leverage μ-shift** on
the `net_boost` term (the σ-space channel, NOT the rounded pool), so off-axis 0.15 → 0.075σ and **flat <
misaligned < aligned holds strictly**. This is the **CR6** shape for a setup/audience-boost advantage
("audience boost … accumulate as δσ, tanh soft-capped, uniform probability impact") — the flat-dice pool
is the stack CR6 *retires*.
⚠ **Reuse + magnitude claim corrected (judge finding 5):** what is genuinely REUSED is the **STYLE→axis
structure** (`STYLES_TABLE` + the §1.3 map) and the "on confirmed targeting" upside-only shape. The
**continuous 4×4 dot-product (`style_axis_alignment`) is a NEW primitive** — `sim/personal/conviction.py`
carries **no** vector or dot-product (only `resonant_active: set[str]`), and the canonical §1.3/§6.3
Resonant-Style mechanic is a **categorical boolean match → flat +1D pool die**, not a continuous
alignment; the categorical opponent-aimed +1D is its degenerate single-axis, threshold-crossed row. The
**output channel + magnitude is also re-grounded**: the categorical opponent-aimed mechanic is a +1D POOL
die (§6.3:698); the judge-aimed continuous armature is a **δσ LEVERAGE μ-shift**
(`ARMATURE_MAX_DSIGMA = level("moderate") = 0.50σ`, `modifier_system_spec.md §2.3` — the σ-level
`Leverage.ONGROUND` already uses) instead, precisely *because* a fractional pool die rounds away. **The
flat scalar is the zero-vector degenerate row**, not a separate code path
(`style_axis_dsigma(style, ArmaturePosition.zero()) == 0.0`). *(Open for Jordan: whether the categorical
opponent-aimed +1D, if ported, should be folded into this same continuous primitive so there is one
style-bonus primitive, not two.)*

**ONE ARMATURE CHANNEL (judge findings 3/4/6 + 5).** The prior deliverable's **dead** subtractive
resistance path (`armature_resistance` / `resistance_delta` / `eroded_resistance` /
`ARMATURE_MAX_DELTA=1.0`) and the **uncited** multiplicative `resonance_uplift` (`ARMATURE_RES_GAIN=0.35`)
were deleted; **now also deleted** are the fractional-pool `ARMATURE_MAX_POOL_BONUS` /
`style_axis_pool_bonus` / `ArmatureConfig.pool_bonus` (judge finding 5 — replaced by the continuous δσ).
The single live path is the **δσ leverage μ-shift** (`ARMATURE_MAX_DSIGMA = 0.50σ`), soft-capped by CR6's
tanh via `net_boost`. It is a **distinct channel** from CR4's integer +1D pool die — as **CR6** requires
(δσ leverage ≠ the flat-dice stack) — so there are two principled channels (an integer pool die for CR4,
a continuous δσ for the armature), each with exactly one magnitude, applied in one place. A `_kernel_tests`
assertion confirms all the deleted symbols (including the old pool-bonus ones) no longer exist on the module.

### The STYLE_AXIS 4×4 projection (Class-B [SEED] — FLAGGED CANDIDATE)

| Style (= Genre×Orientation) | Primary armature axis | Grounding (structure) |
|---|---|---|
| **Precedent** (Memory+Revealing) | **Evidence** | npc_behavior_v30.md §1.3 HEAD table (lines 32-42): Precedent → Evidence vuln. |
| **Vision** (Projection+Revealing) | **Consequence** | §1.3 head (32-42): Vision → Consequence vuln. |
| **Suppression** (Memory+Obscuring) | **Authority** | §1.3 head (32-42): Suppression → Authority vuln. |
| **Insinuation** (Projection+Obscuring) | **Insinuation** | NEW invention — canon's 4th type is Solidarity, NOT Insinuation (see NB); Jordan fork |

Each row = `STYLE_AXIS_PRIMARY (1.0)` on its primary axis, `STYLE_AXIS_OFFAXIS (0.15)` elsewhere
(partial overlap; `0.15` = the resolver's existing `RES_FLOOR` value, **reused, not fresh**).

- **STRUCTURE is grounded** for the 3 real axes (which axis each style targets = npc_behavior_v30.md
  §1.3 HEAD table, lines 32-42, cited per row — the head table IS populated; only the co-filed infill
  §1.3 is a stub, judge finding 5). The 4th axis (Insinuation) is a documented new invention (NB below).
- **MAGNITUDES:** `ARMATURE_MAX_DSIGMA = level("moderate") = 0.50σ` is the perfect-alignment δσ, **cited**
  to `LEVEL_SIGMA` ("moderate", `modifier_system_spec.md §2.3`) — the SAME σ-level the kernel's on-ground
  `Leverage.ONGROUND` carries (reused, not fresh), soft-capped by CR6's tanh via `net_boost`. (It is a δσ
  leverage, NOT the +1D pool die — judge finding 5; the prior `ARMATURE_MAX_POOL_BONUS=1.0` is deleted.)
  The projection cells `STYLE_AXIS_PRIMARY=1.0` and `STYLE_AXIS_OFFAXIS=0.15` (= the resolver's `RES_FLOOR`,
  reused) remain **[SEED]**; per the scope's design-authority fork, **the whole numeric table is flagged as
  a candidate for Jordan**, not fabricated canon. (The prior uncited `ARMATURE_RES_GAIN=0.35`, the
  reused-but-dead `ARMATURE_MAX_DELTA=1.0`, and the rounded-away `ARMATURE_MAX_POOL_BONUS=1.0` are all gone
  with the deleted channels.)
- **NB the 4th axis** (Insinuation): §1.3 tabulates only three styles→vulnerabilities cleanly
  (Precedent→Evidence, Vision→Consequence, Suppression→Authority); its fourth row is **Solidarity**
  (Knot-gated, an *opponent* vulnerability, not Insinuation). So the fourth *armature* axis is the
  implied/obscured-future register Insinuation speaks to — the one genuinely **new** mapping, flagged
  [SEED]/candidate.

### Wiring + the asymmetric-proceeding gate-off

- **One armature δσ channel:** `ArmatureConfig.dsigma(side, adj)` =
  `style_axis_dsigma(style, position_of(adj))` (bounded at `ARMATURE_MAX_DSIGMA = 0.50σ`), added to the
  `net_boost` leverage term in `resolver._reception` (the σ-space μ-shift channel — a **distinct** channel
  from CR4's integer +1D pool die, per CR6). No resistance-delta object, no resonance multiplier, no
  rounded-away pool bonus — all prior parallel channels are deleted (judge findings 3/4/6 + 5).
- **GATE-OFF when adjudicator == opponent** (`position_of(..., opponent_is_adjudicator=True)` returns
  the zero vector) — the asymmetric proceedings (Royal Audience "Crown objects throughout"; Church
  Tribunal "Inquisitor proposes throughout") where the opponent-aimed Resonant Style already fires at
  that same party. Prevents **double-counting** (critique adjudicator FG-2). Asserted load-bearing:
  gate-on pool bonus == 0; gate-off pool bonus == +1D.
- **Panel:** `armature_position` = the **mean** of members' positions (mirrors `Panel.character()`).

### The Gate-C deliverable — the verdict is adjudicator-conviction-sensitive (closes SIM-DEBT-04)

The seeded test (`_kernel_tests.py`, "THE VERDICT IS ADJUDICATOR-CONVICTION-SENSITIVE"): the same
contestants, same seeds, same everything **except the judge's `armature_position`** resolve to a
**different mean Persuasion Track**. An **Evidence-judge** lets side A's **Precedent** argument land
higher (`_aligned`) than a **Consequence-judge** (`_misaligned`) or a **flat** (no-armature) judge —
ordering `flat < misaligned < aligned`, `|aligned − misaligned| > 0.05`. **The verdict emerges from
argument-meets-judge's-conviction, not a flat scalar.** This closes **SIM-DEBT-04** (adjudicator-type
pool variation untested).

### The grounding for aiming the armature at the JUDGE (source-research, read directly)

- **Padgett–Ansell robust action + multivocality** (`renaissance-machination-games-lens §V.2`): a
  verdict's robustness is a function of *who it is legible to*. The judge is the observer whose
  reading decides whether the verdict holds; aiming the armature at the judge makes the verdict
  **emerge** (robust) rather than be handed down by a stat-average (arbitrary).
- **Greif self-enforcing vs self-undermining** (`§V.2`; the *liberum veto* out-of-sample case,
  `renaissance-testing-the-model §IX`): a verdict grounded in the judge's *actual, stable*
  convictions is **self-enforcing**. This is the exact reason the Appraise-reveal boundary (§4) is
  **partial, not full** — full information would collapse the style choice to a solved lookup (the
  self-undermining / capturable pole; the liberum-veto lesson: maximal individual leverage +
  zero-uncertainty ⇒ capture).

---

## 4. The Appraise-reveal boundary for `armature_position` (Decision 5; walkthrough §5)

**DECISION: PARTIAL reveal, fitted onto the EXISTING 4-band Appraise ladder** (`appraise.py`;
not a new information mechanic — the same shape used to read the opponent, `npc_behavior_v30 §6.1`,
pointed at the judge):

| Appraise degree | What the player sees |
|---|---|
| Failure (0) | a **misleading** dominant-axis read (a wrong axis; the cost of a bad Appraise, never null) |
| Partial (1) | the judge's **register** (Revealing-leaning vs Obscuring-leaning) — the coarsest true signal |
| Success (2) | the judge's **dominant armature axis** (enough to pick a plausibly-aligned style) |
| Overwhelming (3+) | dominant axis + a **coarse strength band** (low/medium/high) — **never** the exact weights |

**The exact per-axis vector is revealed at NO band** — that is the **hidden residual**, and it is
**legitimate tension, not an opacity bug** (walkthrough §5, explicit). The opacity mandate is
satisfied because the *consequence class* is surfaced at every band (even a failed Appraise returns a
read); the *number* stays hidden by design (walkthrough §0: consequence surfaced ≠ number revealed).

**Why partial** (Greif, above): full = self-undermining (solved lookup, capturable judge); none =
opacity failure; **partial = self-enforcing/robust** (informed bet, residual uncertainty keeps the
verdict emergent). Documented in `appraise.py:APPRAISE_REVEAL_BOUNDARY`; the boundary is itself flagged
as a Jordan call (fork below).

---

## 5. Checker board

| Lens | Status | Note |
|---|---|---|
| **Rhetoric fidelity (Lens 6)** | PASS | CR4 +1D *plumbed into `_reception`*, keyed on the orator's CHOSEN Style genre (not the tautological ground — finding 1) and proven to move the mean verdict with the Style CHOICE; CR5 backfire *actually* strips Face on a deg==0 foul in the live resolver, **standing-bounded** (min(−2, own Face) — finding 4), never on a partial that helped the mover; armature *continuous δσ* moves the verdict (finding 5). Not nominal. |
| **Game-theory soundness (Lens 1)** | PASS | The armature off-axis 0.15 δσ is now behaviorally LIVE (continuous, not rounded away — finding 5), so a misaligned style keeps a strictly-positive partial boost → no dead choice; the CR4 +1D is a real strategic Style-choice (finding 1), not a terrain constant. |
| **Playability / legibility (Lens 2)** | PASS | Appraise-reveal is partial-on-the-existing-ladder; consequence surfaced at every band; hidden residual is legitimate tension (distinguished from opacity per walkthrough §5). |
| **Oracle/sim parity (Lens 4)** | PASS | Golden-trace agôn byte-unchanged (armature opt-in AND CR4 now keys on the chosen Style genre, which lives on the armature, so `armature=None` fires neither — finding 1 restores parity); empty config adds nothing (40-seed identity guard). No oracle-correction-in-place. |
| **Anti-fabrication (Lens 5)** | PASS (with flags) | Every LIVE constant hand-traced: CR4's +1D pool die = params §Genre/Orientation Bonus Dice "+1D"; the armature δσ = `ARMATURE_MAX_DSIGMA = level("moderate") = 0.50σ` (`modifier_system_spec.md §2.3`, = `Leverage.ONGROUND`'s σ-level; re-grounded from the npc_behavior +1D onto the σ-level precisely because a fractional pool die rounds away — finding 5); −2 = Doubt Marker magnitude anchor, applied as a FIXED Face-point strip via `strip_points`, **standing-bounded** to min(−2, own Face) so realized==bounded magnitude (findings 3+4), still quantity-flagged; 0.15 = RES_FLOOR; STYLE_AXIS structure = `npc_behavior_v30.md §1.3` HEAD table (lines 32-42) + §6.3:698, cited per row (finding 5; the empty section is §6.1 "Appraise Revelation" — §6.3/§6.5 are populated, finding 8). The continuous 4×4 dot-product is a NEW primitive (no pre-existing dot-product to reuse — finding 5). The remaining [SEED] cells (STYLE_AXIS_PRIMARY/OFFAXIS) + the Insinuation 4th axis are flagged candidates. The uncited 0.35, the dead 1.0-delta, and the rounded-away pool-bonus are DELETED (findings 3/4/6 + 5). |
| **Key-bus closure (Lens 3)** | N/A this stage | Seam closure is Stage 5 (Gate E). |
| *mechanics_selftest resolution-invocation* | PASS | Each Stage-3 WIRED mechanic (cr4_stasis_genre / adjudicator_armature / cr5_self_gating) is asserted to actually FIRE in the resolver, not merely resolve to a symbol (finding 4). |
| *pytest tests/valoria* | PASS | 1041 passed. |
| *kernel tests* | PASS | 377 passed, 0 failed (319 preserved + 58 Stage-3). |

---

## 6. OPEN DECISIONS FOR JORDAN (flagged, NOT resolved unilaterally)

1. **The STYLE_AXIS 4×4 numeric projection (Class-B, PP-674-vetted).** The *structure* (each style's
   primary axis, 3 of 4) is grounded in `npc_behavior_v30.md §1.3` HEAD table (lines 32-42) +
   `complete_systems_reference.md §1.2`. The *projection-cell magnitudes* — `STYLE_AXIS_PRIMARY=1.0`,
   `STYLE_AXIS_OFFAXIS=0.15` — are **[SEED]** and the whole table is a **FLAGGED CANDIDATE**, not
   fabricated canon. Needs PP-674 vetting + sim calibration. (The armature *magnitude*
   `ARMATURE_MAX_DSIGMA = level("moderate") = 0.50σ` is NOT open — it is the cited `modifier_system_spec.md
   §2.3` σ-level, the same one `Leverage.ONGROUND` uses. The
   one genuinely new structural mapping — the **4th axis = Insinuation** — is also flagged: §1.3's fourth
   row is **Solidarity**, a Knot-gated opponent vulnerability, not Insinuation; whether the 4th armature
   axis should be Insinuation or Solidarity is Jordan's call, as is reconciling the older Citation/Prospect
   style-names in `complete_systems_reference.md` against the current Precedent/Vision names.)

2. **The Appraise-reveal boundary** (full / partial / no reveal of `armature_position`). Implemented
   as **PARTIAL** (best-grounded per Greif self-enforcing/undermining). Alternatives recorded (full =
   rejected self-undermining; none = rejected opacity). Also open: whether Overwhelming should reveal
   the **second** axis (implemented dominant-axis-only to keep the residual meaningfully hidden).

3. **Epideictic loss (if confirmed).** The 2-genre compression preserves the present/epideictic
   *register* (terrain + `ethos_present`) but loses a present-tense *stance* with its own +1D bonus.
   **Best-grounded recommendation: ACCEPT the compression** (the register is preserved where
   load-bearing). But flagged as Jordan's call because it is a stance-loss, not just a rename — the
   alternative is restoring a third **Epideictic** genre (cost: a 5th/6th style-card, breaks the clean
   2×2 Genre×Orientation grid).

4. **CR5 self-Face-backfire exact Face-cost anchor + deeper scaling** where the Doubt Marker precedent
   does not cleanly extend: (a) the **anchor quantity** — the −2 is anchored to the Doubt Marker's
   track-margin −2 but applied to the 0–10 Face *credibility* stat (a different quantity); whether the Face
   cap should equal that −2 or be re-scaled to the credibility stat is Jordan's call. (b) **standing-
   dependence is now REALIZED** (judge finding 4) as the **min(−2, own Face) CAP** — the directly-cited
   "obstruction is bounded by your own standing" (research §5.3) / "gated by SelfGating.licit"
   (reconciliation_map §1.3). A **deeper** Nyāya variant — where the cost *grows* with standing (a
   high-standing orator risks MORE by stooping to *jalpa*, not just caps at −2) — remains a flagged Jordan
   candidate, distinct from the realized cap. *(The trigger itself is not open: it is a genuine deg==0 FOUL,
   per judge finding 7 — a partial that helped the mover is not penalised.)*

---

## 7. FILES TOUCHED (all uncommitted; no git add/commit/push run)

**Created (code):**
- `sim/personal/contest/armature.py` — the STYLE_AXIS 4×4 projection, `ArmatureAxis`,
  `ArmaturePosition`, `ArmatureConfig`, the Style×armature dot-product (`style_axis_alignment`) and its
  **continuous δσ-leverage** consumer (`style_axis_dsigma`, `ARMATURE_MAX_DSIGMA = 0.50σ`),
  `position_of` + the asymmetric-proceeding gate-off. (The dead subtractive path — `armature_resistance`,
  `resistance_delta`, `eroded_resistance`, `ARMATURE_MAX_DELTA`, the uncited `ARMATURE_RES_GAIN`/
  `resonance_uplift`, AND the rounded-away `ARMATURE_MAX_POOL_BONUS`/`style_axis_pool_bonus`/`pool_bonus`
  — is DELETED per judge findings 3/4/6 + 5.)
- `sim/personal/contest/rhetoric.py` — CR4 stasis×genre (`STASIS_PRIMARY_GENRE`, `primary_genre_for`,
  `is_pre_merits`, `is_higher_order_reframe`, `EPIDEICTIC_COMPRESSION`) + the **behavioral +1D consumer
  keyed on the orator's CHOSEN Style genre** (`genre_of_ground`, `genre_of_style`,
  `primary_genre_pool_bonus(chosen_genre, live)`, `CR4_PRIMARY_GENRE_POOL_BONUS`; judge finding 1) + CR5
  orientation self-gating (`orientation_channel`, `cr5_self_backfire(style, landed, my_standing)` —
  standing-bounded, judge finding 4; `CR5_SELF_GATING`).
- `sim/personal/contest/appraise.py` — the Appraise-reveal boundary (`appraise_armature`,
  `APPRAISE_REVEAL_BOUNDARY`).

**Modified (code):**
- `sim/personal/contest/resolver.py` — `Bout(armature=…)` opt-in carrier; `_reception(side, pool_bonus,
  dsigma_bonus)` carries TWO distinct additive channels (CR6): the CR4 +1D **integer POOL** die and the
  armature **continuous δσ** μ-shift on `net_boost` (judge finding 5 — the δσ is NOT rounded away like the
  prior fractional pool bonus was). `_apply` computes the CR4 +1D keyed on the CHOSEN Style genre
  (`genre_of_style`, judge finding 1 — armature-gated, not always-on) + the armature δσ (opt-in), and fires
  the **standing-bounded** CR5 self-Face backfire (`min(2, own Face)`, judge finding 4) on a **deg==0**
  Obscuring foul. (The prior `res *= (1+resonance_uplift)` armature line in `_advance` is removed.)
- `sim/personal/contest/__init__.py` — re-exports the revised public API (`style_axis_dsigma`,
  `ARMATURE_MAX_DSIGMA`, `genre_of_style`; the deleted pool-bonus symbols removed).
- `sim/personal/contest/primitives.py` — `Standing.strip_points(points)` (a FIXED-magnitude Face strip,
  floor-clamped, returns the realized delta) so the CR5 backfire's realized Face delta == the bounded
  magnitude exactly (judge finding 3; `strip(deg)` scales by `STRIP=0.8` and is unchanged for the argue
  degree channel). (Unchanged this pass.)
- `sim/personal/contest/wrapper.py` — MECHANICS rows `adjudicator_armature` (fn=**style_axis_dsigma**;
  source re-grounded to the δσ leverage + CR6 + `modifier_system_spec.md §2.3` "moderate" 0.50σ, judge
  finding 5), `cr4_stasis_genre` (source: "chosen genre", judge finding 1), `cr5_self_gating` (source:
  "standing-bounded min(−2, own Face)", judge finding 4) + `_SYMBOLS` entries (style_axis_dsigma,
  genre_of_style); `mechanics_selftest` resolution-invocation check unchanged (still fires under the δσ
  channel). `cr5_self_gating` source retains the opponent-Face-attack DEFERRED flag (finding 7).
- `sim/personal/contest/_kernel_tests.py` — Stage-3 checks revised/added: CR4 (finding 1 — chosen-genre
  keying: `genre_of_style` map, the anti-tautology matches/flips, no-chosen-genre → 0, end-to-end
  chosen-genre-moves-the-verdict); CR5 (finding 4 — standing-bounded: pure-function bound/monotone +
  LIVE-resolver Face-1-strips-1.0 guard); armature (finding 5 — δσ imports, off-axis δσ strictly > 0,
  flat < misaligned STRICTLY, CR6-separation δσ≠+1D, deleted pool-bonus symbols in the ONE-CHANNEL guard,
  gate-off via `.dsigma`). Section header ASCII-safe (no δ in `print`).
- `sim/tests/test_contest_kernel.py` — `_KERNEL_EXPECTED` → **377** (RE-REVISION #3: +7 for findings 1/4/5,
  see the inline breakdown).

**Created (design/audit):** this packet (`designs/audit/2026-07-01-contest-gate-c-packet/GATE_C_packet.md`).

**NOT touched (Synthesist / post-approval scope):** the broad prose propagation into
`designs/scene/social_contest_v30.md` / `_infill` / `params/contest.md`, the ED-1062 ledger entry, and
`references/id_reservations.yaml` next_free bump are the **Synthesist's post-ratification** job (the
agonist does not write broadly to canon). The design records live in-module (armature.py /
rhetoric.py / appraise.py grounding blocks) + this packet until Gate C is approved.
