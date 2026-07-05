# Cluster B dossier — bottom-up transport (verbatim agent output)

_Sonnet evidence agent, 2026-07-05. Headline claims Fable-verified against the working tree —
see `verification_log.md`. Verbatim below._

---

## Bottom-Up Transport Cluster — Playability Audit

**Currency note:** `scale_transitions_v30.md` is not listed as its own row in `CURRENT.md`; it is the Architecture/Key-substrate family's companion doc and is treated as canonical per its own `## Status: CANONICAL` line and citation network (`references/module_contracts.yaml`, `faction_behavior_v30.md` both cite it directly). `designs/ui/valoria_ui_ux_v4.md`/`_v4_1.md` — my only source for player-facing presentation of these edges — is **not current-generation and absent from `CURRENT.md`** (confirmed independently and by `designs/audit/2026-07-04-ners-qualitative-audit/01_workings/lenses/lens_playability_legibility.md`, which found it predates d+σ/combat_engine_v1/the contest rebuild and has no replacement). Every FEEDBACK line below that cites it is flagged accordingly.

### E1 · Personal → Faction (scale_transitions_v30.md §3.2)
1. **MOMENT:** An ordinary personal action (e.g., negotiation) is recognized as also being the faction's Domain Action; one roll resolves both.
2. **DECISION:** Real — the scene choice *is* the faction decision, not layered on top of it.
3. **FEEDBACK:** UI doc describes a pre-roll "Domain Echo projection" and post-roll animation (`valoria_ui_ux_v4_1.md` §11.1, line 961) — but this doc is stale/uncurrent (see note above); no current-generation spec covers this edge at all.
4. **LATENCY:** Immediate — "same roll... no extra roll" (§3.2 verbatim).
5. **FRICTION:** Play.
6. **RECIPROCITY:** One-way, personal→faction.
7. **VERDICT:** PLAYS-WELL mechanically / UNDETERMINED presentation · P2 · DELIBERATE (explicit same-roll framing in canon text).

