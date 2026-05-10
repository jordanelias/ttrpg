# R4 — Hero Participation Default in Mass Battle
## Module 4 of combat_arch_residual_stress_01

**Date:** 2026-05-09
**Mode:** A (single-mechanic isolation) + B (interaction chains)
**Source question:** `tests/stress/combat_videogame_arch_2026-05-01/06_synthesis.md §4 R4`
**Question text:** *"When the player character is in a mass battle, is hero participation default-on (player plays scene-scale by default, can opt out to commander view) or default-off (battle is mass-only, player opts in via Zoom-In phase-lock)? Decision affects pacing, agency, and the §B.5 phase-lock protocol's role."*

**Decision shape:** default-on / default-off / context-sensitive

---

## 1. Verification ledger entries

| ID | sim_variable | value | canonical_source | section | quoted_text |
|---|---|---|---|---|---|
| R4-L01 | b5_phase_lock_three_points | Zoom In may only fire at three legal phase-lock points | designs/provincial/mass_battle_v30.md | §B.5 (R3-L06 cross-ref) | "Zoom In may only fire at one of three legal phase-lock points:\n- **After Phase 1** (orders placed, nothing resolved — cleanest entry)\n- **After Phase 3** (manoeuvre complete, pre-Engagement)\n- **After Phase 6 Step 1** (all damage applied, no ghost units)" |
| R4-L02 | player_absent_branch | Player not present → "Where Were You?" retrospective scene replaces aftermath | designs/provincial/mass_battle_v30.md | §D.1 (post-battle) | "**If the player was not present for the battle:** The aftermath scene is replaced by a \"Where Were You?\" retrospective scene per scale_transitions_v30 §4.4. The player learns about the battle's outcome through their social network. The three aftermath choices are not available — the moment has passed." |
| R4-L03 | named_officer_disposition_command_quality | Officer Disposition shifts based on player tactical command quality | designs/provincial/mass_battle_v30.md | §D.2 | "- Player issues a tactically sound command (Battle turn where player's choice contributes to victory): +1\n- Player orders a retreat or sacrifice that saves the unit: +1\n- Player orders the unit into a situation that costs Size ≥ 2: −1" |
| R4-L04 | player_morale_effect_presence | Player physical presence in territory: +1 Discipline to friendly units | designs/provincial/mass_battle_v30.md | §D.3 | "Units in the player's current territory gain +1 Discipline while the player is physically present during battle." |
| R4-L05 | player_wound_morale_shock | Player wounded ≥2 or incapacitated during battle: −1 Discipline morale shock | designs/provincial/mass_battle_v30.md | §D.3 | "If the player is wounded (2+ wounds) or incapacitated during the battle, all friendly units in the battle take −1 Discipline immediately (morale shock)." |
| R4-L06 | player_combat_pause_command_independent | Personal combat pause: Command suspension and Discipline bonus independent | designs/provincial/mass_battle_v30.md | §D.3 | "This bonus applies whenever the player is in the territory, including during a personal combat pause (the player is still present; Command suspension and Discipline bonus are independent effects)." |
| R4-L07 | bg_no_pc_branch | Player Character not in battle: BG resolution fires | designs/provincial/mass_battle_v30.md | §B.5 | "**No Player Character in battle:** BG resolution fires." |
| R4-L08 | scale_transitions_handoff_rules | Scene → Mass and Mass → Personal handoffs canonical (eight-rule set) | designs/architecture/scale_transitions_v30.md | §3 | "## §3 Eight Handoff Rules" |

---

## 2. Three-tier presence/engagement model (post-canon-survey)

The §B.5 + §D.1 + §D.2 + §D.3 stack already defines a layered model. Re-stating in R4 framing:

| Tier | Player state | Mechanical mode | Canonical handle |
|---|---|---|---|
| 0 | Not present | BG abstract resolution; "Where Were You?" retrospective scene | R4-L02, R4-L07 |
| 1 | Present, strategic view (commander) | Player issues tactical commands; named-officer Disposition tracks command quality; +1 Discipline morale aura | R4-L03, R4-L04 |
| 2 | Present, scene scale (Zoom In active) | Player engages individual combat at scene scale; Stamina-banking, Wounds, Threadwork all live; player wound → friendly Discipline shock | R4-L05, R4-L06 |

**The R4 question is: which tier (1 or 2) is the player's default upon battle initiation?** Tier 0 is opt-out (commit to absence); the question is opt-in within presence.

Per R4-L01 (§B.5 phase-lock protocol), Zoom In is a *triggered event* requiring one of three legal phase-lock points. **The structural framing implies Tier 1 is default; Tier 2 is the triggered exception.**

---

## 3. Candidates

