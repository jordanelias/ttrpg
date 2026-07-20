# The gating chain + sets — integrating the four counters (PROVISIONAL)

**2026-06-13 · status: PROPOSED, Jordan-vetoable · the concerns, answered**

**Your four counters substantially answer the concerns I raised — and each one lands on a structure *already in the
engine*, which is why they hold. Weapon properties already carry gate semantics (the source comment on `blade_guard`
says rings "enhance winding"); the `hand` handling field is a ready proficiency hook; the per-tradition **`mode`**
field is a doctrine axis that currently gates nothing — exactly the lever incompatibility needs; and the tradition
**`set`** field already names the canonical synergy bundle. The headline: my sharpest objection, combinatorial
balance, is *largely dissolved*. Hard physical + doctrinal gates prune the legal build space far more than a slot
limit ever could, and set-bonuses turn combination from a balance liability into a designed feature. This is a net
improvement. The bill is real and I name it in §6: a substantial authoring/completeness burden, set-balance work,
and several hardness dials that are yours to set.**

`[READ: combatant.WEAPONS (property keys) · tradition.TRADITIONS (set/mode/channels) · tradition.ADJACENT (familiarity graph) — grepped this session]`
`[SELF-AUTHORED — bias risk: I raised the concerns these answer; I am conceding the wins and naming the new costs, not defending the prior position]`

---

## §1 — Each counter, evaluated

**① Weapon properties gate techniques.** *Holds, strongly.* The `WEAPONS` dict already carries the gate vocabulary,
and it was clearly authored with this intent: `blade_guard` (0–1; "fore/thumb-rings enhance winding" — longsword
0.85, rapier 0.45, spear 0.20) gates **winding/bind** techniques; `percussion`/`mass`/`pob_frac` (the breach physics
validated this session — mace/poleaxe 8) gate **blunt/breach/structure** techniques; `clinch` (dagger 10, longsword
6, spear 2) gates **grapple/close** techniques; `head` (point/cut_thrust/blunt) gates **thrust vs cut vs percussion**;
`reach` gates **range** (stop-hit needs long; closing needs short or high clinch); `hands` gates **two-hand/off-hand**.
*Convergence:* this session flagged `mass`/`pob_frac` as sourced-but-consumed-nowhere — **gating gives them a
consumer.** *New cost:* every technique now declares property requirements (a schema field, `requires:{…}`).

**② Tradition gates weapons → proficiency.** *Holds.* Hooks the existing `hand` handling penalty
(Forgiving/Standard/Demanding): proficiency mitigates the Demanding cost, non-proficiency suffers it — a graded
mechanism, not just binary. A tradition's weapon list is small new content (German KdF → longsword/arming/dagger/
poleaxe; Italian → arming/rapier/dagger; Spanish → rapier; Chinese → spear/staff; Filipino → paired_short/dagger).
*New cost:* the proficiency lists; a roster-proxy note (no katana/messer in the 12-weapon roster — map to
sabre/arming); and the **cross-training dial** — does training a second tradition grant its weapons?

**③ Cross-tradition incompatibility.** *Holds, and it is the sharpest of the four* — because the engine already
encodes the axis. The `mode` field is the doctrine: german `tactile` · italian `temporal-spatial` · spanish
`geometric` · japanese `intentional` · chinese/filipino `kinetic-rhythmic` · english `biomechanical`. Italian and
Spanish share the **same `set`** ('Thrust Duelist') and similar weapons but carry **different `mode`** — and they are
*adjacent* (familiarity 0.93). So "similar weapons, incompatible approach, even what defending means" is precisely
**same set, different mode**: the Italian temporal-spatial defence (counter-thrust in tempo) and the Spanish
geometric defence (atajo off the círculo) are not interchangeable. The `mode` field, which today only flavours,
becomes the **compatibility gate** — Defence especially is mode-locked. *New cost:* the compatibility relation
(reuse `mode`) and the **hardness dial** (hard-lock vs soft-penalty, likely per-phase).

