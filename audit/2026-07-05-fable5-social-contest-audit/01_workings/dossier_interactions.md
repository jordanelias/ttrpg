# Dossier — Interactions Evidence: Domain Echoes · Narrative Emergence · Prose (Agent C, sonnet tier)
## Status: WORKING EVIDENCE — no verdicts; judgment reserved to the orchestrator
## Date: 2026-07-05

---

## Part 1 — Domain echo transport

### 1.1 `designs/architecture/scale_transitions_v30.md §5` full contest-relevant provisions

**§5.1 Trigger + PP-329 cap** (`scale_transitions_v30.md:176-177`):
> "A personal scene qualifies for Domain Echo when it meets Sufficient Scope (§7). One Domain Echo maximum per scene per faction (PP-329)."

**§5.2 Amounts by degree** (`scale_transitions_v30.md:179-187`):
> | Degree | Effect |
> |--------|--------|
> | Overwhelming | ±2 to most relevant faction stat |
> | Success | ±1 to most relevant faction stat |
> | Partial | Narrative only — no faction stat change |
> | Failure | −1 to acting faction's own stat |
>
> "Cap: ±2 per stat per Echo. (ED-071 resolved by PP-329: one Echo/scene/faction prevents compounding)"

**§5.3 Timing (immediate vs seasonal Accounting, PP-109)** (`scale_transitions_v30.md:189-192`):
> "**Full TTRPG (Register Shift):** Domain Echo fires immediately at scene end. No extra roll.
>
> This timing difference is intentional (PP-109): Zoom In is a personal intervention in a strategic situation. Faction consequences propagate through seasonal accounting to prevent real-time manipulation of BG stats from personal scenes."
(Note: the skeleton's second Timing-by-Mode row — the Hybrid/Zoom-In case this "difference" contrasts against — is present only in the infill, §1.3 below; the skeleton head itself states only the Full-TTRPG case.)

**§5.4 Debate → Domain Echo (PP-108)** (`scale_transitions_v30.md:194-199`):
> | Piety Track outcome | Domain Echo |
> |--------------------------|-------------|
> | Track ≥ 7 (winner's side) | Winner faction: +1 Mandate. Loser faction: −1 Mandate if they held institutional authority. |
> | Track 4–6 (compromise) | No Domain Echo. Scene-level consequence only. |
> | Track ≤ 3 (loser's side) | Reversed — loser faction receives penalty. |

**§5.6 Thread Domain Echo (ED-673)** (`scale_transitions_v30.md:218-233`):
> "Thread events produce Domain Echo to faction stats when they meet Thread Significance — distinct from Sufficient Scope (§7).
>
> **Fires when:** (a) Thread operation produces RS change ≥ 1, OR (b) Thread operation witnessed by NPC whose Conviction Scar fires (conviction_track_v1.md §3, formerly npc_behavior_v30 §3.4), OR (c) Thread operation creates/destroys Gap, Lock, or Knot at Territorial+ scale."
>
> | Thread Event | Affected Stat | Direction |
> |---|---|---|
> | Dissolution Success | Controlling faction Stability | −1 |
> | Mending Success (Territorial+) | Controlling faction Mandate | +1 |
> | Gap creation | Controlling faction Stability | −1 |
> | Lock creation (unauthorized) | Controlling faction Mandate | −1 |
> | Public Thread op, Church territory | Church Mandate | −1 |
> | Public Thread op, Varfell territory (VTM ≥ 3) | Varfell Mandate | +1 |
>
> "**Timing:** Queued to Accounting. **Cap:** 1 Thread Domain Echo per scene per faction (PP-329). ... Thread Domain Echo and Accord Domain Echo (§5.5) may both fire from same scene on different stats."

### 1.2 `designs/scene/social_contest_v30.md §6` POST-CONTEST + §6.1/§6.3

**§6 Domain Echo table** (`social_contest_v30.md:287-290`):
> "**Domain Echo:**
> - Decisive win + Memory genre: winning faction's Mandate +1 in the domain of the cited precedent.
> - Decisive win + Projection genre: +1D on first Domain Action pursuing the argued outcome within the season.
> - Compromise: no Domain Echo."

Preceding Thread co-movement table (`social_contest_v30.md:279-284`) is genre-keyed the same way: Memory → "Mending Stability (MS) +1"; Projection → "+1D on the first Domain Action pursuing that outcome within the season. MS +1 if the projection involves Thread-sensitive matters."

**§6.1 Obligations, second transport channel** (`social_contest_v30.md:296-311`):
> "**GM advisory — Obligation tracking (ED-619):** GMs are advised to cap active Obligations at 3 simultaneously across all parties for tracking tractability. ... The system allows any number of concurrent Obligations; the cap is a GM guidance note, not a mechanical limit.
>
> A Decisive win (Persuasion Track ≥ 7 or ≤ 3) in a Formal or Grand Contest produces a binding **Obligation** — a mechanical commitment that persists across seasons. ... **Obligation structure:** The winning side names one specific commitment that the losing side must honor."

Table by contest type (Formal/Grand/Royal/Church Tribunal) gives Obligation Duration + Violation Consequence (e.g. Grand Contest: "Violating faction: Mandate −2. Stability −1. Faction's next DA targeting the violated party faces +2 Ob").

Wager Obligation extension (`social_contest_v30.md:313`): "Wager Obligations are valid only in Grand Contests using Projection genre + Consequence Resonant Style" — a third, narrower echo path layered on Obligations.

**§6.3 Chain Contests** (`social_contest_v30.md:354-369`):
> "When a contest ends in Compromise (Persuasion Track 4–6), the tension is deferred, not resolved. The unresolved contest generates a Scene Slate entry for the following season per player_agency_v30 §4.2 (Priority 1 — the unresolved political tension is a crisis event).
>
> **Chain contest rules:**
> - The follow-up contest starts at the Persuasion Track's final position from the previous contest (not reset to 5)...
> - A chain contest's Decisive win produces an Obligation (§6.1) as normal. A second Compromise extends the chain..."
> "Maximum chain length: 3 contests. After 3 consecutive Compromises, the tension resolves as a permanent stalemate: both parties establish a cold equilibrium."

### 1.3 Reconciliation evidence — §5.4 (Piety-band → Mandate) vs §6 (genre-keyed → Mandate/domain-action): same echo or two?

Side by side:

| Source | Keying scheme | Effect |
|---|---|---|
| `scale_transitions_v30.md §5.4` (line 194-199) | **Track band** (≥7 / 4-6 / ≤3), labelled "Piety Track outcome" | Winner +1 Mandate / loser −1 Mandate if institutional authority; band 4-6 → none; ≤3 reversed |
| `social_contest_v30.md §6` (line 287-290) | **Genre won** (Memory / Projection) × decisive-or-not | Memory decisive win → Mandate +1 "in the domain of the cited precedent"; Projection decisive win → +1D first Domain Action; Compromise → none |

Both schemes agree that Compromise (Track 4-6) never produces a Domain Echo, and both are keyed off a Decisive-or-better outcome — but §5.4's table has no genre axis (its Mandate/penalty applies regardless of Memory vs Projection) while §6's table has no track-magnitude axis beyond "decisive" (its Mandate/domain-action split turns entirely on which genre was won, not how decisively). §5.4 also specifies a **loser-side penalty** ("Loser faction: −1 Mandate if they held institutional authority") that §6 does not carry at all — §6's Compromise/decisive split is binary (Mandate+1 or +1D or nothing), with no loser-stat-penalty row.

**"Piety Track" terminology reconciliation:** `scale_transitions_v30.md §5.4`'s table header and both `npc_behavior_v30.md` (`:394` "A Contest produces decisive outcome (Piety Track ≥ 7 or ≤ 3)") and the `tests/emergent_arc_skeleton_test_*` prose corpus (`batch2.md:23,124` "Grand Contest victory (Piety Track ≥ 7)") use "Piety Track" for what `social_contest_v30.md` itself calls "Persuasion Track" throughout (§2 Step 4, §6, §7, etc. — "Piety Track" does not appear in `social_contest_v30.md` at all; confirmed by grep). `references/glossary.md:84` resolves this explicitly:
> "| Piety Track | CT* | 0–10 | Debate position tracker. Side A wins at ≥ 7; Side B wins at ≤ 3. Compromise zone: 4–6. Canonical doc: `designs/personal/conviction_track_v1.md` (promoted PP-681). |"

— i.e. the glossary treats "Piety Track" as the corpus-wide name for the same 0-10 debate tracker `social_contest_v30.md` calls "Persuasion Track" (identical bands: ≥7/4-6/≤3), while also citing a different canonical doc (`conviction_track_v1.md`) for it than `social_contest_v30.md`. `references/glossary.md:23` separately notes CI/CT vocabulary confusion history ("CI is no longer used — historically ambiguous between Church Influence... and Piety Track (CT)"). No file found that resolves whether §5.4's "Piety Track" is (a) a straight synonym-drift for Persuasion Track, (b) a distinct religious-devotion tracker that happens to share the same 0-10/≥7/4-6/≤3 banding by coincidence, or (c) an editorial residue of an earlier unmerged draft. `params/scale_transitions.md:44,73` repeats the same "Piety Track ≥7... [PP-108]" phrasing as the `scale_transitions_v30.md` skeleton, i.e. the terminology is consistent across that lineage, just not aligned to `social_contest_v30.md`'s own vocabulary.

Grep performed: `PP-108` across `designs/` (5 files: this audit's own grounding doc, `2026-05-28-resolution-diagnostic/intensified_pipeline_all_directions.md`, `scale_transitions_v30_index.md`, `_infill.md`, `.md`) — `PP-108` never appears inside `social_contest_v30.md`. Grep for "Piety Track" across `designs/` returned 80 files; none is `social_contest_v30.md`.

### 1.4 Code side

`sim/personal/contest/faction.py:1-5` (module docstring):
> "faction.py — ADAPTER (not canon). Models the canonical Parliamentary action (faction_layer §5) on the contest engine, to exercise the engine in the faction-action context. The faction layer keeps its own ratified resolution (§5.5 Rebuttal roll, §5.3 Mandate-weighted vote, §5.4 thresholds); this maps that SHAPE onto the engine..."

What it actually transports: `Faction.mandate` is used purely as **vote weight** (input) in `_one_vote`/`vote`/`coalition_vote` — the functions return `(passed, share)` or a `'pass'/'committee'/'fail'` string; no function in `faction.py` writes back to a Mandate/Stability/any faction stat. It computes whether a motion passes, not a Domain Echo.

`sim/personal/contest/wrapper.py:187-215` (GAMES router):
> "# ─── GAMES ROUTER TABLE ───────────────────────────────────────────────────────────────────────────
> # game -> {resolve, status, source}. status: WIRED | STUB. Only 'agon' is WIRED this stage (the
> # canonical Persuasion-Track path). The other three games are registered STUB rows for later stages
> # (Stage 4 Consensus is largely promote-existing per faction.py; Negotiation/Inquiry author-new)."
>
> `GAMES = {"agon": {..., "status": "WIRED", "source": "social_contest_v30 §2-§6 (Persuasion Track)..."}, "consensus": {"resolve": _stub("consensus"), "status": "STUB", "source": "social_contest_v30 §10 BG-Vote / §7.2 (largely in faction.py — Stage 4)"}, "negotiation": {...STUB...}, "inquiry": {...STUB...}}`

Cross-scale domain-echo emission — `sim/cross_scale/domain_echo.py` exists (`compute_domain_echo`, `compute_accord_echo`, `compute_thread_echo`, docstring: "Step 10.1 from Phase 7 follow-on... This Tier 0 lands the §5 protocol; **consumers wire in**.") and correctly encodes §5.2's amount table, §5.5, and §5.6. But tracing its actual consumer, `sim/cross_scale/scene_dispatch.py:16-32` states the boundary explicitly:
> "OUTCOME->ECHO MAPPING GAP: resolved-scene outcomes are passed to zoom_out, but the resolver-result -> accord/faction-stat echo mapping is resolver/canon-specific and is left empty (flagged) rather than fabricated. Consequence (intended): the scene phase is SIDE-EFFECT-FREE on strategic state, so wiring it in cannot regress the strategic loop."

And concretely, `scene_dispatch.py:100-117` (`_resolve_slot`): for `st == "contest"`, it calls `cr = contest.run_contest(parts, ctx.get("stakes", {}), world=world, rng=rng)` (line 106) and stores `cr` in `out["result"]`, but the immediately-following feedback call is `zo = zoom_in_out.zoom_out({}, world)` (line 116) — an **empty dict** literal, not `cr` or any derivative of it. `zoom_in_out.zoom_out()` (`sim/cross_scale/zoom_in_out.py:99-138`) only produces non-empty `domain_echoes_queued` when its `scene_outcomes` argument supplies `'accord_changes'` / `'other_echoes'` keys — which `scene_dispatch.py` never populates from a contest result. So `compute_domain_echo`/the §5 Debate table/§6 genre table are not reached from the one live scene-dispatch path found for `scene_type == "contest"`; `domain_echo.py`'s `compute_domain_echo` itself is never imported by anything in `sim/cross_scale/` or `sim/personal/contest/` (grep found only its own definition and the docstring cross-references).

**Board-game path (§10 Parliamentary Vote):** `sim/personal/parliamentary_vote.py` implements §10 including the Total Victory Mandate penalty, and this one **does** write to faction state:
> `sim/personal/parliamentary_vote.py:194-206`: "if track >= PERSUASION_TOTAL_VICTORY or track <= PERSUASION_TOTAL_DEFEAT: ... dominant = max(losing_names, key=lambda n: world.factions[n].L) ... world.factions[dominant].adjust("L", BG_VOTE_TOTAL_VICTORY_MANDATE_DELTA * MULTS["L"]) ..." — comment: "§10 Total Victory: '{dominant}' (losing dominant) takes Mandate -1 [one-season penalty; temporary-modifier restoration deferred to season_manager]"

`social_contest_v30.md:596` states plainly: "Thread consequences do not fire from BG Parliamentary Vote (personal-scale argument required)." — matching that `run_parliamentary_vote` has no Thread-echo call.

`run_parliamentary_vote` is called by `sim/personal/parliamentary_stay.py:85` and `sim/provincial/parliamentary_transfer.py:151`; grep of `sim/mc_v18.py` for `parliamentary_stay|parliamentary_transfer|parliamentary_vote` returned no matches — the campaign-loop entry point does not appear to call any of the three.

### 1.5 PR #77 dossier edges (`designs/audit/2026-07-04-ners-qualitative-audit/01_workings/dossiers/dossier_social_contest.json`)

Full `edges` array:
```json
[
  {"dir": "in", "other": "npc_behavior (Resonant Style +1D targeting)", "mechanism": "categorical Style-vs-Conviction match, opponent-aimed", "status": "implemented", "cite": "npc_behavior_v30.md §1.3/§6.3; armature.py contrast"},
  {"dir": "out", "other": "npc_behavior 2-cycle", "mechanism": "scene.contest_resolved/state.opinion_revised", "status": "divergent", "cite": "grounding doc 02(a)6 - npc_behavior-side dampers unconfirmed [OPEN-Jordan]"},
  {"dir": "out", "other": "faction (Domain Echo, Mandate)", "mechanism": "Memory/Projection decisive-win Mandate+1 or Domain-Action bonus", "status": "declared-only", "cite": "social_contest_v30.md §6; wrapper.py notes faction.py is Stage-4 scope"},
  {"dir": "out", "other": "threadwork (MS/RS co-movement)", "mechanism": "§6 Thread co-movement table, §9.3/9.4/9.4b junctures", "status": "divergent", "cite": "present in design doc; zero hooks in sim/personal/contest/"},
  {"dir": "in", "other": "fieldwork (Evidence Track Findings)", "mechanism": "+1D per cited Finding, cap +2D, contest prep", "status": "declared-only", "cite": "social_contest_v30.md §9.1; no fieldwork import in sim package"},
  {"dir": "out", "other": "faction_politics/domain_actions", "mechanism": "Obligation blocks NPC actions that would violate it", "status": "declared-only", "cite": "social_contest_v30.md §6.1; faction_politics doc:null per module_contracts"}
]
```

---

## Part 2 — Narrative emergence feed

### 2.1 `skills/valoria-arc-generator/SKILL.md`

Emergence discipline line (`SKILL.md:74`):
> "**Emergence standard:** Each arc must satisfy: *no single player decision caused this; it required multiple independent systems running simultaneously.* If a single player choice is sufficient to explain the arc, it is a plot hook, not an emergent arc."

Directive to read `params/contest.md` (`SKILL.md:53-54`):
> "**Read if arcs involve social/debate:**
> - `params/contest.md`"

### 2.2 T-24 convergence markers — `references/arcs/arc_register_events.md §VI`

Section-header concession (`arc_register_events.md:25`):
> "Non-obvious intersections where simultaneous vectors produce pressure qualitatively different from either alone. Not named for dramatic effect — named because the combined pressure is not predictable from the constituent vectors without the marker."

The 8 markers listed (`arc_register_events.md:29-60`) and their trigger text:

| Marker | Trigger (quoted) | Contest-fed? |
|---|---|---|
| COLLISION A — Church Double Fracture | "Klapp conversion (ARC-S21) coincides with Olafsson exposure (ARC-S06 investigation)." | No (conversion + investigation exposure) |
| COLLISION B — Practitioner King | "Almud Discovery Event (ARC-S17: TS 28→30) + Elske installed independently (ARC-S23) + Torben in Altonia (ARC-S07)." | No |
| COLLISION C — Tutoring + Southernmost | "Torben Loyalty ≤ 3 (ARC-S07) coincides with Southernmost Ritual [UNNAMED — ED-416] failure (ARC-T04)." | No |
| COLLISION D — Niflhel Weaponises | "Full Church-Niflhel exposure + 218 AG assassination perpetrator identified as Niflhel + Varfell Private Collection in Niflhel's hands." | No |
| COLLISION E — Einhir Elder and Baralta's Claim | "Witness institutional testimony (ARC-T23...) + Baralta Solmund claim (ARC-S19) + Klapp archive access." | **Payload yes**: combined effect includes "Grand Debate (5 exchanges). If reinterpretation fails: Inspiration loss, Destabilisation Trigger fires fully..." — a contest is the resolution mechanism of the collision, not its trigger. |
| COLLISION F — Succession Triangle | "Almqvist deed-presumption weakens... while both Lenneth and Baralta programmes are active." | Indirectly: text notes "three-way succession contest" (Succession Contest is a Grand-Contest variant per §7.2), but the marker's own trigger clause names deed-presumption/programme conditions, not a contest outcome. |
| COLLISION G — Einhir Triangle | "Lenneth revival programme + Baralta's suppression + Vaynard's revolutionary restoration all active simultaneously." | No |
| COLLISION J — Church Siege of the Southern Gates | "Church controls T9 + T2 (TE-28 active) + TC ≥ 60 (Seizure active) + RS ≤ 39 (Fractured)." | No |

PR #77 F-2 (`designs/audit/2026-07-04-ners-qualitative-audit/ners_qualitative_audit_v1.md:136-146`):
> "**F-2 · The 'emergent narrative engine' has no engine** `[N/Ω-a · P2 · top-down · UNDETERMINED]`
> The corpus's flagship emergence mechanism — 8 Convergence Markers, canonically 'the game's emergent narrative engine' (`references/throughlines_complete.md` T-24 L200) — exists only as hand-authored trigger+payload annotations in `references/arcs/arc_register_events.md §VI`, whose own header concedes the combined pressure 'is not predictable from the constituent vectors.' No Key type, module contract, sim module, or resolver detects trigger-coincidence or applies the combined payload; T-24 is the only throughline with no Implementation-status line."

### 2.3 `tests/emergent_arc_skeleton_test_*` prose corpus (design intent, NOT contract)

**batch2, NEW-S23 (`emergent_arc_skeleton_test_2026-04-17_batch2.md:12-17`):** SETTLEMENT-TARGETED OBLIGATION — NPC PRIORITY TREE BLOCK:
> "Root: Grand Contest Obligation (§6.1 social_contest_v30): tracked as clock, 4 seasons or until condition ... NPC priority tree: any action violating the Obligation is BLOCKED while Stability ≥ 3"

**batch2, NEW-S24 (`emergent_arc_skeleton_test_2026-04-17_batch2.md:82-135`):** OBLIGATION CLOCK × CHAIN CONTEST CASCADE, the "install Obligations (clean)" escalation incentive:
> "**New emergence:** Chain Contests create a Priority 1 Scene Slate debt that compounds faster than it can be paid down if the player runs multiple concurrent social actions. The optimal strategy is deliberate escalation to Grand Contest resolution precisely to install Obligations (which are clean) and prevent Chain Contest accumulation (which is noisy)." (line 135)

**batch2, Category L (`emergent_arc_skeleton_test_2026-04-17_batch2.md:524,531`):** THREAD IN CONTEST × HERESY EVIDENCE:
> "## CATEGORY L: THREAD IN CONTEST × HERESY EVIDENCE" ... "Root: §9.3 social_contest_v30: Practitioner TS ≥ 30 in active Thread contact adds floor(TS÷30)D in contests"

**batch3_with_audit, Friction Point 2 (`emergent_arc_skeleton_test_2026-04-17_batch3_with_audit.md:1136-1137`):** Dialogue Lattice → Social Contest handoff:
> "**Friction Point 2 — Dialogue Lattice → Social Contest handoff:** The Lattice session's Style choices (Revealing/Obscuring × Memory/Projection) are not specified to carry into the Contest that follows (NEW-OI-20). When a Lattice session escalates to Contest, the genre is re-established at GM Setup (Step 2). This creates discontinuity..."

**batch2, NEW-OI-20 (`emergent_arc_skeleton_test_2026-04-17_batch2.md:1245`):**
> "| NEW-OI-20 | Style bonus fix (social_contest_v30 Step 3) + Dialogue Lattice handoff: when Lattice session escalates to Contest, does the Lattice session's utterance style... inform the Contest's primary genre?... | P3 |"

**batch4, Category AH (`emergent_arc_skeleton_test_2026-04-17_batch4.md:544,568,587-589`):** NPC-INITIATED DEMAND × DEFLECTION MECHANICS — Heresy Tribunal via contest:
> "## CATEGORY AH: NPC-INITIATED DEMAND × DEFLECTION MECHANICS" ... "A) Comply (no roll): accept the tribunal → Church Investigation proceeds → Heresy Investigation resolved via social contest (formal contest, Church Tribunal adjudicator → Cognition-primary)" ... "→ Tribunal convenes: Grand Debate 5 exchanges, Church Tribunal adjudicator (Cognition-primary, Church +1D) ... → Failing the Tribunal: Heresy confirmed → Excommunication eligible"

### 2.4 Code-side narrative surface — `sim/personal/contest/narrative.py`

Chronicle/`classify()` outcome taxonomy (`narrative.py:25`):
> `SHAPES = ("ROUT", "CLEAR_WIN", "NAIL_BITER", "REVERSAL", "COLLAPSE", "DEADLOCK", "SPLIT_DECISION")`

`venue_brief()` (`narrative.py:157-170`) produces a public pre-contest cue string, e.g. `"rewards {la}; favours {lt}-ground argument; opens on {venue.start_ground}; fatal: {...}"`.

Consumers: grepping the repo for `narrative.summarize|classify|venue_brief|Chronicle` (excluding `narrative.py`'s own definitions) found only `sim/personal/contest/_kernel_tests.py` (the module's own test suite, e.g. `_kernel_tests.py:257,260,269,274-275,284,291,297,342,346-347,354,378,450`). No campaign-loop, scene-dispatch, or arc-generation consumer imports `narrative.py`'s output. `sim/personal/contest/__init__.py:98,120` exports `narrative` as part of the package's public surface but nothing outside the package consumes it.

A separate, differently-scoped "Chronicle" concept exists in `sim/cross_scale/articulation.py` (`generate_chronicle_entry(event, world)`), but that whole module is an unimplemented stub:
> `sim/cross_scale/articulation.py:5,20,31-32`: `Status: [PROVISIONAL — Pass 2l armature stub 2026-05-17]` ... `# [PROVISIONAL — Pass 2l armature stub; implementation pending against canonical source]` ... `def generate_chronicle_entry(event, world: GameState): raise NotImplementedError("sim/cross_scale/articulation.py — Pass 2l armature stub")`

So no structured outcome record from the contest kernel is confirmed to reach any arc-generation surface in the working tree; `narrative.py`'s `Chronicle` is the only structured per-bout record the kernel produces, and its only confirmed reader is its own test file.

---

## Part 3 — Prose surface

### 3.1 `skills/prose-writer/SKILL.md`

**The Ratchet Principle** (`SKILL.md:205`, in full):
> "**The Ratchet Principle (political/faction content).** Political dynamics always escalate. Principals advance into positions they cannot retreat from. Each encounter tightens constraints that cannot be loosened. Resolution does not come from the principals de-escalating — it comes from an external force or a marginal actor that none of the principals were watching. The detonation is in the margins: the delegate who was flipped, the subordinate who recalculated, the intelligence operative who carried the folio. Scenes between political principals should end with all parties having advanced and the space between them narrower than it was. Never write political resolution as mutual accommodation. The accommodation is the next ratchet click."

**Focalization discipline** (`SKILL.md:139-151`):
> "## The Master Principle: Focalization
>
> Every passage is filtered through a perspective. There is no neutral omniscient voice. What looks neutral is a chronicler-voice with attitudes, and that chronicler is itself a perspective.
>
> Before writing, name the focalization:
> - A specific character (their attitudes, education, vocabulary, blind spots)
> - A community (the village's collective view, the faction's institutional voice)
> - A chronicler (a later historian with their own framing)
> - A retrospective self (the narrator looking back, knowing more than the experiencing self knew)
>
> The focalization determines what the prose can say. Editorial words ('sinister,' 'noble,' 'wretched') are licensed when they belong to a focalized perspective. They are not banned. They are owned.
>
> **Chronicle-mode prose has a canonical constraint.** Per P-03, no omniscient narrator is canonically possible for in-world chronicles. All chronicle-mode prose must be focalized through one of the four named chroniclers: Church Chronicler (Certainty 5, TS 0), Hafenmark Chronicler (Certainty 4, TS 0), Restoration Chronicler (Certainty 2, TS 0), Warden Chronicler (Certainty 0, TS 70+)."

**"Mechanical reality underneath"** (`SKILL.md:201`):
> "Mechanical reality underneath. Prose can gesture at systems without exposing numbers."

**PC framing** (`SKILL.md:153-160`):
> "## Player-Character Framing
>
> The player-character is observed, not inhabited. All prose involving the player-character (PC) uses third-person — the PC is referred to by name or pronoun. Second-person ('you ride into the village') is not used in prose.
>
> - **Narrative prose is third-person on the PC.** 'Vael walked the lane' not 'you walk the lane.'
> - **Choice-hooks remain player-facing.** Options offered to the player are imperatives ('Approach the parish house') or third-person action descriptions.
> - **Direct speech is unchanged.** Characters speaking to the PC use second-person ('Tell me what you saw').
> - **The player's vantage is genuinely omniscient.** The player sits outside the narrative, watching it happen."

**Solmund-voice override** (`SKILL.md:207-217`):
> "### Solmund Voice Canon (Scoped Override)
>
> For **in-world ecclesiastical artifacts** — Solmund manuscripts, cathedral inscriptions, liturgical text, doctrinal treatises, creeds — and for **Solmund clergy speaking ecclesiastically** (sermons, formal pronouncements, theological discourse), the prose-writer skill's twelve-author synthesis does **not** apply. Use the Solmund voice canon at `designs/world/solmund_voice_v30.md`.
>
> The prose-writer skill **continues to apply** for:
> - All narration *about* Solmund clergy, manuscripts, or ceremonies
> - Codex entries describing Solmund institutions
> - A bishop's private interior monologue, casual speech, or non-ecclesiastical action
> - Any focalization through a Solmund character that is not formal religious discourse"

### 3.2 Tension evidence (facts only)

**(a) Ratchet Principle vs Compromise / TIE handling:**

Ratchet Principle (`SKILL.md:205`, quoted in full above) — "Never write political resolution as mutual accommodation. The accommodation is the next ratchet click."

`social_contest_v30.md` Compromise outcome (`:276`):
> "Persuasion Track ≥ 7 = Side A wins; ≤ 3 = Side B wins; 4–6 = compromise (GM narrates partial outcome proportional to final position)."

And `§6` Domain Echo table (`:290`): "Compromise: no Domain Echo." Also `§6.3` (`:354-356`): "When a contest ends in Compromise (Persuasion Track 4–6), the tension is deferred, not resolved. The unresolved contest generates a Scene Slate entry for the following season..." — i.e. the mechanical spec itself frames Compromise as deferral/tension-carry-forward (chain contest), not settlement.

TIE handling (`social_contest_v30.md §4 Step 4`, `:204-207`):
> "**TIE** (equal successes, any interaction type):
> - Both orators take 1 strain. **Exception (PP-236): if the interaction type is CROSS, no strain is dealt**...
> - Persuasion Track moves +1 toward first-to-speak holder's position.
> - First to speak stays with holder."

**(b) Numbers-hidden prose doctrine vs player-interaction-walkthrough §0:**

Prose doctrine (`SKILL.md:201`, quoted above): "Prose can gesture at systems without exposing numbers."

`designs/audit/2026-07-01-contest-player-interaction/player_interaction_walkthrough_v1.md:19-24` (§0, DRAFT):
> "**Every number the resolver uses to decide the outcome is a number the player can see before they commit to a choice that depends on it.** This is the direct answer to the stated core pain (opacity): not 'hide less,' but 'the hidden-GM-ledger and the player-facing screen are the same data, rendered.' Where the *resolved value* is legitimately hidden (an NPC's exact Conviction vector, an opponent's Face total), the player still gets the *consequence class* (an Appraise hint, a visible debuff icon)..."

### 3.3 Contest-outcome narration guidance — what exists, what does not

Searches performed: grep for `chronicler|narration|narrate` (case-insensitive) in `social_contest_v30.md` — no matches for "chronicler" or "narration"; two matches for "narrat[es]": line 276 (Compromise: "GM narrates partial outcome proportional to final position" — no template given) and line 348 (§6.2, quoted below). Grep for `contest.*chronicler|chronicler.*contest|Appraise.*narrat|narrat.*Appraise` (case-insensitive) across `designs/` returned 4 files, none of which specify contest-outcome prose templates on inspection (`gate0_packet.md` and `reconciliation_map_raw.md` matches are code-scaffold discussions of `narrative.py`'s module history, not in-game narration guidance; the other two are unrelated combat/accounting docs). Grep for `contest|Contest` in `designs/world/narrative_voice_canon_v30.md` — no matches; the voice canon does not mention contests at all.

What exists: `social_contest_v30.md §6.2` (`:348`, Conviction Scar Visibility) gives one exact player-facing narration line:
> "When a player's contest argument produces a Conviction Scar on an NPC... the player receives a narrative signal. The GM states: 'Something shifted in [NPC]'s expression. Your argument reached something they cannot dismiss.' This is not a stat reveal — the player does not learn the Scar count. They learn that their words had structural impact."

What does not exist (per the searches above): no doc found specifying prose templates, chronicler-hooks, or narration guidance for Appraise reveals, armature reveals, CLASH/REINFORCE/CROSS exchange resolution, or Persuasion-Track-band outcomes generally, beyond the two lines in `social_contest_v30.md` itself (the bare "GM narrates" instruction at line 276, and the single template at line 348).

### 3.4 P-03 evidence — does `narrative.py`'s `classify()` attach a perspective?

`narrative.py`'s `Chronicle` dataclass (`narrative.py:39-51`) fields: `winner, why, shape, margin, lead_changes, turning_point, decisive_appeal, decisive_ground, beats, room_leader` — no `focalization`, `chronicler`, `perspective`, or `pov` field of any kind. `classify()` (`narrative.py:83-100`) takes `(winner, why, leads, margin, lead_changes, late_crossing)` — purely numeric/structural inputs, no perspective/observer argument. `Chronicle.render()` (`narrative.py:53-80`) produces strings like `"[REVERSAL] {w} came from behind — overtaking at exchange {self.turning_point}..."` and `"[CLEAR WIN] {w} took it by {pct}, the case resting on {factor}."` — third-person, engine-computed, addressed to no named observer; the module docstring (`narrative.py:2-4`) frames it as "turns a resolved bout into legible, story-shaped output. PURE CONSUMER of the raw beat log... it never touches resolution." The output shape is a neutral computed summary keyed to sides `A`/`B` (via `_name()`, `narrative.py:35-36`), not routed through any of the four canonical chroniclers named in `prose-writer/SKILL.md:151`.

---

## Anomalies noticed in passing

- `scale_transitions_v30.md §5.4`'s table header names "Piety Track," which does not appear anywhere in `social_contest_v30.md` (the doc §5.4 is nominally bridging into) — see §1.3 above. The same "Piety Track" phrasing recurs in `npc_behavior_v30.md`, `params/scale_transitions.md`, `params/factions/npc_stance_triangles.md`, `params/bg/core.md`/`tracks.md` (a *different* Piety Track: "Starting Piety Track (PT) values" for territories, `params/bg/core.md:117`, `params/bg/tracks.md:139` — a per-territory BG stat, not obviously the 0-10 debate tracker), and the `tests/emergent_arc_skeleton_test_*` corpus. Two distinct referents ("Piety Track" as debate-position tracker per the glossary vs "Piety Track (PT)" as a per-territory BG stat per `params/bg/`) share one name; not reconciled in any file found.
- `sim/cross_scale/domain_echo.py` is a complete, individually-correct implementation of scale_transitions §5.1-§5.6 (amount tables, caps, gating) that appears to have no caller anywhere in the sim package outside its own module — a fully-built mechanism with the wiring gap sitting one level up in `scene_dispatch.py` (§1.4 above), rather than in the echo-computation itself.
- `sim/personal/contest/faction.py` (an ADAPTER inside the `contest/` package modeling Parliamentary vote *shape*) and `sim/personal/parliamentary_vote.py` (a separate, sibling-package module that actually implements and wires §10's Mandate penalty) are easy to conflate by name/purpose; they are different modules with different WIRED/adapter status, and only the latter mutates faction state.
- `emergent_arc_skeleton_test_2026-04-17_batch2.md` NEW-S24's title says "Obligation Clock × Chain Contest Cascade," but the worked example (lines 89-132) never actually enters Deadlock or invokes the §6.3 Deadlock/hard-stop rule (resistance drop, 3-Compromise cold-equilibrium cap) — it only exercises the "Compromise → Priority 1 Scene Slate" and "Decisive win → Obligation" halves of §6.3, not the chain-terminator rule itself.
