# Tradition representation — are channel weights the right primitive? (design exploration, PROVISIONAL)

**2026-06-13 · status: PROPOSED, Jordan-vetoable · follows the tradition-gate reconciliation**

Two questions, then the directive: explore *all* alternatives that retain **qualitative specialization for
unique play styles** and **mix-and-match abilities for unique builds**.

**Verdict first: the scalar channel-weight vector is the wrong primitive for both goals, and it cannot be
rescued by calibration. It differentiates traditions *quantitatively* (degree, not kind), which is not what
"qualitative play styles" means, and — proven below — its magnitude cannot simultaneously specialize and
stay vacuum-balanced. The qualitative identity belongs in node-preference + composable abilities; the
continuous competence it half-provides is already supplied by the base stats. Recommended direction:
dissolve the per-tradition scalar vector; make abilities the primary qualitative + composable layer; keep
"channels" only if reconceived as a balanced, player-allocated affinity budget that gates abilities.**

`[SELF-AUTHORED — bias risk]` Reconsiders a layer this session's own gate proposal leaned on; the argument
below is written to retire it, not protect it.
`[READ: combat_engine_v1/tradition.py — the channel vectors, the ABILITIES/lever system, eff_cw]`
`[READ: combat_engine_v1/systems.py + wrapper.py — the 19 eff_cw/channel_weight σ-sites]`

---

## §1 — Question 1: are the weights just poorly calibrated? (No — proven.)

The imposition contest depends on the **difference** of defining-channel weights, so for every tradition's
average to sit at 0.50 you need **all defining-channel weights equal**. Measured:

| calibration | impose-spread | what it costs |
|---|---|---|
| current (1.15–1.35) | **18.8 pp** | balance |
| equalize defining channel (all 1.30) | **0.0 pp** | *all* differentiation — every tradition imposes at 0.50 |
| equal-sum point-buy | **20.1 pp** | nothing — equal totals don't equalize the defining channel |

Balance ⟺ equal defining weights ⟺ no magnitude differentiation. The magnitude cannot both **differ** (to
specialize) and be **equal** (to balance) — it is not a tuning you can find, it is a contradiction in the
representation. (This is about *imposition* specifically. Channels as pure *in-node competence* can in
principle be balanced by offsetting cost/cycle — but as an imposition driver they cannot.)

**So: not a calibration bug. The scalar magnitude is structurally unfit to drive imposition.**

## §2 — Question 2: should channels exist at all?

The per-tradition channel vector does two jobs. Neither needs *this* primitive:

