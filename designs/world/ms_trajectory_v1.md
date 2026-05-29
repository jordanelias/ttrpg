# VALORIA — Mending Stability Trajectory
## Status: CANONICAL (with two provisional elements flagged in §8)
## Date: 2026-04-20
## Scope: Trajectory of the peninsula-wide Mending Stability scalar from the Einhir Catastrophe (−12 AG) through game start (245 AG)
## Authority: This document is canonical for substrate-integrity values at specific historical dates. Supersedes MS values cited in prior session logs or audit drafts.
## Cross-references: `designs/world/calamity_radiation_v30.md` (radiation matrix; MS band → territory effect lookup), `designs/threadwork/threadwork_v30.md` §5 (MS system), `canon/03_canonical_timeline.md` (historical events), `canon/02_foundations_amendment_leap_mechanism.md` (operation-type taxonomy governing substrate cost), `canon/01_foundations_amendment_self_rendering.md` (Warden Coherence dynamics).

[EDITORIAL: Batch 3 ED-735-adjacent — resolved 2026-04-20. Source: session_master_2026_04_20.md Part III. D-1 (12-year emergence / 7-year ministry) adopted per ED-722. PR-3 (propagate MS over RS) adopted per ED-731. Two provisional elements remain (§8): colonial revolt specification; Himmelenger R-7 interpretation.]

---

## §1 Design Principle

MS measures global substrate integrity of the peninsula's thread-lattice. A single scalar (0–100) maps to radiation effects per territory via node distance from T15 (Askeheim); the territory-level lookup is specified in `designs/world/calamity_radiation_v30.md`. This document traces the scalar's trajectory across the ~257 years from Catastrophe (−12 AG) to game start (245 AG).

**P-07 compliance.** The substrate does not respond, heal, or repair. Ein Sof is constitutive continuous spooling of positive being (P-02). Damage is interruption to that spooling; "recovery" is the resumption of undisrupted spooling at the wound margin, not reactivity. The ground is not an agent. Prose characterising the trajectory uses *constitutive spooling resumes at the wound margin*, *substrate continuity re-establishes as disruption decays*, *damage is interruption; coherence is baseline*. It does not use *the substrate repairs itself*, *reality responds*, or *Ein Sof heals the wound*.

---

## §2 The Three Forces on MS

**Force 1 — Baseline continuity.** Always positive. Decelerating (logarithmic). Rate proportional to remaining disruption: fastest when damage is severe, slowest as MS approaches baseline. Sourced from Ein Sof's constitutive spooling at the wound margin. Alone, this returns MS to 100 only across millennia.

**Force 2 — Warden Mending.** Always positive. Variable over time (§3 below). Accelerates the continuity process to human-relevant timescales. Restorative operation aligned with substrate tendency — no inherent Coherence cost (`canon/02_foundations_amendment_leap_mechanism.md` Amendment 3; `designs/threadwork/threadwork_v30.md` §31 Mending Coherence Asymmetry). Warden Coherence erodes from environmental exposure at wound margins (proximity to Gaps, dissolution residue, third-mode presences), not from Mending operations themselves.

**Force 3 — Rendered-world disruption.** Always negative, always small, always recoverable. Wars, revolts, oppression, political violence. These cannot cause large MS drops — the substrate is affected only by substrate-level operations (manipulative or destructive threadwork through the Leap). Rendered-world events produce shallow, temporary notches.

**No post-Catastrophe substrate-level operations occur at scale.** The Einhir civilisation is destroyed; Wardens perform only restorative Mending; the Church suppresses threadwork. Solmund is the single post-Catastrophe restorative intervention at structural scale, and it is constructive rather than disruptive. The resulting trajectory is a strongly upward-trending curve with shallow rendered-world notches, not a sawtooth with deep valleys.

---

## §3 Warden Rate Is Not Constant

**Early Wardens (~0–50 AG).** Drawn from surviving Einhir practitioners. Existing training, existing Thread Sensitivity, pre-prophylaxis population. Maximum Warden capacity. Per-year Mending output is highest in this window.

