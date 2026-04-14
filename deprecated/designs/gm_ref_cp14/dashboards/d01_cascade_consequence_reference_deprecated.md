<!-- DEPRECATED -->
> **DEPRECATED — 2026-04-11**
> CP14 dashboard. Based on outdated CP14 mechanics. Do not use for table play.
> Do not use as a canonical source.

---

<!-- DERIVED FROM: Checkpoint 14 (compilation/valoria_ruleset_checkpoint_14.md, 2026-03-26) -->
<!-- SESSION: 2026-03-30 / 2026-03-31 — see session_log_archive.md -->
<!-- STATUS: Pre-release reference tool. Not valid against any post-CP14 ruleset. -->

# D-01 — CASCADE CONSEQUENCE REFERENCE
*Keep on Game Master screen every session. All rates per season unless marked.*

---

## THREAD TENSION (Thread Tension) — Starting: 28

| Thread Tension Band | State | Active Effects |
|---------|-------|----------------|
| 0–19 | Dormant | Leap fails automatically; no Thread operations possible |
| 20–39 | **Stirring** ← START | Leap available. No mechanical penalties. |
| 40–59 | Wakening | Shifting Objects spontaneously form (1 random/season). Thread ops nominal. |
| 60–79 | Fracturing | **All Thread ops: +1 Ob.** Gaps may open. |
| 80–99 | Rupturing | **All Thread ops: +2 Ob.** Entities establish territory. |
| 100 | The Rupture | Campaign event. |

**Thread Tension Cross-Clock Fires (check each accounting):**
- Thread Tension > 45 → Theocracy Counter +1/season AND Institutional Pressure +1/season
- Thread Tension > 60 → Theocracy Counter +2/season (total, replaces above) AND Institutional Pressure +2/season (total)
- Thread Tension > 60 + Theocracy Counter > 60 simultaneously → both at maximum acceleration

**Spontaneous Gaps by Thread Tension:**
- Thread Tension 40–59: 1d10/season; result 1–2 → Gap in lowest-Stability territory
- Thread Tension 60–79: 1d10/season; result 1–4 → Gap in lowest-Stability territory
- Thread Tension > 79: 1d10/season; result 1–6 → Gap in lowest-Stability territory

**Thread Tension Passive Drift:** +1 per full campaign year (4 seasons)

---

## THEOCRACY CLOCK (Theocracy Counter) — Starting: 22

| Theocracy Counter Band | State | Active Effects |
|---------|-------|----------------|
| 0–19 | Institutional Pressure | Lobbying only. No mechanical penalties. |
| 20–39 | **Consolidation** ← START | Church assumes civil domain authority. |
| 40–59 | The Ultimatum | Formal demand placed before Parliament. |
| 60–79 | Schism Politics | Excommunication threats; Templar movement political. |
| 80–99 | Theocratic Seizure | Church may attempt territorial seizure (roll vs Ob). |
| 100 | The Holy State | Campaign event. |

**Theocracy Counter Cross-Clock Fires:**
- Theocracy Counter > 40 + Institutional Pressure > 45 → Institutional Pressure +1/season additional (Church mediation cover)
- Theocracy Counter > 60 → Institutional Pressure +2/season (total; Secession Wars clause violation)
- Theocracy Counter > 60 + Institutional Pressure > 45 → Almaic Kyriakos begins formal documentation

**Theocracy Counter Passive Drift:** None. Theocracy Counter only changes from explicit triggers.

**Church Stability Brake:** When Church Stability ≤ 3, Theocracy Counter generation from Mandate pauses (Cardinals competing). Rendering Stability cross-clock unaffected.

---

## ALTONIAN PRESSURE (Institutional Pressure) — Starting: 20

| Institutional Pressure Band | State | Active Effects |
|---------|-------|----------------|
| 0–29 | **Dormant** ← START | Trade continues. Spies monitor. |
| 30–44 | Aggressive | Sanctions. Tutoring Demand triggers (Prince Torben). |
| 45–59 | Hostile | Border skirmishes. Vassalage demands. |
| 60–74 | Warlike | Invasion preparations. Factions pressured directly. |
| 75–99 | Invasion Imminent | Merchant Consortium collapses. |
| 100 | Invasion | Campaign event. |

**Institutional Pressure Direct Triggers:**
- Public Thread use (observed by Altonian agents) → +2/event
- Succession delayed past 2 arcs → +2
- Schoenland trade alliance → −2/year; removes MC political cover
- Grand Diplomatic Scene victory → Institutional Pressure frozen; peace treaty available
- Unified Valorian diplomatic front → Institutional Pressure passive drift halts 1 season

---

## FACTION STABILITY CHECKS (Thread Tension-driven)
*Only when Thread Tension > 79 (Critical band)*

Each faction: Stability check Ob 1 per season
- Fail → Mandate −1 (minimum 0)
- Mandate 0 fail → Faction Fracture (sub-faction splinters; Game Master event)

---

## ENDGAME TRIGGER
All three clocks above their midpoints simultaneously (Thread Tension > 50, Theocracy Counter > 50, Institutional Pressure > 50) → Campaign enters endgame phase.

---

## ACTIVE EFFECTS QUICK-CHECK (tick applicable boxes each session)
- [ ] Thread Tension > 45: Theocracy Counter/Institutional Pressure +1/season
- [ ] Thread Tension > 60: Theocracy Counter/Institutional Pressure +2/season (total); +1 Ob all Thread ops
- [ ] Thread Tension > 79: +2 Ob all ops; Stability checks Ob 1/season
- [ ] Theocracy Counter > 40: Institutional Pressure +1/season (if Institutional Pressure > 45)
- [ ] Theocracy Counter > 60: Institutional Pressure +2/season; Almaic Kyriakos active
- [ ] Theocracy Counter > 79: Territorial seizure available to Church
- [ ] Institutional Pressure > 30: Tutoring Demand active
- [ ] Institutional Pressure > 44: Hostile posture; vassalage demands
- [ ] Institutional Pressure > 74: MC collapses; invasion imminent
