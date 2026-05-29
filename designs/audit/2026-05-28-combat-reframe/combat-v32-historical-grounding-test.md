# Combat v32 — Historical-Grounding Test (weapons × schools)

A grounding pass over combat_v32's **8 weapon classes** (§8) and **10 combat Traditions / "martial schools"** (§5), testing each against the three historical-precedent documents produced earlier in this work, with each finding cross-referenced to the canonical NERS criteria and the resolution-diagnostic lessons where it bears.

`[SELF-AUTHORED — bias risk]` combat_v32 is prior-Claude-session work (the reframe blueprint states it "reframes my own proposal"). Per the resolution-diagnostic skill's first guardrail this is tested as **external** work; the bias to guard against is congratulating the design for "matching history."

---

## VERDICT (read first)

**The weapon and school layers are historically coherent, but the test cannot independently *validate* them — it can only check internal consistency and surface divergences — because v32 was very likely built from the same historical traditions this test uses as its yardstick.** That circularity is the governing caveat (next section). Within it: the **school layer (§5) is the stronger of the two** — its ten Traditions map almost one-to-one onto the precedent documents' traditions, and, more tellingly, v32's *Intent-Reading tier* ranking independently reproduces the manual's ranking of which traditions theorise intent most deeply. The **weapon layer (§8) is mostly grounded** but carries **one real divergence (the staff), one genuine gap (no short-blunt class), and one internal-consistency defect (the "seven vs eight" miscount)**. None of these is a canonical defect — historical divergence can be the correct *game* choice — they are design flags for Jordan.

**Scope of this pass.** This is the *historical-grounding* lens only — essentially the diagnostic's Phase-5 intent gate plus a cross-tradition coherence check. It is **not** the full per-system 4-stage NERS diagnostic (that is 18 separate multi-stage runs), and it is **not** the I-17 numerical balance sim (history cannot tune matchup percentages). It **complements** the existing `ners_verdict_combat_v32.md`: the staff and short-blunt findings here are **new** (absent from that verdict); the rest sit alongside it.

---

## THE CIRCULARITY CAVEAT (governs every "PASS" below)

The precedent documents are **external research, not Valoria canon** — so a weapon "passing" or "failing" them is a heuristic, never a canonical pass/fail. But there is a sharper problem than externality: **the correspondence between v32 and the historical record is partly built-in.** The §5 aspect bundles read like a direct transcription of the traditions — Forward-point stance *is* Agrippa; Tactile reading *is* German *Fühlen*; Geometric reading + Curvilinear footwork *is* Spanish Destreza's *círculo* and *compás curvo*; Triangular + Paired *is* Filipino *sinawali*; the Curved-blade-cavalry "Thumb-anchor grip" *is* the Polish *szabla*'s *paluch* thumb-ring; the Tier-5 Single-strike Tradition *is* Itto-ryū's *kiriotoshi*. If v32's designer drew on these same sources, then "testing v32 against them" is checking v32 against **its own inspiration** — consistency, not independent validation.

