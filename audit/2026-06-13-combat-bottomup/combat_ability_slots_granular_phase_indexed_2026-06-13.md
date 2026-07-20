# Granular, phase-indexed slots — refining the FFT/TO parallel (PROVISIONAL)

**2026-06-13 · status: PROPOSED, Jordan-vetoable · the granularity refinement**

**The four FFT categories (Action / Reaction / Support / Footwork) are too coarse for this engine. The state graph
resolves ~7 distinct *phases*, and the substrate already names ~7 competence *channels* — reading, measure, tempo,
feel, leverage, composure, structure. The slot taxonomy should mirror those, not collapse approach + reopen +
reading + feint into one "Footwork/Action" bucket. Refinement below: two grounded layers — a per-channel *affinity*
profile (continuous) and *phase* technique slots (discrete), each wired to real levers. The one rule carried intact
from the FFT model: the *bound*. Granularity without a bound is the combinatorial soup the slot limit existed to
prevent — so the affinities are a fixed point-buy and the phase slots are method-filled with only a few free
overrides. Granular in texture, bounded in build space.**

`[READ: wrapper.py phases + systems.py/tradition.py lever sites — grepped this session]`
`[SELF-AUTHORED — bias risk: refines my own prior doc on your steer; the steer is correct — four buckets lose texture]`

---

## §1 — Why granular: the engine's real phases

The state graph (`wrapper.engagement`) is a sequence of distinct resolution moments, each with its own competence
domain and its own levers:

| Phase | What it resolves | wrapper site |
|---|---|---|
| **Approach / Measure** | closing, reopening, point-displace, stop-hit at range | `:66–86` (`close_rate`, `approach_displace`, `reopen_prob`, `stophit`) |
| **Reading** | pre-contact anticipation — does the defender read the commit or guess | `:130–134` (`read_a/read_d`, `familiarity`, `legibility`) |
| **Feint / Deception** | manipulating the opponent's read | `:121–124` (`feint_eval`) |
| **Commitment** | the attack — commit-depth, the strike, thrust vs cut | `:99–107`, `:160–162` |
| **Defence** | parry / dodge / wind — the mode contest | `:135–140` (`mode_sigma`) |
| **Bind / Winding** | the tactile-leverage contest in contact, kuzushi | `:235–254` (`bind_sigma`, poise-break) |
| **Counter / Riposte** | the steal, the single-time counter, displace-step-in | `:147–159`, `:188–215` |

Four FFT buckets blur the first four of these into "Action/Footwork." You named **reading** and **approach** — they
are *separate phases with separate levers*, and so they should be separate slots.

---

## §2 — The two granular layers

### A. Affinity profile — continuous competence, **one slot per channel** (point-buy bounded)

The engine's seven channels map 1:1 to seven affinities. This is where reading, measure, etc. get their *graded*
reflection. Method sets the base distribution; a **fixed point-buy budget** lets you specialize (every fighter
spends the same total — the balance guarantee).

| Affinity | Engine channel | Lever sites |
|---|---|---|
| **Perception** (the read) | `visual` | reads `:132–133`; reopen-reads `systems:220–221`; anti-feint `systems:203` |
| **Measure** (distance) | `measure` | footwork `systems:171–173`; Vor-hold `systems:272` |
| **Timing** (tempo) | `tempo` | initiative `:118`; counter-reach `:159`; steal `systems:267`; grip-keep `systems:278` |
| **Feel** (the bind sense) | `tactile` | bind `systems:236–237`; steal `systems:266` |
| **Leverage** (the bind force) | `leverage` | bind `systems:234`; kuzushi `:244` |
| **Composure** (anti-deception) | `precommit` | read-protection `systems:203` |
| **Structure** (footing/poise) | `balance` | footwork `systems:171`; dodge/stance; poise recovery |

### B. Phase technique slots — discrete techniques, **one slot per phase** (method-filled + few free)

Each of the seven phases (§1) is a slot that holds one active technique. Your **method fills its signature phases**
(its identity — a Binder fills Bind + Approach-close; a Duelist fills Counter + Measure-hold); you have a **bounded
number of free phase-slots** (≈2–3, sim-tunable) to override a method phase or add to an empty one, including
**cross-method** techniques (earned by training that method — the FFT secondary depth).

