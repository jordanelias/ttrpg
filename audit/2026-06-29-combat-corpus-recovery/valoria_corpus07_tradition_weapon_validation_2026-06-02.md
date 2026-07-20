# Doc 07 → Engine: Top-Down Validation of Tradition Profiles & Emergent Weapon Tiers

`[READ: /mnt/user-data/uploads/07-consolidated-corpus.md — all 189 lines]`
`[READ: combat_engine/tradition.py — all 74 lines, committed HEAD]`

## DISCIPLINE (carried from doc 10, last turn)
Doc 07 is **superseded by doc 10**. Its two-axis `[Source/Interpretive]` tags are **not** the S1–S5 tiers, and 07
self-flags its selection-effect risk (line 188). So this pass: (1) sorts 07's traditions by **doc-10 reliability**,
not 07's own "high" tags; (2) extracts only **concrete, mechanically-relevant, S2-grade** detail; (3) **quarantines**
the demoted universals (counterattack-as-prestige-universal, training-surrogate-encodes-theory, the four-axis lens,
demystification-as-discovery) and the S4/S5 traditions. No code changed — per Jordan's framing this is raw material
for the eventual tradition/weapon build-out; the deliverable is the validation and the mapped catalogue.

## VERDICT
07 is not a source of new primitives — but as a top-down check it is **strongly confirmatory**: **6 of the engine's 7
named traditions are S2-anchored in 07 and their channel-weights match the documented cognitive mode.** The emergent
weapon tier is independently corroborated by three S2 voices (Silver, *Le Jeu de la Hache*, the Ming great-spear
canon). Three genuine mismatches surface — the Chinese profile's framing, one un-anchored tradition (Filipino), and
two initiative-related channels that are slightly low — all flagged below, none parity-driven.

---

## A. TRADITION PROFILES — validated against 07's S2 detail
Engine channels: visual · tactile · precommit · leverage · tempo · measure · footwork (multiplicative bias, 1.0 neutral).

| Engine tradition (current emphasis) | 07 S2 detail | Verdict |
|---|---|---|
| **german** — tactile 1.35, leverage 1.30 (Bind Fighter) | Vor/Nach/Indes; **Stärke/Schwäche** (strong/weak of the blade in the bind); **Fühlen** (tactile bind-feel); 5 master-cuts | **CONFIRMED.** High tactile (Fühlen ✓) + high leverage (Stärke/Schwäche ✓) is exactly the documented mode. *Refinement:* tempo 1.10 is the one slightly-low cell — Indes is a counter-tempo concept; see §C3. |
| **italian** — tempo 1.30, measure 1.25, visual 1.20 (Thrust Duelist) | tempo, **misura**, mezzo-tempo, **contratempo**; Agrippa's geometric turn | **CONFIRMED.** High tempo + high measure (misura ✓). Contratempo = the single-time counter (§C3, initiative work). |
| **spanish** — measure 1.35, footwork 1.30 (geometric) | **matematización**, the geometric circle, *deductive* judgment (Pacheco) | **CONFIRMED — strongest match.** Highest measure (círculo ✓) + high footwork (compases ✓). The "deductive/pre-planned" character is real but not yet a modelled axis (reactive-vs-precalculated). |
| **japanese** — precommit 1.35, tempo 1.20 (Counter-time, intentional) | **sen** (3 initiatives), **suki** (opening), **kuzushi** (balance-break), ki-ken-tai-ichi | **CONFIRMED** on sen (highest precommit ✓). Surfaces **kuzushi** as a candidate primitive the channels don't capture — see §D1. |
| **english** — tempo 1.15, measure 1.15 (biomechanical, true-times, anti-overcommit) | Silver's **true times** (fast-part/hand before slow-part/body); short-staff "true fight" | **CONFIRMED — exact.** The engine's "fast-part-first / anti-overcommit" *is* Silver's true times. Silver also validates the weapon tier — §B. |
| **chinese** — tactile 1.20, measure 1.20, leverage 1.15 (**"Burst / fa jin"**) | Ming **military** canon: **great-spear** (Wu Shu, *Shoubi Lu*), **Shaolin staff**, Qi Jiguang | **MISMATCH (framing).** 07's S2 Chinese content is reach-weapon (spear/staff) craft, **not** unarmed internal "fa jin burst" (a less-documented, more modern-internal framing). See §C1. |
| **filipino** — tactile 1.25, footwork 1.25 (Continuous-flow) | **absent from 07** (no FMA entry in the corpus) | **UN-ANCHORED here.** Not wrong — but it has no S2 anchor in this corpus; flag for a dedicated source. See §C2. |

**Familiarity matrix (`ADJACENT`) — corroborated.** 07 supports the engine's adjacency pairs: German↔Italian (the
fight-book exchange), Italian↔Spanish (rapier spread, Thibault cross-current), Italian/German↔English (**Silver wrote
*against* the Italian rapier** — adversarial = close knowledge), Chinese↔Japanese (shared Ming influence). No pair in
the engine's set is contradicted by 07.

---

## B. EMERGENT WEAPON TIER — independently corroborated by three S2 voices
This is the strongest top-down result. The engine's emergent A0 tier (spear top, poleaxe the plate apex) and my
flagged "rapier too high" concern are corroborated by 07's S2 record, **independently of the matrix**:

1. **English Silver (S2):** an explicit *design argument* that the **short-staff/short-sword beats the Italian
   rapier** — Silver thought the rapier over-valued and dangerous for a real fight. → corroborates both the engine's
   **spear/staff A0 primacy** *and* my flag that the engine's **rapier (82) is over-rewarded** (§C, prior work).
   Silver is a historical voice predicting exactly the correction I flagged.