**Mid-period Wardens (~50–200 AG).** Recruits from populations under Church prophylaxis. TS development requires confrontation despite institutional moral terror; recruitment difficulty increases as the prophylaxis matures. Warden numbers decline. Mid-period Mending output is moderate and declining.

**Late-period Wardens (200–245 AG).** Post-independence, but prophylaxis firmly established. Lowest Warden numbers in the trajectory. Institutional continuity is preserved (the order survives) but per-year Mending output is diminished.

Combined with Force 1's logarithmic decay, the overall curve is strongly front-loaded. Most of the 67-point climb from Catastrophe floor to game-start is completed within the first 50 years post-dissolution.

---

## §4 Anchor Points

| Date | MS | Event | Rate (MS/yr) | Drivers |
|---|---|---|---|---|
| ~−12 AG | **5** | Einhir Catastrophe. Foundational-scale manipulative operation inverts across the full Einhir site-network. Peninsula-wide disruption; T15 Rupture; Critical radiating outward. | — | — |
| −12 to −7 AG | 5 → 7 | Solmund coalescing rendering (no perceivable ministry yet). | ~0.4 | Baseline continuity only; Solmund not yet rendered as locatable being |
| −7 to 0 AG | 7 → 30 | Solmund's 7-year perceivable ministry (per D-1, ED-722). | ~3.3 avg, decelerating | Solmund dominant; max-rate continuity; early Einhir-survivor Wardens |
| 0 AG | **30** | Solmund dissolution in Altonia. | — | Restorative force removed |
| 0 to 50 AG | 30 → 50 | Early Warden period. | ~0.40 | Einhir-survivor Wardens + decelerating continuity |
| ~50 AG | 50 → 47 | Altonian conquest (D-4 proposes ~18 AG; current canon ~50 AG — see §8 gap). | dip −3 | Rendered-world disruption; small recoverable notch |
| 50 to 195 AG | 47 → 68 | Colonial period. | ~0.145 | Declining Warden numbers + slow continuity; 3–5 minor revolt dips across 145 years [PROVISIONAL: specific revolts unwritten — see §8] |
| 195–200 AG | 68 → 63 | Secession Wars (concentrated in north: T3, T14, T1, T2, T10). | dip −5 | Rendered-world disruption; small recoverable notch |
| 200–245 AG | 63 → **72** | Post-independence. | ~0.20 | Peace allows slight re-acceleration; minor notch from ~218 AG hunting-accident assassination + Schoenland tensions |
| 245 AG | **72** | Game start (canonical). | — | Strained band; only T15 and distance-1 territories mechanically affected |

**Contribution decomposition, total ΔMS from Catastrophe to game start = 67:**
- Solmund (coalescing 5y + perceivable ministry 7y): ~25 points (~37 % of total, anchor-forced)
- Wardens (cumulative ~245 years): ~26 points
- Baseline continuity (cumulative ~257 years): ~13 points
- Net rendered-world dips: ~−8 to −10 points (conquest, Secession Wars, colonial revolts)

Point totals sum within bounded uncertainty on the per-period rate assumptions, which are approximate in §2–§3.

---

## §5 Band Crossings and Territory Normalisation

As MS rises, territories at each node distance lose radiation effects progressively. Crossings define the cultural geography of post-Catastrophe history.

**Territory distance map (per canonical `calamity_radiation_v30.md`):**

- d0: T15 Askeheim
- d1: T6 Stillhelm, T13 Oastad
- d2: T5 Feldmark, T12 Sigurdshelm
- d3: T1 Valorsplatz, T14 Ehrenfeld, T4 Grauwald, T11 Halvardshelm
- d4: T2 Kronmark, T16 Schoenland, T9 Himmelenger, T7 Rendstad, T10 Spartfell
- d5: T3 Lowenskyst, T8 Gransol, T17 Halvarshelm