The **standing resources** — Initiative/Vor, Poise/Structure, Conditioning — are **not** separate slots; they are
*results* of the affinities + stats + what happens in the phases (Timing→Vor-hold, Structure→poise, Conditioning
from Endurance). Leaving them emergent rather than slotted is deliberate: it keeps the count bounded and avoids
slots for things the engine already derives.

---

## §3 — The bound (the load-bearing part)

Granular taxonomy, bounded build space — the two are reconciled by three limits, all carried from the FFT model:

1. **Affinities are a fixed point-buy.** Seven channels, one shared total. You redistribute; you cannot inflate.
   Balance is validated over budget-distributions, which is a bounded set.
2. **Phase slots are method-filled with few free overrides.** Six-to-seven phases, but the method pre-fills most;
   only ≈2–3 are yours to change. The build choice is *which phases you personalize*, not a free pick across all.
3. **Library-gating + cross-method cost.** You may only slot what you have unlocked; cross-method techniques cost
   the training. The earned bound on borrowing.

So the combinatorial space is (affinity budget-distributions) × (≈2–3 phase-overrides from the unlocked set) — small
enough to sim-validate, exactly as the coarse FFT model was. **The granularity is in the texture and the readout,
not in an explosion of free choices.** That is the whole point: the player *sees* seven phases and seven channels
(rich, legible, the combat's real anatomy) while *choosing* within a bounded few.

---

## §4 — Worked granular loadout

**German Binder** *(method: Kunst des Fechtens)*

- **Affinity profile** (point-buy over 7): Feel ▰▰▰ · Leverage ▰▰▰ · Measure ▰▰ · Perception ▰▰ · Timing ▰ ·
  Composure ▰ · Structure ▰▰ — weighted into the bind channels, the method's identity.
- **Phase techniques** (method-filled ●, free override ◆):
  - Approach ● **Closing** (`close_rate` — get to the bind)
  - Reading ● **Fühlen-read** (`visual`+`tactile` anticipation)
  - Feint ○ *(empty — Binders don't deceive; they dominate contact)*
  - Commitment ● **Zornhau** (wrath-cut: feint→deep commit)
  - Defence ● **Winden-defence** (bind the incoming)
  - Bind ● **Stärke-Schwäche** (`bind_sigma` dominance + kuzushi)
  - Counter ◆ **Indes-steal** (free override — `init_steal_factor`, the Vor through the bind)
→ a fighter who closes, wins the winding, breaks structure, and steals the tempo in contact — every phase legible,
every choice within the bound.

*(Compare an Italian Duelist: Timing/Measure-weighted affinities; Counter + Measure-hold + Stop-hit phases filled;
Bind left thin. The two read differently across all seven phases — that is the differentiation, made visible.)*

---

## §5 — Honesty / decisions

- **The trade is real: granularity vs legibility.** Seven phases + seven channels is more to reason about than four
  buckets. What keeps it legible is (a) the organization *by the combat's actual phases* — the player already lives
  through approach→read→commit→bind, so the slots match felt experience — and (b) the bound, which means most of the
  taxonomy is method-set, not a blank grid. If even this is too much surface, the fallback is to **group** the seven
  channels into ~4–5 (Perception, Measure+Structure, Timing, Feel+Leverage, Composure) — a dial you set.
- **Mechanical, not creative.** Methods and techniques are mechanical playstyles; the world-fiction (who trains
  what) is yours. Historical names (Winden, Zornhau, Fühlen, the stop-hit) stay anchored; mechanical fill graded
  `M`; no fabricated history.
- `[CONFIDENCE: high]` that phase-indexing is the right granular axis (the phases are real, levered, and named in
  source). `[CONFIDENCE: medium]` on the exact counts (7/7 vs grouped; 2–3 free slots). `[GAP: unvalidated]` —
  point-buy budget, free-slot count, and the method-fill maps need the sim test (budget × override configs flat
  within ±2–3 pp at N≈3000).
- **Decisions for you:** (a) channel granularity — 7 (1:1 with the engine) or grouped to ~5; (b) phase count and
  which phases a method fills by default; (c) the free-override budget (≈2–3); (d) the affinity point-buy size;
  (e) whether standing resources stay emergent or get their own slots; (f) the sim plan.

Provisional; engine unchanged. Refines — does not replace — the FFT-parallel doc: same bounded, earned model, now
at the engine's true grain.

*The visual companion is now even more apt: an equip screen with the seven phase slots down one side and the
seven-channel affinity profile down the other, resolving live against the engine. Say the word and I'll build it.*