### E2 · Scene → Faction Domain Echo core (§3.4, §5.1–5.3, §7 Sufficient Scope)
1. **MOMENT:** A qualifying scene (any of 7 §7 conditions) ends; a Domain Echo (§5.2 degree table) applies to a faction stat.
2. **DECISION:** Mixed — combat-vs-officer (bullet 5) and Disposition-reach (bullet 6) can be deliberately pursued; leader-named, institutional-challenge, investigation, Thread-op-scale, and settlement-Order conditions are largely emergent side-effects of an otherwise personal choice, not something the player targets as "trigger an Echo."
3. **FEEDBACK:** Only the combat-vs-officer condition has a documented pre-roll warning: `valoria_ui_ux_v4.md` §7.10 shows an explicit banner ("⚠ SUFFICIENT SCOPE... Victory: target faction Stability −1... Defeat (you lose): target Mandate +1... The player knows before rolling. No hidden faction consequences.") plus a post-scene audio/visual cue (§20.3: map flash, faction-color pulse, direction-encoded chord) — again, stale doc, uncurrent. The other 6 §7 conditions have **no** documented pre-warning at any vintage.
4. **LATENCY:** Queued to Accounting except Full-TTRPG register-shift (§5.3, immediate) — deliberate, PP-109 anti-manipulation (cited explicitly).
5. **FRICTION:** Admin for the queued path — Accounting is a separate, non-pausable "viewing phase" (v4.1 line 168) a season later.
6. **RECIPROCITY:** One-way bottom-up; nothing in this section returns a faction-initiated signal to the acting scene.
7. **VERDICT:** Cap (1 Echo/scene/faction, PP-329) and the multi-condition tie-break priority order (§3.4: Thread op > Combat victory > Settlement governance > Disposition reach > Investigation > Faction-leader-direct > Other) are both **unsurfaced** — nothing tells the player which of several simultaneously-qualifying acts "won," or that a second qualifying act in the same scene was capped away. Failure (§5.2: −1 to the *acting* faction's own stat) is pre-warned only for the officer-duel case; for the other 6 conditions it is an undisclosed self-penalty. INERT (tie-break)/DEGENERATE-RISK (failure-gotcha) · P1 · UNDETERMINED (absence, not a stated design choice).

### E3 · Debate → Mandate (§5.4, PP-108)
1. **MOMENT:** A Grand Debate/contest resolves; a track crosses ≥7 / 4–6 / ≤3.
2. **DECISION:** Real — deliberate contest entry and argument choices.
3. **FEEDBACK:** §5.4 names the gating stat "Piety Track," but the identical ≥7/4–6/≤3 schema is elsewhere the **Persuasion Track** (`designs/scene/social_contest_v30.md` line 276, 594), while "Piety Track" is independently a *different*, per-territory religious-alignment stat (`faction_politics_v30.md` A-06, already logged as an open CV/PT naming collision). §5.4 appears to mislabel the mechanic actually driving Debate outcomes.
4. **LATENCY:** Not stated in §5.4; inferred to fall under the general queued-to-Accounting rule (§5.3) — UNGROUNDED beyond that inference.
5. **FRICTION:** Play for the debate; admin uncertainty for the Mandate update.
6. **RECIPROCITY:** Bottom-up only, no described return.
7. **VERDICT:** PLAYS-ROUGH — a player cannot name, in one sentence, which track decided their faction's Mandate shift. P2 · NOT-INTENDED (matches pre-existing open A-06 collision, not a deliberate dual-track design).

### E4 · Accord Domain Echo (§5.5, peninsular_strain_v30.md §2.5–2.8)
1. **MOMENT:** Player publicly governs, destabilizes, negotiates, or commits violence at settlement scale.
2. **DECISION:** Real and well-specified (§2.7 table: 6 concrete qualifying player actions).
3. **FEEDBACK:** Genuinely strong and *current* (peninsular_strain_v30.md is the Settlement/territory head in `CURRENT.md`): a 4-tier environmental-description table (§2.8) plus an explicit causal-narration line ("the market closing earlier... the baker... serves you in silence").
4. **LATENCY:** Split — violent/destabilizing acts apply immediately; cooperative/administrative acts queue to Accounting (§2.7 table) — harm bites now, virtue waits a season.
5. **FRICTION:** Admin for the queued half, compounded by a genuine rule contradiction (next point).
6. **RECIPROCITY:** Bottom-up; province Accord recomputes as `floor(mean(settlement Order))` at Accounting — a derived echo, not a narrated response.
7. **VERDICT:** §5.5 states personal Domain Echoes "do not stack with faction-level Govern actions in the same territory the same season — whichever produces the higher Accord applies," but §2.7 of the same subsystem's own head doc states the opposite: "Personal-scale Order changes and governor governance actions stack normally... cap ±1 per source per settlement per season." The Accounting procedure these both cite (`peninsular_strain_v30.md` §7 Step 4c) enumerates only garrison/passive-normalization checks and never resolves Domain-Echo-vs-Govern at all. A player who spends a season improving a settlement cannot know, from any doc, whether their personal effort adds to or is silently overridden by the governor's action that season. DEGENERATE-RISK · P1 · UNDETERMINED (neither passage acknowledges the other; no ED reconciles them).

### E5 · Thread Domain Echo (§5.6, ED-673)
1. **MOMENT:** A Thread op (Dissolution/Mending/Gap/Lock/Knot) produces RS Δ≥1, is witnessed by a Scar-firing NPC, or occurs at Territorial+ scale.
2. **DECISION:** The Thread op is a deliberate, rich choice; *whether it also counts as Thread Significance* is a derived side-effect, not a targeted decision.
3. **FEEDBACK:** Full clock-band crossings get explicit environmental narration (§4.3.3, "the world visibly changes"), but §5.6(a) fires on *any* RS change ≥1 — well below band-crossing — so most individual Thread Echoes get none of that; the only other candidate cue (audio chord/map pulse) is in the stale UI doc.
4. **LATENCY:** Queued to Accounting (§5.6 explicit).
5. **FRICTION:** Admin, plus the MS/RS naming split (flagged by `lens_playability_legibility.md`: `threadwork_v30` §5 calls it MS, `params/threadwork.md` calls it RS) means a player may not be able to name which world-track a given Echo touches.
6. **RECIPROCITY:** §5.6 notes Thread Domain Echo and Accord Domain Echo "may both fire from same scene on different stats" — whether the player sees one merged consequence line or two is UNGROUNDED (no doc addresses it).
7. **VERDICT:** INERT-leaning — the richest personal-scale decision space produces a strategic consequence pitched below the game's own perceptual threshold for Thread events. P2 · UNDETERMINED.

### E6 · PC Faction Embedding (§9, ED-075)
1. **MOMENT:** PC is physically present in a territory; once/season, that territory's faction gets +1D on one Domain Action.
2. **DECISION:** None — passive byproduct of location ("PCs are always mechanically present... narrative confirmation required," `params/factions/stats_1_7_scale.md` §PC Faction Embedding).
3. **FEEDBACK:** None found anywhere. The infill doc's own §9 section (`scale_transitions_v30_infill.md` line 56) is a bare heading with zero prose — no scene, no notification, no confirmation of which DA received the bonus or that the once/season budget was spent.
4. **LATENCY:** Applies to one unspecified DA per season.
5. **FRICTION:** Zero play-cost, but also zero agency — nothing to choose, verify, or trace.
6. **RECIPROCITY:** One-way; nothing narrates back.
7. **VERDICT:** INERT — mechanically live (even extended by `companion_specification_v30.md` line 146 to 2 DAs with a companion present) but experientially indistinguishable from not existing. P2 · mechanic DELIBERATE (ED-075 resolved) / presentation NOT-INTENDED (unauthored gap, not a ruled "stay invisible" choice).

### E7 · Fieldwork → BG Domain Echo (§3.9 rows; `fieldwork_v30.md` ~line 147)
1. **MOMENT:** An investigation Finding names a faction leader, or Disposition reaches Bonded (+5) with a faction officer.
2. **DECISION:** Real — Examine/Read/Interview/Reconstruct are deliberate scene actions building toward threshold.
3. **FEEDBACK:** Evidence Track progress and Finding reliability tags are shown in-scene (`fieldwork_v30.md` §4.1/§4.3, degree table). Whether the *qualification itself* ("this Finding met faction-level scope") is confirmed to the player is undocumented — the precise gating rule (Structural threshold 8 any topic; Complex threshold 5 only if institutional; Documentary/Verified evidentiary tags) lives only in the design prose, not in any confirmed UI surfacing.
4. **LATENCY:** Follows §3.4 → queued to Accounting.
5. **FRICTION:** Admin, plus cognitive load — requires the player to independently know the evidence-tag taxonomy to predict eligibility.
6. **RECIPROCITY:** Bottom-up; a separate, asymmetric NPC-side channel exists ("NPC learning mechanism," fieldwork_v30 line 151) but is not itself the Domain Echo.
7. **VERDICT:** PLAYS-ROUGH — well-specified mechanically, no scene-level confirmation that a faction consequence just fired. P2/P3 · UNDETERMINED.

### E8 · Consumption side (scene.contest_resolved / battle_concluded / investigation_resolved / combat_resolved → faction_state, npc_behavior)
1. **MOMENT:** Player wins a duel/contest/investigation/battle against faction-linked NPCs.
2. **DECISION:** N/A (resolution side).
3. **FEEDBACK:** `references/module_contracts.yaml` lines 71–76 lists `scene.contest_resolved`/`battle_concluded`/`investigation_resolved` in faction_state's `consumes`, but `faction_behavior_v30.md` §5.2 (ED-936, the module's own canonical doc) states the opposite for contest/combat: *"Faction-state does not consume `scene.contest_resolved` / `scene.combat_resolved` directly; these reach faction stats via the Domain Echo path... The §5.2 table above is the direct-consumption set only."* Contract and doc disagree specifically on `scene.contest_resolved`. For `scene.combat_resolved`, both sources agree it is unconsumed — confirmed absent from faction_state's actual `consumes` list, and `module_contracts.yaml:844` states the registry's declared `consuming_systems: [npc_behavior, faction_layer, articulation]` (`designs/architecture/key_type_registry_v30.md` §7) is not yet mirrored in either module's contract.
4. **LATENCY:** For the officer-duel case, identical to E2 — gated by Sufficient Scope, queued to Accounting.
5. **FRICTION:** The player is told (in the stale banner) exactly what a duel-win does to faction stats, but the only currently-wired delivery path is the Domain Echo gate (ED-936) — direct consumption is a dead letter for combat, contested for contest.
6. **RECIPROCITY:** npc_behavior's `consumes` list *does* name these types (lines 121–128) — NPCs update off contest/battle/investigation resolution somewhat more directly than factions do; background asymmetry, not player-visible.
7. **VERDICT:** `scene.combat_resolved` unconsumed = MISSING, re-affirmed at higher severity than the generic calibration note suggests, because it is the literal delivery mechanism for the flagship "beat a faction officer" moment (§7 bullet 5) — P1, sequenced-not-abandoned per gap_notes (DELIBERATE-to-defer). `scene.contest_resolved` contract/doc contradiction is NEW — P2, UNDETERMINED.