What this pass therefore *can* legitimately do:
1. **Check internal consistency** of the historical mapping (does each Tradition's bundle actually cohere as the tradition it names?).
2. **Find divergences** — places where v32 departs from its own apparent historical basis (these are the findings with teeth: the staff, the short-blunt gap, the German intent tier).
3. **Test whether each divergence is deliberate** (Phase-5 intent gate: does the proposal *state* a rationale?), distinguishing a considered game choice from an unexamined inheritance.

What it **cannot** do: certify that v32 is "well-designed because it matches history." It does not, and history is not the design goal (`design_doc_framing`: the test is Godot-implementability and player experience, not historical fidelity).

---

## PART 1 — WEAPON CLASSES (§8) grounding matrix

v32 values cited from `combat_v32_proposal §8.1/§8.2/§8.4`; canonical TN/STR/armour from `combat_v30 §5` via the verified `m3_weapon_class_layer.py` constants. Historical anchors from the three precedent docs.

| # | v32 class | Handling · Speed | Historical anchor | Grounding | Finding |
|---|---|---|---|---|---|
| 1 | Long thrust-primary | Demanding · +1.5 | Italian/Spanish **rapier** | **PASS (strong)** | Demanding-precision + Forward-point fit = Agrippa exactly; the manual rates the rapier Demanding. |
| 2 | Long cut-and-thrust | Standard · +0.5 | German **longsword** (Liechtenauer) | **PASS (strong)** | Wind/Press/Grip-change + Half-grip-available = *Winden* + *Halbschwert*; Standard handling matches the manual. |
| 3 | Curved cut-primary | Standard · +2 | **sabre** family | **PASS** | "curved blade slides out of contact / limited binds" = the draw-cut, less-binding profile; the manual's many-traditions sabre. |
| 4 | Long pole (spear) | Forgiving · 0 | **spear** (Chinese *qiang* et al.) | **PASS (strong)** | Forgiving + reach/zone control = the mass-troop "king of weapons"; matches both precedent docs. |
| 5 | Long pole (staff) | **Forgiving** · 0 | **quarterstaff / gùn** | **TENSION** | **F-W1:** v32 = low-ceiling generalist's tool; Silver ranked the short staff a *superior* weapon and the Chinese *gùn* is a master's weapon. Handling diverges from the record. |
| 6 | Paired short | Demanding · +2.5 | Filipino **doble baston** / paired blades | **PASS (strong)** | "no decisive single strike," both blades active = the *flow* paradigm + *sinawali*; Demanding two-blade coordination is the manual's reading. |
| 7 | Single short | Forgiving · +3 | **dagger** (Fiore; rondel) | **minor TENSION** | **F-W3:** rated Forgiving/low-ceiling, but Fiore treats the dagger as a *foundational, technically rich* weapon. Defensible for a generic short blade; flag is mild. |
| 8 | Long Heavy Blunt | Demanding · −0.5 | **pollaxe** (war hammer/poleaxe) | **PASS** (with residual) | Proposal anchors Demanding to the pollaxe (*cf. Le Jeu de la Hache*) — historically correct; the pollaxe is the one percussion weapon with a rich art. **Residual F-W4** below. |

**Coverage flags (not per-class):**
- **F-W2 — no short-blunt class.** The eight classes have **no home for one-handed percussion** (mace, club, cudgel — Irish shillelagh, French *canne*, Zulu *isikhwili*, *tonfa*). The completed blunt survey confirms this is a *real* tradition family, though a thin one (much of it reconstruction/sport/conditioning). Genuine gap; low-stakes to fill.
- **F-W5 — "seven vs eight" miscount.** §8 states "**Seven** weapon classes" but enumerates **eight** rows (and `m3` encodes eight). Internal-consistency defect; cosmetic but should be reconciled.

---

## PART 2 — COMBAT TRADITIONS (§5) grounding matrix

The ten Traditions, their historical anchors, and Intent-Reading tier (`combat_v32_proposal §5.2`). Faction bindings are Valoria world-canon and are **not** tested against history (project-owner contract — they are the world's own content).

| # | v32 Tradition | Intent tier | Historical anchor | Grounding |
|---|---|---|---|---|
| 1 | Long-thrust dueling | 2 Steady | Italian rapier (Agrippa) | **PASS (strong)** — Forward-point + Linear + Decisive. |
| 2 | Long-blade contact | **1 Surface** | German longsword (Liechtenauer) | **PASS, minor flag F-S1** — Tactile + Yielding/Pressing + half-grip = *Fühlen*/bind/*Halbschwert*; but Tier-1 intent arguably undersells German *Indes*. |
| 3 | Long-thrust geometric | 1 Surface | Spanish **Destreza** | **PASS (strong)** — Geometric reading + Curvilinear footwork = the *círculo* and *compás curvo*; "mathematical training" is Destreza exactly. |
| 4 | Counter-time | **4 Pre-empt** | Italian *contratempo* (counter cluster) | **PASS (strong)** — Drawing + Reactive + Hand-led counter; the "Pre-emptive counter" Master technique = *contratempo* / *sen-no-sen*. |
| 5 | Single-strike | **5 Master** | Japanese **Itto-ryū** | **PASS (strong)** — Stance-flux + Intent focus; "Single decisive strike" = *kiriotoshi* / *issatsu no tachi*; highest intent tier = the consciousness mode. |
| 6 | Curved-blade cavalry | 1 Surface | Polish/Mamluk **sabre cavalry** | **PASS (strong)** — "Thumb-anchor grip" = the *szabla*'s *paluch* thumb-ring; Rhythmic + Burst = cavalry sabre. |
| 7 | Continuous-flow | 2 Steady | Filipino **FMA** | **PASS (strong)** — "Continuous (no discrete stance)" + Triangular + Paired + Rhythmic = the kinetic-rhythmic *flow* paradigm. |
| 8 | Mounted multi-weapon | 2 Steady | Mamluk **furusiyya** / knightly *Roßfechten* | **PASS** — lance→saber→sword multi-weapon = furusiyya's "proficiency in all weapons" + European mounted combat. |
| 9 | Conditioning-and-grappling | 1 Surface | Fiore **abrazare** / pehlwani | **PASS (strong)** — grappling-as-foundation = Fiore's base; the name literally matches the blunt survey's finding that the Indian akhara gada is *conditioning, not combat*. |
| 10 | Formation-and-discipline | 1 Surface | pike block / Korean military standardisation | **PASS** — Patterned anticipation + Coordinated approach + formation positioning = the formation-deployment tradition. |

**The ten Traditions span the manual's full cognitive-modes typology** — temporal-spatial (1, 4), tactile (2), geometric (3), consciousness-theoretical (5), kinetic-rhythmic (6, 7), and the cross-context modes (8 cavalry, 9 grappling-base, 10 formation). The taxonomy is complete and coherent, not arbitrary. (Read with the circularity caveat: this is strong *internal* coherence, not independent proof.)

---

## PART 3 — THE FINDINGS WITH TEETH (the divergences)

Review discipline: the matrix is mostly PASS, so the value is in the few divergences. Each is a **design flag for Jordan**, not a canonical defect.

### F-W1 — The staff's handling contradicts the historical record (TENSION; the one real weapon divergence)
v32 rates `Long pole (staff)` **Forgiving** — "accessible percussive control," H capped at 3 (low ceiling), no cut, lower wound-transition rate (`§8.2/§8.4`). The precedent record says the opposite: **George Silver ranked the "short staff" at or near the top of all single-combat weapons** (reach + speed + two-handed control beating sword-and-dagger and rapier), and the **Chinese *gùn* is the "grandfather of weapons" with the oldest datable Chinese fight manuals** devoted to it. Historically the staff is a *master's high-ceiling weapon*, not a generalist's low-ceiling one.
- **Intent-gate status:** the proposal gives a one-line rationale ("accessible percussive control") but does **not** address the contradiction with the staff's historical standing → treat as **deliberate-but-unexamined**; surface for a decision.
- **Diagnostic/NERS bearing:** touches **NERS-S** (consistency) and the build axis — if the staff is mechanically a floor weapon while every developed tradition treats it as a ceiling weapon, builds that should reward staff mastery don't. Not a balance *defect* per se; a grounding-and-flavour divergence with a mild build-axis cost.
- **Options (Jordan's call, not proposed here):** re-rate the staff Standard or Demanding to match its historical standing; *or* split the class (a forgiving "simple stave" vs a demanding "staff method"); *or* ratify Forgiving as a deliberate game simplification and document the divergence.

### F-W2 — No short-blunt class (genuine gap)
Covered above; restated as a finding because it is the one *missing* weapon family rather than a mis-parametrised one. The eight classes are all *long* or *short-blade*; one-handed percussion (mace/club/cudgel) has no class. **NERS-N bearing is inverse:** adding a class must itself be necessary — and the blunt survey shows the short-blunt art corpus is thin (reconstruction/sport/conditioning), so this is a *low-priority* gap, arguably below the "necessary" bar. Flag, don't force.

### F-W4 — The bare mace is not represented (RESOLVED — recorded for completeness)
Earlier in this work I flagged that `Long Heavy Blunt` fuses a *Demanding* pollaxe with a *forgiving* bare mace. The proposal **resolves this in its own favour**: it explicitly chooses the **pollaxe** as the archetype (Demanding, *cf. Le Jeu de la Hache*) and lists the bare mace/war hammer only as examples. The blunt survey **vindicates the choice** — the bare mace has almost no transmissible art, so modelling the pollaxe (which does) rather than the bare mace is the correct call. **No action;** the only residual is that the cheap, forgiving, levy-weapon *bare mace* simply isn't a separate option, which is fine unless Jordan wants a peasant-mace flavour (it would pair with F-W2).

### F-W5 — "Seven vs eight" count (internal consistency)
§8 says seven classes, lists eight. Cosmetic; reconcile the prose to the table.

### F-S1 — German tradition's Intent tier may undersell *Indes* (minor school flag)
`Long-blade contact` (German longsword) is given **Intent Tier 1 (Surface)**, the lowest. The German tradition's *Indes* / *Fühlen* — deciding on contact, "within the duration of a sustained note" — is a *sophisticated* perceptual skill in the manual's reading, arguably warranting more than Surface. The mitigant: the Tradition carries **Tactile reading** as its aspect, so bind-feel is represented *as an aspect* even if the *Intent* tier is low; and Intent-Reading in v32 is a specific pre-/intra-commit track distinct from tactile bind-sensitivity. So this is a **mild** flag, not a clear error — but if the design intends Intent-tier to track "perceptual sophistication," the German tradition is plausibly underranked relative to the Italian (Tier 2) and especially the counter/decisive traditions (Tiers 4–5).

---

## PART 4 — THE STRONG CORRESPONDENCES WORTH RECORDING

Review-mode permits positives that *narrow where the design is solid / confirm grounding*. These do that. (Still under the circularity caveat.)

1. **Intent-tier ranking reproduces the manual's intent-depth ranking.** v32's two highest Intent tiers go to **Counter-time (Tier 4)** and **Single-strike (Tier 5)** — precisely the Italian-*contratempo* and Japanese-*sen* traditions the manual identifies (§15.5 and the *sen* tiers) as theorising pre-commitment intent most finely. v32 independently ranked intent-reading depth the way the manual ranks it. This is the single most striking correspondence and the strongest internal-coherence signal.
2. **The §15.5 counterattack-context result holds.** The high-intent traditions (Counter-time, Single-strike) are the **dueling-context** ones (Hafenmark duelists, Niflhel sword-saints); the **multi-opponent / cavalry / formation** traditions (6, 8, 10) get the *low* intent tiers. This matches the manual's load-bearing finding that counterattack-prestige is the *dueling-context* apex and not universal — v32's tier assignments fall out the way the manual's analysis predicts.
3. **Weapon↔school fit instantiates "weapon constrains the option-set; the school selects from it" (Throughline T7).** The same `Curved cut-primary` weapon fits both Curved-blade-cavalry and Continuous-flow (`§8.7`) — exactly the manual's "same sabre family, different cognitive frameworks."
4. **Stance Counter kept authored = the manual's stance-as-irreducible-cyclic-counter.** §7.1 keeps the 5×5 Stance Counter authored because it is ~85% cyclic (resists reduction); the manual independently confirms stance-as-relational-counter is a genuine, cross-cultural, *irreducible* feature — so the §7.1 decision is historically as well as mathematically sound.

---

## PART 5 — NERS / DIAGNOSTIC CROSS-REFERENCE & DISPOSITION

**Mapping the findings to the canonical frame** (NERS per `canon/definitions.yaml` / PI `<definitions>`; lessons per `valoria-resolution-diagnostic`):

| Finding | NERS criterion | Diagnostic lesson | Severity (grounding lens) |
|---|---|---|---|
| F-W1 staff handling vs Silver | S (consistency) + R (build) | Lesson 2 (uniform impact) only loosely | **Moderate** — flavour + mild build cost |
| F-W2 no short-blunt class | N (inverse — necessity) | — | **Low** — thin corpus; below necessity bar |
| F-W3 single-short Forgiving vs Fiore | (flavour) | — | **Minor** |
| F-W4 bare-mace non-representation | N | A5 (derive/represent only what's needed) | **Resolved** |
| F-W5 seven-vs-eight count | (internal consistency) | — | **Cosmetic** |
| F-S1 German Intent tier vs *Indes* | (taxonomy consistency) | — | **Minor** |

**Relationship to `ners_verdict_combat_v32.md`.** That verdict's open items (F3 shared Concentration, F7 Reading over-split) and new concerns (N1 stance-transition swing, N3 σ-space divergence, N4 set cliff, N5 handling necessity) are **balance/structure** findings; the findings here are **grounding/flavour** findings. The two are orthogonal — except **N5 (is handling necessary?)**, which this pass speaks to directly: the precedent record supplies cross-cultural *evidence that ease-of-use is a real attested dimension* (spear forgiving, rapier/paired demanding, pollaxe demanding), i.e. **evidence toward keeping handling** — while **F-W1 simultaneously shows one handling assignment (the staff) is miscalibrated against that same evidence.** So: keep the handling *axis*; revisit the staff *value*.

**Editorial-ledger disposition.** These are **design-review** flags, not canon-consistency gaps, so none *forces* a `canon/editorial_ledger.jsonl` entry under the audit protocol. If Jordan wants any logged, **F-W1 (staff)** and **F-W2 (short-blunt gap)** are the two worth an entry. Note: a ledger write needs a commit, and **branch protection (finding B6) currently blocks PAT commits to main** — so logging would stage inline + flag `[DRIFT]` per protocol, not commit. Not done here (not requested + B6).

**This pass is the grounding lens, complete for weapons and schools.** The natural next tranches, each a distinct effort: (a) the **full per-system 4-stage NERS diagnostic** on the priority weapon(s)/tradition(s) the findings flag (staff first); (b) feeding the grounding findings into the **I-17 balance sim** as calibration inputs (esp. the staff handling value); (c) extending the grounding lens to the parts not covered here — the **§7 Reaction families** and the **§6 aspect specialisations** (stances, footwork, grips) at the same depth.

---

`[CONFIDENCE: high — every v32 claim cites the fetched proposal §5/§7/§8 or m3-encoded combat_v30 §5; every historical claim cites the three precedent docs]`
`[CONFIDENCE: medium — on the strength of the "PASS" verdicts specifically, because of the circularity caveat: high internal-consistency, not independent validation]`
`[SELF-AUTHORED — bias risk: v32 is prior-Claude work; I led with the circularity caveat precisely so the near-universal PASS verdicts are not mistaken for the design validating itself, and I kept the report's weight on the divergences (F-W1, F-W2, F-S1) rather than on the flattering correspondences]`
`[READ: combat_v32_proposal.md §5 (L476–632), §7+§8 (L992–1181); m3_weapon_class_layer.py (full, prior); canon/02_canon_constraints.md (fetched this session for audit-gate compliance; deep P-01–P-15 mapping deferred to the full NERS pass); valoria-resolution-diagnostic-SKILL.md + PI <definitions> (NERS criteria)]`
`[ASSUMPTION: "testing ... with historical precedents as guides" = the historical-grounding lens, not the I-17 numerical sim — basis: history cannot tune matchup percentages; the precedents bear on design coherence. Surfaced; proceeded.]`

*Grounding documents (external, heuristic — not Valoria canon): `combat-manuals-seven-axes-throughlines.md`, `manual-vs-combat-v32-bridge.md`, `blunt-weapon-martial-traditions-completed.md`. v32 source: `designs/proposals/combat_v32_proposal.md` (PROPOSAL; canon baseline is `designs/scene/combat_v30.md`). Findings are design flags for Jordan; none is a canonical defect, and historical fidelity is not the design goal.*
