# Combat traditions — from flat σ-tuning to state-graph imposition (design proposal)

**2026-06-13 · status: PROPOSED, Jordan-vetoable · design exploration (Lane A) · companion to the puncture/top-down inventory**

The request: take the tradition systems (top-down, grounded in historical precedent), make them bottom-up
as *modulators of how a character reads / defends / attacks*, and specifically — let a fighter's **success
at their tradition's characteristic contest open a gate in the state graph**, so the exchange runs on their
preferred terms (node pathing / shape), rather than flat tuning. Nothing committed.

`[SELF-AUTHORED — bias risk]` Extends Claude-authored engine + this session's audit. The mechanism is a
proposal; the tradition *content* it routes is the corpus's, not invented (see grounding).

Grounded against the corpus:
`[READ: designs/audit/2026-05-28-combat-reframe/historical-precedents/manual-vs-combat-v32-bridge.md — Parts A,B (state-graph reframe; measure/stance/initiative axes; named sets; state-gating precedent)]`
· `[READ: designs/audit/2026-05-29-combat-armature/martial_traditions_synthesis.md — phase-curve principle, the niche/weakness roster]`
· `[READ: designs/scene/combat_engine_v1/{tradition,systems,wrapper}.py — the implemented flat-σ form + the live state-graph transitions]`

---

## §0 — Diagnosis: the structure the implementation flattened

**What the corpus designed.** The combat reframe is a *probability-weighted state graph*: the bout traverses
`Out-of-contact → Closing → In-bind → Breaking → [Disengaged|Wounded|Felled]` (bridge Part A, citing
`reframe_blueprint §1.2`). Traditions were meant to be **curves over those phases, not flat bonuses**
(synthesis: "reach inverts across the phase pivot… every tradition is a curve over the phases"). And the
reframe *already* state-gates some mechanics: the Stance Counter is "state-gated to the Closing-opening"
(§7.1); Reaction is "gated by field of view" (§7.2). The named sets — Bind Fighter, Thrust Duelist,
Counter-time, Burst, Continuous-flow — are explicitly preferred-fight encodings (§6).

**What the implementation does.** `combat_engine_v1` reduced all of that to **flat multiplicative channel
weights**: `eff_cw(c, channel) × σ_term` at ~21 sites (`reach_sigma`, `bind_sigma`, `feint_eval`,
`init_steal_factor`, `init_hold_decay`, `init_overcommit_loss`, the `reading` term, …). A German is a
`tactile 1.35 / leverage 1.30` vector; an Italian is `tempo 1.30 / measure 1.25`. The difference is a few
percent of σ at shared nodes — the traditions differ *quantitatively at the same fight*, never
*qualitatively in which fight happens*. The Bind Fighter does not drag you into the bind; the Thrust
Duelist does not keep you at the point. The structure the manual says *defines* each tradition — imposing
your preferred engagement — was flattened into tuning.

**So this is reconnection, not invention.** The state graph exists in the engine; the phase-curve principle
and the named-set preferred-fights exist in the corpus; the state-gating precedent exists (Stance Counter,
Reaction-FoV). The missing piece is letting a tradition's success **route the path**.

---

## §1 — The mechanism: the tradition imposition gate

Replace "tradition = a σ multiplier at a node" with "tradition = the right to **impose its node**, won by
succeeding at the contest it is built for."

**The imposition contest (bottom-up: the advantage is earned, not asserted).** At a state-graph transition,
a fighter attempts to impose their tradition's preferred structure. The attempt is an *opposed contest*
whose input is the fighter's competence at their defining channel — so the channel weights become the
**contest input**, not a flat bonus:

```
impose = reading(imposer) · eff_cw(imposer, pref_channel) · familiarity(imposer, opponent)
resist = reading(opponent) · eff_cw(opponent, pref_channel)
P(gate opens) = logistic( (impose − resist) / SCALE )
```