## Candidate findings

1. **Accord Echo/Govern stacking contradiction** — `scale_transitions_v30.md` §5.5 ("whichever produces the higher Accord applies") directly conflicts with `peninsular_strain_v30.md` §2.7 ("stack normally... cap ±1 per source"); neither cites the other, and the Accounting procedure (§7 Step 4c) resolves neither. Player-chair failure: invest a season on personal Order gains, faction governor also Governs the same settlement — outcome is undecidable from canon, and whatever happens is unnarrated. Severity P1. Intent: UNDETERMINED.
2. **`scene.contest_resolved` consumption contradiction** — `module_contracts.yaml` (consumes list) vs `faction_behavior_v30.md` §5.2/ED-936 (explicit denial of direct consumption). Severity P2. Intent: UNDETERMINED.
3. **Debate mechanic naming collision reaches Mandate** — §5.4's "Piety Track" almost certainly means "Persuasion Track" (identical ≥7/4–6/≤3 thresholds used for social-contest resolution); conflated with the unrelated, already-logged CV/PT Piety-Track collision (`faction_politics_v30.md` A-06). Severity P2/P3. Intent: NOT-INTENDED.
4. **Presentation-layer currency collapse** — every FEEDBACK mechanism found for this entire cluster (Sufficient Scope banner, Domain Echo animation, direction-encoded audio chord) lives in `valoria_ui_ux_v4.md`/`_v4_1.md`, confirmed stale and absent from `CURRENT.md` (`lens_playability_legibility.md`). Even within that stale doc, only 1 of 7 Sufficient Scope conditions (combat-vs-officer) got a bespoke player warning. Severity P1 (systemic — it undercuts every other edge's FEEDBACK line above). Intent: UNDETERMINED/NOT-INTENDED.
5. **Multi-condition tie-break and Echo cap are unsurfaced** — §3.4's priority order and PP-329's 1-per-scene cap have no documented player-facing trace of which condition won or that a second qualifying act was silently capped. Severity P2. Intent: NOT-INTENDED.
6. **Failure self-penalty is a gotcha outside the one warned case** — §5.2's "Failure = −1 to acting faction's own stat" is pre-warned only for combat-vs-officer (stale banner); the other 6 §7 conditions carry the same self-penalty with zero warning at any vintage. Severity P1. Intent: UNDETERMINED.
7. **PC Faction Embedding is authored but unpresented** — real mechanic (ED-075), zero infill prose (`scale_transitions_v30_infill.md` §9 is a bare heading), zero UI trace. Severity P2. Intent: mechanic DELIBERATE / presentation NOT-INTENDED.
8. **`scene.combat_resolved` unconsumed, re-scoped to severity** — already KNOWN per calibration, but its player-facing stakes are higher than a generic wiring gap: it is the sole current delivery path implied for the "duel vs faction officer" moment the design foregrounds with its only bespoke UI banner. Severity P1 (reframed upward). Intent: DELIBERATE-to-defer (gap_notes name it as sequenced).

## Threadwork note

P-14 ("Board/VG modes must express inseparability: co-movement cannot be omitted in any play mode," `canon/02_canon_constraints.md`) bears directly on this cluster's two Thread-flavored edges — §3.5 Thread→Faction ("the Thread operation IS the faction action... No extra roll") and §5.6 Thread Domain Echo (scalar faction-stat deltas keyed off RS change / witnessed Scar / Gap-Lock-Knot creation). Both collapse a Thread event into a single scalar faction-stat delta with no described three-dimensional (temporal CD, epistemic certainty, actualized consequence) co-movement at the aggregate scale — exactly the unresolved question logged as **A-9** in `designs/audit/2026-05-16-faction-ners-all-directions.md` ("Is Domain Action a thread operation under P-14? If yes, three-dimensional auto-effects must fire and §3.7 DA Ob calculation needs to engage them") and left OPEN, Jordan-owned, never appended to the editorial ledger (`designs/audit/2026-05-16-session-handoff.md` line 59). This audit did not find a later resolution. It is not new, but it lands squarely in bottom-up transport: every Thread event that gets abstracted upward through §3.5 or §5.6 is a live instance of the exact P-14 boundary question A-9 raised and never closed — worth re-surfacing for Jordan's decision rather than re-discovering from scratch.