**④ Skill sets → set bonus.** *Holds, and it closes the loop with history.* A loadout set — a declared combination
of slotted techniques granting an emergent ability/coherence bonus — makes combination **qualitative** (not stacked
dials) and gives the player legible build goals. *Convergence:* the tradition **`set`** field already names the
canonical bundle (Bind Fighter, Thrust Duelist, Counter-time, Burst, Continuous-flow) — completing it grants the
archetype's signature emergent ability. And this is the **integrated-method reality as a mechanic**: the historical
point that traditions are coherent doctrines whose pieces reinforce each other becomes a literal set bonus.
*Naming caution:* the engine's `set` (tradition archetype) ≠ your "skill set" (loadout bonus); I call the latter a
**combination/loadout set**, with the tradition archetype as its canonical instance. *New cost:* set authoring +
set-balance (the best-set problem).

---

## §2 — The three relations, disentangled (the key insight)

These were one blur in my earlier docs; the engine keeps them separate, and so must the design:

| Relation | Engine field | What it governs | Example |
|---|---|---|---|
| **Archetype** | `set` | what kind of fighter | Italian & Spanish are both 'Thrust Duelist' |
| **Doctrine** | `mode` | **compatibility** — can two methods fuse | Italian 'temporal-spatial' ≠ Spanish 'geometric' → incompatible |
| **Legibility** | `ADJACENT` | how well they read each other | Italian–Spanish adjacent (0.93) → they *understand* each other |

The error to avoid: treating adjacency (mutual legibility) as compatibility. **You can read an opponent's game
perfectly and still be unable to fuse your method with theirs.** Italian–Spanish is the proof case: adjacent, same
archetype, incompatible doctrine.

---

## §3 — The integrated gating chain

```
 TRADITION ──sets──▶ channel base profile (identity)  ·  mode (doctrine/compat)  ·  set archetype (canonical bundle)
     │
     ├─proficiency─▶ WEAPONS you wield well ──(mitigates the `hand` Demanding penalty)
     │                   │
     │              properties ──gate──▶ TECHNIQUES physically possible
     │                   (blade_guard→wind · percussion/mass/pob→breach · clinch→grapple · head→thrust/cut · reach→range)
     │
     ├─mode-compat──▶ which CROSS-tradition techniques may be slotted
     │                   (same mode → borrow; different mode → locked, hard on Defence + signature phases)
     │
     └─sets────────▶ completing a coherent bundle → emergent ability / coherence bonus
```
…all layered on the **granular phase/affinity slots**: you fill the 7 phase slots (Approach · Reading · Feint ·
Commit · Defence · Bind · Counter) from the **gated** pool — *weapon-possible ∧ mode-compatible ∧ unlocked* — shape
the 7-channel affinity profile (point-buy, method-based), and aim to complete a set.

---

## §4 — The combinatorial objection, dissolved

The naive build space C(library, k) shrinks under three **hard** gates before the slot limit even applies:

> legal techniques = (your weapon can physically do it) ∩ (your mode permits it) ∩ (you have unlocked it)

That intersection is *small* per (tradition, weapon) — a rapier cannot wind (low `blade_guard`) or breach (zero
`percussion`); a Spanish fighter cannot slot the Italian tempo-defence (mode); you can only use what you trained.
Within the legal set, **sets create attractors** — the design actively steers toward coherent builds (which balance
because they are intended) and away from incoherent soup (which the gates forbid). Balance is validated over
*(tradition × weapon × legal-loadout × set)* — bounded and sim-tractable, and the gates do far more pruning than the
slot count alone. The objection was aimed at a *free* mix; the gating chain means there is no free mix.

---

## §5 — Worked example (the gates, and a block)

**German KdF fighter** — mode `tactile`, set `Bind Fighter`, proficient {longsword, arming, dagger, poleaxe}.
- Picks **longsword**: `blade_guard` 0.85 → winding unlocked · `grip_len` 1.6 → leverage · `percussion` 4 ·
  half-sword form available (`base: longsword`).
