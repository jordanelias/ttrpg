# Quantity Reference & Decision Surface — planning companion to the Attribute/Value Coherence Audit

## Status: REFERENCE (read-only synthesis, 2026-07-08) · Lane: IN · Anchor: ED-IN-0029
## Companion to: the 2026-07-08 attribute/value coherence audit (this folder) and `proposed_quantity_armature_extension.md`
## Not canon, not a docket. This document RULES nothing — it assembles, in one place, what every
## contested quantity *is*, where it is *used*, and what *choosing* each way would cost, so the
## ED-IN-0029 docket (`ed_options.md`, OPT-AV-1..18) can be ruled from a single surface.

---

## §0 · How to use this document

The audit proper (`attribute_value_coherence_v1.md`) is verdict-first and defect-oriented: it proves
*that* the corpus is incoherent and *where*. This companion is the inverse — it explains, for a
reader deciding the docket, *what each quantity means in the game*, *every place it is consumed*, and
*what each fork's options would actually do to the corpus*. Read it alongside:

- `ed_options.md` — the 18-item Jordan-rulable docket (the decisions).
- `02_census/quantity_census.{md,yaml}` — the 88-row machine inventory (the raw data).
- `01_workings/dossier_C{1..7}.md` + `critic_C{1..7}.md` — the per-cluster forensic traces.
- `proposed_quantity_armature_extension.md` — the proposed fix (registry deltas + A17/A18 checks + wave).

**The three-tier structure of the decision.** Every docket item falls into exactly one of:
- **A genuine design fork** — competing options with real consequences, no pre-existing ruling. These
  need Jordan. §3 expands each with options + consequences.
- **A propagation of an already-made ruling** — the decision exists; only the corpus never caught up.
  Pure execution, no judgment. §4 lists these.
- **A tooling/enforcement build** — new checks (A17/A18), registry filings, tier promotions. Sequenced
  in §5.

**The one-sentence diagnosis.** The per-*quantity* mechanical layer is mostly sound (~50 of 88
quantities are coherent). The incoherence lives in the **carriers** (the same number restated in N
places, drifting) and the **enforcement** (nothing stops a doc from reintroducing a stale name or
formula — every attribute key is `warn`-tier, the registry test is dead, `stat_deltas` accepts any
string, and no tool parses prose formulas at all).

---

## §1 · The core problem, stated precisely

Jordan: *"we desperately lack unity, consistency and coherence with our explosion of attributes and
derived scores across all our different systems and subsystems developed in silos."*

The audit confirms the diagnosis and sharpens it into four structural failure-classes. Every docket
item is an instance of one or more of these:

| Class | What it is | Canonical examples |
|---|---|---|
| **Roster divergence** | The *set* of quantities disagrees across surfaces | 4 incompatible attribute rosters (7/9/10/10); `Recall`/`Coherence` load-bearing but unregistered |
| **Formula re-transcription** | One quantity, N restated formulas, drifting | Combat Pool ×3; Knot Pool ×4; Health ×3; Mandate ×2 |
| **Name collision** | One name, N unrelated quantities (or N names, one quantity) | "Discipline" (faction vs unit); "Standing" (3–4 senses); "Influence" (attribute alias vs faction stat); MS/RS, IP's three names, PT/CT/CV |
| **Enforcement gap** | Nothing can *catch* the above | all `warn`-tier; dead registry test; `stat_deltas` unvalidated; no prose-formula detector; 13 secondary indices with no live generator |

The armature framing (this audit is the quantity-layer extension of the Key & Echo Armature,
ED-IN-0018) names the root cause in doctrine terms: silo-grown stat vocabularies are **shape
divergence** (holonic doctrine ED-1083 §2) — the same disease the armature §2.4 already fixed for
provenance naming (the `causes[]`/`cause_keys`/`origin_keys` split).

---

## §2 · Quantity reference — what each contested quantity is and where it is used

Organized by domain. For each: the **concept** (what it models in the fiction/game), its **scale**,
the **canonical definition** (the one authoritative site), and its **consumers**. Citations are
`file:line`; where a formula is contested the divergence is flagged inline and expanded in §3.

### §2.1 · Personal attributes

