# Martial-Traditions Synthesis — Valoria-Native Traditions (Class-C proposal · OPEN)
**Companion to `combat_engine_v1` + `martial_traditions_mapping.md` · grounded in the project's own research/abstraction · no canon retconned**

Purpose: synthesize **new, Valoria-native martial traditions** from our abstracted combat research, organized **legible to the engine** — each tradition expressed as the four engine objects (`tradition.py` channel-vector + set/mode label + equipped abilities on the armature + `familiarity` edges). This is NOT a historical-conversion exercise and NOT generic game archetypes; each tradition is built up from a coherent **cognitive-mode commitment** (the canon `mode=` field) and a coherent answer to the information-tempo economy, so its richness is a product of internal grounding. Status: **open** — the structural decisions in §6 are Jordan's and are deliberately left unresolved here.

---

## 1. Analytical basis (corrected NERS-synthesis charter, compressed)

The synthesis rests on the throughlines, re-judged for a **NERS-compliance** goal (not historical fidelity):

- **The substrate is the universal; a tradition is a bias-vector over it** (`tradition.py`: the engine resolves only in the substrate; a tradition biases *how* its fighter reads/selects). Universalization is therefore mostly *done* — synthesis = new channel-vectors + new selections over the existing armature.
- **One engagement = one information-tempo economy** (emit / acquire / control-measure / price-of-action / time-of-action / act). A tradition is grounded when it has a coherent answer to all six.
- **Reach inverts across the phase pivot** (ratified W3): approach → bind → grapple → break; every tradition is a *curve* over the phases, not a flat bonus.
- **Context flips the apex** (ratified C1): duel rewards finesse/tempo/counter; battlefield suppresses defensive σ-leverage → Strength/armour-defeat. No tradition is globally best.
- **Strength↔Finesse, phase-picked** (ratified ST1/L1): Finesse rules the open-duel placement (σ-leverage → degree → damage); Strength rules bind/clinch/battlefield/vs-armour. (Perception feeds Finesse as an input, not a third pole — NERS-Elegance.)
- **Knowledge-of-others is the deep hook** (`familiarity()`): an unread tradition is read at 0.85; the matchup web is the emergent-narrative engine. Novelty self-damps (a new style read poorly until it spreads — a *bounded* loop, NERS-Robust).
- **Source-tier is a label, not a gate, under synthesis.** The armature's "no ability without an S1/S2 historical anchor" rule is the fidelity gate; Valoria-native traditions cite no single school. See §2.