- It uses *existing* engine quantities (`reading`, `eff_cw`, `familiarity`) — no new primitive.
- `familiarity` bounds it: you impose your fight better on a style you read (the corpus's "knowledge-of-
  others is the deep hook"; novelty self-damps).
- It is **opposed and probabilistic** — the opponent contests with their own competence at that channel,
  and can impose *their* fight in turn.

**The gate = a state transition, not a σ bonus.** On success the exchange is *routed into the imposer's
preferred node* (a transition is forced or its probability boosted). Crucially the gate sets the **terms,
not the outcome**: once in the preferred node the fighter must still win the contest *there* (the German in
the bind still rolls `bind_sigma`; the Italian at measure still has to land the counter). The channel
weights remain as the **in-node competence** — which is exactly where they belong.

So a tradition now does two things from one vector: (1) it *competes to impose its node* (the new structural
layer), and (2) it *is good inside that node* (the existing channel weights). The advantage emerges from
fighting your fight, not from a number.

---

## §2 — Per-tradition mapping (grounded; preferred node → contest → gate)

The preferred node and the imposing channel come from the corpus's own characterisations; the gate is the
transition in the *implemented* state graph (`wrapper.engagement`) that the imposition routes.

| Tradition (set) | Preferred node | Impose via | The gate (live transition it routes) | Grounding |
|---|---|---|---|---|
| **german** (Bind Fighter) | **the bind** (Krieg/Winden) | `tactile` | force/extend bind-entry (the `wind+success→bind` transition; deepen the winding loop) | bridge: stance "transforms into a bind relationship — Stark/Schwach, Winden" |
| **italian** (Thrust Duelist) | **measure / single-time counter** | `tempo` | fire the stop-hit / single-time counter; **refuse** bind-entry (stay at the point) | bridge: contratempo is the duelling apex |
| **spanish** (Destreza, geometric) | **measure-hold** (the círculo) | `measure` | boost `reopen_prob`; deny the close (hold out-of-contact) | bridge: atajo / I.33 obsessio = "taking the opponent's line" |
| **japanese** (koryū, intentional) | **pre-commitment seizure** | `precommit` | open the indes-steal / counter *at the commit* (even below the commit-4 gate) | bridge: "the Japanese alone names a pre-commitment tier (sen-sen-no-sen)" |
| **english** (Silver, Counter-time) | **clean counter at the true time** | `tempo` (+`anti_overcommit`) | route a won read into the counter; refuse over-commitment/grapple | bridge: Silver true-times; Counter-time set "+0.5D counter on a successful Reading" |
| **chinese** (Burst, fa jin) | **the burst from reach** | `leverage` (reach) | continue/extend the burst (multi-exchange run) from the long weapon | tradition.py: Burst ≈ fa jin; the qiang corpus |
| **filipino** (Continuous-flow) | **the flow** | `tactile` | sustain the exchange (continue rather than separate) — extend the burst laterally | tradition.py: Continuous-flow (hubud) |
| **none** | — | — | **no gate** (neutral; default fighters unaffected) | — |

Two tradition pairs naturally *collide* at the bind transition — the German imposes it, the Italian/English
refuse it — which is precisely the emergent matchup story the synthesis names ("Tempo-read … loses the bind
to Constraint"; the duelist who will not be dragged in). The gate makes that legible in play.

---

## §3 — NERS + loop-safety (the gate is a feedback structure — treat it as one)

A gate that routes you into a node where you are stronger is **positive feedback** (impose → better terms →
more likely to impose). The resolution-diagnostic's Lesson 5 applies: no loop undamped *and* unbounded.

- **Damper (gain < 1 per cycle).** The contest is opposed, per-transition, `familiarity`-bounded, and
  probabilistic — not a lock. The opponent can **counter-impose** their own node, so it is not a one-way
  ratchet. A failed imposition cedes nothing structural (the exchange proceeds at the default path).
- **Cap (hard bound).** The gate sets the *node*, never the *outcome* — the fighter must still win the
  contest inside it; `UPSET_FLOOR` (the 95% cap) and the substrate σ-caps still bound the resolution. So a
  tradition that always imposes its fight does not always win it.
- **Mirror = 50, default unaffected.** Same-tradition fighters impose symmetric gates → neutral; `none`
  imposes nothing → mirror and stat-only fighters are invariant by construction (matches the engine's
  existing neutral-tradition discipline).

NERS:
- **N — yes.** This is what makes traditions *qualitatively* distinct; the flat σ tuning does not express
  them. (The corpus built the named sets to mean something structural; the gate delivers that.)
- **R — improved.** Strategic depth: play to your fight, deny your opponent's, counter-impose. The matchup
  web (synthesis) becomes mechanical, not cosmetic.
- **S — clean.** It rides the *existing* state-graph transitions and reuses the existing channel/`familiarity`
  quantities; no new primitive, no new node. Channel weights keep their in-node role.
- **E — at the boundary; hold the scope.** A gate *adds* apparatus, so it must earn it (over-engineering is
  a defect). It earns it because expressing the traditions is the entire reason they exist — but the
  discipline is **one imposition contest per tradition at its one preferred transition**, not a gate at
  every node. The σ-multiplier layer should *not* be duplicated by the gate; pick one role per channel
  (input/in-node competence) and let the gate be the structural layer on top.

---

## §4 — Wiring points (where the gates attach in `wrapper.engagement`)

The gates clip onto transitions that already exist — minimal surface:

- **bind-entry** (`if mode=='wind' and rng()<WIND_BIND_P: bind=True`, and partial+wind): German imposition
  can set `bind=True` on a won tactile contest even without the wind path; Italian/English imposition can
  *refuse* it (convert to a counter-attempt instead).
- **single-time counter** (`if read_win and commit>=4: counter_attempt = …`): Japanese/Italian/English
  imposition opens `counter_attempt` (Japanese even at `commit<4` — the pre-commitment tier), or boosts its
  selection probability.
- **reopen / measure** (`reopen_prob(longer, shorter, …)` and `close_rate`): Spanish/Reach imposition boosts
  `reopen_prob` and suppresses the opponent's `close_rate` (hold the círculo).
- **burst continuation** (`if not (hit>0 or riposte or bind): return None`): Chinese/Filipino imposition
  continues the exchange on a clean-defence beat that would otherwise separate (extend the burst), bounded
  by `BURST_MAX` (the existing cap — the damper is already there).

A single `tradition_gate(imposer, opponent, transition, TR, cfg, rng)` evaluates the §1 contest for the
imposer's preferred node and returns the routing decision for that transition. One function, four call-sites.

---

## §5 — Mechanism demonstration (the contest, not yet the full fight)

`tradition_gate.py` (companion) implements the §1 contest + the per-tradition `PREFERRED` map and a self-test
that computes imposition odds for representative matchups. It demonstrates the contest produces
**tradition-distinct, opponent-sensitive, mirror-fair** imposition probabilities from the real channel
competences — i.e. the mechanism is well-defined and behaves as designed. It is **not** a balance validation:
routing the actual path in full fights (and tuning `SCALE` + the per-transition boosts) is the build step.

---

## §6 — Scope / honesty / decisions

- `[CONFIDENCE: high]` on: the diagnosis (the flat-σ form vs the corpus's state-graph conception — both
  read); the per-tradition preferred-node mapping (each row cites the corpus); the loop-safety analysis.
- `[GAP: balance unvalidated]` The gate's effect on win-rates and the parameter tuning (`SCALE`, the
  transition boosts, whether an imposed node over-rewards) are **not** measured — this is a design + a
  contest demonstration, not a sim'd result. The synthesis itself flags that "the structural decisions… are
  Jordan's and are deliberately left unresolved."
- **The line.** The tradition *content* (what each fights for) is the corpus's, grounded above — not
  invented. The *mechanism* (imposition gate vs flat tuning) is the mechanical-tier exploration Jordan
  asked for. Where the two meet — e.g. should the German be *able* to force a bind on an unwilling Italian,
  and how strongly — is a design decision (the matchup-balance call), and it is yours.
- **Decisions for Jordan:** (a) adopt the imposition-gate layer at all? (b) keep channel weights as
  contest-input + in-node competence (recommended) — or have the gate *replace* the flat σ multipliers
  entirely (more elegant, larger change)? (c) which transitions get gates (the scope discipline — all four,
  or start with the bind collision only)? (d) the damper/cap parameters (`SCALE`, boosts, BURST interplay)
  are sim-tuning, to be set against the harness once wired.
- Nothing committed. Canon engine unchanged. `tradition_gate.py` is an illustrative proposal module.