| ID | Name | Description |
|---|---|---|
| **C4.1** | Default-on (Tier 2 baseline) | Player plays scene-scale by default upon battle entry; Tier 1 (commander view) is opt-out via UI. |
| **C4.2** | Default-off (Tier 1 baseline) | Player commands strategically by default; Tier 2 (scene scale) opt-in via §B.5 phase-lock Zoom In. |
| **C4.3** | Context-sensitive | Default tier depends on (a) battle stakes — T-Boss / T-Cultural / T-Honor-call triggers force Tier 2; (b) hero stat relevance — high-Combat-Pool heroes default Tier 2, low-Combat-Pool heroes default Tier 1; (c) phase progression — Tier 2 unlocks only at phases 1, 3, 6.1 per §B.5. |

---

## 4. NERS at full grain — 24 cells per candidate

### C4.1 — Default-on (Tier 2 baseline)

| Direction | N | E | R | S | Notes |
|---|---|---|---|---|---|
| Top-down | ⚠ | ✗ | ⚠ | ✗ | **E ✗:** every battle = full scene combat overhead. Pacing drag. **S ✗:** contradicts §B.5 phase-lock protocol (R4-L01) which structurally treats Zoom In as a triggered event, not the baseline state. |
| Bottom-up | ⚠ | ✗ | ⚠ | ✗ | Combat Pool, Stamina, Wounds, Threadwork all engaged every battle. Personal-scale resolution math runs on every battle even when stakes are low. |
| Vertical | ✓ | ⚠ | ⚠ | ⚠ | Scale traversal happens every battle by default — strains the cleanly-bounded handoff rules in scale_transitions_v30 §3 (R4-L08). |
| Diagonal | ⚠ | ✗ | ⚠ | ⚠ | Threadwork operations during battle (§A.10) become routine rather than exceptional. Wound penalty (PP-716 −1D Pool) compounds across all battles regardless of stakes. |
| Lateral | ✓ | ✗ | ⚠ | ⚠ | Stamina depletion, Composure, Concentration all engaged every battle. Resource attrition across-battles per-session is much higher under default-Tier-2. |
| Horizontal | ✓ | ⚠ | ✗ | ⚠ | **R ✗:** all battles "feel the same" — every one is full scene combat. Eliminates the strategic-layer mode the architecture explicitly preserves. |

**Verdict C4.1:** N=⚠ on 3, E=✗ on 4, R=✗ on 1 + ⚠ on 4, S=✗ on 2 + ⚠ on 3. **REJECT — categorical S-fail (contradicts canon §B.5 phase-lock protocol) + E-fail (overhead per battle).**

### C4.2 — Default-off (Tier 1 baseline) — canon-aligned

| Direction | N | E | R | S | Notes |
|---|---|---|---|---|---|
| Top-down | ✓ | ✓ | ✓ | ✓ | Aligns with §B.5 framing (R4-L01): Zoom In is triggered, not default. Player commands strategically by default; Zoom In is the meaningful exception. |
| Bottom-up | ✓ | ✓ | ✓ | ✓ | Personal-scale resolution math engaged only when player opts in. Combat Pool / Stamina / Wounds engaged on Tier 2 episodes only. |
| Vertical | ✓ | ✓ | ✓ | ✓ | Scale traversal at phase-lock points (R4-L01) is the structural feature; default-off uses it correctly. |
| Diagonal | ✓ | ✓ | ✓ | ✓ | Threadwork in battle remains exceptional. Wound accumulation bounded to Tier-2 engagements. |
| Lateral | ✓ | ✓ | ✓ | ✓ | Resource attrition limited to opt-in moments — preserves campaign sustainability. |
| Horizontal | ✓ | ✓ | ✓ | ⚠ | ⚠ on the videogame-genre expectation: some players may expect Sekiro-class scene-scale combat as primary mode. The opt-in framing requires UI clarity. Otherwise: full alignment. |

**Verdict C4.2:** 23/24 ✓, 1 ⚠ on Horizontal (UI/expectation gap). **PASS — canon-aligned.**

### C4.3 — Context-sensitive

| Direction | N | E | R | S | Notes |
|---|---|---|---|---|---|
| Top-down | ⚠ | ⚠ | ✓ | ⚠ | Decision rules need spec: (a) which T-triggers force Tier 2, (b) what stat threshold makes hero "high-Combat-Pool," (c) interaction with §B.5 phase-lock points. ⚠ N: undefined criteria. |
| Bottom-up | ⚠ | ⚠ | ✓ | ✓ | Threshold spec needed but mechanically integrable. |
| Vertical | ✓ | ⚠ | ✓ | ✓ | Tier-2 unlock at phase-lock points (R4-L01) compatible. |
| Diagonal | ✓ | ⚠ | ✓ | ⚠ | T-trigger interaction with Conviction Wager (R5-pending) creates cross-system coupling — needs joint spec. |
| Lateral | ✓ | ⚠ | ✓ | ⚠ | Hero stat threshold for default-Tier-2 creates build-incentive: high-Combat-Pool builds default to scene combat (matches stat-relevant agency); low-Combat-Pool builds get strategic-only mode. |
| Horizontal | ✓ | ⚠ | ✓ | ✓ | Best-of-both: Sekiro-class scene moments at meaningful triggers + strategic agency at routine battles. |