*Discipline notes carried forward (low-severity, honest):* the channel model has a documented residue it cannot hold (deductive-judgment, no-mind, capture-objective) — we *evoke* those modes, we do not claim to represent them; founding-legend / idiom are worldbuilding *methods* (Jordan's), not facts to recover.

---

## 2. PROPOSED interface amendment — `grade = 'V'` (Valoria-synthetic)  `[OPEN — Jordan ratify]`

`ability_armature.md §1.5` and `tradition.py` currently gate equippable abilities behind an S1/S2 **historical** anchor (priority-gap traditions get none). Valoria-native traditions have no such anchor by construction. Proposed amendment:

- Add `grade = 'V'` = **Valoria-synthetic**: grounded **bottom-up** on the engine channel/competence it modulates and **top-down** on a *convergent universal* (a pattern recurring across ≥3 documented traditions, T3), **not** on one school. Gated by **NERS**, not sourcing.
- Historical-tradition abilities keep their S-tier gate unchanged; only native-tradition abilities use `V`. This preserves the selection-effect discipline for fidelity work while admitting synthesis. Bounded/Class-C values, invariant-safe (no-op unequipped) — all existing armature §1 principles still bind.

---

## 3. The engine-legible form (how every tradition below is specified)

A Valoria tradition = exactly four engine objects, nothing bespoke:
1. **Channel-vector** — 7 channels (`visual, tactile, precommit, leverage, tempo, measure, balance`), multiplicative, neutral `1.0`, canon band ~`0.88–1.35`. Sub-`0.95` lows are deliberate **weakness-encodings** (the defining blindness, in the data).
2. **`set` + `mode`** labels (the bridge fields; new labels are Class-C).
3. **Equipped abilities** — each targets one lever (live: `seize`/`counter_success`/`counter_select`/`anti_overcommit`; channel-pending: `measure`/`tempo`/`leverage`/`visual`/`tactile`/`precommit`/`balance`; not-built: `reopen`/`disengage`). **Reuse a built ability where the competence already exists; add a `grade='V'` ability only for a genuine gap.** *What a tradition does NOT equip is as characterful as what it does.*
4. **`familiarity`** edges — which traditions read it well (ADJACENT, 0.93) vs at baseline (0.85).

Abilities *modulate, never unlock* (armature §1.1): every fighter has the whole vocabulary; a tradition only biases it.

---

## 4. Locked template — tradition **"Constraint"** (working label; Jordan to name)

A fusion of the **tactile** + **geometric** modes — a pairing no historical school made. Theory of the fight: *the eye lies and the rush dies* — walk a calculated angle into contact, then win the felt conversation.

```python
'constraint': dict(visual=0.88, tactile=1.35, precommit=0.95, leverage=1.30,
                   tempo=0.95, measure=1.25, balance=1.30,
                   set='Constraint Fighter', mode='tactile-geometric'),   # new set+mode, Class-C

'v_line_constraint': dict(tradition='constraint', grade='V', lever='measure',  op='*', value=1.18,
    desc="walk the angle to constrain the line into contact — abstracts the convergent geometric "
         "entry (Destreza atajo + maai-step + FMA triangle); competence=Measure, phase=Approach"),
'v_bind_break':      dict(tradition='constraint', grade='V', lever='leverage', op='*', value=1.20,
    desc="structure-break from sustained contact — abstracts the bind-as-channel universal "
         "(Winden + ting jin + hubud); competence=Leverage/binding, phase=Exchange"),

ADJACENT |= {frozenset({'constraint','german'}), frozenset({'constraint','spanish'})}
# vs italian/japanese it sits at FAMILIARITY_DEFAULT 0.85 — the mechanical face of "loses the approach to a feint-fencer"
```

Equips **nothing** on the live initiative/counter levers → in the Initiative phase it runs at substrate baseline with low `precommit`/`tempo`: its approach-weakness is *in the data*, not described. **NERS:** N — sole "arrive-by-geometry, win-by-contact" niche; R — low `visual` + no initiative ability = a real exploitable hole; S — pure existing channels/levers (needs only the queued `eff_cw` wiring); E — *walk the line in, win the conversation.* Felt practice (= in-game teaching mode): an unbroken contact-drill scored by who loses structure first. Lore hooks (Jordan): patient-rationalist founding legend; idiom around "the conversation."

---

## 5. PROPOSED roster — six native traditions spanning the canon mode-space

Working labels (Jordan to name). Channel-vectors **provisional** (grounded in the canon `mode` + niche); only Constraint's abilities are fully grounded — the other five carry intended levers, abilities pending the §6/§2 confirmation and the armature §6 grounding workflow.

| Label | mode | Niche (one-sentence commitment) | Provisional vector (v,ta,pc,lev,te,me,ba) | Levers | Structural weakness |
|---|---|---|---|---|---|
| **Constraint** | tactile-geometric *(fusion)* | arrive by angle, win by contact | 0.88,1.35,0.95,1.30,0.95,1.25,1.30 | measure(V),leverage(V) | the approach (no seize, low visual) |
| **Tempo-read** | temporal-spatial/biomech | win the *when* — stop-hits, true-times | 1.15,1.00,1.00,0.95,1.30,1.20,1.10 | anti_overcommit,counter_select | the bind (low tactile/leverage) |
| **Intent-seize** | intentional | win *before* the blade moves | 1.05,1.15,1.35,1.05,1.20,1.10,1.05 | seize,counter_success | high-variance — read-dependent |
| **Flow** | kinetic-rhythmic | unbroken percussive rhythm | 1.00,1.25,1.05,1.00,1.15,1.05,1.25 | counter_select,tempo(V) | a hard tempo-break disrupts it |
| **Root** | structural-leverage *(new mode label)* | win by structure/root — overpower, armour-defeat | 1.00,1.20,1.00,1.35,0.92,1.10,1.05 | leverage(V),strike(V) | slow, low tempo — out-paced in the open |
| **Reach** | measure-spatial *(fusion)* | own the approach, deny contact | 1.20,0.90,1.00,0.90,1.15,1.35,1.05 | measure(V),reopen* | the bind/grapple (W3 reach-inversion) |

`*` `reopen` is the not-yet-built separation lever (armature §7) — Reach is partly blocked on it; flagged.

**Matchup web (the emergent-narrative payoff, all on existing substrate):** Reach owns the approach but dies in the bind to Constraint/Root; Tempo-read stop-hits Flow but loses the bind to Constraint; Intent-seize is high-variance against everyone; Root rules clinch + battlefield (C1/ST1) but is out-paced in the open duel. Two traditions (Constraint, Reach) are genuine mode-fusions the record never made; four re-ground existing canon modes as in-world natives.

---

## 6. OPEN decisions — Jordan's calls (not resolved in this proposal)

- **D-α `[OPEN — Jordan]` — replace vs coexist (structural-ontological).** Do the native traditions **replace** the historical-named scaffold in `tradition.py` (german/italian/… demoted to grounding comments), or **coexist**? Coexistence yields 8+6 = 14 (fails NERS-E). Author's default: **replace**. Not assumed here.
- **D-β `[OPEN — Jordan]` — count.** Proposed **six** (each universal weapon then reachable by 3–5 traditions; keeps NERS-E). Tunable to ~4–5 or ~8.
- **D-γ `[OPEN — Jordan ratify]` — the `grade='V'` amendment** (§2).
- **D-δ `[OPEN — Jordan]` — in-world naming + metaphysics.** All working labels, the `set`/`mode` strings, founding legends, and any essence-system coupling are Jordan's creative layer. This doc provides only the grounded structure + lore *hooks*.

Once D-α/D-β/D-γ are set, the five remaining traditions get full channel-vectors + `grade='V'` abilities (each grounded bottom-up + top-down per armature §6) and the set is run through the resolution-diagnostic (Stage 1–4: small-pool/thin-profile extreme, familiarity floor, loop/cliff checks) before any wiring.

---

## Citations
- designs/scene/combat_engine_v1/tradition.py (channels, traditions, abilities, levers, familiarity)
- designs/scene/combat_engine_v1/ability_armature.md (phases, competences, lever map, grounding rules, §1.5 source-tier gate)
- designs/audit/2026-05-29-combat-armature/martial_traditions_mapping.md (weapon census, tradition-per-weapon, seven-axes mapping)
- designs/audit/2026-05-29-combat-armature/RATIFIED_2026-05-29.md (+ addenda: ST1, L1, C1, W3 reach-inversion)
