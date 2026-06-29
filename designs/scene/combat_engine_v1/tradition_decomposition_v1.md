# Tradition Decomposition (bottom-up) — scene-combat WS-3

**Status:** Decomposition artifact (mechanical-tier; the foundation WS-4 consumes). Evidence-traced, source-tier
graded; **not** canon — the in-world naming and which cultures train which tradition stay Jordan's creative layer.

## Why this exists (req 2 + your directive)

The current `tradition.py` models a tradition as a 7-dim scalar channel-weight vector (e.g. `german tactile=1.35`).
The recovered analysis proved that primitive is structurally wrong (it differentiates *quantitatively*, not
*qualitatively*, and cannot specialize AND stay vacuum-balanced — measured 18.8pp imposition spread), and the
WS-8 harness measured the live consequence: a **6.8pp unconditional win-rate spread** across traditions (none
lowest at 45.1) — they are not vacuum-balanced. The scalar magnitudes are also **~30% asserted top-down**: the
seven-axes structure is grounded, but no doc derives the specific numbers.

This decomposition replaces the assertion with evidence: each tradition is decomposed **bottom-up** from the
researched corpus into atomic records, each tracing a **documented technique → the substrate primitive it uses
→ the state-graph node it acts at → the weapon-affordance that gates it → the access/bias/tendency it becomes**,
with a source tier. The aggregate per-tradition profile then *emerges* from these records; §6 reconciles that
emergent profile against the current hand-set numbers.

## Sources (the corpus, all in-repo)

- `designs/audit/2026-05-28-combat-reframe/historical-precedents/combat-manuals-seven-axes-throughlines.md`
  (the 7 axes + throughlines T1–T9; the master cross-reference)
- `.../manual-vs-combat-v32-bridge.md` (named-set ↔ cognitive-mode mapping; the measure/stance/initiative axes)
- `designs/audit/2026-05-29-combat-armature/martial_traditions_mapping.md` (MAP 3: per-tradition technique census)
- `designs/scene/combat_engine_v1/ability_armature.md` §5 (the per-tradition documented-technique menu + S-tiers)
- `designs/audit/2026-06-13-combat-bottomup/martial_tradition_research_skeleton_2026-06-13.md` (the capture schema)

**Source tiers** (from ability_armature §5): S1 primary/critically-edited · S2 peer-reviewed · S3 specialist ·
selection-effect honoured (counter-prestige is European/Japanese, not universal); a tradition with no S1/S2
anchor gets **no asserted ability** (extract one distinctive mechanic or flag — the sparse-tradition rule).

## The target vocabulary (what each record maps onto)