The player-character attribute roster. This is the single most divergent surface: `params/core.md`
carries a **10-attribute / 4-group** roster (Physical 3 / Mental 3 [Cognition, Recall, Focus] / Social
3 / Metaphysical 1 [Spirit]); `descriptor_registry.yaml` carries a **9-attribute / 3-group** roster
that folds Spirit→"Will" into mind and *omits Recall entirely*; `glossary.md` carries a **7-attribute**
table missing Focus, Recall, Bonds, Charisma; `canonical_registry.md` carries a **second** 10-table
that `CURRENT.md` never indexes. See OPT-AV-1 (§3.1).

| Attribute | Concept | Key consumers (file:line) | Coherence |
|---|---|---|---|
| **Cognition** *(registry: "Acuity")* | Reasoning, memory, analysis — builds cover / reads deception | Command `clamp(round((2·Cha+Cog)/3),1,7)` (`params/mass_combat.md:139`); Argue pool Expert/Judge `Cog×2+Hist` (`params/contest.md:19`); Fieldwork Investigation primary (`params/core.md:244`); Concealment/Cover pools (`fieldwork_v30.md:159,198`); combat `reading()` (`combat_engine_v1/systems.py:100`) | **Contested name.** Fold-target "Acuity" has 0 consumers; ED-899 ratifies "Cognition" live |
| **Spirit** *(registry: "Will")* | Internal coherence, resolve, Thread capacity (unrelated to Certainty, `params/core.md:214`) | Thread Pool `Spirit×2+Hist+TPS` (`params/threadwork.md:20`); Stamina `3·End+2·Spirit` (`params/core.md:159`); Concentration `3·Foc+2·Spirit` (`params/contest.md:140`; `config.py:61`); Thread Fatigue `Spirit×5`; Wound Interval `round(End+4+0.4·Spirit)` | **Contested name + category.** 0 live formulas use "Will"; core.md treats Spirit as its own Metaphysical group, registry folds it to mind |
| **Recall** | Knowledge/retention; sets per-History point cap | History cap (`params/core.md:151`); Fieldwork Research primary; Appraise pool `Attunement+Recall` (`params/contest.md:23`); +2D citation bonus in Argue | **Unregistered.** Absent from descriptor_registry AND names_index despite gating ratified pools |
| **Focus** | Concentration, discipline, precision | Thread ops/session (`Focus−1`, ED-694); Concentration `3·Foc+2·Spirit`; Focus defence `floor(Foc/2)×3` (`params/contest.md:139`) | **Registered cleanly.** But `glossary.md:52` mis-files its Thread-duration role as a separate "derived stat"; homonym "Cardinal Focus" (Church BG action slot) unrelated |
| **Bonds** | Relational *capacity* (not warmth) | Knot eligibility `Bonds≥5` + cap `floor(Bonds/2)+1` (`params/core.md:147`); Knot Pool `(Bonds×2)+3` (one of 4 variants); Stance Triangle thresholds; contest Corroborate bonus | Registered; role settled; but see §2.5 (Knot Pool) and the Bonds/`bucket:track` crosswalk gap |
| **Charisma** *(alias: "Influence")* | Social force, rhetorical gravity, Debate base | Composure `Cha×3`; Face_max `Cha×3`; Command primary (weight 2); Argue Crowd type; Appraise Ob `opp Cha/2` | **Alias collides.** `fac.influence` is an unrelated faction stat; *every* live "Influence" formula means the faction stat — the Charisma alias is vestigial |

*Aggregates* `agg.body/mind/social` are registry placeholders with **zero live consumers** anywhere —
confirmed orphaned; the legacy "Stat×3" derived multipliers (e.g. Composure) remain the live mechanism.

### §2.2 · Clocks & tracks (strategic layer)