| MS Crossing | Band Change | Approximate Date | Territories Affected |
|---|---|---|---|
| 20 | Critical → Fractured | ~−7 AG | d4 territories (T2, T7, T9, T10, T16) exit Folklore effects |
| 40 | Fractured → Fragile | ~20–30 AG | d3 territories (T1, T4, T11, T14) normalise |
| 60 | Fragile → Strained | ~140–150 AG | d2 territories (T5, T12) exit Folklore → Normal |
| 80 | Strained → Stable | *not reached* | MS maxes at 72 at game start; d1 territories (T6, T13) remain at Folklore level; T15 never normalises within game timeframe |

### §5.1 Band Hysteresis and Leading Warning Signal — RATIFIED (ED-882, 2026-05-29)

**[RATIFIED 2026-05-29, ED-882 — Jordan-directed.** Tested candidate: `designs/audit/2026-05-28-resolution-diagnostic/sim_ms_hysteresis.py`. Validated against ecological regime-shift precedent (Scheffer, Holling; via `ners_historical_precedent_matrix.md` entry 1): real alternative-stable-state systems show **hysteresis** (the recovery threshold sits above the collapse threshold — the reverse path is not the forward path) and **leading warning signals** (critical slowing / rising variance) before a tip. The band crossings above were symmetric single thresholds — the one behavior real regime-shifts do not exhibit.]**

**Hysteresis (asymmetric band edges).** The MS thresholds in the table above are the **collapse (falling) edges** — MS dropping past 20 / 40 / 60 enters the worse band at those values (unchanged; the territory-normalisation crossings above are the falling direction and are canonical as written). **Recovery (rising) requires climbing past the edge + a hysteresis gap of +8 MS** to escape the worse band:

| Transition | Falling (collapse) edge | Rising (recovery) edge |
|---|---|---|
| Critical to/from Fractured | MS 20 | MS 28 |
| Fractured to/from Fragile | MS 40 | MS 48 |
| Fragile to/from Strained | MS 60 | MS 68 |

So a substrate that has fallen into Fractured does not return to Fragile at MS 40 — it must be restored to **MS 48** (over-correction past a different bifurcation point). This is path-dependent: the same MS value maps to a worse band when recovering than when collapsing. The gap (8) is bounded below the minimum band width (20), so no band can be skipped, and sufficient recovery always escapes (not a trap). Falling-direction lookups are unchanged — no regression to the §5 territory-effect crossings.

**Leading warning signal.** When MS is within **12** of a collapse edge *from above* (approaching a tip from the safer band), a diegetic early-warning trend activates — rising Shifting-Object frequency / variance (extends the canonical Fragile-band "spontaneous Shifting Objects" from a state into a *legible trend the player reads before the tip*). This is the critical-slowing analog; it improves Smoothness and Elegance (the player can intuit the approaching band change rather than being surprised by a step).

**Parameters** (ratified, tunable by future Jordan-logged ratification): hysteresis gap +8 MS; warning window 12 MS. **P-07 compliance:** this is a property of how the *rendered world's band effects* resolve, not a claim that the substrate heals (Ein Sof is constitutive; Force-1 recovery remains as specified). GD-1 unaffected (no victory interaction).

**Distance 5 (T3, T8, T17):** Never experienced Calamity effects at any MS band (canonical matrix: d5 = Normal in all bands). The far north.

---

## §6 Cultural Geography Produced

**d5 (T3, T8, T17) — the Far North.** ~250 years of continuous stability. Minimal Calamity folk memory. Normal life throughout.

**d4 (T2, T7, T9, T10, T16) — the Mid-North.** Normalised ~−7 AG. Himmelenger (T9) sits here: substrate clean for ~250 years, which the Church reads as Solmund's grace (R-7). Actual cause: node distance + Solmund's northward passage through the region during his ministry. Evidence real, explanation wrong. [PROVISIONAL: R-7 interpretation — see §8 gap 2.]

**d3 (T1, T4, T11, T14) — the Crown Heartland and Mid-South.** ~32–35 years of Fractured conditions (~−12 to ~22 AG). Normalised before Altonian conquest (whether ~18 AG per D-4 or ~50 AG per current canon; both pre-date full stabilisation marginally). Cultural formation for the Crown's governing institutions happens on post-Calamity-stabilised substrate with fresh Calamity memory but no ongoing effects.