- **Job A — differentiate traditions.** A scalar multiplier encodes *degree* ("the German is 1.35× tactile"),
  i.e. a better-at-the-same-fight. "Qualitative play style" means *kind* ("the German fights *to the
  bind*"). Degree-differentiation is the wrong category for the goal — and it is the exact source of §1's
  imbalance. Kind-differentiation lives in **which node** a tradition imposes (the gate's preferred-fight)
  and **which abilities** it equips (Winden, stop-hit, atajo…). The channel vector adds little *qualitative*
  signal beyond its weakness-encodings (the sub-0.95 lows), and those can be expressed as "equips nothing on
  this lever" instead.
- **Job B — feed the σ-sites.** The 19 `eff_cw` sites need a competence input. But the **base stats already
  provide a continuous competence surface**: `reading` (cog/att), `reflex`, `balance_eff` (agi/str),
  `weapon_tempo`, etc. The channel layer is a *per-tradition multiplier sandwiched between* stats (continuous
  competence) and abilities (discrete specialization) — and it is the sandwich layer that is both
  quantitative-not-qualitative *and* balance-breaking.

Decisive structural fact: **the ability system already targets the channels as levers.** `measure`, `tempo`,
`leverage`, `visual`, `tactile`, `precommit`, `balance` are *registered ability levers* — "registered but
INERT until the eff_cw routing lands." So channels-as-a-fixed-vector and channels-as-equipped-abilities are
two implementations of the same effect. One is a free per-tradition bias (unbalanced, quantitative); the
other is composable and costable (the mix-and-match the directive wants).

**Conclusion: the scalar per-tradition channel vector should not be a thing. What may survive is "channels"
reconceived as a balanced, player-allocated *affinity budget* (a build currency + ability prerequisite) — a
different object that serves mix-and-match and is balanced by construction.**

---

## §3 — The design space (three orthogonal choices)

| Choice | Options |
|---|---|
| **What carries QUALITATIVE identity** | (i) node-preference (which fight) · (ii) equipped abilities (discrete named mechanics) · (iii) access-gating (which options a build *can* use) · (iv) conditional triggers (abilities that fire only in their node/situation) |
| **What produces VACUUM-BALANCE** | (a) normalization · (b) cyclic/RPS structure · (c) cost (paid from a shared economy) · (d) opportunity cost / slots (a strength forgoes another) · (e) point-buy budget (every build sums equal) |
| **What enables MIX-AND-MATCH builds** | (1) equippable abilities from a shared pool · (2) fixed slots · (3) point-buy currency · (4) trade-off pairs (a boon carries a flaw) |

The directive fixes the targets: identity from (ii)+(iv) primarily; balance from (b)+(c)+(d)+(e); builds
from (1)+(2)+(3). The only real question is *how much of the scalar channel layer to keep*.

---

## §4 — Concrete solutions, assessed

Scored on **Qual** (qualitative specialization), **Bal** (vacuum-balance), **Mix** (mix-and-match builds),
**E** (NERS-elegance / over-engineering), **Fid** (corpus fidelity), **Cost** (implementation/authoring).

| # | Solution | Qual | Bal | Mix | E | Fid | Cost |
|---|---|---|---|---|---|---|---|
| **S0** | status quo: scalar channels, no abilities wired | ✗ degree-only | ✗ 18.8pp | ✗ vector is fixed | ◐ | ◐ | — |
| **S1** | calibrate channels (normalize) | ✗ | ✗ can't (proven) | ✗ | — | — | low |
| **S2** | channels demoted to in-node only + cyclic/cost node-gate | ◐ node | ◐ (gate balanced; in-node still offset) | ◐ via abilities | ◐ keeps the layer | ◑ | med |
| **S3** | **dissolve channels into abilities** (drop vector; wire channel-levers; tradition = node + ability bundle) | ✓ kind | ✓ slots+cost+conditional | ✓ compose abilities | ✓ fewer primitives | ✓ named sets = bundles | high (author abilities) |
| **S4** | **channels → point-buy affinity budget** (player-allocated; gates abilities as prereqs; modest in-node) | ◑ via abilities | ✓ equal budget | ✓✓ affinities + abilities | ◐ two systems | ✓ | med-high |
| **S5** | pure cyclic-node + abilities, no channels | ✓ | ✓ the cycle | ✓ abilities (+multi-node) | ✓ | ◑ RPS is a construction | med |
| **S6** | **hybrid**: thin *normalized* in-node channel bias + abilities-primary + node-gate (conservative) | ✓ | ✓ (budget + gate) | ✓ abilities | ◐ keeps a thin layer | ✓ | med |

S1 is dead (proven). S0/S2 keep the broken primitive. The live candidates are **S3, S4, S6** (and S5 as the
RPS-purist variant).

---

## §5 — Recommendation: abilities-primary, channels-as-affinity-budget (S3 ⊕ S4), S6 as the fallback

A single coherent design that hits all three targets:

1. **Abilities are the primary qualitative + composable layer (S3).** Each ability is a discrete, *named*,
   conditional mechanic that modulates a lever or a node — Winden (in the bind, re-contest on leverage),
   stop-hit (on a read at measure, counter before the commit lands), atajo (take the line at measure),
   sen-no-sen (seize at the opponent's commit), fa-jin (extend the burst). The channel-levers get **wired**;
   the per-tradition **scalar vector is removed**. The σ-sites read `base-stat competence × ability_factor`
   instead of `channel_weight × ability_factor`. A **tradition = a node-preference + a curated ability
   bundle** (the named set — Bind Fighter, Thrust Duelist — exactly the bridge's "named sets grant set
   bonuses"). A **build = any legal bundle**, including cross-tradition hybrids (a German Winden + an Italian
   stop-hit = "trained in two schools," historically real).

2. **"Channels" survive only as a balanced affinity budget (S4).** Replace the fixed multiplier with a
   **player-allocated point-buy** over the seven affinities, equal budget for all → balanced by construction
   (answers Q1). Affinities do two things: **gate** which abilities a build may equip (prerequisites — you
   cannot equip Winden without tactile affinity) and supply a **modest** in-node competence. A tradition
   ships a *starting* affinity template + ability bundle; the player **reallocates affinities and swaps
   abilities** → unique builds. (If minimal change is preferred, **S6**: keep a thin *normalized* affinity
   bias for cheap continuous texture and skip the full point-buy.)

3. **Structural fight-shaping = the node-gate, balanced cyclically + by cost (from the reconciliation).** The
   imposition gate routes *which* node; balance via the cyclic node relation + a node-cost (which also gives
   the unwilling defender a paid void/exit). Imposition is **not** driven by any channel magnitude (that was
   the impossible part).

**Why this answers the directive:**
- **Qualitative specialization** — from named abilities (kind) + node-preference, not multipliers (degree).
- **Mix-and-match unique builds** — affinities (point-buy) + abilities (slots) compose freely; named sets
  are presets, hybrids are legal and bounded.
- **Vacuum-balance** — equal affinity budget (e) + ability slots/cost (d)(c) + conditional/situational value
  (an ability good only in its node is context-bounded → C1) + cyclic node relation (b). Every lever that
  broke balance (the free magnitude) is gone.

**Balance is bounded by:** slot count (you cannot equip everything), per-ability cost (strong abilities cost
more slots/points), **conditional value** (an in-node ability is worthless out of node — so raw power is
self-limiting and context-flips per C1), and the equal point-buy budget. Cross-tradition mixing is bounded
by slots + the **familiarity** web (you read the schools you have trained — a hybrid is read as both, which
is its own trade-off).

---

## §6 — Honest caveats / what this costs / decisions

- **This is a foundational structural decision — yours, not mine.** What a tradition *is*, what it attaches
  to, and how the build system is organized is design-ontology (the authority line). I have explored and
  recommended; the choice among S3/S4/S5/S6 — and whether to retire the channel vector at all — is yours.
- **The cost is real (Fid/Cost column).** Dropping the vector means **authoring discrete abilities** to
  cover the texture the 19 σ-sites currently get from channels, and **per-ability balancing** (harder than
  tuning one vector). S3/S4 trade *fewer primitives* for *more content*. S6 keeps a thin vector to soften
  this.
- **Balance is a sim claim, not a proof.** As with the gate, vacuum-balance of a slot+point-buy+ability
  system is established only by **measuring** each tradition/build's unconditional win-rate flat within the
  parity noise floor (±2–3 pp at N≈3000), then tuning slots/costs/cycle. Context *should* still flip the
  conditional advantage (C1).
- **Mixing vs identity.** Free mixing risks diluting tradition identity. The guards: traditions are the
  *preset bundles* + the *familiarity* web; slots cap "equip everything"; thematic prerequisites keep
  bundles coherent. A hybrid is meant to be a real, costed choice, not a dominant catch-all.
- **The prior gate work is not wasted.** The node-imposition gate is the *which-fight* layer; this question
  is the *how-competence-is-represented* layer. They compose: node-gate (structure) + abilities (qualitative
  competence) + affinity budget (balanced customization).

**Decisions for Jordan:**
- (a) Retire the per-tradition channel vector? (S3/S4/S5) — or keep a thin normalized one (S6)?
- (b) Affinities as full point-buy currency (S4) or not at all (S3/S5)?
- (c) Ability granularity + slot count + cost schedule (the authoring + balance surface).
- (d) How freely may builds mix across traditions (identity vs build freedom), and is familiarity directional?
- (e) The cyclic node relation + node-cost (carried from the reconciliation).

Provisional; commit alongside the reconciliation. Tradition *content* stays the corpus's; the
representation, the affinity budget, and the slot/cost system are mechanical-tier proposals. Canon engine
unchanged.
