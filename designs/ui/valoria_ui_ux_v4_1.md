# VALORIA — UI/UX Comprehensive Reference v4.1
## Godot-development-ready interface specification, canon-compliant

**Date:** 2026-04-16
**Supersedes:** valoria_ui_ux_v4.md (earlier today)
**Status:** CANONICAL — structural supplement to v4. v4 remains authoritative for content-level UI specification until incremental restatement completes. Spec-autonomy target: v4.2+ (see valoria_ui_ux_v4_2_workplan.md, F-69 Option B)
**Audit trail:** incorporates all critical findings from valoria_ui_ux_v4_audit.md + valoria_ui_ux_v4_audit_addendum.md (both 2026-04-16)
**Structural changes from v4:** 25 parts → 14 parts + 5 appendices; Layer 3 haptic-equivalent deleted; Thread UI progressively gated by TS; chrome visibility rules capability-gated; setting violations corrected (period music, non-anachronistic colors, hermetic Thread typography, pre-Gothic portrait era); canon gaps filled (monster encounter, Threadcut, memory pulling, Southernmost forgetting)
**Dependencies:** all 19 v30 canonical design documents + combat_v30 ED-548 Wound Interval patch
**Resolves in this revision:** UI-01 through UI-15 (from v4, confirmed); canon P-03/P-04/P-06/P-08/P-09/P-10/P-11/P-12/P-13/P-15 compliance gaps; Jordan's three corrections (C-1 cut Layer 3, C-2 TS gating, C-3 capability-gated chrome); setting anachronisms
**New editorial items:** none

---

# HOW THIS DOCUMENT WORKS

Read linearly as one argument, or non-linearly by section. §N.N cross-references use the format. Each Part:

1. **Authoritative sources** — v30 files the Part renders
2. **What the player sees** — surface description
3. **Why it is that way** — design argument grounded in canon and setting
4. **How it is built** — Godot-facing implementation

Appendices A–E are reference material, not linear reading. Part 14 (Resolved Items Index) is bookkeeping.

The document's central argument is that the interface should match the character's capability. A starting Operative-Stature non-sensitive character's chrome is minimal; an advanced practitioner-leader's chrome is dense. **The player earns their HUD.**

---

# TABLE OF CONTENTS

- **Part 0** — Three design oaths (with violation tests)
- **Part 1** — State machine, phases, scene action economics
- **Part 2** — Persistent chrome with visibility rules
- **Part 3** — Travel, zoom, the peninsula, settlements
- **Part 4** — Fieldwork (exploration, investigation, socialising)
- **Part 5** — Dialogue as Disco-Elysium Conviction interface
- **Part 6** — Social contest (Parliament, Tribunal, Royal Audience, Treaty)
- **Part 7** — Personal combat
- **Part 8** — Mass combat and settlement invasion
- **Part 9** — Threadwork (progressive unlock, felt radicality)
- **Part 10** — Encounter UI variations (monsters, Threadcut, memory, Southernmost)
- **Part 11** — Faction, settlement, character, party management
- **Part 12** — The integrated loop (walkthrough)
- **Part 13** — Cutscenes and feel layers
- **Part 14** — Resolved items index

Appendices:
- **A** — Accessibility, input, resolution scaling
- **B** — Precedent attribution
- **C** — Typography and visual specification
- **D** — Music and audio specification
- **E** — Godot implementation reference (scene tree, signals, resources, assets)

---

# PART 0 — THREE DESIGN OATHS WITH VIOLATION TESTS

**Oath I — The world is always present.** The peninsula, the clocks, the factions, the Scene Slate persist visually across all layers. Zoom in does not hide the world. No screen is modal except cutscenes and commit-confirmations for permanent decisions.

*Violation test:* Does the screen remove the breadcrumb and chrome when entering a non-cutscene, non-commit-confirmation scene? If yes → FAIL.

**Oath II — Transparency is not over-explanation.** Every number the player needs to plan with is visible. Every number they do not need is hidden but inspectable. Bands over raw values by default; numbers on hover. **Only surface UI elements the character can use.**

*Violation test 1:* Does the UI display a control for a capability the character does not currently have (e.g., a Thread sight toggle on a TS 0 character)? If yes → FAIL.
*Violation test 2:* Does a faction-specific display (Victory path, Hand Panel) appear for a character not aligned with that faction? If yes → FAIL.
*Violation test 3:* Does the UI reveal information the character's perception cannot render (e.g., Liminal-depth content to a non-sensitive character)? If yes → FAIL.

**Oath III — The game is felt, not narrated.** State changes are shown before they are labeled. Cutscenes carry weight that a notification cannot carry. The UI does not announce via text what the art, audio, and animation can communicate.

*Violation test:* Does the UI announce a state change via text before the state change is shown visually or audibly? If yes → FAIL.
*Violation test:* Does a major arc moment (death, coup, Rupture, first Leap, Convergence Marker firing) resolve via notification alone? If yes → FAIL — it requires a cutscene per §13.

---

# PART 1 — STATE MACHINE, PHASES, SCENE ACTION ECONOMICS

Authoritative sources: player_agency_v30 §4–6, board_game_v30 §9.1+§9.8, companion_specification_v30 §4.3.

## §1.1 Top-level states

14 states. Deterministic transitions, either player-initiated (P) or game-initiated (G). No ambiguous dwells.

```
[MAIN MENU] → [CHARACTER CREATION] → SEASON LOOP
                                       ├── Phase 0 Briefing (G auto)
                                       ├── Phase 1a Duty Assignment (G, Counselor+ may negotiate)
                                       ├── Phase 1b Slate Reveal (G auto)
                                       ├── Phase 1c Personal Phase (P-driven, scene action budget)
                                       │     ├── Scene modes: Fieldwork · Dialogue · Contest · Combat · Threadwork · Travel · Cutscene
                                       │     └── loops on scene resolve
                                       ├── Phase 2 Strategic (G+P) — faction board play
                                       ├── Phase 3 Cascade (G) — animated 5-step accounting
                                       └── Phase 4 Aftermath (G+P) — companion scene + Conviction revision
                                       │                                 → next Briefing OR Endgame
                                       ▼
                                   [ENDGAME]
```

Cutscenes are a state that preempts any phase. Queue rules in §1.4.

## §1.2 Phase timings and save boundaries

| Phase | Target duration | Save on enter | Skippable |
|-------|-----------------|----------------|-----------|
| 0 Briefing | 30–60s | yes | Partial (cutscene skip after first) |
| 1a Duty | 60–120s | no | Counselor+ after first season |
| 1b Slate Reveal | 10–15s | no | Yes |
| 1c Personal | 30–120 min | at scene resolution boundary | N/A |
| 2 Strategic | 60–180s | yes | N/A |
| 3 Cascade | 60–120s | no | Per-step dismiss after first (scroll persists) |
| 4 Aftermath | 60–180s | yes | Yes after first |

**Atomic scene rule:** no saves mid-resolution. Once a roll starts, reload goes to the most recent phase or scene boundary — never mid-roll.

## §1.3 Scene Action Cost Table

*Single source of truth for scene action economics. Replaces scattered cost rules in prior v4 §3.7, §5.7, §6.1.*

**Base budget per season (player_agency §6.1):**
- Narrative difficulty: 5 actions
- Normal: 4 actions
- Hard: 3 actions

**Modifiers:**
- Lieutenant Stature (Standing 4+): +1
- Knot with local NPC in active territory: +1 in that NPC's territory
- Out of Breath (Stamina 0): −1
- Wounded (2+ Wounds): −1

**Cost per action type:**

| Action | Cost | Notes |
|---|---|---|
| Enter a location and perform one fieldwork action | 1 | covers Examine/Research/Surveil/Read/Converse/etc. |
| Dialogue (single conversation) | 1 | any number of exchanges within one scene |
| Reconstruct (investigation synthesis) | 0 | free within a scene that already had fieldwork |
| Social Contest (1–3 exchanges) | 1 | |
| Grand Contest / Parliament / Tribunal (4–5 exchanges) | 2 | extended engagement |
| Combat (any length) | 1 | |
| Mass combat battle (full) | 2 | |
| Thread contact (one Leap, any operations within contact window) | 1 | Leap commits the round; operations within contact are included |
| Travel within settlement | 0 | |
| Travel within province | 0 | |
| Travel between provinces | 1 per province traversed | Altonian-adjacent always +1 surveillance risk |
| Governance (if governor) | 0 | mandatory seasonal action, automatic |
| Lobby (pre-Parliament) | 1 per target | |

**Chain rule:** a scene that contains multiple resolution modes (fieldwork → dialogue → contest in one go) costs the highest single cost, not the sum. A scene that contains combat always costs at least 1 regardless of what preceded.

The scene action counter in the top bar updates after each commit. It displays `X/Y` with amber at 1, red at 0.

## §1.4 Cutscene queue rules

Cutscenes queue during scene resolution and fire at the next phase boundary. Multiple cutscenes ordering:

1. Arc-critical (Rupture, Victory, Coup, Convergence Marker) — fire immediately regardless of phase
2. Death Cascade / Knot rupture / Conviction fulfillment — fire at end of current scene
3. First-occurrence mandatory (First Leap, First Domain Echo, band transitions) — fire at next phase boundary, in chronological order
4. Atmospheric (seasonal, §13.5) — fire at Phase 1b or Phase 4, deferred if higher-priority cutscene queued

**No nested cutscenes.** A cutscene cannot trigger another cutscene while playing. If state changes during a cutscene would queue a new cutscene, queue it for the cutscene's exit.

## §1.5 Pause behavior

- Personal Phase: pausable. Menu available.
- Strategic Phase: pausable. Board animations freeze.
- Cascade: NOT pausable. It is a viewing phase; the world closes its accounts.
- Cutscenes: pausable (menu); not fast-forwardable until fully watched once.

## §1.6 State data shape (Godot)

See Appendix E.

---

# PART 2 — PERSISTENT CHROME WITH VISIBILITY RULES

Authoritative sources: player_agency §5 (Stature), threadwork §1–2 (TS gates), companion_specification §2, canon P-03.