| Quantity | Concept | Scale / mode | Key thresholds & consumers | Coherence |
|---|---|---|---|---|
| **Piety Track (PT)** *(also CT/CV)* | A territory's *felt spiritual identity*: 0 = Einhir Restoration, 5 = Solmund Orthodoxy. NOT institutional control (that's Accord) | Per-territory (BG/Hybrid) | Church Seizure Ob `10−PT−infra` (`ci_seizure.md:31`); Consecrated status; RM-emergence (≥3 territories PT≤1); feeds CI generation | **4–6-way name tangle.** PT/CT/CV + a per-character Scar mechanic + a glossary mis-citation; ED-644/1006/1009/919 all open. See OPT-AV-13 (§3.2) |
| **Church Influence (CI)** | The Church's institutional political credibility (modeled on the historical Papacy) | Global 0–100 (BG/Hybrid) | Ladder 40/55/65/80/100 (`ci_political_v30.md:81-97`); Church vote `Mandate+⌊CI/20⌋`; opposition `−⌊CI/30⌋`; Mass Seizure at CI≥60 | Ladder solid; **TTRPG start value unstated** (BG=28 solid; TTRPG=15 cites a nonexistent file). See OPT-AV-11 (§3.6) |
| **Theocracy Counter (TC)** | CI's *former name* (renamed ED-756, mis-cited as ED-782) | — | (mechanically = CI) | **Incompletely retired.** Still a live writable clock in `module_contracts.yaml:256` beside CI; infill doc never renamed. See OPT-AV-7/§4 |
| **Institutional/Invasion Pressure (IP)** | External geopolitical pressure from Altonia (invasion countdown). Driven by *failure to consolidate* (Accord≤1 territories), not conquest — Pax Romana logic | Global 0–100 (BG/Hybrid) | IP≥75 Vanguard; IP≥100 invasion; 3-phase Occupation gates (`module_contracts.yaml:523`) | **Name split ×3** (Invasion / Institutional / Imperial), no cross-ref |
| **Mending Stability (MS)** *(formerly RS)* | Cosmological substrate integrity of the Thread-lattice — how intact reality itself is post-Calamity | Global 0–100, **all modes** (TTRPG 60 / BG 72) | Bands Stable→Critical→0; Second Calamity terminal at MS≤5 sustained; Calamity Drift erodes PT at MS 50/35/20; band hysteresis +8 (ecological regime-shift model) | **Genuinely mode-split by design** — but `campaign_modes.md:45` teaches the BG value (72) under the TTRPG label. Propagation bug, not a fork. See OPT-AV-7/§4 |

All five cite `clock_registry_v30.md` (self-declared CANONICAL "single source of truth for all clocks")
as authority via `module_contracts.yaml` — yet that file is **absent from `CURRENT.md`** and carries a
self-contradicted stale value (Torben Loyalty) on its own page. See OPT-AV-18 residuals / §4.

### §2.3 · Faction & settlement quantities

The strategic layer's stat stack, three scales: **faction-wide** (5 playable factions), **province/
territory** (17 T-nodes), **settlement** (35–37 nodes — the count itself is inconsistent across docs).

| Quantity | Concept | Scale | Formula / consumers | Coherence |
|---|---|---|---|---|
| **Mandate** | A faction's aggregate legitimacy-to-govern, size-weighted (CK3-Development analogue) | Faction | `clamp(round(7T/(T+6)),0,7)`, `T=Σ W_s·(q_s/7)`, `q_s=0.5L_s+0.5PS_s` (`settlement_layer_v30.md:165`); feeds Parliament votes, Excommunication, victory, `Legitimacy=Mandate×20` | **Dual-form.** `factions_personal.md:14` carries a stale LINEAR form; ED-784 already blessed it as a "personal view" — so a *marking* fix, not a fork. See OPT-AV-10 (§3.5) |
| **Legitimacy / Popular Support (L/PS)** | Slow institutional acceptance / fast populace mood | Settlement (0–7 each) | Feed Mandate; Public Expectation strictness; Excommunication side-effects | Registered; LPS-2e settled the re-graining to settlement scale |
| **Fort Level** | Fortification hardness (Fort 3 ≈ 70% defender win at even Military) | **Province** (0–4, 17 nodes) | Siege Ob `2+Fort`; battle defender bonus; Garrison Strength term | **Unregistered + scale-mismatch.** Consumed by a *settlement*-scale formula with no province→settlement inheritance rule. See OPT-AV-18 (§3.7) |
| **Garrison Strength** | Settlement military defensibility (single legible number) | Settlement | `Defense×20 + Fort Level×30` (`settlement_layer_v30.md:48`) | Home §9 stamps itself "PENDING/Not canonicalized" while contracts gate it live. See OPT-AV-18 (§3.7) |
| **Local Economy** | Settlement economic-output *display* figure | Settlement | `Prosperity×50` — but this is **not** the Treasury income formula (`Σ Prosperity×10`); the doc conflates them | Same PENDING-vs-live status gap |
| **Public Order** | Civil stability / riot risk | Settlement | `Order×20`; <0 triggers riots. Raw Order *also* feeds Accord `floor(mean Order)` | Same PENDING-vs-live status gap |
| **Discipline (faction)** | Internal organizational cohesion (infighting, succession) | Faction | `Stability×10` (`derived_stats_v30.md:301`); feeds Army Morale composite | **Name collides with unit Discipline** (below). See OPT-AV-18 (§3.7) |
| **Discipline (unit)** | A battlefield unit's cohesion under casualties | Unit / sub-unit | `min(general Command, Military-ceiling)`; 0 = Formation Broken; persists across battles | Different scale, different owning module; only touches faction Discipline at the Army Morale composite |
| **Political Pool** | A faction's per-motion parliamentary vote weight | Faction (per motion) | Church `Mandate+⌊CI/20⌋`; opponents `max(0,Mandate−⌊CI/30⌋)` | Name settled ("Political Pool" per prior art); the 8th uncatalogued pool. See OPT-AV-18 (§3.7) |
| **Intel** | Institutional intelligence capacity (Council-of-Ten analogue) | Faction (1–7) | Spy Ob `floor(Intel/2)+1`; counter-espionage at ≥4; strategic fog | Registered; but registry gives no explicit floor (blanket `1-7`) while source gives per-stat floors. See OPT-AV-18 (§3.7) |
| **Treasury** | Liquid spendable reserves (vs Wealth = structural ceiling) | Faction | `Wealth×100`; income `Σ Prosperity×10`; 0-for-a-season damages Wealth | Registry `not_descriptors` list omits it (and 7 other derived values). See OPT-AV-3/§5 |