**Verdict C4.3:** N=⚠ on 2, E=⚠ on 5, R=✓ on 6, S=⚠ on 3. **PASS with spec gaps** — needs trigger criteria explicitly enumerated.

### Cross-candidate summary

| Candidate | N pass | E pass | R pass | S pass | Verdict |
|---|---|---|---|---|---|
| C4.1 Default-on | 3/6 (3⚠) | 0/6 (4✗ + 2⚠) | 1/6 (1✗ + 4⚠) | 0/6 (2✗ + 4⚠) | **REJECT — multi-axis fail; contradicts canon** |
| C4.2 Default-off | 6/6 | 6/6 | 6/6 | 5/6 (1⚠) | **PASS — canon-aligned** |
| C4.3 Context-sensitive | 4/6 (2⚠) | 1/6 (5⚠) | 6/6 | 4/6 (2⚠) | **PASS with spec gaps — refinement of C4.2** |

---

## 5. Mode B — Interaction chain analysis

### Chain 1: Battle initiation → tier selection → resolution mode

Under C4.1 (default-on): every battle starts at Tier 2. UI prompt asks "step back to Tier 1?" Player friction increases per battle; mass-resolution mode becomes vestigial.

Under C4.2 (default-off): every battle starts at Tier 1. Player commands; named officers respond (R4-L03); morale aura active (R4-L04). Zoom In opportunity surfaces at phase-lock points (R4-L01); player chooses to engage at Tier 2 only when meaningful.

Under C4.3: at battle initiation, system evaluates triggers (T-Boss / T-Cultural / T-Honor-call from R2/Q5); if any fire → Tier 2 default; else Tier 1 default. Hero stat threshold checked for "default Tier 2 even without trigger." Mid-battle, triggers can flip the default at the next phase-lock point.

### Chain 2: Player wound during battle → friendly Discipline shock (R4-L05)

R4-L05 specifies player wound ≥2 = −1 Discipline to friendlies. This requires player to be at a tier where wounds can occur. Under C4.1, this fires routinely (every Tier-2 battle = wound-exposure). Under C4.2, this fires only on opt-in Zoom In sessions. The morale-shock mechanic gains weight under C4.2 (rare, dramatic) and degrades under C4.1 (routine, expected).

### Chain 3: Named officer Disposition shifts (R4-L03) → cross-campaign relationship

Officer Disposition tracks player command quality (R4-L03). The "tactically sound command" criterion presumes the player IS commanding — i.e., at Tier 1. Under C4.1 default-Tier-2, the player is fighting individually most of the time; commands are issued only as opt-out exceptions; named officer Disposition has fewer shift events. Under C4.2, the relationship channel runs continuously through default battle play. C4.2 better integrates §D.2's officer-Disposition mechanic.

### Chain 4: Personal combat pause (R4-L06) → Command suspension + Discipline aura

R4-L06 specifies that personal combat pause has independent effects on Command (suspended) and Discipline (still active because player is present). This canon explicitly anticipates that scene-scale combat is an *interruption* of strategic play, not the baseline. Strong evidence for C4.2.

### Chain 5: BG no-PC branch (R4-L07) vs Tier 0 absent branch (R4-L02)

R4-L07 ("BG resolution fires" when no PC) and R4-L02 ("Where Were You" retrospective when player absent) are structurally distinct. R4-L07 implies that *with* a PC, BG resolution does NOT fire by default — full Part A unit-scale resolution does, with the player commanding (Tier 1). Under C4.1, this distinction collapses (PC always at Tier 2 = scene scale, never at unit-scale-and-commanding). Under C4.2, the distinction is preserved.

---

## 6. Mode D — Edge cases (compressed)

### Boundary
**EC-D4.B-01 [P3] (C4.1):** What does "step back to Tier 1" cost mid-engagement? If free, players spam toggle; if costly, players locked into wrong tier per moment. UX trap.

**EC-D4.B-02 [P2] (C4.3):** "T-trigger forcing Tier 2" must be deterministic — can the player refuse? If yes, C4.3 becomes C4.2 with prompts; if no, C4.3 becomes C4.1 conditional on trigger.

