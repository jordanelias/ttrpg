# Ability library + classes — alternatives, adversarial review, reconciliation, consolidation (PROVISIONAL)

**2026-06-13 · status: PROPOSED, Jordan-vetoable · the rigor pass on the comprehensive proposal**

**Verdict first: the abilities-primary direction holds, but the comprehensive proposal's two specific bets —
a *flat atomic* library and *free* mix-and-match — do not survive review. The library is dial-heavy (only
~10–15 of 55 abilities reshape the exchange; the rest are competence modifiers — the quantitative-not-
qualitative problem the channel critique already rejected, at finer grain); free mixing makes combinatorial
balance intractable and dilutes identity; conditional value breeds dead slots. Historical and game-design
precedent both point to integrated *methods* + bounded customization, not atom-soup. Consolidate toward
composite *techniques* + *method-primary* identity + *bounded, earned* customization. This narrows "free
mix-and-match" toward "bounded build customization" — a real freedom-vs-balance/identity trade-off whose dial
is yours.**

`[SELF-AUTHORED — bias risk]` This attacks my own two-turns-prior proposal; the review is written to break it.
`[READ: combat_traditions_classes_ability_library_2026-06-13.md — the design under review; tradition.py — the anchor discipline]`

---

## §1 — Alternatives (the structural choices the proposal made)

Four decisions, each with options. Scored: **Id** (identity strength) · **Bal** (balance tractability) · **Div**
(build diversity) · **Auth** (authoring cost) · **Leg** (legibility).

**D1 — class structure**
| | Option | Id | Bal | Div | Leg |
|---|---|---|---|---|---|
| A | flat library + free build *(proposal)* | ✗ | ✗ | ✓✓ | ✗ |
| B | class-locked trees + *earned* cross-borrow (job system, FF-Tactics) | ✓✓ | ✓ | ◑ | ✓ |
| C | **method/stance-primary + a few flex slots** | ✓ | ✓ | ✓ | ✓ |
| D | classless perk-web (PoE) | ✗ | ✗✗ | ✓✓ | ✗ |
| E | trade-off/drawback portfolios (each boon carries a flaw) | ◑ | ✓ | ✓ | ◑ |

**D2 — ability granularity**
| | Option | note |
|---|---|---|
| a | atomic dials *(proposal, ~55)* | max customization; **most are +competence, not techniques** (§2.1); high authoring + balance cost |
| b | **composite techniques (~20–30)** | fewer, richer, *active*, distinctive, legible; less granular |
| c | macro-archetype (class = one package) | strongest identity, least customization |

**D3 — balance** (overlaps the gate work, but the *build space* is harder): point-buy budget · slots+cost
*(proposal)* · cyclic-at-method · drawback-paired · sim-tune. The proposal leans slots+cost+cyclic, but the
cycle balances *archetypes*, not arbitrary *builds* (§2.2).

**D4 — anchor split**: strict historicism · free invention · **anchored + `M`-fill** *(proposal)* ·
fully-decoupled (historical schools as one set, mechanical methods as a separate set that never blurs). The
proposal's split is right but still co-tables schools and mechanical classes, inviting the blur.

---

## §2 — Adversarial review (objective)

1. **The library is dial-heavy (grounded).** Of 55 abilities, only ~10 are unambiguously active maneuvers and
   19 are pure passive competence-dials; most of the remaining 26 are σ-bumps with active-sounding names. So a
   clear majority are **+competence**, not technique — the exact quantitative-differentiation the channel-weight
   critique killed, reintroduced one level down. A "+measure" and a "+tempo" ability differ only in which σ they
   nudge; the player experiences "slightly better at a thing," not a distinct technique.
2. **Combinatorial balance is intractable.** Flat library + free slots = C(55, k) builds, each needing
   vacuum-balance. The **cyclic web balances archetypes, not arbitrary builds** — a custom build can step *outside*
   the cycle by buying the counter to its own weakness (a Binder takes True Times and the "kept-at-measure" loss
   vanishes). This is the CRPG degenerate-combo problem, and it bites hardest exactly where the directive pushes
   (free builds).