### §2.4 · Reputation quantities (the "Standing" and "Renown" families)

| Quantity | Concept | Scale | Formula / consumers | Coherence |
|---|---|---|---|---|
| **Renown** | Cross-faction personal fame/legend | Personal 0–10 | Sources: Convictions, Duties, Domain Echoes, Knots, battles; governance penalty table (`derived_stats_v30.md:409-420`); thresholds 3/5/7/9 (7+ = independent Domain Action pool `floor(Renown/2)`) | **Defined** (census "orphaned" verdict was wrong). Open question: capped at 10 or uncapped? Possible bleed-in from Shadow Renown's cap. See OPT-AV-18 (§3.7) |
| **Shadow Renown** | Covert/Riskbreaker mirror of Renown | Personal 0–10 (capped) | Assassination/sabotage/intel; spillover→Deniability Debt 1:1; exposure→−1 public Renown each | Distinct track; the likely source of the "10 cap" that muddies Renown |
| **Standing (contest kernel)** | Transient in-proceeding ethos built during one social contest | Personal 0–10, start 5 | `Face_current = round(Standing/10 × Face_max)` (`params/contest.md:144`); Readiness weighting | Coherent in its own kernel |
| **Face** | Social capital/composure at stake *this proceeding* (retired "Composure" re-homed) | Per-contest | `Face_max=Charisma×3`; Rattled threshold; Knot-buffer redirect; tiebreak | Coherent; Rattled-vs-strain wiring is an honest gap |
| **Standing (BG faction-political)** | Political capital with Crown/Parliament (banked, spent as tokens) | Faction | `+1 Standing` (Honour pledge, `parliament.md:68`); "Standing tokens against Crown" gate Deposition; "Bank Standing" (NPC default) | **Range collides with itself:** glossary 0–10 vs clock_registry 0–5 for the *same* construct. See OPT-AV-12 (§3.4) |

"Standing" denotes at minimum **three, arguably four** distinct quantities (contest-kernel 0–10;
player_agency per-faction 0–5; BG faction-political — itself 0–10 *or* 0–5 depending on file) with no
unifying cross-reference.

### §2.5 · The Knot relationship system

A **Knot** is a formed Thread-substrate relationship — an *ontologically real* bond (the two can
perceive each other at distance, remote-read Thread-state, and suffer relational contagion), crossing
from deep friendship into magically-bound intimacy. It cannot be walked away from — only strained,
ruptured, or deliberately dissolved.

- **Bonds** (attribute) gates it: `Bonds≥5` to form, `floor(Bonds/2)+1` simultaneous cap. Bonds 1–4
  characters can max Disposition but are locked out of Knots and six downstream systems.
- **Disposition** (−5..+5, per-NPC-per-PC, ED-912) is the everyday relationship dial. Must reach +5
  ("Bonded") to attempt a Knot; a Knot break snaps it to −3. Separate track from the Knot's own gauge.