- Gated pool includes **Winden** (needs high `blade_guard` ✓), **Stärke-bind**, **half-sword breach**.
- Fills phases: Bind = Winden · Approach = Closing · **Defence = Winden-defence (tactile)** · Commit = Zornhau.
- Completes the **Bind-Fighter set** → emergent *"dominate the bind"* coherence bonus.

**The block:** the German tries to borrow the **Spanish atajo-defence** (mode `geometric`). **Refused** — Defence is
mode-locked, and `geometric ≠ tactile`. Note this is *not* a legibility issue (German–Italian and Italian–Spanish are
adjacent); it is doctrine: you cannot defend by the Spanish circle while fighting the German bind. This is your
"what defending should do is incompatible," grounded in `mode`.

**The soft trade:** the German *may* borrow an English (`Counter-time`, `biomechanical`) anti-overcommit technique
into a *peripheral* phase — but doing so breaks the Bind-Fighter set (cross-mode forfeits the coherence bonus). A
real cost, a real choice.

---

## §6 — The bill (honest) + decisions

The wins are real; so is the cost. A fair reviewer names both.

- **Authoring/completeness burden — the main cost.** Every technique needs property-requirements + a mode tag; every
  tradition needs a proficiency list; every set needs a definition + a balanced bonus. The weapon properties exist;
  the rest is new content, and it must be *complete* (a missing tag means an illegal build slips through or a legal
  one is blocked). This is the same completeness discipline the project applies elsewhere — applied to a larger
  surface.
- **Set-balance.** Sets can mint dominant builds (the best-set problem); each set bonus needs vacuum-balance, and the
  archetype sets must be cross-balanced (no tradition's set strictly dominates). Still a sim problem — now with
  set-bonuses layered on.
- **NERS-E watch.** The apparatus is now large. The defence: it is *qualitative* apparatus — gates and sets do
  qualitative work (forbid the impossible, reward the coherent), unlike 55 additive dials. That is more defensible,
  but "large and qualitative" still must justify itself against "small and legible." Keep an eye on it.
- **Decisions (the dials are now concrete):** (a) **mode-lock hardness** — hard on Defence + signature phases,
  soft (penalty / set-forfeit) on peripheral phases? (b) **cross-training weapon access** — does a second tradition
  grant its weapons? (c) **partial sets** — 2-piece/4-piece thresholds, or all-or-nothing? (d) **proficiency grading**
  — binary or a scale on the handling penalty? (e) the roster-proxy mappings (katana/messer → sabre/arming);
  (f) the sim plan: legal-loadout × set win-rates flat within ±2–3 pp at N≈3000.
- **Mechanical, not creative.** The gating chain, proficiency lists, and sets are mechanical; which cultures train
  which tradition — the world-fiction — is yours. Historical names (Winden, Zornhau, atajo, the círculo) stay
  anchored; mechanical fill graded `M`; no fabricated history.

`[CONFIDENCE: high]` that the four counters answer the concerns and that the combinatorial objection is largely
dissolved (each gate grounded in an existing field). `[CONFIDENCE: medium]` on the exact hardness/threshold settings.
`[GAP: unvalidated]` — the gating completeness and set-balance need the sim test before any of this is canon.

Provisional; engine unchanged. This consolidates the ability-system thread (comprehensive library → reconciliation →
FFT parallel → granular phases → these four counters) into one coherent model: **granular phase/affinity slots,
populated through a tradition→proficiency→weapon→property→mode gating chain, rewarded by coherence sets.**

*The visual is now the right capstone: an equip screen that walks the chain — pick tradition → see proficient
weapons → pick weapon → the technique pool lights up only what's legal → slot into the seven phases → a set-meter
fills as a coherent bundle completes, with the cross-mode block shown live. Say the word.*