### Cascade
**EC-D4.C-01 [P3] (C4.1):** Wound accumulation across all battles → high carry-load; PP-716 MW cap (max 4 wounds) reached early-campaign → players felled in routine engagements they should have command-resolved. Cascades into combat avoidance / unfun.

### Regression
**EC-D4.R-01 [P3] (C4.1):** The named-officer Disposition channel (R4-L03) runs only on commands. Default-Tier-2 → fewer commands issued → officers stay at neutral Disposition through campaign → R4-L03's relationship-tracking mechanic is starved.

### Crunch cascade
**EC-D4.CR-01 [P3] (C4.1):** Per-battle full Combat Pool / Stamina / Wound / Composure / Concentration tracking on routine battles. Tabletop play: 30 min per "routine" battle that should resolve in 5 min via Part B abstract.

### Ambiguity
**EC-D4.A-01 [P1] (C4.3):** Trigger criteria undefined. T-Boss, T-Cultural, T-Honor-call were proposed in Q5 but not formally specified. Without spec, C4.3 collapses to GM-judged.

### Incoherence
**EC-D4.I-01 [P1] (C4.1):** Direct contradiction with §B.5 phase-lock framing (R4-L01). Zoom In is structurally a triggered event; making it default inverts the canonical model.

### Optimal play
**EC-D4.O-01 [P3] (C4.1):** Player optimal: avoid engagement entirely (Tier 0 absent branch R4-L02) to skip overhead. Battles become offstage. Inverse of design intent.

**EC-D4.O-02 [P3] (C4.2):** Player optimal: opt in to Zoom In only at high-payoff phases (post-Phase-3, pre-Engagement, where commit can swing outcome). Aligns with intended exceptional use.

---

## 7. Decision-shape findings

**Recommendation: C4.2 (default-off, Tier 1 strategic baseline; Zoom In as opt-in via §B.5 phase-lock).**

**Secondary: C4.3 (context-sensitive) — adopt as a refinement of C4.2 only after the T-trigger criteria (T-Boss / T-Cultural / T-Honor-call from Q5) are formally specified. C4.3 alone has a P1 ambiguity (trigger criteria undefined).**

**Rationale:**

1. **C4.2 passes 23/24 NERS** with a single ⚠ on Horizontal (videogame-genre UX expectation). Aligns with §B.5 phase-lock framing (R4-L01), preserves the named-officer Disposition channel (R4-L03), and uses the personal-combat-pause + Command-suspension model (R4-L06) as canonically intended.

2. **C4.1 fails categorically** on S (contradicts §B.5 framing), E (overhead per battle), and the named-officer Disposition channel R4-L03 starves under default-Tier-2.

3. **C4.3 has rich appeal** but a central P1 ambiguity (EC-D4.A-01): trigger criteria are not specified anywhere in canon. Without spec, the candidate cannot be evaluated mechanically. Recommend: adopt C4.2 immediately; revisit C4.3 as a refinement after Q5 T-triggers are formalized in canon.

4. **§D.3 player morale + wound shock (R4-L04, R4-L05)** are designed for *exceptional* presence and *exceptional* wound exposure. Under C4.2 these are dramatic events; under C4.1 they become routine and lose dramatic weight.

**Implementation under C4.2 (no new code; documentation):**

- Affirm in mass_battle_v30 §D.0 (or §B.5 preamble) that the default state when player is present in a battle is Tier 1 (strategic / commander view).
- Tier 2 (scene scale) is opt-in via §B.5 phase-lock Zoom In, consistent with R4-L01.
- Named-officer Disposition channel (§D.2 / R4-L03) operates throughout Tier 1 default play.
- Personal combat pause (R4-L06) remains the established mechanic for entering scene scale during battle.

**Decision-shape statement for Jordan ratification:**

> When the player is present in a mass battle, the default tier is strategic / commander view (Tier 1). The player issues tactical commands; named-officer Disposition tracks command quality; the player's territorial presence grants +1 Discipline morale aura. Scene-scale combat (Tier 2) is opt-in via §B.5 phase-lock Zoom In at one of three legal entry points. Tier 0 (player absent) remains a separate branch with the "Where Were You" retrospective. Context-sensitive auto-Tier-2 (T-trigger forced engagement) is a refinement to revisit after T-trigger criteria from Q5 are formally specified in canon.

---

## 8. Module status

| Item | Status |
|---|---|
| Canonical sources fetched at full depth | ✓ |
| Verification ledger entries (8) | ✓ |
| NERS full-grain analysis (72 cells across 3 candidates) | ✓ |
| Mode B chains (5) | ✓ |
| Mode D edge cases | ✓ |
| Decision-shape finding (C4.2 primary; C4.3 deferred refinement) | ✓ |
| Three-tier presence model formalized for downstream R5–R10 | ✓ |

**Module 4 status: verified.**