- **Knot strain gauge** (−5..+5; Distant tier −2..+5, Close −5..+5) tracks durability under
  instrumental use. **Rupture** at +5 (bond torn; both take Composure damage). **Tempered** at −5
  (Close only) absorbs one rupture — a relationship that has proven itself.
- **Knot Pool** (formation roll) is the flagship divergence: **4 live, disagreeing formulas** —
  `(Bonds×2)+3` (summary table), `Spirit×2+History` (normative procedure §3.2), bare `Spirit×2`
  (fieldwork sibling), and the running code's `Spirit×2+History` minus the `+3`. See OPT-AV-9 (§3.3).

### §2.6 · Combat armor/damage constants (the RESIST family)

The personal-combat engine models armor at two distinct layers:

- **Damage layer** — how much force lands: `damage = impact × coupling × QUAL × DMG_SCALE`.
  - **RESIST** (`core.py:86`): material × mode resistance (cloth/mail/plate × percussion/shear/puncture),
    grounded against Alan Williams' armor metallurgy. `transmit = 1 − RESIST[mat][mode]`.
  - **GAP_EXPOSURE / GAP_PREC_REF**: the "gap game" — thrusts seek coverage gaps (visor, armpit) rather
    than punching plate; scaled by the weapon's derived `gap_precision`.
  - **QUAL / DELIVERY / COVERAGE_GAP**: roll-degree quality; head-shape delivery efficiency; bare-zone
    floor (COVERAGE_GAP is **dead today** — `coverage` never leaves its `'full'` default).
- **Control layer** — who controls the exchange *before* dice: the **ADEF** (armor-defeat) family
  feeds `net_sigma`. A pure cutting edge vs armor scores *negative* (a liability); blunt/point are
  positive defeaters; the per-tier threshold rises monotonically with armor (re-swept 2026-06-30, ED-1050).
- **Globals**: `DMG_SCALE=1.55` (even hit ≈ 1 Wound Interval); `DECISIVE_OB=3` (degree-band centers).

**This whole family is what drifted in the Godot port** — RESIST alone is stale in 4/12 cells, and
GAP_EXPOSURE was never ported at all. See OPT-AV-15 (§3.8).

---

## §3 · The decision surface — genuine forks (need Jordan)

Each fork below is a real design choice with no pre-existing ruling. Options are listed with the
audit's recommended default first where one exists, and the consequence of each path.

### §3.1 · OPT-AV-1 — Attribute roster ratification `[P1 · blocks queue-13, ED-IN-0008, Godot descriptor keys]`

**The choice:** which roster is canonical, and (sub-forks) which way the two contested names fold.

| Option | What it does | Consequence |
|---|---|---|
| **(a) Registry's 9 as written** | Keep Acuity/Will as primaries | Requires renaming Cognition→Acuity and Spirit→Will across *every* live formula, engine constant, and doc. Contradicts ratified ED-899. Highest churn, highest miss-risk |
| **(b) Registry's 9-structure + reverse the folds + add Recall (recommended)** | Cognition and Spirit stay primary; add `attr.mind.recall` as 10th key | Near-zero corpus churn (Acuity/Will have no consumers); agrees with ED-899; converges toward `params/core.md`'s 10-shape. Still must retire glossary's 7-table and reconcile the 2nd 10-table |
| **(c) Promote a 10-table wholesale** | Declare `params/core.md` or `canonical_registry.md` authoritative, supersede the registry approach | Resolves by replacement not reconciliation; more invasive to the registry's alias machinery |
| **(d) Defer** | — | Costs nothing today but remains the literal blocker on M3 Godot descriptor keys |

**Sub-forks (settle alongside):** Cognition-vs-Acuity (ED-899 already uses Cognition live);
Spirit-vs-Will (0 live "Will"); the "Influence" alias collision (drop it — Presence covers Charisma —
or scope-tag it). All three point the same direction as (b).

### §3.2 · OPT-AV-13 — Piety/Conviction family naming (PT/CT/CV) `[P1 · ED-644/1006/1009/919 open]`

**The choice:** one name for the family, or split into distinct registered quantities.