3. **Identity dilution.** If everything mixes freely, schools/classes are cosmetic presets — the German identity
   dissolves the instant a German equips Italian abilities. The familiarity web is the only guard and it is weak
   (reading-only, symmetric, cancels in pairwise contests).
4. **The schema/economy is a major subsystem, not "additive."** `trigger` + `cost` + `prereq` + a slot economy +
   an affinity point-buy is a substantial new build/economy layer (UI, per-use resource accounting, prereq
   gating). Calling it "invariant-safe" hides that it is most of a CRPG loadout system. NERS-E: does the apparatus
   earn its weight?
5. **Conditional value breeds dead slots.** "An in-node ability is dead out of node" is sold as balance, but from
   the seat it means abilities that do nothing for whole fights (a bind-only technique vs a duelist who never
   binds). The mechanism that bounds power manufactures feel-bad inertness.
6. **The mechanical archetypes are a generic roster.** Binder/Duelist/Skirmisher/Breacher/… is the standard
   MMO/fighting-game lineup. Loosely anchored, yes — but several are near-duplicates by node (Measure-master vs
   Duelist; Closer vs Binder), and it is not shown they each earn a *distinct* Valoria play-feel.
7. **Unreconciled with the physics.** The damage techniques (Power Strike, Armour-Breach, Precision Thrust) hook
   the very damage stack the session's percussion/PoB work is restructuring. Their values cannot be tuned until
   the go-continuous decision (b) lands; the proposal tunes against a moving target.
8. **Legibility at scale.** 55 abilities × 20 archetypes × free builds, layered over an already-deep state graph
   (measure, Vor economy, kuzushi, bind sub-loop), risks an illegible soup where the player cannot tell *why* an
   exchange went the way it did. "Legibility is a requirement" is asserted, not engineered.

---

## §3 — Historical precedent (loosely)

- **Traditions are integrated methods, not atom-menus.** The Kunst des Fechtens is one doctrine — Vor/Nach/Indes,
  the Meisterhäue, Winden — taught as a coherent way of moving, not a shop of swappable buffs. You *train a
  method*; you do not assemble it from perks. The corpus's own **named sets** (Bind Fighter, Thrust Duelist,
  Counter-time) are exactly composite identities, which favors composite techniques (D2-b) over atomic dials.
- **Cross-training was real but costly.** Masters did absorb other systems (the corpus's ADJACENT exchanges;
  Bolognese absorbing earlier forms; Silver writing *against* the Italians shows live awareness) — but at the
  grain of "trained in a second whole method," not "equipped three atoms from school A and two from B." That
  favors *earned, costed* cross-training (D1-B/C), not free flat pick.
- **Game-design precedent (loosely) agrees.** The durable combat-class systems are discipline/stance-primary with
  bounded flex, or gate cross-class behind mastery (FF Tactics earns a few borrowed abilities). Fully-flat
  skill-soup (PoE) treats degenerate builds as a *feature* — which a balanced, narrative-first game cannot afford.
  Both precedents point to **method + bounded customization**.

*(Held loosely, per the request and the historical-anchor discipline — gesturing at the pattern, not adjudicating
sources.)*

---

## §4 — Reconcile (judiciously)

**What survives.** Abilities as the qualitative layer (the prior decision stands). The node-cycle balance. The
historical-anchor + `M`-fill split. The mechanical-vs-creative line.

**What changes.**
- **Granularity → composite.** Techniques become integrated, *active*, distinctive maneuvers (~20–30), not atomic
  dials. The passive **+competence** abilities fold back into the **stat/affinity** layer — where continuous
  competence belongs; a dial is not a technique. (Fixes 1, 8.)
- **Freedom → method-primary + bounded flex.** Identity is one integrated **method** (its core techniques +
  node-preference + familiarity); customization is a *few flex slots* for specialization or **earned, costed**
  cross-training — not a free flat pick. (Fixes 2, 3; matches precedent.)