**This Part implements Oath II and Jordan's correction C-3. Chrome elements are capability-gated. The UI shows what the character can use, and nothing else.**

## §2.1 Visibility rules table

Every chrome element has a visibility condition. When the condition is false, the element does not appear at all — not greyed out, not collapsed, not there.

| Element | Visibility condition |
|---|---|
| Breadcrumb trail | Always visible |
| Season display | Always visible |
| Scene action counter | Always visible during Personal Phase |
| Main menu access | Always visible |
| **Global clocks** | |
| GEN (generation/year) | Always visible |
| RS bar in the current territory | Always visible |
| TC (Theocracy Clock) | Visible once the character has interacted with Church content (Stature 1+ anywhere, or having attended any Church scene) |
| IP (Invasion Pressure) | Visible once IP has reached ≥ 20, OR character is in a border territory, OR Altonian-related investigation is active |
| Three-clock summary panel (all visible clocks together) | Agent Stature+ (Standing 2+) OR Renown 3+ |
| **Framework Drift strip** | Agent Stature+ (sees faction intelligence per player_agency §5.1) |
| **Stature block (Standing pips + Renown + stature label)** | Always visible IF character is faction-aligned; Renown only if Independent |
| **Convictions block** | Always visible — Convictions are the player's authored stance per player_agency §2 |
| **Beliefs inspection (on character sheet only)** | Always visible via character sheet |
| **Obligations block** | Visible only when character has at least one active Obligation (otherwise absent) |
| **Duty card** | Visible only when character is faction-aligned with active Duty |
| **Faction Hand Panel** | Counselor Stature+ (Standing 3+) AND faction-aligned AND currently in Strategic Phase |
| **Victory progress access (V key)** | Always accessible, but panel content differs — Independent characters see only their own Renown-based path |
| **Thread sight toggle** | TS 1+ (any Thread perception at all; see §9.1 progressive unlock table) |
| **Coherence stat in HUD** | Only during active Thread contact (§9.4) — not in general HUD even for practitioners |
| **Thread operations panel** | Only during active Thread contact AND TS 30+ AND Approach Training tag |
| **Slate dock** | Always visible during Personal Phase |
| **Companion strip** | Only if at least one companion is present (0, 1, or 2 slots visible) |
| **Left context panel** | Varies by layer; content-driven |

**Implementation note:** on every chrome element, the UI subscribes to its own visibility signal. Changes in Stature, TS, faction alignment, or Obligation count fire the relevant signals. Elements mount/unmount rather than show/hide — this is meaningful for accessibility (screen readers should not encounter hidden elements at all).

## §2.2 Starting character baseline chrome

A new Operative-Stature, faction-aligned, non-sensitive, no-companions, no-obligations character sees:

```
┌──────────────────────────────────────────────────────────────────────┐
│ Peninsula › Valorsplatz (T1)            Winter · Year 1    actions: 4/4 │
├────────────────┬─────────────────────────────────────┬───────────────┤
│                │                                      │               │
│ [SLATE DOCK    │                                      │  GEN · Year 1 │
│  3 entries]    │       [MAIN VIEW]                    │  RS · Stable  │
│                │                                      │               │
│                │                                      │  STANDING     │
│                │                                      │  Operative    │
│                │                                      │  Renown 0/10  │
│                │                                      │               │
│                │                                      │  CONVICTIONS  │
│                │                                      │  A · ...      │
│                │                                      │  B · ...      │
│                │                                      │  C · ...      │
│                │                                      │               │
│                │                                      │  DUTY         │
│                │                                      │  Investigate  │
│                │                                      │  Vaelke       │
│                │                                      │               │
└────────────────┴─────────────────────────────────────┴───────────────┘
```