| Option | What it does | Consequence |
|---|---|---|
| **(a) Ratify PT** | Adopt the collision-database's own (never-propagated) ruling; strike CT/CV; file `track.*` key(s) | Overrides glossary's stated "CT preferred"; rewrites `module_contracts.yaml`'s live CV state-key; must also settle PT's residual collision with "Piety Territory" |
| **(b) Ratify CT** | Match glossary's preference | Overrides the collision-DB ruling and the machine contract layer |
| **(c) Split into N quantities** | Treat the ≥4 referents (territory Piety / character Scar / display abbrev / contest-track mis-citation) as distinct | Biggest task — authoring N registered quantities — but the honest fix if they really are different things |
| **(d) Defer** | — | The status quo through 4 prior EDs; machine contract keeps disagreeing with the "canonical" glossary |

**No cheap default** — both existing authorities (collision-DB, glossary) claim canonicity and
disagree. Whatever wins should settle the TC/CI coexistence in the same pass (same state block).

### §3.3 · OPT-AV-9 — Knot Pool formula `[P1 · feeds FI · ED-920 open]`

**The choice:** which of four live formulas is canonical.

| Option | What it does | Consequence |
|---|---|---|
| **(a) `Spirit×2 + History + 3` (recommended)** | Matches running code's shape; restores the `+3` idiom shared by Argue/Thread/Fieldwork pools; Bonds becomes pure eligibility-gate/cap | Fold into open ED-920 — but that **widens ED-920's current scope** (today only the fieldwork bare-Spirit variant); flag the widening explicitly |
| **(b) `(Bonds×2)+3`** | Thematically appealing (relationship attribute drives relationship pool) | Requires rewriting the actual running code, which doesn't implement this |
| **(c) Treat fieldwork-Knot and other-Knot as different mechanics** | — | Nothing in the corpus supports this today (unlike Coherence's *intentional* cross-scale reuse) |

**Regardless of winner:** the pool formula has **zero regression-test coverage** (tier-gauge tests
never assert it) — a test must be added, since untested silent drift caused the four-way split.

### §3.4 · OPT-AV-12 — Standing `[P1 (sharpened) · feeds SC + FA]`

Two problems, one of which is not deferrable:

| Sub-problem | Options | Consequence |
|---|---|---|
| **Cross-scale homonym** (contest-kernel 0–10 vs BG faction-political vs player_agency per-faction) | (a) rule intentional homonym like Coherence; (b) rename/split | No doc endorses this as intentional (unlike Coherence); recommend treating as accidental |
| **Within-scope range collision** (BG faction Standing: glossary 0–10 vs clock_registry 0–5) | Rule the range | **Live bug regardless of the homonym question** — a token gated at "Standing ≥ 7" behaves completely differently at cap 5 vs 10. Not deferrable |

Needs both SC and FA sign-off (touches both lanes' constructs).

### §3.5 · OPT-AV-10 — Mandate dual-form `[P1→marking · feeds FA]`

**Not actually an open fork** — ED-784 (closed 2026-05-02) already ruled the linear form is a
deliberate "personal_mandate_view" coexisting with the canonical saturating aggregate.

| Option | Consequence |
|---|---|
| **(a) Confirm ED-784, mark & fix citation (recommended)** | Essentially free — mark `factions_personal.md:14` as the personal view, fix its stale citation |
| **(b) Revisit ED-784, retire the dual view** | A real reversal with consequences for anywhere using the simple linear form for display |

Likely a wave-through.

### §3.6 · OPT-AV-11 — CI starting-value provenance `[P1 · feeds FA]`

Less contradictory than it first appeared: BG=28 is solid across 5 sources; the TTRPG value is
essentially *unstated* (one broken-citation guess of 15).

| Option | Consequence |
|---|---|
| **(a) Adopt the MS-style TTRPG/BG split (recommended)** | Either author a real cited TTRPG start, or declare CI BG/Hybrid-only |
| **(b) Keep 15, fix the citation** | Asserts a never-validated number by fiat |
| **(c) Standardize 28 universally** | Contradicts the MS precedent |

The same table also mislabels MS's *BG* default (72) as the TTRPG value — that half is pure
propagation (see §4), fix regardless.

### §3.7 · OPT-AV-18 — Residual forks (six, one line each)

| Item | The choice | Recommended / note |
|---|---|---|
| **Renown cap** | Capped at 10 or uncapped? | Likely uncapped + the "10 cap" is Shadow Renown bleeding in via citation error → pure correction. If genuinely capped, two docs never got the memo |
| **Fort Level inheritance** | How does province Fort Level (17 nodes) reach the settlement Garrison formula (37 nodes)? | (a) 1:1 inheritance (cheapest, one sentence — but every settlement in a province gets identical Garrison); (b) re-grain to per-settlement (LPS-2e-style, real work); (c) redefine Garrison to read a settlement-scoped stat (shifts tuned numbers) |
| **Garrison/Local-Economy/Public-Order ratify-vs-mark** | Promote to CANONICAL or mark `[ASSUMPTION]`? | **The audit's "promote" default goes past bookkeeping** — the doc hedges these as pending *balance* design; treating it as pure hygiene would quietly settle an SE-lane design question. Needs SE sign-off |
| **Discipline rename** | Which of the two Disciplines renames? | (a) rename the faction meter to "Faction Discipline" (display-only, smaller footprint — recommended); (b) rename the unit stat (touches §A.2-A.13 + 4 EDs); (c) cross-ref only |
| **Political Pool name** | "Political Pool" vs "Parliamentary Vote Tally" vs rename Faction Domain Pool | (a) adopt "Political Pool" per existing prior art (least new debt) |
| **Intel floor** | Floor 0, floor 1, or leave blanket | **The one item with no existing ruling anywhere** — authoring new canon, not reconciling. (a) floor 0 matching the other non-Influence stats |

### §3.8 · OPT-AV-15 — RESIST re-export `[P1 · feeds PC/GO]`

**Not a substance fork** — the oracle's values are unambiguously ratified; the port is just stale
(4/12 RESIST cells; GAP_EXPOSURE never ported).

| Option | Consequence |
|---|---|
| **(a) Re-export now** | Mechanical; the outstanding half of the ED-1050 "fix canon, re-export" discipline |
| **(b) Fold into the exporter-widening (OPT-AV-17)** | Bundle with the `core.py`-constants scope-fence decision |

Only the *timing* is a decision. Lower urgency while Godot is Gate-0-deferred, but whoever next
touches the combat slice debugs against silently wrong armor values until fixed.

### §3.9 · OPT-AV-8 — Shaping-wave sequencing `[no severity · Jordan sequencing call]`

Where "Quantity/descriptor unification wave (IN)" slots against armature waves 1–5.

| Option | Consequence |
|---|---|
| **(a) Accept proposed** (after wave 1, before params-transcribing waves) | Single unit; A17/A18 get transport traffic to check |
| **(b) Split (recommended on inspection)** | The hygiene batch + most registry deltas have *no* wave-1 dependency and can land immediately; only A17/A18 measurement needs wave-1 traffic |
| **(c) Push to end** | Treats quantity coherence as strictly lowest priority |

---

## §4 · Execution-ready work (rulings already made — pure propagation, no fork)

These need only a go-ahead; each cites the ruling it propagates. This is **OPT-AV-7** (the hygiene
batch) plus the non-fork halves of other items. ~20 items:

- **Combat Pool**: strike the stale PP-247 header comment (`params/core.md:4`); the live table (`:161`),
  `module_contracts.yaml:810`, and `combat_config.gd` already agree on `max(5, History+6)`.
- **Health / Stamina**: regenerate `params/core.md`'s Derived Scores rows from the ratified
  `derived_stats_v30.md §4.1/4.2` (ED-1021); strip formulas from `glossary.md`'s tables (two
  supersessions behind).
- **Focus**: mark `params/core.md:152`'s pre-ED-694 Contact-Rounds rule as superseded (line 162 already
  states the replacement).