**Substrate primitives** (the engine's physical axes, the only things an access may modulate): `measure`
(distance control), `tempo` (commitment-window timing), `feel`/tactile (in-bind contact-read), `leverage`
(bind/displace mechanical advantage), `perception`/visual (pre-contact read), `precommit` (intent-read),
`structure`/balance (footwork/geometry). **State-graph nodes** (from `state_graph.py`): Approach, AwaitTempo,
Exchange{read, commit, mode, roll}, Bind, Riposte, HitLanded. **Affordance gates** (from `capabilities.py`):
half-sword / gap-thrust / percussive-blow, plus blade_guard (bind quality, continuous), leverage edge.
**Access kinds:** `access` (a learnable permission to attempt a transition — bind-and-wind, atajo, stop-hit),
`bias` (a node-preference — "fights to the bind"), `tendency` (a propensity — counter-readiness).

---

## Decomposition — well-anchored traditions (S1/S2)

Each row: **technique** · source-tier · **primitive** · **node** · **affordance gate** · **becomes**.

### German — Kunst des Fechtens / Liechtenauer (S1/S2; the best-anchored)

| technique | tier | primitive | node | gate | becomes |
|---|---|---|---|---|---|
| **Winden** (winding in the bind) | S1/S2 | leverage + feel | Bind | blade_guard (high) | **access** `wind`: re-contest leverage in the bind |
| **Fühlen / Indes** (feeling, the in-tempo decision) | S1/S2 | feel + tempo | Exchange.read→Riposte | — | **access** `indes_counter`: same-tempo counter on a read |
| **Stärke-Schwäche** (strong/weak of the blade) | S1/S2 | leverage | Bind | blade_guard | **bias** dominate-the-bind (leverage emphasis) |
| **Vorschlag** (the first strike that takes the Vor) | S1/S2 | tempo | Approach→Exchange | — | **tendency** seize-first (see §5 — `seize` is DEAD in-engine) |
| **Zornhau / Meisterhäue** (master cuts) | S2 | tempo + structure | Exchange.commit | gap-thrust (cut_thrust) | **access** master-cut: cut that threatens the bind |
| **Halbschwert** (half-sword) | S1/S2 | leverage + measure | closed.form_switch | **half-sword gate** | **access** half_sword (already live; the literal "no half-sword without a sword") |
| **Ringen am Schwert** (grappling at the sword) | S2 | leverage | Bind→clinch | clinch | **access** `clinch` (contact axis — currently unbuilt) |

**Emergent German profile:** preferred node = **the bind**; signature accesses = wind, indes_counter,
half_sword, clinch; emphasis = leverage + feel; mode = tactile. *Fights to the crossing of the blades.*

### Italian — Fiore → Bolognese → rapier (S2)

| technique | tier | primitive | node | gate | becomes |
|---|---|---|---|---|---|
| **Mezzo tempo / contratempo** (the half-time counter) | S2 | tempo | Exchange.read→Riposte | — | **access** `single_time_counter` (already live as counter_select) |
| **Misura** (larga/stretta/fuori — measure control) | S2 | measure | Approach | — | **bias** hold the lunge-optimal measure |
| **Stringere** (constraining the blade, finding it) | S2 | measure + feel | Approach→Exchange | gap-thrust | **access** find-the-blade: constrain to open the line |
| **Gioco stretto / largo** (close/wide play) | S2 | measure | Approach | — | **tendency** prefer the wide game (stay at the point) |
| **Cavazione / disengage** (slip the contact) | S2 | tempo + measure | Bind→Separation | — | **access** `disengage` (contact axis — the rapierist's escape, unbuilt) |

**Emergent Italian profile:** preferred node = **measure / the single-tempo counter**; signature accesses =
single_time_counter, find-the-blade, disengage; emphasis = tempo + measure; **refuses the bind** (cavazione
out). *Fights at the point, in tempo — your exact "Italian rapier avoids the bind" example, grounded.*

### Japanese — koryū (S2)

| technique | tier | primitive | node | gate | becomes |
|---|---|---|---|---|---|
| **Sen-sen-no-sen** (pre-emptive seizing) | S2 | precommit | Exchange.read (pre-commit) | — | **access** `precommit_read`: read intent before the blade moves |
| **Sen-no-sen** (simultaneous seize) | S2 | tempo + precommit | Exchange→Riposte | — | **tendency** counter-at-the-commit |
| **Maai** (the meeting distance) | S2 | measure | Approach | — | **bias** distance-zone control |
| **Kiriotoshi** (cut that parries and strikes as one) | S2 | tempo + structure | Exchange.mode→HitLanded | gap-thrust | **access** fused parry-strike |
| **Metsuke / suki** (gaze; perceiving the opening) | S2 | perception + precommit | Exchange.read | — | **bias** perception emphasis |

**Emergent Japanese profile:** preferred node = **pre-commitment seizure**; signature = precommit_read,
counter-at-commit, fused parry-strike; emphasis = precommit + perception. *Wins before the blade moves.*

### Spanish — La Verdadera Destreza (S2/S3, flagged)

| technique | tier | primitive | node | gate | becomes |
|---|---|---|---|---|---|
| **Atajo** (blade-constraint off the círculo) | S2/S3 | measure + leverage | Approach→Exchange | — | **access** `atajo`: constrain via geometry |
| **Compás** (the steps — geometric footwork) | S2/S3 | structure (balance) | Approach | — | **access** `perfect_geometry`: footwork that holds the measure (your "perfect geometry" example) |
| **Ángulos / círculo** (the geometry of the circle) | S2/S3 | measure + structure | Approach | — | **bias** geometric measure-hold |

**Emergent Spanish profile:** preferred node = **measure-hold (the círculo)**; signature = atajo,
perfect_geometry; emphasis = measure + structure. *Owns the geometry of the approach.* (S2/S3 — flagged as
partly-reliable; the engine already over-rigours the corpus on source honesty.)

### English — George Silver (S2)

| technique | tier | primitive | node | gate | becomes |
|---|---|---|---|---|---|
| **True & false times** (fast-part-first) | S2 | tempo + structure | Exchange.commit | — | **access** `true_times`: commitment discipline (already live as anti_overcommit) |
| **Four governors** (judgement / distance / time / place) | S2 | tempo + measure | Approach→Exchange | — | **bias** measured counter-time |

**Emergent English profile:** preferred node = **the clean counter at the true time**; signature = true_times;
emphasis = tempo + measure (biomechanical). *Counters at the right instant, refuses over-commitment.*

## Thin traditions — sparse-tradition rule (extract one mechanic, do not fabricate)

- **Chinese** (qiang/staff; Ming manuals are mnemonic shorthand per Shahar — S2 caution): no S1/S2 technique
  menu. Extract **one** distinctive mechanic: the **burst from reach** (fa-jin extension off the long weapon)
  → a `burst_extend` tendency at HitLanded→AwaitTempo. No further ability until an anchor exists.
- **Filipino** (FMA): explicitly **unanchored** at S1/S2 (ability_armature §5). Extract the **continuous-flow**
  tendency (sustain the exchange) → `flow` bias at the burst-continuation gate. **No abilities** asserted.

---

## §6 — Reconciliation: emergent vs the current hand-set channel numbers

The decomposition says a tradition is *preferred-node + a bundle of accesses/biases* — **not** a scalar vector.
Mapping the emergent emphasis back onto the current `tradition.py` channels:

| tradition | current vector (top-down) | emergent emphasis (evidence) | verdict |
|---|---|---|---|
| german | tactile 1.35, leverage 1.30 | feel + leverage @ Bind | **supported** in *kind* (bind), but the *magnitude* is asserted — replace with the bind node-preference + wind/indes/clinch accesses |
| italian | tempo 1.30, measure 1.25 | tempo + measure, **refuse bind** | **partly supported**: the "refuse bind" (cavazione/disengage) is **missing entirely** from the scalar model — the vector cannot express it |
| spanish | measure 1.35, balance 1.30 | measure + structure @ Approach | supported in kind; the `balance` channel is **80% suppressed** in-engine (only 1 of 5 balance_eff sites) so Spanish "perfect geometry" barely fires — WS-4/WS-5 fix |
| japanese | precommit 1.35 | precommit + perception | supported in kind, but `precommit` fires only in feint (~30%) — isolated; the "win before the blade moves" identity is mostly inert |
| english | tempo 1.15, measure 1.15 | tempo + measure (true-times) | supported; true_times already live |

**Conclusions for WS-4:**
1. The *kind* (preferred node + signature techniques) is evidence-grounded; the *scalar magnitudes* are not — drop
   them for the node-preference + access-bundle representation.
2. Three identities the scalar vector **structurally cannot express** and that the decomposition surfaces:
   Italian's **bind-refusal** (disengage), the **contact axis** (clinch/disengage/choke), and Spanish's
   **footwork-as-geometry** (suppressed today). These are the WS-4/WS-5 accesses.
3. Every asserted ability traces to an S-tier source; thin traditions yield one mechanic or are flagged — no
   fabricated anchors (the discipline the engine already out-rigours the corpus on).

## What this feeds

WS-4 (representation re-architecture) consumes this as the **access catalogue + per-tradition bundles + the
gating chain inputs** (proficiency/mode/set). WS-5 (The Approach) consumes the **preferred-node + imposition**
column. The contact-axis rows (clinch/disengage/choke) are the genuinely-missing accesses the 06-26 distillation
isolated. All of it is gated by §C of the plan: the re-architecture ships only if it beats the keep-bias baseline
(the measured 6.8pp spread) on the WS-8 harness while keeping traditions qualitatively distinct.