**d2 (T5, T12) — the Near-South.** ~150 years of active instability (~−12 AG through the 60 crossing ~140 AG). Normalised mid-colonial. Deeper Calamity folk memory. Einhir cultural substrate preserved longer because substrate effects kept the memory alive under the prophylaxis.

**d1 (T6 Stillhelm, T13 Oastad) — the Borderlands.** Still at Folklore level at game start. The "uneasy" territories. Strongest surviving Einhir folk practice. ~257 years of continuous mild instability shape local institutions, mysticism, and Church suppression patterns.

**T15 (Askeheim) — the Southernmost.** Permanent wound. Wardens and Church containment. No normalisation possible within the game timeframe.

The Restoration Movement's territorial support follows the gradient of lived Calamity memory. The caste system's experiential basis — cultural blame against southern Einhir practitioners (timeline §Catastrophe stigma) — persists because their descendants live in d1–d2 territories where Calamity effects remain felt. The grievance is renewed by ongoing experience, not maintained by pure institutional memory.

---

## §7 Resolved Decision Points

The MS trajectory originally had five decision points gating its commit. Three are resolved as of 2026-04-20 session:

- **Solmund contribution (25 MS) — RESOLVED.** Anchor-forced by MS at Catastrophe = 5, MS at dissolution = 30, ministry duration per D-1. No free parameter.
- **Ministry duration — RESOLVED (D-1, ED-722).** 12-year Catastrophe-to-dissolution: 5-year coalescing + 7-year perceivable ministry. Table §4 reflects this.
- **Terminology (MS vs RS) — RESOLVED (ED-731).** Propagate MS. Sweep completed in commit 576e9fea across core canonical files. Per-file RS remnants may persist in non-canonical documents; follow-up sweep pending.

---

## §8 Provisional Elements

Two items remain provisional pending subsequent editorial:

**Gap 1 — Colonial revolt specification.** The 50–195 AG colonial period includes 3–5 minor revolt dips totalling approximately −8 to −12 MS distributed across 145 years. The specific revolts (names, dates, territories affected, magnitude of each dip) are not written. The aggregate shape of the trajectory is stable across plausible revolt specifications, but any scenario or NPC content referencing a specific colonial revolt should either use a flagged placeholder or contribute to the eventual specification. [PROVISIONAL: colonial revolt specification pending.]

**Gap 2 — Himmelenger R-7 interpretation.** §6 characterises Himmelenger's ~250-year substrate-clean status as distance-caused (d4 node distance from T15) plus Solmund's northward passage, with the Church's "material stability advantage" claim being a misattribution that reads the geographic effect as theological favour. The alternative framing — that the Altonian containment grant genuinely gifted the Church stability Himmelenger would not otherwise have had — is not adopted here but is not inconsistent with all other constraints. Jordan confirmation preferred. [PROVISIONAL: R-7 interpretation pending.]

**D-4 Altonian conquest timing.** The conquest's exact year (~18 AG per D-4 vs ~50 AG per current canon) produces a minor shift in the conquest-dip's position on the trajectory (earlier = lower starting MS at dip; later = higher MS at dip). Shape is robust to either choice; precise plotting will update when D-4 is integrated into the canonical timeline. [PROVISIONAL: dating propagation pending D-4 integration workplan.]

---

## §9 Cross-references

`designs/world/calamity_radiation_v30.md` (MS band → territory effect; radiation matrix) · `designs/threadwork/threadwork_v30.md` §5 (MS system, substrate integrity mechanic) · `canon/03_canonical_timeline.md` (historical events; game start = 245 AG) · `canon/02_foundations_amendment_leap_mechanism.md` Amendment 3 (operation-type taxonomy; restorative operations non-corrosive; substrate cost differential) · `canon/01_foundations_amendment_self_rendering.md` (Warden Coherence dynamics) · `canon/00_philosophical_foundations.md` §4.3 (Confrontation as Constitutive Finitude; confrontation does not damage; operation against substrate tendency does) · ED-722 (D-1 ministry duration) · ED-731 (PR-3 MS terminology).