- **TC/CI**: strike the "TC (Theocracy Counter)" row from `module_contracts.yaml:256`; sync the un-renamed
  `conviction_track_v30_infill.md` §3 headers; correct the garbled ED-782→ED-756 citation.
- **MS**: fix `campaign_modes.md:45`'s MS=72-mislabeled-as-TTRPG (correct is 60 per `params/core.md:101`
  and the OWN-1/2 videogame resolution); fix its 3 broken source-filename citations.
- **Mass Combat Pool**: add the ED-899/ED-1013 caveat to `derived_stats_v30.md:589` (the one uncaveated
  carrier); populate the empty `mass_battle` `state:` block with the live formula.
- **Thread/Mending**: strike the pre-PP-616/625 "Attunement+Focus" Mending pool at `threadwork_v30.md:968,1008`.
- **Broken indexes**: `params/board_game.md` and `params/factions.md` link to nonexistent
  `references/params_bg_*.md` / `params_factions_*.md` — repoint to the real `params/bg/*` and
  `params/factions/*` content.
- **Dead registry test**: `tests/registry/test_descriptor_registry.py` (broken import + zero pytest
  collection) — revive or replace (pairs with the tier-promotion in §5).
- **clock_registry_v30.md**: add to `CURRENT.md`; fix the stale Torben Loyalty row (PP-498→PP-599).
- **Public Support residual**: fix the mislocated `name_collision_database.yaml:469` citation; add the
  real live residual at `mechanical_terms_index.md:196,1167`.