**What is absent:** no TC, no IP (haven't interacted with those systems), no Framework Drift (not Agent-Stature), no Thread sight toggle (TS 0), no Obligations block (none), no companion strip (no companions), no faction hand panel (not Counselor+), no three-clock summary.

This is the baseline. Most players start here.

## §2.3 Advanced character chrome (30+ seasons in)

A Counselor-Stature, faction-aligned, TS 42 with Approach Training, 2 companions, multiple Obligations, active investigations:

```
┌──────────────────────────────────────────────────────────────────────┐
│ Peninsula › Gransol (T8) › Parliament     ✦ Thread sight (off)        │
│                                           Winter · Year 5    actions: 3/4 │
├────────────────┬─────────────────────────────────────┬───────────────┤
│                │                                      │ CLOCKS        │
│ [SLATE DOCK    │                                      │ RS · Fragile  │
│  7 entries]    │       [MAIN VIEW]                    │ TC · Strained │
│                │                                      │ IP · Strained │
│                │                                      │ GEN · Year 5  │
│                │                                      │               │
│                │                                      │ FRAMEWORK     │
│                │                                      │ Crown ↑       │
│                │                                      │ Church ↑      │
│                │                                      │ Hafen ·       │
│                │                                      │ Varfell ↓     │
│                │                                      │               │
│                │                                      │ STATURE       │
│                │                                      │ Counselor     │
│                │                                      │ Renown 6/10   │
│                │                                      │               │
│                │                                      │ CONVICTIONS   │
│                │                                      │ A/B/C w/ scars│
│                │                                      │               │
│                │                                      │ OBLIGATIONS   │
│                │                                      │ Crown binding │
│                │                                      │ Eira's sister │
│                │                                      │               │
│                │                                      │ DUTY          │
│                │                                      │ Investigate   │
│                │                                      │ Vaelke        │
├────────────────┴─────────────────────────────────────┴───────────────┤
│ [ Eira : Equity ] HP 8/40 · Social  · 💬 "Push her."                   │
│ [ Tamm : Order ]  HP 12/40 · Governance at S-008                       │
└──────────────────────────────────────────────────────────────────────┘
```

This is the accreted chrome. The player has earned it.

## §2.4 The breadcrumb trail

Always visible. Segments: Peninsula › Province › Settlement › Location/Scene. Rightmost is current. Clickable segments zoom out. See §3.6 for zoom transitions.

## §2.5 The Slate dock

Docked to left edge during Personal Phase. Expandable. Entries by priority (0 mandatory, 1 crisis, 2 duty-aligned, 3 conviction-aligned, 4 world-state).

**Overflow rule (new in v4.1, resolves prior audit L-02):** max 12 visible entries. If more than 12 generate in a single season, a `+N more (archived priorities 3–4)` expander appears at the bottom. Archive-sensitive: Priority 0–2 entries never hide into expander; only 3–4 can be archived behind the expander.

Entry format:
```
⚠0 Ambush in Feldmark          [ Eira : Equity ]
●1 Heresy investigation opens  [ Tamm : Order ]
●1 Treasury crisis at Gransol  [ Eira : Equity ] ✦ Conviction B
●2 Duty: investigate Vaelke
●3 Warden emergence forming    ✦ Conviction C
```

Companion tag format `[ Name : Conviction ]` per Jordan's specification — the companion's primary Conviction from npc_behavior §1.2 taxonomy.

## §2.6 Companion strip

Only present when a companion is present. Tiered visibility per prior audit resolution:

- **Always visible:** name, portrait, Conviction tag, Disposition, Knot status, HP/wounds, current-scene commentary (if any)
- **Revealed via Connect actions:** private arc phase, hidden Beliefs, personal trauma details

## §2.7 Right rail layout principles

Scene-aware ordering. Elements promote to top based on scene relevance:

- **Dialogue scene:** Convictions promote to top; clocks demote
- **Contest scene:** Convictions + Obligations promote
- **Combat scene:** Wound/Stamina/Composure promote to left context (see Part 7); right rail compresses
- **Thread contact:** right rail compresses further; Thread panel takes over main view; Coherence and CD surface only during contact
- **Faction Strategic Phase:** Framework Drift + Hand Panel promote; Convictions demote to bottom

This is the single revision fix for prior audit finding L-01 (right rail saturation).

---

# PART 3 — TRAVEL, ZOOM, THE PENINSULA, SETTLEMENTS

Authoritative sources: fieldwork_v30 §3.3, settlement_layer_v30 §4.1, scale_transitions_v30 §4, geography_v30.

## §3.1 The four layers

| Layer | Scope | Surface |
|-------|-------|---------|
| Peninsula | 17-territory overhead | Illustrated map |
| Province | One territory | Panel with settlement nodes |
| Settlement | One settlement | Location list (Darklands / Pentiment) |
| Scene | One resolution | Surface-specific (combat grid, dialogue, contest, Thread) |

Chrome persists at all four. Only cutscenes dismiss chrome.

## §3.2 The Peninsula map — art direction

**Precedent corrected from prior v4:** Triangle Strategy is *not* the Peninsula map precedent. Valoria is pre-Reformation European medieval. Correct precedents:
- Medieval portolan charts for coastlines
- T-O maps and manuscript-illumination cartography for territorial divisions
- Hereford Mappa Mundi aesthetic (without the religious abstraction)
- Pentiment's map interludes (closest modern precedent)

**Rendering:** hand-illustrated ink-and-wash on parchment, with inked territory borders, painted color fills for faction control, hatched overlays for occupation, marginalia for legend. The map feels like a period document, not a fantasy overview.

**Encoding:**

| Element | Visual |
|---------|--------|
| Faction control | Color fill per territory — **see §3.2.1 for corrected palette** |
| Accord | Saturation (3+ full, 1–2 muted, 0 desaturated with agitation shader) |
| Occupation | Hatched overlay in occupier color |
| Framework Drift | Edge pulse (1.2s cycle, 80% alpha) in faction color — Agent+ Stature only |
| RS substrate state | Global shader on the whole map (see §9.5) |
| Calamity gradient | Static radial darkening from T15 Askeheim, per calamity_radiation_v30 |
| Player position | Illustrated character silhouette (heraldic style, not photorealistic) |
| Companion positions | Smaller silhouettes beside player |
| Active Slate anchor | Amber marginal illumination halo around the relevant settlement node |
| Incoming threat | Red ink-drawn arrow from source to target, visible 1 season before resolution |

## §3.2.1 Faction color palette — corrected

Prior v4 had anachronistic colors. Corrections:

| Faction | Prior v4 | v4.1 (setting-faithful) | Rationale |
|---------|----------|------------------------|-----------|
| Crown | forest-green | unchanged (greenwood/royal hunting) | OK |
| Church of Solmund | indigo | **deep purple / sable** | Indigo is post-period import. Purple is liturgical (penitential/royal); sable is Church-institutional |
| Hafenmark | amber | unchanged (mercantile gold) | OK |
| Varfell | violet | **slate / peat-brown** | Violet conflicts with Church purple; slate/peat reads highland |
| Löwenritter | oxblood | unchanged (martial) | OK |
| Restoration Movement | teal | **woad-blue** | Teal is non-medieval; woad is the period blue dye |
| Guilds | ochre | unchanged (counting-house) | OK |
| Niflhel | — | no public color (covert) | Only shown through revealed presence |
| Wardens | — | ash-grey / bone-white | Southernmost register |
| Uncontrolled | grey | unchanged | OK |

## §3.3 Province panel

Opens on clicking a territory. Peninsula dims to 40% behind.

Shows:
- Controller + provincial authority tension line (if governor ≠ provincial authority)
- Accord calculation shown transparently: `⌊(Order_S1 + Order_S2 + Order_S3) / N⌋`
- Fort Level and garrison composition
- Calamity proximity (Distant / Near / Close / Adjacent / Askeheim)
- Settlement cards in rough geographic arrangement
- Subnational presences — overt listed directly, covert shown as `? something · Cognition N required to parse`

**Covert Niflhel cue (resolves UI-15):** always-ambient `?` entry. Cognition ≥ 3 parses it as a specific cue ("unease at S-015 — covert presence"). Below Cognition 3, reads as "something unclear here." This makes the information gate perceptual-gradient per P-03, not binary.

## §3.4 Settlement interior — location list

Darklands / Pentiment precedent. Locations rendered as painted vignettes (pre-Gothic era, simpler figure drawing per Appendix C), not 3D walkaround.

Each location card:
- Name and atmospheric description
- Vignette illustration
- Depth access pips (§4.2)
- NPCs present with Disposition
- Active Slate anchor if one anchors here
- Enter button

Starting Operative character sees only Surface depth (1 pip filled) at most locations. As Histories develop and Depth access increases, more pips fill.

## §3.5 Scene surface

The innermost layer. Differs per mode: fieldwork action panel (§4.3), dialogue (§5), contest (§6), combat hex grid (§7), Thread panel (§9). All retain chrome except combat at full focus (chrome compresses to edges) and cutscenes (chrome hidden).

## §3.6 Zoom transitions

Setting-faithful audio cues: parchment rustle, manuscript page turn, ink drying sound, cloth movement.

| Transition | Duration | Easing | Audio |
|------------|----------|--------|-------|
| Peninsula → Province | 400ms | ease-out cubic | Manuscript page turn |
| Province → Settlement | 500ms | ease-out cubic | Cloth rustle, muted bell |
| Settlement → Scene | 600ms | ease-in-out | Soft drawn breath |
| Scene → Settlement | 500ms | ease-in cubic | Soft release |
| Settlement → Province | 400ms | ease-in cubic | Page turn back |
| Province → Peninsula | 400ms | ease-in cubic | Broader air |
| Any → Thread contact | 1500ms | special (see §9.3) | see §9.3 |

Skippable via Settings after first campaign.

---

# PART 4 — FIELDWORK

Authoritative source: fieldwork_v30.md (full).

## §4.1 What fieldwork is

The master Personal Phase activity. Encompasses exploration, investigation, socialising — all sharing a unified pool system and the depth-axis perception gate (§4.2).

## §4.2 Depth axis as perception system

Per fieldwork §1. Five depths: Surface (0), Settled (1), Hidden (2), Buried (3), Liminal (4). Canon P-03 made mechanical.

```
Location: Gransol Parliament · Court
Your Depth access: [●●●○○]
 · Surface   — unlocked
 · Settled   — unlocked
 · Hidden    — unlocked
 · Buried    — requires TS ≥ 10 OR Disposition +3 with Court NPC
 · Liminal   — requires TS ≥ 30
```

**This is not a menu. It is the character's perceptual horizon rendered as UI.** A non-sensitive character (TS 0) will never see Liminal-depth options in any scene because the options are not rendered to their consciousness. P-03 operational.

**ED-544 resolution:** this IS the videogame rendering model. Depth-access gating + Thread sight toggle (§9.2) + environmental shaders (§9.5) together constitute the P-03 implementation. No further rendering model needed.

## §4.3 Action panel

See v4 §4.3 for the layout. Unchanged in v4.1 structurally; Exposure projection on each button, confirm-before-commit flow, Journal updates in-scene.

**Cost per entry:** 1 scene action per scene (entering a new location). Sub-actions within a scene (Read + Converse + Examine in one location) are free. This is codified in §1.3 Scene Action Cost Table.

## §4.4 Cover and Exposure

Per fieldwork §6.

- **Cover** (character stat): `Cognition + relevant concealment History`. Determines Exposure thresholds.
- **Exposure** (per-territory, per-season). Actions generate Exposure. Thresholds trigger consequences.

Display in left context panel during fieldwork — unchanged from v4.

## §4.5 Journal

Accessible via `J`. Investigation list sorted by status. Evidence with reliability tags and source attribution.

**Inert Knowledge evidence (P-08 compliance):** non-sensitive characters who encounter Thread-related evidence see it with strikethrough text and a tooltip: "You can recite this but cannot act on it with Thread-level precision." The evidence occupies a Journal slot but provides no mechanical benefit for Thread-related investigations or rolls.

## §4.5.1 Southernmost forgetting (P-13 compliance)

Evidence acquired in T15 Askeheim or directly related to Southernmost phenomena, by non-sensitive characters, visibly decays in the Journal over seasons:

- Season 0 (acquired): full text, legible
- Season +1: one word strikethrough ("I saw a ~~figure~~ ~~standing~~ at the ~~pillar~~ and then..."). Ghostly.
- Season +2: half the entry strikethrough, reading as fragments
- Season +3: entry reduced to "something happened at Askeheim that I cannot explain"
- Season +4: entry auto-archives; Journal slot freed

A sensitive character (TS 30+) does not experience this decay — the evidence remains legible. If a non-sensitive character acquires TS mid-campaign (via lifepath), previously-decayed evidence does NOT restore. The rendering failure was historical; the evidence is lost.

This is P-13 made mechanical. Non-sensitives cannot hold Southernmost knowledge stably.

## §4.6 Reconstruct

Deduction board template per investigation type. Resolves UI-12.

- Simple investigation: 3 evidence slots + synthesis
- Complex: 5 evidence slots + 2 synthesis branches
- Structural: 8 evidence slots + 3 synthesis branches

Templates scaffold structure without overdetermining. The arrangement is mechanically meaningful; the Reconstruct roll determines whether the arrangement produces a correct Finding or a wrong conclusion the player will not know is wrong until contradictory evidence surfaces later.

Case of the Golden Idol precedent — the detective's pinboard with pre-set slots.

---

# PART 5 — DIALOGUE AS DISCO-ELYSIUM CONVICTION INTERFACE

Authoritative sources: player_agency §2, fieldwork §10.4, social_contest §9.5, npc_behavior §1, §3, §6.

## §5.1 What dialogue is

The conversational register. Single scene of back-and-forth. Player Convictions and NPC Convictions form the frame that constrains what can be said.

## §5.2 Dialogue layout

See v4 §5.2. NPC portrait (painted, pre-Gothic per Appendix C), dialog text, 5–8 response options, companion commentary below.

**Portrait art direction corrected:** 12th–14th century illumination aesthetic. Pre-Gothic figure drawing. Iconographic rather than naturalistic. Hand gestures indicating speech/rank. Clothing encoding social position (per period sumptuary conventions). NOT Pentiment's 16th-century manuscript style — too late.

## §5.3 The eight row types

| Row type | Visual | Mechanical effect |
|----------|--------|-------------------|
| Mechanical social action | Plain text + pool | Standard fieldwork §5.2 roll |
| Conviction-driven | ✦ gold mark + Conviction text | +1 Momentum on Belief-aligned success |
| Framework-aligned | Amber mark + framework name | −1 Ob per social_contest §2 Step 3 |
| Belief-targeted | Purple ◆ mark + Belief text | Adds pressure; 3 cumulative = Belief Scar |
| Negotiate | Plain with pool | Below contest threshold; escalates above |
| Walk away | Muted text | No roll, no cost, ends scene |
| Locked by Conviction | 🔒 red + Conviction text | Override costs +1 scar on player Conviction |
| Locked by prerequisite | 🔒 grey + requirement text | Cannot be selected; hover shows requirement |

### §5.3.1 Thread-gated options (new clarification for v4.1)

Thread-related dialogue options (Thread sight reveals, Thread-focused queries, Leap-assisted perception) appear ONLY at the appropriate TS threshold. A non-sensitive character (TS 0) does not see Thread options at all — they are not locked, they are not rendered. P-03 operational.

A TS 1–29 character sees limited Thread options (Read Thread-sensitivity of NPC, recognize Thread-phenomena in environment).

A TS 30+ character sees the full Thread dialogue set.

This is symmetric with the UI-chrome gating in §2 — dialogue options also obey capability gating.

## §5.4 Convictions limit player speech

Options that contradict a Conviction appear locked. Override opens confirmation modal with scar consequence. Unchanged from v4.

## §5.5 NPC Convictions limit their responses

NPC responses constrained by their Stance Triangle (npc_behavior §2). The italic subtext above NPC speech shows the constraint: `[ Conviction: Precedent restrains her to procedural language ]`.

**Always present** when a Conviction-driven or Belief-targeted option is relevant. No Spirit check required. Resolves UI-11.

**Thread-specific internal voices:** shown only at Coherence ≤ 5 or during Thread contact (§9.6). For a non-sensitive character, these never appear.

## §5.6 History as skill-voice

Each social action shows the relevant History. Tooltip one line of skill-voice explanation.

## §5.7 Flow and budget

One scene = 1 scene action (§1.3). Dialogue ends when: walk away, escalate to Contest, NPC cuts off (Disposition → −3), budget consumed, event interrupts.

## §5.8 Companion voice

`[ Name : Conviction ]` format followed by one line of in-voice commentary. Conviction is the companion's primary Conviction per npc_behavior §1.2: Faith, Order, Reason, Equity, Precedent, Autonomy, or Continuity.

Example format across Conviction types:

- `[ Arne : Faith ]` "The Confessor spoke. We must go."
- `[ Almud : Order ]` "This one first. The rest can wait."
- `[ Maret : Reason ]` "The evidence contradicts her account."
- `[ Eira : Equity ]` "These people have no one. Go to them."
- `[ Inge : Precedent ]` "Parliament has ruled on this before."
- `[ Lisbeth : Autonomy ]` "Let them choose."
- `[ Edeyja : Continuity ]` "The work continues."

## §5.9 Ambient cues

Per §13 feel layers. Audio shifts with NPC mood; portrait animates subtly (Pentiment-style blink cycles, brow adjustments); background shifts with time of day and weather.

---

# PART 6 — SOCIAL CONTEST

Authoritative sources: social_contest_v30.md (full).

*Consolidates prior v4 Part 6 + Part 15 Parliament + Part 16 Inquisition + Part 17 Treaty into variants of the same underlying mechanic. Per prior audit E-01.*

## §6.1 The generic contest interface

Contest opening: NPC Stance Triangle revealed, Piety Track displayed, exchange count set, player's opening bonuses (preparation, Findings).

Each exchange:
1. Appraise (both orators roll Attunement)
2. Style selection (Memory/Projection × Revealing/Obscuring)
3. Corroborate (companion assist)
4. Evidence citation (Finding from Journal if available)
5. Resonant Style targeting (+1D on match to NPC's revealed styles)
6. Argue roll (pool assembles visibly with bonuses)
7. Resolution (CLASH / REINFORCE / CROSS / TIE)
8. Composure damage
9. Doubt Markers / Obscuring effects
10. Next exchange or final resolution

Resolves UI-13: layered stage view. Top-down tally view for vote-based contests; first-person chamber cutaway at key moments (opening statements, Veto, Rebuttal, Total Victory). Auto-switches on decisive events. `C` key toggles manually.

## §6.2 Parliament (§6 variant)

Chamber view with spatial faction arrangement. Motion declared, tally tracked, targeted faction may Veto or Rebuttal. See v4 §15 for details — unchanged structurally in v4.1.

Lobbying (pre-vote, 1 scene action per target) is where Parliament becomes personal-scale — player persuades individual faction representatives via brief private contests.

## §6.3 Inquisition Hearing (§7 variant)

Asymmetric register per social_contest §7. Darker palette (deep purple for Church per §3.2.1 color correction, sable accent), formal gothic typography, Inquisitor portrait prominent.

Accused constraints: no Corroboration, no Findings, Church Obscuring boost, halved audience resistance, asymmetric strain.

Accused advantages: may target Inquisitor Resonant Style; Martyrdom effect on loss (Church Stability +1).

## §6.4 Royal Audience

Parallel to Inquisition but less asymmetric. Crown green palette, warm. Petitioner may cite Findings and have Corroboration unless explicitly denied.

## §6.5 Treaty and Grand Debate

Three phases per faction_layer §3.3:
1. Positioning (Influence rolls)
2. Concession Declaration (no rolls, structured negotiation)
3. Ratification (Mandate rolls, Guarantor option)

Grand Debate escalation: full TTRPG social contest with Parliament as Crowd adjudicator. Result modifies Ratification rolls.

This is the game's central vertical — personal-scale rhetoric reshaping faction-layer diplomacy.

## §6.6 Chain contests

Compromise outcomes queue next-season chain. Max 3, then cold equilibrium.

---

# PART 7 — PERSONAL COMBAT

Authoritative source: combat_v30.md (full, ED-548 Wound Interval correction applied).

## §7.1 The corrected Wound system (ED-548)

`Wound Interval = Endurance + 6` (7–13 range)
`Max Wounds = floor(Endurance / 2) + 1` (1–4 range)
`Total Damage Capacity = Wound Interval × (Max Wounds + 1)` (14–65 range)

A character with Endurance 5: WI 11, Max Wounds 3, Total 44. Wounds accrue at 11, 22, 33. Incapacitation at 44. Each Wound: −1D Combat Pool.

## §7.2 Combat HUD

Left context panel during combat. Unchanged from v4 structurally:

```
HEALTH — current WI  [■■■■■■■■□□□] 8/11
WOUNDS  ●●○ 2/3 (−2D pool)
Total: 20/44
STAMINA [■■■■□] 4/6
COMPOSURE [■■■■■■■■■■■] 11/11
MOMENTUM ● ● ○ ○  2/4
Rattled: 0  OOB: no
```

**Coherence is NOT in the general combat HUD.** Coherence appears only during active Thread contact (§9.4). This is the v4 correction per Jordan's C-2/C-3.

## §7.3 Hex grid (resolves UI-01)

12×8 standard. 16×10 set-piece (settlement interior fights with multiple combatants). Never below 10×6 or above 20×12.

## §7.4 Turn structure, asymmetric declaration

Per combat §2–3. Phase-based round, lower-initiative declares first blind, higher-initiative counter-declares.

## §7.5 Actions list

12 actions from combat §4. Dimmed actions show unlock condition on hover.

**Leap action (new clarification):** appears in the action list ONLY for characters with TS 30+ AND Approach Training tag. Absent from the action list for non-practitioners — not greyed out, not there. This is Oath II violation test #1 compliance.

## §7.6 Dice, damage, Fibonacci bonus, Rescue, Death Cascade

See v4 §7.6–7.9. Unchanged.

**Death Cascade cutscene trigger:** when the dead NPC was central to an active Conviction, a cutscene fires per §13. For non-Conviction-related deaths, the 5-step Death Cascade panel plays without cutscene.

## §7.7 Sufficient Scope indicator

Pre-combat banner for officer-level targets, showing projected faction consequences. Unchanged from v4.

---

# PART 8 — MASS COMBAT AND SETTLEMENT INVASION

Authoritative source: mass_battle_v30.md (full), settlement_layer §5.

## §8.1 Battle map

16×10 hex, unit tokens, formation indicators, terrain modifiers. See v4 Part 8 for detail.

## §8.2 Phase structure

7 phases per mass_battle §A.7. Each phase has its own UI affordances: Strategy grid, Volley animation, Manoeuvre drag-drop, Offensive Thread panels (only if practitioner commanders), Engagement splits, Cascade simultaneous damage, Reform.

**Thread-Offensive Phase (Phase 4):** only visible to commanders with TS 30+ Approach Training. For non-practitioner commanders, Phase 4 is skipped silently (auto-advanced to Phase 5). A practitioner General-Duel option appears in Phase 5 only when both combatants have the capability to engage.

## §8.3 General Duel Zoom In

Per mass_battle §A.5. Personal combat embedded in mass combat. 1 exchange = 1 mass combat turn. Mass battle freezes behind.

## §8.4 Settlement invasion

Assault / Siege / Bypass options per settlement_layer §5.1. Bypass locked unless Military > Defense + 3. Settlement capture mid-battle fires side-panel notification, does NOT interrupt current Phase (resolves UI-09).

## §8.5 Post-battle consequence

Priority 0 Slate entries for next Personal Phase. Player walks the field at personal scale. Non-negotiable.

## §8.6 Southernmost constraint

Dragging a unit to T15: each individual checked for TS ≥ 30 per mass_battle §A.11. Non-qualifying individuals dissolve; unit Size reduces. Red × on drop-failure.

---

# PART 9 — THREADWORK (PROGRESSIVE UNLOCK, FELT RADICALITY)

Authoritative sources: threadwork_v30.md (full), canon P-03, P-06, P-08, P-11, P-12, P-15.

*This Part is rewritten for v4.1 to correct v4's universal-Thread-UI assumption. Thread UI is **progressively unlocked** by TS. Most characters see none of it.*

## §9.1 Progressive unlock table (Jordan's correction C-2)

| Character TS | Approach Training | UI visible |
|---|---|---|
| TS 0 | no | **No Thread UI at all.** No Thread sight toggle. No Coherence. No Thread dialogue options. Thread phenomena in the world render as "something uncategorizable" — Inert Knowledge per P-08. The player sees effects but cannot parse them as Thread. |
| TS 1–29 | no | **Thread sight toggle only.** Reveals Thread practitioner sensitivity in NPCs (an inner shimmer), major Gap locations (environmental shader distortion), and the fact that Thread phenomena exist nearby. No Coherence stat yet — Coherence tracks only once the character has Leapt. Dialogue gains `?` interpretive tags on Thread-related NPC statements. |
| TS 30+ | yes | **Full Thread UI unlocks on first Leap.** Coherence stat initializes at 10/10. Thread operations panel accessible during contact. Personal-scale operations (Depth 1–3) selectable. Leap action appears in combat. Cutscene fires on first Leap per §13. |
| TS 50+ | yes | **Relational-scale unlocks.** Depth 5 becomes selectable. Knots can be target of operations. |
| TS 70+ | yes | **Structural-scale unlocks.** Depth 8 becomes selectable. RS and territorial Thread configurations become targetable. Depth 13 remains mechanically impossible per canon. |

**First Thread acquisition scene (new content for v4.1):** when a character acquires TS for the first time through a lifepath event or the Approach Training acquisition scene (which is itself a cutscene-triggered event — see §13), a short scene fires at the moment of crossing into TS 1:

> The Peninsula feels different now. Not wrong. Not right. **Different.**
> You notice the Clerk's edge — a faint pulse, a rhythm you had not perceived before. You notice the stone floor — old, laid long ago, bearing memory.
> This is how it begins. The Thread was here. You simply did not see it.

This is the Thread UI's "first boot." The Thread sight toggle appears in the chrome for the first time. A codex entry unlocks ("On Sensitivity"). The character is no longer naïve.

## §9.2 Thread sight toggle (TS 1+)

Toggle in top bar for any TS 1+ character. Manual activation per prior resolution UI-08.

**Prior audit I-02 correction (Thread sight always-payoff):** every location has a Thread signature — a baseline history-resonance that Thread sight reveals. At Gransol Parliament Court, Thread sight reveals faint silhouettes of past debates, ink-echoes of prior writs. At a tavern, it reveals the Thread of shared grief or celebration. At Askeheim, it reveals the substrate itself, unmediated.

This means Thread sight always produces SOMETHING. It is not a dead toggle in low-Thread scenes. A TS 1 character using Thread sight in a non-Thread scene sees location history made visible — a minor revelation, but a revelation.

**Non-visual equivalent for screen readers (prior audit A-01):** Thread sight also generates screen-reader audio descriptions of the Thread signature. "Court. You perceive the Thread of this chamber. Echoes of prior debates. The Clerk of Seals carries configuration suggestive of oath-related strain."

## §9.3 The Leap (TS 30+ only)

Appears as an action in combat and as a fieldwork option only for characters with TS 30+ AND Approach Training.

Leap transition — 1.5 seconds:
```
[screen desaturates to 40%]
[ambient audio dampens 70%]
[a low, barely-audible drone enters at 40Hz]
[UI elements shift 1–3 pixels in semi-random directions, then resettle]
[the Leap resolution modal appears]
```

This is not a loading screen. It is the character's consciousness suspending layer 2 rendering (P-15). The player feels the suspension.

Leap commit modal: shows pool, TN, Ob for current TS band, vulnerability window duration (all dice to Defence for the Leap round), contact duration, operations available during contact. Pre-commit transparency per Oath II.

## §9.4 Thread panel (during contact)

Visual register shifts when contact is established:

- Persistent low-frequency visual shimmer across all elements
- Ambient audio replaced with layered drone (evolving, operation-type-dependent per prior audit)
- UI chrome borders acquire Thread-tensile lines, barely perceptible
- Animation speeds decrease 20% — the world is slower because the player has stepped out of it
- Non-practitioner NPCs on screen appear less defined — their consciousness unengaged with the substrate

**Typography correction (setting fix):** Thread operations use **hermetic / Kabbalistic diagram typography**, not illuminated manuscript. Church uses illumination; Thread is explicitly opposed to Church per P-08. Thread typography should evoke esoteric tradition — geometric, cipher-like, with diagram annotations in Hebrew-derived or Pythagorean registers. The "illuminated initial letter" aesthetic is reserved for Church/Tribunal UI (§6.3).

Three-axis Ob builder:
- **Scale:** Object / Personal / Relational (TS 50+) / Territorial (TS 70+) / Structural (TS 70+)
- **Depth:** 1 / 2 / 3 / 5 / 8 (13 locked even at TS 70+)
- **Distance:** adjacent / province / adjacent province / cross-peninsula

Scale options above the character's TS band are absent, not greyed. A TS 35 character literally does not see Relational, Territorial, or Structural buttons.

**Pre-commit co-movement preview (P-01 compliance fix):** before casting, the panel shows projected three-axis cost with the auto-effect table reference. The player sees the temporal (CD accumulation range), epistemic (which NPCs will register the operation), and actualized (co-movement card pool) costs BEFORE commit.

## §9.5 Co-movement panel (P-01)

Fires after every operation. 3-second minimum display. Cannot be dismissed early.

Shows:
- **Temporal axis:** CD accumulation (with current total and band), History Resonance event if triggered
- **Epistemic axis:** Certainty shifts on observers, Inert Knowledge formations
- **Actualized axis:** Co-movement card drawn, mechanical effect

## §9.6 RS environmental rendering

| RS Band | Peninsula map | Settlement interior | Audio |
|---------|---------------|--------------------|----|
| 100–80 Stable | Warm ink palette | Grounded, natural | Clean consort music |
| 79–60 Strained | Slight muting | Occasional flicker in torch flames | Underlayer of distant harmonics (vielle drone) |
| 59–40 Fragile | Shifting-Object animations on high-traffic Thread territories | Objects subtly mispositioned | Detuned psaltery |
| 39–20 Fractured | Gap overlays visible on map | Strong color aberration, memory inconsistency | Dissonant bass drone (hurdy-gurdy) |
| 19–1 Critical | Map aberration; territory tint shifts unpredictably | Full rendering failures | Terror bed: sub-audible pulse |
| 0 Rupture | Cutscene fires — see §13 | — | — |

The Peninsula breathes with RS. RS 85 play feels different from RS 25 play.

## §9.6b World Survival Display — RS and WC (F-04, wc_survival_spine.md)

RS and WC are the survival contest's two axes. They require persistent, prominent UI presence.

**RS indicator (persistent HUD):** Numerical value + band label (Stable/Strained/Fragile/Fractured/Critical). Color-coded green→amber→red matching §9.6. Visible at ALL times in the persistent world-state strip alongside season clock.

**WC indicator (persistent HUD, adjacent to RS):** 4-pip track (0–3). WC 0: all grey. WC 1: first lit (blue). WC 2: two (brighter). WC 3: three (gold glow — Edeyja active Mending). Tooltip: current WC effects.

**Rationale:** Every other track is the political contest. RS and WC are the survival contest. The player must always see both — the problem (RS) and the response (WC). See wc_survival_spine.md.

## §9.7 Coherence and rendering corruption (TS 30+ only)

**Coherence is a practitioner-only stat.** It does not exist for non-sensitive characters. It initializes at 10/10 when the character first Leaps.

Degradation visible in UI per state:

| Coherence | UI state |
|-----------|----------|
| 10–8 Stable | Normal |
| 7–5 Dissonant | Occasional 1-pixel UI jitter; minor ambient shift |
| 4–3 Fragmented | Menus rarely flicker; one-word dialogue displacements; minor color aberration |
| 2 Fractured | Heavy aberration; Beliefs show ghostly second version (transforming framework); Convictions occasionally flicker to altered text |
| 1 Severed | UI fights the player: menus rearrange between clicks; audio drops briefly |
| 0 Crisis | Cutscene fires — **TS-branched outcome (P-15 compliance):** TS 30–49 produces dissolution-of-self narrative resolution (character becomes NPC); TS 50–69 produces ontological freefall (−3 RS/session); TS 70+ forces layer-3 self-maintenance (−1 RS/session, survives but strained) |

**Taint distinguished from Coherence (P-10 compliance fix):** Taint is a separate track, 0–6 per threadwork §16. Taint represents epistemic seduction — the practitioner's perceptual shift toward monstrous-rendering. Coherence is layer-2 self-rendering integrity. Both track independently. At Taint 4+, Beliefs show transformation-candidates ghosted above current Beliefs. At Coherence 2, Beliefs flicker between current and transformed.

Taint is shown in the character sheet (§11.3) for practitioners — ONLY. Non-practitioners have no Taint track.

## §9.8 CD accumulation display (P-11 compliance)

Calamity Drift accumulates across Thread operations per P-11. Visible in Thread-contact HUD (not general HUD) as a track:

```
CD this session: 3 / — (no threshold yet)
CD contribution to next RS tick: −2
```

Practitioners see their own temporal cost accruing. This was absent in v4; added for v4.1.

## §9.9 Knot visualization (P-12 compliance)

Silver thread between player portrait and Knotted NPC's portrait. Visible on companion strip, NPC character sheet, briefly during scenes where the Knotted NPC is present.

Strain pips beside thread. Silver → gold (wrongness) → red (rupture imminent). Rupture triggers cutscene per §13.

**Knot graph (new for v4.1, P-12 compliance):** §11.5 Relationships screen includes a network graph showing all Knots the player's Knotted-with NPCs carry. If Eira is Knotted to Maret, and the player is Knotted to Eira, transformation propagates visibly along the graph when any party is Tainted. Strain auto-accumulates per P-12 Patch O (+1 strain/season on Close Knots at Taint 4–6).

## §9.10 Why this is "radically unique"

Per Jordan's requirement. Re-stated briefly:

1. The game's visual/audio register changes during Thread contact (§9.4). Not a special effect — a structural shift.
2. Co-movement is mandatory, visible, unskippable (§9.5).
3. UI degrades at low Coherence (§9.7). The interface you trust becomes unreliable.
4. Structural-scale operations can end the campaign (RS 0 Rupture).
5. **Non-practitioners cannot see any of this.** A character with TS < 30 has no Thread panel, no Thread sight above TS 1, no Leap in combat. The entire Thread layer is literally invisible. P-08 operational.

A player playing a non-sensitive sees the Peninsula as solid. A player playing a practitioner sees the same Peninsula as configuration. Both are playing the same game; neither plays the full game.

---

# PART 10 — ENCOUNTER UI VARIATIONS

*New in v4.1. Fills four canon gaps flagged in the prior audit addendum: monster encounters (P-04), Threadcut beings (P-06), memory operations (P-09), Southernmost entities (P-13).*

## §10.1 Monster encounters (P-04)

Monstrous entities are rendering failures, not villains (P-04). The UI expresses this by failing to render them coherently — not by presenting them as enemies.

When a monster enters a scene:
- It does NOT appear with a combat token, stat bar, or nameplate
- Instead, its rendering is deferred: an empty hex with environmental distortion, audio distortion, ambient color-shift
- The character's HUD shows: "rendering failure — ob 3 Cognition check to resolve, ob 5 to engage"
- Non-sensitive characters can only see the effects of the entity (objects moved, people affected) and cannot target it directly
- TS 30+ characters see a partial configuration — the monster appears as a non-Euclidean hex presence (4–7 hexes simultaneously), with Thread-visible tensile lines showing its partial rendering

Combat against a monster uses the standard grid, but monster hexes are ambiguous. Movement through a monster hex triggers a Coherence check (practitioner) or a Composure check (non-practitioner).

No stat block is shown to the player. Monster threat is conveyed through environment, not numbers. Control / Outer Wilds precedent (corrected from v4's mistaken Control attribution) — the thing is dangerous because the game cannot show you what it is.

## §10.2 Threadcut beings (P-06)

Threadcut beings do not participate in organic temporal accumulation (P-06). UI implications:

- Threadcut opponent combat token appears normal but the Wound Interval bar is replaced with a different display: "Thread cost accumulating — 0 / ? operations to sever"
- Past-Pulls against a Threadcut being auto-produce a Gap (animated with environmental distortion, Exposure cost +2)
- Age-based lifepath effects do not apply to Threadcut beings — the character sheet (if inspectable) shows no age, no aging history
- Taint track does not apply
- Killing a Threadcut being requires sustained Thread work; a standard Strike does not produce standard damage

The combat HUD dynamically reconfigures when facing a Threadcut opponent. The player sees immediately that this is not a normal engagement — the normal progress bars are gone.

## §10.3 Memory pulling operations (P-09)

Memory pulling is detectable (P-09). When a practitioner performs a Memory Pull:

- Co-movement panel (§9.5) explicitly shows "orphaned configuration created at [location]"
- The orphaned configuration appears on the Peninsula map as a subtle environmental marker for TS 30+ observers (a faint discontinuity icon)
- TS 30+ Diagnosis roll Ob 3 reveals the pull occurred
- The memory target NPC has Certainty reduction displayed in their character sheet (if revealed)

Non-practitioners cannot detect memory pulls directly. They may notice behavioral changes in the target NPC (Disposition shifts, Belief revisions) but cannot attribute these to memory alteration without a practitioner's Diagnosis.

The UI does not allow clean, undetectable memory erasure. This is Oath II and P-09 operational.

## §10.4 Southernmost entities (P-13 UI)

Wardens, Einhir survivors, Threadcut Southernmost beings all share a common UI treatment:

- Nameplate uses the Warden typeface (ash-grey / bone-white, per §3.2.1 palette) instead of faction colors
- Dialogue uses the Forgetting mechanic (§4.5.1) — non-sensitive players' recall of the encounter decays across seasons
- Non-sensitive players see Southernmost entities as "a figure" or "a silhouette" — no face, no name, no coherent description
- TS 30+ players see full description (face, name if known, identifying details)
- The Codex entry on any Southernmost entity locks to fragment-only for non-sensitives (§11.4 below)

The encounter itself, while happening, is fully legible to both sensitives and non-sensitives. The legibility erodes afterward for non-sensitives. This is P-13 operational.

---

# PART 11 — FACTION, SETTLEMENT, CHARACTER, PARTY MANAGEMENT

*Consolidates prior v4 Parts 11, 12, 13, 14 per audit finding E-01.*

## §11.1 Faction management (Counselor Stature+ only)

Visible only to Counselor+ faction-aligned characters. Content unchanged from v4 Part 11.

**Hand panel (resolves UI-02):** iconic card art, illuminated manuscript aesthetic with faction-specific typography per Appendix C. Card readiness, cooldowns, Casus Belli indicators.

**Domain Action flow:** target selection → confirmation with Domain Echo projection → Uphold/Appease prompt if challenging Mandate ≥ 4 faction → dice roll → degree result → Domain Echo animation if Sufficient Scope fires → state propagation.

**Victory progress panel (V key):** content differs by faction. Independent characters see only Renown-based path. Faction-aligned see universal condition + faction-specific path + co-victory pairings + shared-loss risk.

## §11.2 Settlement management (Counselor Stature+ governors only)

Governor Panel docked to left in settlement view — only if player governs this settlement. Otherwise, settlement view shows location list without governor affordances.

Governance action this season (free, mandatory): Develop / Fortify / Pacify / Administer. Each resolves via roll.

Subnational delegation. Companion delegation (social vs governance free action). Settlement events auto-generated per settlement_layer §4.3.

**Companion governance animation (resolves UI-14):** Phase 3 Cascade includes brief 2-second overlay of companion governance roll result on the settlement panel. Overwhelming or band-transition results extend to 4-second cutaway.

## §11.3 Character management

Character sheet via `C` key. Full view.

```
[name and lifepath] · [Stature and faction] · Renown
Attributes (10 stats)
Histories (earned + lifepath)
Derived (ED-548 corrected Wound Interval)
Convictions (3 active, scar pips)
Beliefs (5 active, revisable)
Knots (active + strain)
Current Duty (if faction-aligned)
Status (wounds, Stamina, combat reputation, obligations count)

[ONLY for practitioners — TS 30+ with Approach Training:]
Thread Sensitivity
Coherence (current/max)
Taint (separate from Coherence per §9.7)
Approach tag
```

The Thread stats block is absent for non-practitioners. No Coherence, no Taint, no TS field — these stats do not apply to their character.

**Conviction revision (Phase 4):** Restate / Transform / Abandon paths per v4 §13.2. Unchanged.

**Independence path (§5.3):** a character may refuse faction alignment at creation or abandon mid-campaign. No Duties. Slate generation from Convictions only. No faction stat pool until Renown 7+. At Renown 9+, may call Grand Contest any time. Independent characters see the same character sheet minus the faction-alignment fields (no Standing, no Duty, no Obligations-to-faction — only personal Obligations).

## §11.4 Codex

Via `K` key.

Entry states per entry:
- ● Fully known — encountered and engaged
- ◐ Partially known — encountered but not deep
- ○ Heard of — mentioned, not encountered
- 🔒 Unknown — not yet in player awareness

**Epistemic access rules (P-08 compliance, new in v4.1):** Codex entries gated by character knowledge state.

- Thread-related entries for a non-sensitive character: always show as fragmentary, with a note: "writings attribute certain phenomena to practitioners; details untransmittable." No mechanical content available for rolls.
- Southernmost entries for non-sensitives: fragment-only; the "Full lore" section is not accessible.
- Faction-interior Codex entries (e.g., Niflhel organization chart, Church internal politics): require Agent+ Stature in a faction that has investigated.

This prevents a non-sensitive player from using the Codex to look up Thread-level mechanics their character cannot operationally possess.

## §11.5 Party management

Companion cap 2. Connection action during social scene: requires Disp +3, not faction leader, not under active Heresy Investigation, 2+ prior scenes.

Companion panel: painted portrait, `[ Name : Conviction ]` tag, Disposition, Knot status, HP, Stamina, Conviction violations this season (3 = forced departure), active arc phase (tiered: Knot/public always visible, private via Connect).

**Knot graph (new for v4.1, P-12 compliance):** Relationships screen includes a network visualization. All Knots the player has + all Knots those Knotted-NPCs carry. Transformations propagate visibly along the graph. This surfaces P-12 contagion at the interface.

Companion departure: always a scene, never silent. Player may attempt 1-exchange persuasion contest.

---

# PART 12 — THE INTEGRATED LOOP

Authoritative sources: synthesis of all v30 mechanics.

*Unchanged from v4 Part 10. This is the document's strongest single Part. The walkthrough demonstrates every transition, every state persistence, every consequence propagation in a single 7-scene example.*

## §12.1 Transition inventory

| From → To | Trigger | UI handoff | Animation |
|-----------|---------|-----------|-----------|
| Fieldwork → Investigation | Examine/Research succeeds | Journal icon pulses; Evidence bar fills | 0.3s |
| Investigation → Contest | Negotiate exceeds informal threshold | ESCALATE TO CONTEST button | 0.5s fade |
| Contest → Combat | NPC declares violence | Initiative rolls; hex grid fades in | 0.8s |
| Combat → Fieldwork | Combat resolves | Action panel reappears; Exposure updated | 0.5s |
| Fieldwork → Combat | Exposure Compromised crossed | Full-screen "Ambush!" event | 1.0s tension ramp |
| Fieldwork → Thread | Thread-Read declared (TS 30+ only) | Leap transition 1.5s | §9.3 |
| Contest → Fieldwork | Contest resolves; Obligation logs | Post-contest panel; return to Settlement | 0.5s |
| Any → Cutscene | Priority 0 event | Chrome dismisses; cutscene loads | 1.0s to black + 1.0s in |

## §12.2 The 7-scene walkthrough (ED-548 formula)

[content from v4 §10.2 carries forward unchanged — Aldric at Endurance 5 with WI 11, MW 3, Total 44. The sequence: fieldwork Examine → continued fieldwork Read + dialogue with Conviction option → Reconstruct → Domain Echo fires → travel + dialogue escalates to Contest → Contest-to-combat transition when Niflhel plant draws weapon → post-combat fieldwork → Phase 4 Aftermath with companion scene]

Scene action accounting under the unified Cost Table (§1.3):
- Scene 1 (fieldwork Examine): 1
- Scene 2 (continued same location — Read + dialogue): 0 (chain rule — highest cost already paid)
- Reconstruct within scene: 0
- Scene 4 (travel + dialogue → Contest): 1 (contest absorbs the dialogue)
- Scene 5 (combat): 1 (auto from contest→combat transition, not additional)
- Scene 6 (post-combat Examine): 1

Total: 3 actions of 4 budget. One action remaining for a fifth scene or saved for next season's +1.

## §12.3 Why this is smooth

Chrome persists. Journal persists. Slate persists. Right rail persists. Only the scene surface swaps. Every transition has an explicit cue. Every outcome ripples visibly via animated Domain Echo, Conviction pip update, Obligation card append. No loading screens.

---

# PART 13 — CUTSCENES AND FEEL LAYERS

Authoritative sources: synthesis; Jordan's request ("bypass the game merely telling the player that something happened").

*Consolidates v4 Parts 19 + 20. Layer 3 (haptic-equivalent) deleted per Jordan's correction C-1.*

## §13.1 Cutscene philosophy

Painted backgrounds (pre-Gothic illumination aesthetic per Appendix C). Character portraits half-body. Dialog in calligraphy. **Period ensemble music** — NOT orchestral. See Appendix D for instrumentation.

Duration: 30s (minor arc beat) to 3 minutes (major arc climax).

## §13.2 Mandatory trigger inventory

From v4 Part 19 — 22 mandatory triggers. Unchanged.

Plus Convergence Marker cutscenes (COLLISION A/B/C/D from arc_register §VI).

Plus: **First Thread acquisition cutscene (new in v4.1)** — fires when character acquires TS 1 for the first time (lifepath or Approach Training event). 30-second scene; the character's perception shifts; the Thread sight toggle appears in chrome thereafter.

## §13.3 Convergence Marker cutscenes

From v4 §19.3. Four cutscenes (Church Double Fracture, Practitioner King, Tutoring + Southernmost, Niflhel Weaponises). Each 3 minutes, bespoke.

## §13.4 Seasonal atmospheric mini-cutscenes (new in v4.1)

Prior audit I-01: v4 cutscene density can drop below 1-per-3-seasons in short campaigns. Fix: 5–8 atmospheric mini-cutscenes (30s each) fire on low-density triggers:

- New season opens with notable weather (first snow, harvest season)
- Home-territory Accord band transition
- Companion Disposition reaches +5 (Devoted)
- Standing promotion (Operative → Agent, Agent → Counselor, etc.)
- Renown crossing a multiple of 3
- First visit to a Seat settlement
- First Parliament session attended
- First season with all 3 Convictions at 0 scars (consolidation moment)

These are skippable on any viewing and exist to ensure cutscene density never falls below 1-per-2-seasons.

## §13.5 Cutscene skip policy

First viewing of a cutscene TYPE: not skippable (after 3-second grace period allows pause). Second+ viewings: skippable via ESC. Pause always available. Rewatch via Codex.

## §13.6 Music register (resolves setting finding SET-1)

**Cutscene music is period ensemble, NOT orchestra.** See Appendix D for full specification.

- **Forms:** estampie, chanson, organum, motet (Church scenes), consort music (court scenes)
- **Instruments:** lute, vielle, rebec, hurdy-gurdy, psaltery, recorder family, shawm, sackbut, tabor, nakers, vocal chant
- **NOT USED:** violin family, full brass, timpani, romantic-period orchestral swells, modern drum kit

## §13.7 The four feel layers

*Corrected per Jordan's C-1. Layer 3 deleted.*

### §13.7.1 Layer 1 — ambient (always on, unobtrusive)

- Lighting per settlement type (Seat diffuse, Fortress torchlit low-angle, Port overcast, Outpost sparse, Cathedral stained-glass colored, Mine dark-close-lamp, Town/Village golden-hour)
- Weather by season and **terrain region** (prior audit I correction): northern continental vs southern Mediterranean-inflected
- Time of day: Dawn / Morning / Noon / Afternoon / Dusk / Night. NPC availability varies with time.
- NPC presence: named NPCs move through settlements in routines. Archivist at Archives in morning, Court in afternoon.

### §13.7.2 Layer 2 — cue (intermittent, specific)

- Roll landings: dice-click, paper rustle, chime on 10s
- Success/failure audio chords: Overwhelming major, Success minor tonic, Partial unresolved, Failure dissonant sub-tonic
- Scene transitions: each transition per §3.6 has specific audio signature (parchment-turn, etc.)
- Menu open/close: parchment rustle, quill scratch, ribbon close
- Portrait expression shifts: subtle audio cue

**Critical events (crit hit, death, band transitions, Domain Echo):** use cue audio appropriate to the event. No additional visual treatment beyond what the event's primary UI already shows. This is the v4 Layer 3 deletion applied.

### §13.7.3 Layer 3 — threadwork-radical (the fracture)

*Formerly Layer 4 in v4. Renumbered after deletion of v4's Layer 3.*

Only active for practitioners in Thread contact OR at Coherence ≤ 5 OR in RS ≤ 40 territories:

- Animation speeds decrease 20%
- Low-frequency drone replaces ambient
- UI chrome acquires Thread-tensile lines
- Non-practitioner NPC portraits desaturate (their dormancy relative to substrate becomes visible)
- Thread operations panel uses hermetic typography (per §9.4 correction)

At Coherence 4: menus flicker; one-word displacements in dialogue; minor color aberration.

At Coherence 2: Beliefs show ghost-versions; Convictions flicker; scene transitions take an extra 200ms and feel wrong.

At Coherence 1: menus rearrange between clicks; audio drops briefly.

At Coherence 0: cutscene — TS-branched per P-15 and §9.7.

### §13.7.4 The Peninsula's pulse (Layer 4 — ambient environmental)

*Formerly under §20.6. A distinct layer in v4.1.*

The Peninsula map, when viewed, has 6-second visual breathing cycle. Faction territories pulse in their own rhythms:
- Crown: slow
- Church: regular procession
- Varfell: irregular, rustic
- Hafenmark: measured parliamentary
- Löwenritter: martial drumbeat
- RM: communal
- Niflhel: erratic
- Guilds: counting-house regular

Pulse speed scales with Accord — slowest at high Accord, agitated at Accord 0 (revolt). The peninsula shows its mood without showing a number.

---

# PART 14 — RESOLVED ITEMS INDEX

| ID | Resolution | Location |
|---|---|---|
| UI-01 | Combat grid 12×8 standard, 16×10 set-piece | §7.3 |
| UI-02 | Hand panel iconic card art, faction typography | §11.1 + Appendix C |
| UI-03 | Involuntary Thread perception via Coherence ≤5 and Thread sight reveal | §9.7 |
| UI-04 | Slate volume at Hard difficulty (9 entries) manageable via priority tier + companion commentary | §2.5 |
| UI-05 | Obligations block in right rail, expand-on-click | §2.1, §2.3 |
| UI-06 | Framework Drift pulse 80% alpha 1.2s; RS band shader scales | §2.1, §9.6 |
| UI-07 | Panel adjudicator flexibility (ED-137 dependency) | §6 |
| UI-08 | Thread sight manual toggle | §9.2 |
| UI-09 | Settlement capture side-panel, General Duel full Zoom In | §8.4, §8.3 |
| UI-10 | Companion arc phase tiered visibility | §11.5 |
| UI-11 | Internal voices always present; Thread voices at Coherence ≤5 | §5.5, §9.7 |
| UI-12 | Reconstruct templates per investigation type (3/5/8) | §4.6 |
| UI-13 | Parliament dual-view (tally + cutaway) | §6.1–6.2 |
| UI-14 | Companion governance Phase 3 animation | §11.2 |
| UI-15 | Covert Niflhel ambient `?` parseable at Cognition 3+ | §3.3 |
| ED-544 | P-03 videogame rendering = depth gate + Thread sight + environmental shader | §4.2, §9 |
| ED-545 | Zoom In triggers expanded via Scene Slate Priority 0/1 | §2.5 |
| ED-548 | Wound Interval formula: WI × (Max Wounds + 1) total, wound every WI damage | §7.1 |

Canon compliance gaps from audit addendum, resolved in v4.1:
| Canon | v4.1 resolution |
|---|---|
| P-01 | Pre-commit co-movement preview in Thread panel (§9.4) |
| P-03 | Chrome capability gating (§2.1, §9.1) — fundamental rewrite |
| P-04 | Monster encounter UI (§10.1) |
| P-06 | Threadcut encounter UI (§10.2) |
| P-08 | Codex epistemic access rules (§11.4) |
| P-09 | Memory pulling detection UI (§10.3) |
| P-10 | Taint distinguished from Coherence (§9.7) |
| P-11 | CD accumulation track in Thread HUD (§9.8) |
| P-12 | Knot graph in Relationships screen (§11.5) |
| P-13 | Southernmost forgetting in Journal (§4.5.1) + Southernmost entities UI (§10.4) |
| P-15 | Coherence 0 TS-branched outcomes (§9.7) |

Jordan's three corrections:
| Correction | v4.1 resolution |
|---|---|
| C-1 Cut Layer 3 haptic-equivalent | Deleted; §13.7 renumbered |
| C-2 Thread UI TS gating | §9.1 progressive unlock table; Thread chrome only at appropriate TS |
| C-3 UI only for capabilities | §2.1 chrome visibility rules; all elements capability-gated |

Setting corrections:
| Finding | v4.1 resolution |
|---|---|
| SET-1 Orchestral → period ensemble | §13.6 + Appendix D |
| SET-2 Thread typography hermetic not illuminated | §9.4, Appendix C |
| SET-3 Faction typefaces specified | Appendix C |
| SET-4 Map precedent Pentiment/medieval not Triangle Strategy | §3.2 |
| SET-5 Portrait era pre-Gothic | §5.2, Appendix C |
| SET-6 Church purple/sable, RM woad, Varfell slate | §3.2.1 |
| SET-7 Weather terrain-regional | §13.7.1 |

Prior audit's additional findings addressed in v4.1:
| Finding | Resolution |
|---|---|
| E-03/S-02 Scene action costs scattered | §1.3 unified Cost Table |
| E-01 25 parts structurally bloated | Consolidated to 14 parts + 5 appendices |
| L-01 Right rail saturation | §2.7 scene-aware ordering |
| L-02 Slate overflow rules | §2.5 overflow with expander |
| I-01 Cutscene density floor | §13.4 atmospheric mini-cutscenes |
| I-02 Thread sight always-payoff | §9.2 Thread signatures |
| I-04 Oath Violation Tests | §0 |

Remaining v4.2+ backlog: A-01 through A-04 (accessibility — Thread sight screen-reader partial in §9.2; dice narration, hex motor access, cognitive accessibility still open), L-03 (typography consolidation — partial via Appendix C), L-04 (pool visualization for large pools), R-01 (Thread ops strategic matrix — analytic), R-02 (hand panel customization), R-03 (archived Slate resolution panel), precedent corrections (Appendix B).

---

# APPENDIX A — ACCESSIBILITY, INPUT, RESOLUTION

Input: keyboard + mouse, controller, touch (tablet landscape). Full remapping.

Key shortcuts: J (Journal), K (Codex), C (Character), M (Map), V (Victory — if accessible), R (Relationships), T (Thread sight — if TS 1+), ESC (menu/cancel), Space (confirm).

Resolution: 1280×720 minimum, 1920×1080 native, 3840×2160 scaling. UI scale 75%/100%/125%/150%/200%.

Accessibility features:
- Colorblind modes (Deuteranopia/Protanopia/Tritanopia); secondary encoding via shape/pattern
- High contrast
- Motion reduction (suppresses ambient pulses and Peninsula breathing)
- Text size range, dyslexia font option
- Screen-reader support at every UI element
- Cutscene subtitles on by default
- Reduced-flicker mode for Coherence degradation (mechanical effect preserved, visual replaced with warning banner)

**Thread sight screen-reader parallel (partial v4.1 implementation):** Thread sight toggle generates audio descriptions of Thread signatures per §9.2. Full audio-equivalent of Thread panel content deferred to v4.2.

Minimum specs: 4GB RAM, Vulkan 1.1, 8GB storage, 1280×720.
Target: 8GB RAM, GTX 1060+, 16GB storage, 1920×1080.

---

# APPENDIX B — PRECEDENT ATTRIBUTION

Prior audit identified precedent errors in v4's Part 23. Corrections:

| Subject | v4 Precedent | v4.1 Corrected |
|---|---|---|
| Thread sight / altered perception | Control | **Outer Wilds / The Stanley Parable** (rendering-as-consciousness precedent) |
| Hex combat action declaration | XCOM 2 | **XCOM 2 for declaration pattern; Battle Brothers for hex mechanics** (XCOM uses squares) |
| Officer-to-leader emergence | ROTK | **CK3 + Mount & Blade (distinct precedents)** (ROTK is 4X, different model) |
| Seasonal settlement growth | M&B + Manor Lords grouped | **Manor Lords distinct; Mount & Blade cited separately for renown mechanic** |
| Into the Breach | NOT CITED | **Added for Phase 3 Cascade animated-state-change pattern** |
| Kingdom Come: Deliverance | NOT CITED | **Added for dialogue-as-investigation (Cuman interrogation, Epilogue trial)** |

Full precedent table with 19 games (v4's 17 + ITB + KCD) available in v4 Part 23 structure. Maintained elsewhere for design-historical reference; moved to appendix per audit E-01.

---

# APPENDIX C — TYPOGRAPHY AND VISUAL SPECIFICATION

*New in v4.1. Consolidates all typography decisions per prior audit L-03.*

## C.1 Type families by context

| Context | Type family | Era | Rationale |
|---|---|---|---|
| Body text, general UI | A warm serif reading face | n/a (functional) | Crimson Text / EB Garamond acceptable. No geometric sans-serifs. |
| Cutscene dialog | Bastard secretary / late-medieval chancery cursive | 14th c. | Period-faithful but legible. |
| Codex headers | Blackletter (textura or fraktur) | 12th–14th c. | Manuscript heading tradition. |
| Illuminated initials (Codex, certain Church UI) | Period-illuminated capitals | 12th–14th c. | Church-adjacent monastic register. |
| Thread operations panel | Hermetic / geometric cipher typography | n/a (esoteric) | NOT illuminated manuscript. Thread is opposed to Church. |

## C.2 Faction typography

Applied to hand panel cards (§11.1), settlement governance UI, Parliament/Tribunal chamber signage.

| Faction | Type tradition |
|---|---|
| Crown | Carolingian miniscule / royal chancery blackletter |
| Church of Solmund | Uncial or Carolingian with illumination |
| Hafenmark | Gothic cursive (mercantile document tradition) |
| Varfell | Insular miniscule (Celtic-register) |
| Löwenritter | Heraldic / shield-iconography |
| Restoration Movement | Deliberately archaic/reconstructed uncial |
| Guilds | Ledger hands / counting-house cursive |
| Niflhel | No public typography (covert) |
| Wardens | Runic-adjacent or abstract |

## C.3 Portrait art direction

Pre-Gothic figure drawing. 12th–14th century illumination. Simpler figures, iconographic rather than naturalistic. Hand gestures encoding speech and rank. Clothing encoding position per period sumptuary conventions.

**Corrected from v4's "Pentiment-style":** Pentiment is 16th century. Valoria is earlier. The pre-Gothic register means simpler, flatter figures with more symbolic than naturalistic treatment.

## C.4 Map rendering

Hand-illustrated ink-and-wash on parchment. Portolan-inspired coastlines. Manuscript-illumination cartography for territorial divisions. NOT Triangle Strategy aesthetic.

## C.5 Color palette (corrected per §3.2.1)

| Faction | Hex (indicative) | Source |
|---|---|---|
| Crown | #2d4a3e forest green | Royal greenwood |
| Church | #3b2a4d deep purple + #1a1018 sable | Liturgical purple, institutional sable |
| Hafenmark | #7a5e2e amber | Mercantile gold |
| Varfell | #4a4f5a slate | Highland stone |
| Löwenritter | #5a2d2d oxblood | Martial blood-iron |
| RM | #2e4a6e woad-blue | Period blue dye |
| Guilds | #8a6a3e ochre | Counting-house |
| Wardens | #c8c4b8 ash-bone | Southernmost |
| Uncontrolled | #6a6863 neutral grey | |

---

# APPENDIX D — MUSIC AND AUDIO SPECIFICATION

*New in v4.1. Per setting finding SET-1 and prior audit I-03.*

## D.1 Register

**Period ensemble, early-music practice.** NOT modern orchestra.

## D.2 Instrumentation palette

**Strings:** lute, vielle, rebec, hurdy-gurdy, psaltery, harp.
**Winds:** recorder family (soprano/alto/tenor), shawm, sackbut (rare), bagpipes (Varfell/highland scenes).
**Percussion:** tabor, nakers, hand-drum; occasional church bell.
**Voice:** chant (plainsong for Church scenes); secular polyphony for court scenes.

**Explicitly NOT USED:** violin family, full brass section, timpani, romantic-period orchestral textures, modern drum kit, synthesizers (except rare sub-audible elements in §13.7.3 Threadwork-radical drone).

## D.3 Forms

- **Estampie:** dance-like, rhythmic — used for Hafenmark court scenes and lighter moments
- **Chanson:** song form with vocal — used for Crown scenes, character-themes for named NPCs
- **Organum / motet:** polyphonic church — used for Church scenes, Tribunal, Cathedral settlements
- **Consort music:** instrumental ensemble — used for general play music, Parliament (secular)
- **Drone-based:** sustained underlayer — used for Varfell forest scenes, Askeheim, Threadwork-radical layer

## D.4 Leitmotif structure

8 faction themes. 12 NPC leitmotifs for major named NPCs. Themes use period instrumentation and form; e.g., Crown theme is a stately chanson motif on lute + vielle + tenor recorder, with a counter-voice in chant for royal/ceremonial scenes.

Motif combination during cutscenes: layered polyphonically (per period consort practice), not orchestrated. Three-voice counterpoint maximum — period-faithful, distinguishable.

## D.5 Threadwork audio

Layered drones. Hurdy-gurdy as primary drone instrument (period-appropriate drone producer). Psaltery high-partial overtones for Thread sight. Sub-audible 40Hz layer for Leap transition — the one permitted modern/synth element, because the Thread itself is mechanically outside the setting's music register.

Operation-specific drone variations per prior audit:
- Weaving: rising pitch
- Pulling: descending glissando
- Mending: sustained tonic
- Locking: sustained, heavy, rigid
- Dissolution: descending with decay
- Past-Oriented Pull: chronological fragments layered (hurdy-gurdy ostinato with phase shift)

## D.6 Cutscene audio

Music swells at key moments. Dialog in voiced narration where possible (cutscene-quality production); otherwise silent-film-style text with period-ensemble underscore. Final lines carry full musical resolution.

---

# APPENDIX E — GODOT IMPLEMENTATION REFERENCE

[Content from v4 Part 24 carries forward with corrections:]

- Engine: Godot 4.2+ (Vulkan)
- GDScript core + C# for performance-critical
- Scene tree structure: Main → GameState (singleton), SignalBus (singleton), ChromeRoot, LayerStack, DiceEngine, RNGManager, AudioDirector, SaveManager, EventLog
- Signal bus: 50+ typed signals including capability-gating signals (`ts_threshold_crossed`, `stature_changed`, `faction_alignment_changed`) that drive chrome mount/unmount
- Core resources: Attribute, Character, Conviction, StanceTriangle, Faction, Territory, Settlement, Investigation, SlateEntry, CutsceneRef
- Dice engine: seeded PCG RNG, standard d10 pool
- State machine: deterministic FSM with legal transitions; cutscene queue per §1.4
- Asset manifest outline (not exhaustive; proper asset pipeline doc lives in valoria-game repo):
  - 17 territory illustrations
  - 36 settlement vignettes
  - ~40 NPC portraits (pre-Gothic era, 3 expression states each)
  - 72+ card arts (faction-typographed)
  - 40+ cutscene backgrounds (including 5–8 seasonal atmospheric)
  - ~120 UI icons
  - Peninsula map shaders × 5 RS bands
  - Period music: 8 faction themes + 12 NPC leitmotifs + Threadwork drone variants + UI cues (~40)
- Save system: phase-boundary only; version-headered binary; backward-migratable
- Deterministic RNG: single seed per campaign

---

**END OF v4.1 REFERENCE DOCUMENT**

*Audit coverage: 19 v30 canonical design documents + ED-548 + all canon P-01 through P-15 compliance checks.*
*Resolutions: UI-01 through UI-15 + ED-544 + ED-545 + ED-548 + C-1, C-2, C-3 + P-03/P-04/P-06/P-08/P-09/P-10/P-11/P-12/P-13/P-15 + SET-1 through SET-7.*
*Structure: 14 parts + 5 appendices (was 25 parts in v4).*
*Status: CANONICAL; approved for Godot development reference.*
*Known gaps for v4.2+: A-01 through A-04 accessibility depth, L-03/L-04 minor legibility, R-01/R-02/R-03 robustness enhancements, precedent table full audit.*