- **Conditionality → sparing.** Techniques should be node-*relevant* but usefully-active elsewhere, not dead;
  prefer shape-the-fight over passive +X. (Fixes 5.)
- **Schema → minimal.** Lean on the method's built-in node-conditionality and a small flex budget; do **not** build
  a heavy per-use economy. (Fixes 4.)
- **Damage techniques → deferred** until the physics decision (b) resolves. (Fixes 7.)
- **Roster → consolidated.** Collapse the 12 mechanical classes to the node-distinct methods that earn it (~6),
  each grounded in a node + a loose style touchstone; cut the near-duplicates. (Fixes 6.)

**Conceded, plainly.** This **narrows** the directive's "free mix-and-match." I am recommending *less* build
freedom than my prior proposal — because free mixing fails balance, identity, and precedent together. The freedom
dial is **yours**: more freedom buys more builds at the cost of degeneracy + identity; the recommended
bounded-method point is the balance/identity-preserving setting. I surface the trade-off and recommend; I do not
override your stated want.

---

## §5 — Consolidate (the design)

**Method-primary + composite techniques + bounded, earned customization.**

1. **Method** *(primary identity)* — one integrated method per fighter: its **core composite techniques**
   (defining, fixed), its **node-preference**, its **familiarity** profile. Roster = the **8 historical schools**
   + **~6 mechanical methods** (node-distinct, consolidating the 12: Binder · Duelist · Skirmisher · Breacher ·
   Counter-fighter · Pressure-fighter). Strong identity, no dilution.
2. **Composite techniques** *(the qualitative layer)* — ~20–30 integrated, active, distinctive maneuvers (Winden,
   stop-hit, atajo, the rush, kuzushi, the reopen, the breach), grade-tagged (anchored vs `M`), each *shaping* the
   exchange and *legible* in play. Passive competence is **not** a technique — it lives in stats/affinities.
3. **Bounded customization** — core techniques fixed by method + a **few flex slots** (specialize, or cross-train
   at a real cost). A balanced **affinity point-buy** gates technique prereqs. Cross-school is **earned/costed**,
   not free.
4. **Balance** — the **cyclic web at the method level** (methods balance by node-cycle) + the bounded flex (the
   combinatorial space is now *small* → validate the ~14 methods and their bounded variants, not C(55,k)) +
   sim-tuning. Loop-safety: techniques modulate strictly **within** the engine's existing dampers/caps (Vor decay
   + `INIT_CAP`, poise floor, `BURST_MAX`).

**Retains:** qualitative specialization (composite techniques + method identity — *stronger* than the atomic
version) and customization (bounded flex + earned cross-training). **Narrows:** free flat mixing → bounded (the
honest trade-off).

---

## §6 — Honesty / decisions

- `[CONFIDENCE: high]` on the dial-heavy finding (grounded), the combinatorial-balance argument, and the precedent
  reading. `[CONFIDENCE: medium]` on the consolidated roster (a reasonable consolidation, not a unique one).
  `[GAP: unvalidated]` — the method set, flex budget, and cyclic relation need the sim balance test (each method +
  bounded variant's unconditional win-rate flat within ±2–3 pp at N≈3000).
- **The build-freedom dial is the key decision, and it is yours** — your game, your call on freedom vs
  balance/identity. I recommend bounded-method; I will not set that dial for you.
- The mechanical-vs-creative line and the historical-anchor honesty carry over unchanged.
- **Decisions:** (a) granularity — composite *(recommended)* vs atomic; (b) freedom — method + bounded flex
  *(recommended)* vs free flat; (c) the method roster — consolidate 20 → ~14 (8 schools + ~6 methods); (d) schema
  weight — minimal *(recommended)* vs full economy; (e) defer the damage techniques to physics decision (b); (f)
  the sim validation plan.

Provisional; canon engine unchanged. Supersedes nothing — it is the rigor pass *on* the comprehensive proposal,
which stays the fuller catalogue of hooks should you choose the freer end of the dial.