- **Accord phrasing**: add "writes to settlement Order, not Accord directly" to `scale_transitions_v30 §5.5`.

Lane-owned propagation (co-sign the owning lane): Mandate marking (FA), the MS/CI TTRPG-value halves (FA).

---

## §5 · Tooling & enforcement builds (the durable fix)

The proposed quantity armature extension (`proposed_quantity_armature_extension.md`) specifies these;
they are what stops the corpus from re-diverging after §4 cleans it up:

- **OPT-AV-3 — descriptor_registry extension** (16 deltas): register `Recall`, `Coherence` (per ED-830,
  a resolved-but-unpropagated ruling), Thread Sensitivity/TPS, Fort Level (new territory kind), the 8
  missing `not_descriptors` derived values, Face, Political Pool, WR, plus schema additions (alias
  scope-tags, a `formula_pointer` field, per-entry faction-stat floors, a `bucket:`↔KIND crosswalk).
- **OPT-AV-4 — A17 (stat-vocabulary closure)**: every stat named in a Key payload / contract state /
  params table / export resolves to one registry key. Deterministic. Seeded backlog ~34/88 (39%);
  ~23/34 (68%) of contract declarations. **Report-only first; flip to blocking only after OPT-AV-1
  ratifies the roster.**
- **OPT-AV-5 — A18 (formula single-source) + prose-drift detector**: exactly one defining surface per
  formula; the (unbuilt) detector parses `params/*.md` markdown tables + inline formulas, normalizes
  unicode, and diffs against the defining surface. This is the missing tool CLAUDE.md §5 names and the
  concrete next slice of ED-1052. Seeded backlog ~25–27/88 (28–31%). Sequence **after** A17.
- **OPT-AV-16 — `stat_deltas` vocabulary hook**: the Key substrate's `KeyLog._validate` checks
  `impact_vector` axis names but *nothing* on `stat_deltas` keys (any string rides in). Add a warn-tier
  check mirroring the axis check (candidate invariant 9 in `key_substrate_v30.md §2.3`).
- **OPT-AV-6 — warn→block tier promotion** + revive the dead registry test — **only** at zero A17
  backlog on the ratified roster.
- **OPT-AV-14 — secondary-index disposition**: 13 unconsumed registries/indices (values_master + 6
  sampled + 7 more with zero tool consumers). Mark historical snapshots (values_master precedent) or
  re-platform the few wanted as live A17/A18 signal.
- **A17a/b/c companion micro-checks**: export-fence (every Godot constant round-trips or is annotated —
  closes the RESIST-drift class), dead-export lint (7/181 dead CFG keys), registry-liveness header.

---

## §6 · Recommended reading path for ruling the docket

1. **Rule OPT-AV-1 first** — it is the keystone. It unblocks A17 blocking-mode, the tier promotion, and
   the Godot descriptor keys, and it settles the Cognition/Spirit/Influence naming that half the other
   items reference. Recommended: option (b) (9-structure, reverse the folds, add Recall).
2. **Batch the propagation (§4 / OPT-AV-7)** — no design content; a single `[cleanup]`-style pass, each
   edit citing its ruling. Can land before or independent of everything else.
3. **Rule the lane-owned forks** where you're ready — Knot Pool (FI), Standing range (SC+FA, the
   non-deferrable bug), CI/MS values (FA). Mandate (OPT-AV-10) and RESIST (OPT-AV-15) are wave-throughs.
4. **Approve the tooling (§5)** on the report-only→flip lifecycle; sequence the unification wave per
   OPT-AV-8 (recommended split: hygiene + registry now, A17/A18 after wave 1).
5. **The Piety-family fork (OPT-AV-13)** is the one with no cheap default — leave time for it, or
   explicitly defer it as ED-644 already has (a defer *is* a ruling, recorded, per the armature §5.8/5.9
   precedent).

Once ruled, the execution path is already drafted: `proposed_quantity_armature_extension.md §4` (Wave Q)
sequences the worklist, and this document + `ed_options.md` are the input to that wave.