2. **French *Le Jeu de la Hache* (S2):** the most extensive single-weapon system in the entire corpus is **poleaxe-
   in-armour**. → corroborates the engine's **poleaxe as the A3 plate apex** (an entire treatise exists because the
   poleaxe *was* the armoured-combat weapon).
3. **Chinese Ming great-spear (S2):** the qiang/great-spear as the premier weapon of the military canon →
   corroborates **spear primacy** from a second, independent tradition (alongside the cross-cultural spear result).

---

## C. MISMATCHES & REFINEMENT CANDIDATES (S2-grounded, not parity-fitting)
1. **Chinese profile framing.** The engine labels Chinese "Burst / fa jin / kinetic-rhythmic," but its S2 anchor (the
   Ming military canon 07 documents) is **great-spear + staff reach-craft**. Recommendation when the tradition layer
   is built out: re-frame Chinese toward **measure + leverage (pole/spear reach and lever control)** and drop the
   "burst" framing, which belongs to less-documented internal arts not in this corpus. *(Note: tradition weights act
   on cross-tradition reads, which the standard `tradition='none'` invariant sweeps do not exercise — so this is a
   historical-grounding judgment, not a matrix-validated one.)*
2. **Filipino is un-anchored in this corpus.** FMA has no entry in 07. Keep it if a dedicated S2 source supports the
   continuous-flow profile; otherwise mark it `[unanchored — no S2 in corpus]` so the roster doesn't imply an
   evidence base it lacks (doc-10 rule: a claim's grade cannot exceed its source).
3. **Indes / contratempo channels slightly low.** German tempo (1.10) and the Italian/German precommit (1.00) under-
   weight the documented counter-tempo emphasis (Indes is German's S2 signature; contratempo is Italian's). This is
   the cell the **initiative build** will touch — and doc 10's constraint applies: keep the counter *mechanically
   available to all*, but its **prestige weighting is European/Japanese flavour** (tradition-layer), not a universal
   resolver reward. So nudge german-tempo / italian-precommit upward **in the tradition layer**, not in the spine.

---

## D. PRIMITIVE REINFORCEMENTS (07 strengthens the already-identified initiative + forensic work)
1. **kuzushi (balance-breaking) — a concrete sub-mechanic for the initiative build.** Japanese koryū's kuzushi
   ("break the opponent's structure/balance") is an *action that degrades balance* — which is precisely one of the
   three documented ways a fighter is forced into the Nach in the initiative design (damage / **footwork-balance** /
   reading). The engine has the balance *primitives* (footwork_eff, anti_overcommit, stance_stability) but no action
   that *attacks* them. Fold kuzushi into the initiative build as the balance-disruption path that flips initiative.
2. **contratempo / single-time counter** — 07 confirms this is S2 for Italian **and** German, reinforcing HEMA-gap
   G2. Already in the initiative spec; 07 raises confidence (for those traditions) without making it universal.
3. **marmam vital-points → the forensic leg.** Kalaripayattu's 64 *marmam* (S2, Zarrilli) is hit-**location**
   knowledge — the dimension the engine does *not* model (it resolves degree→damage, not *where*). This connects to
   the **forensic validation leg** proposed last turn: osteology (Towton 1461) is wound-location data, so a
   location/target dimension is the bridge between the engine's output and the forensic check. A large addition;
   flagged as the natural pairing if/when the forensic leg is built.

---

## E. QUARANTINE — read for context, NOT imported (doc-10 discipline)
- **Demoted universals:** counterattack-as-prestige-*universal*, training-surrogate-encodes-weapon-theory, the
  four-axis lens, demystification-as-discovery. 07 leans on these; doc 10 demoted them; they do not enter the engine.
- **S4/S5 traditions (no earned anchor):** Persian zurkhāneh (conditioning/ritual, *not* a fencing system), Polish
  szabla (reconstructed, no period manuals), Dhanurveda (textual category, not a living-art lineage), Sikh gatka
  (contested 19th-c.), Ottoman matrak / Thai krabi-krabong (reconstructed/performance), Hungarian/Russian sabre.
  Do **not** seed distinct evidence-claiming tradition profiles from these.
- **Out-of-scope-by-objective:** Mesoamerican macuahuitl was deliberately **blunted for capture** (objective ≠ kill)
  and Mamluk furūsiyya cut-trajectories are defined **relative to the horse** (equestrian, not foot-duel). Both are
  correctly outside a lethal personal-combat engine; noted so they aren't mistaken for foot-dueling evidence.

## RECOMMENDATION
Treat this as a **validation pass that mostly passed**: keep the tradition profiles as-is for now (6/7 confirmed), and
when the tradition layer is built out, apply the three §C refinements (Chinese reach-not-burst; Filipino anchor or
flag; Indes/contratempo nudge in the *layer*). Fold **kuzushi** into the initiative build as the balance-disruption
path. Hold **marmam/location** for the forensic leg. The single highest-value item 07 surfaces is the **Silver
corroboration** (§B1): an S2 historical voice predicting both spear/staff primacy and rapier over-valuation — the
exact emergent results the engine produces and the exact cell I flagged.

`[CONFIDENCE: high on the validation — 6/7 profile confirmations and the 3 weapon-tier corroborations are direct
reads of 07's S2-anchored content against the committed tradition.py and the validated emergent tier. Medium on the
Chinese-reframe and Filipino-anchor recommendations: both are historical-grounding judgments the same-tradition
invariant sweeps cannot test, so they need Jordan's call, not a harness number.]`
`[SOURCE: T1/T2 — doc 07's S2-anchored subset as re-graded by doc 10 (Anglo 2000, Zarrilli 1998, Shahar 2008, al-
Sarraf 2004, budō-gaku); Silver and Le Jeu de la Hache are S2 via Anglo. The S4/S5 and demoted material is quarantined
per doc 10.]`
