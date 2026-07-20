# Cluster C-FA dossier

_Opus evidence cluster, read-only; archived verbatim by the Fable orchestrator (2026-07-07).
Verdicts pending refuter pass + Fable adjudication — see `unaddressed_areas_audit_v1.md`._

**Mandate & read-only compliance:** No files created/edited/deleted. All findings are working-tree reads. Calibration items (fork 10 / ED-FA-0001; ep-14; EP-2 / ED-FA-0002; NERS "thin choice density"; ~87% win-share) are treated as KNOWN and not re-reported as discoveries. C-EMERGE owns measurement of the 87%; this dossier explains candidate mechanisms only.

**Central finding up front:** The faction *oracle* (`sim/`, the 1:1 Python reference the Godot port is built from — CLAUDE.md §7) implements a **pre-LPS-1, superseded faction model**. The entire canonical accounting engine documented in `faction_canon_v30` / `faction_behavior_v30` / `settlement_layer_v30 §1.8` — Mandate `7T/(T+6)`, per-settlement Legitimacy/Popular-Support, the α/β/γ/λ dynamics, Treasury attribution — **is unimplemented in the sim**. Every prior faction audit (NERS dossier, hunt_faction_minmax) reasoned about the *doc* model; none cross-checked it against the oracle. That gap is where most of this dossier lives.

---

## Math-vs-docs table

Canon side vs. oracle (`sim/`) side. "ABSENT" = the canonical construct has no oracle expression at all.

| Engine term | Canon (file:line · value/formula) | Sim / oracle (file:line) | Verdict |
|---|---|---|---|
| **Mandate** (headline stat) | `settlement_layer_v30.md:165-166` (authoritative LPS-2e) & `faction_canon_v30.md:214`: `Mandate = clamp(round(7·T/(T+K)),0,7)`, `T=Σ W_s·(q_s/7)`, `q_s=0.5L_s+0.5PS_s`, `W_s=base(Type)+Prosperity+FacilityTier`, `K=6` | **No Mandate field.** `game_state.py:84-101` Faction = `{L,Sta,W,I,Mil}`; `accounting.py:37-79 run_accounting()` computes CI/MS/insurgency/NPE only — **no Mandate recompute** | **MISMATCH — ABSENT.** The two docs agree with each other; the oracle has neither the stat nor the aggregation. |
| **Popular Support (PS)** | per-settlement 0–7 (`faction_canon_v30.md:204`, `settlement_layer_v30.md:631`) | **No PS field** anywhere in `game_state.py`; no per-settlement L/PS registry | **MISMATCH — ABSENT** |
| **α (cascade blend)** | `faction_canon_v30.md:126`: `α_base=0.4`, `α_seniority` −0.2..+0.4, `α_institution` −0.2..+0.2 | not implemented (no faction Cascade in provincial engine) | **ABSENT**; also **symbol-overloaded** — see α (temperament) below |
| **α/β (temperament)** | `faction_behavior_v30.md:256-262` & `faction_canon_v30.md:162-168`: α(outcomes)/β(conduct) per temperament, `α+β=1` (`:248`) | ABSENT (`temperaments.py` handles NPC drift, not L/PS integration) | **ABSENT.** α glyph reused for two different quantities (§3.2 blend vs §3.4 outcome-weight) — doc-internal overload |
| **γ (event shock)** | `faction_behavior_v30.md:235,250`: `+ γ×(random shock)`, `γ default 0.5` | ABSENT | **ABSENT** |
| **λ (Legitimacy integrators)** | `faction_canon_v30.md:157`: `λ_continuity, λ_procedural, λ_expectation, λ_violation` | ABSENT | **ABSENT + UNQUANTIFIED IN CANON** — the four λ are *named* but given **no numeric values and no ΔL formula** anywhere in the heads. Spec stub, not just an unimplemented one. |
| **ΔPopular_Support/season** | `faction_behavior_v30.md:232-236`: `α_temp×attributed_mission_outcome + β_temp×cascade_fidelity×outcome_polarity_gate + γ×shock`; input = `da_outcome.*` Key stream (`:240`) | ABSENT. `faction_action.py` emits **string labels** (`"Conquest:Success"`, `:189`), not `da_outcome.*` Keys — even the *input plumbing* is missing | **MISMATCH — ABSENT** |
| **Treasury attribution** | **Two conflicting canon values, both cite derived_stats:** `settlement_layer_v30.md:47` = `Prosperity × 50`; `settlement_layer_v30.md:169` = `Σ Prosperity × 10`. (Plus `:499` "+50/season" Mine case.) | ABSENT. `game_state.py:120` Territory has `prosperity:int` but it feeds only battle/starting flags; no gold/Treasury accrues to faction `W`; `run_accounting` has no Treasury step | **DOC-INTERNAL CONTRADICTION (5×)** *and* ABSENT in oracle |
| **Faction stat lineup** | canonical **6-stat**: Mandate/Influence/Wealth/Military/Intel/Stability (`faction_canon_v30.md:199`, LPS-1 ruling 2026-05-30) | oracle **5-stat**: L/Sta/W/I/Mil (`game_state.py:88-92`). No Mandate, no Intel; **keeps L as a faction scalar** | **MISMATCH.** The sim's faction-scalar `L` is exactly the "7-stat" model `faction_canon_v30.md:239-241 §5.3` declares the **defect** that LPS-1 resolved. Oracle predates the fix. |
| **Excommunication prereq** | `faction_canon_v30.md §9` → `EXCOMM_PREREQ_L_LIGHT=3` (`excommunication.py:29`) reads `church.L` | consistent *with the superseded* faction-scalar L | Internally consistent, but built on the **non-canonical** L axis |
| **Victory "PS"** | GD-1 canon "Political Stability ≤ 6" (`victory.py:29` PS_MAX=6.0) | `victory.py:73`: `ps = world.clocks.get('Turmoil')  # PS mapped to Turmoil` | **NAMING COLLISION:** code "PS" = Political Stability (Turmoil clock); docs "PS" = Popular Support. Same acronym, two meanings across the port boundary. |
| **Victory threshold** | `victory.py:27` = 15 (all 15 territories, "Jordan 2026-06-19 J-22") | `mc_v18.py:41` DEFAULT_PARAMS `VICTORY_THRESHOLD: 11` — **never passed to victory.py** | **DEAD PARAM** — mc_v18 advertises 11, oracle enforces 15. (Also mismatches the NERS dossier's "11+", `dossier_faction_political.md:18`.) |

---

## faction_politics reconciliation

**The PP-660 CANONICAL home exists and is substantial.** `designs/provincial/faction_politics_v30.md` — 1,116 lines, `## Status: CANONICAL (approved Jordan 2026-04-17, commit PP-660)` (`:3`). Section map (`:14`–`:910`+) covers:
- **Part 1** — 8-position Standing ladders (0–7) for Crown/Hafenmark/Varfell/Church, each with the "Skyrim Eight" dimensions + demotion magnitude (§1.0a, ED-776).
- **Part 2** — seven sub-office ladders (Löwenritter, Riskbreaker + Shadow-Renown/Deniability-Debt mechanics §2.2b, Inquisitor, Templar, Guild, Niflhel, Warden).
- **Part 3** — caste integration (advancement/renown/initiation/disposition-floor/conviction-scar).
- **Parts 4–7** — naming reconciliation, CI×rank integration, Baralta Crown Claim × rank succession, Ministry/Committee/Dicastery/Council expansion.

**What module_contracts assumes vs. what the home provides.** `module_contracts.yaml:707-725`: `faction_politics` has `doc: null`, `resolver: deterministic_accounting [ASSUMPTION]`, `consumes: []`, emits 4 Keys (`scene.investigation_resolved`, `state.coup_attempted`, `state.standing_change`, `state.succession`), gap_note "*home doc [GAP]*" + "*boundary vs faction_state unestablished [OPEN — Jordan]*". Every one of those 4 emit-clauses has a clear home in the existing doc: `state.standing_change` ← Part 1 rank ladders; `state.succession` ← SUC/LIN + Part 6 Baralta; `state.coup_attempted` ← Coup Counter (§1.1d, Kreutz); `scene.investigation_resolved` ← Inquisitor/Heresy (§2.3).

**Why it's still `doc: null` — a stalled restructure, not a missing doc.** `restructure_ledger.md:165` records the move `designs/systems/faction_politics_expanded_v1.md → designs/provincial/faction_politics_v30.md` as **PENDING**. The old path is gone (`ls` confirms no file), yet **36 files / 101 occurrences** across the corpus still cite the dead `faction_politics_expanded_v1.md` path (e.g. `propagation_log.md:552-586`). Calibration's "57 citations" and my "36 files / 101 occurrences" are the same stalled-rename artifact. The doc was relocated; the pointer-repointing + `doc:null` flip + CURRENT.md indexing were never finished. Additionally: **`faction_politics_v30` is orphaned from CURRENT.md** — the faction row (`CURRENT.md:29`) lists faction_canon/layer/behavior/state_authoring + overview but **not** faction_politics_v30 (nor faction_succession_split_v30), despite its self-declared CANONICAL status.

**What flipping `doc: null` → `designs/provincial/faction_politics_v30.md` would change:**
1. Supplies the authoring home for all 4 emitted Key types → their consumer-closure/boundary can finally be verified (today they emit into a doc-less void).
2. Resolves the "boundary vs faction_state [OPEN]" gap: faction_politics = per-actor **rank/Standing** ladder; faction_state = faction-scalar stability/mission/Mandate. The `faction_state` SCOPE note (`module_contracts.yaml:98`) already gestures at the dual-emit boundary.
3. Removes one module from the port-blocking `doc:null ×10` set (CLAUDE.md §6) — the highest-content of them.
4. **Necessary but not sufficient for contract closure:** `consumes: []` stays empty (the ladder actually consumes Duty outcomes, Disposition, Renown, CI — none declared), and `resolver` stays `[ASSUMPTION]` (the doc is prose rank tables, not a typed resolver). Flipping doc:null closes the *home* gap, not the *implementability* gap.
5. Should be co-done with the 36-file citation sweep + CURRENT.md faction-row insert, or the dead path keeps propagating.

---

## J-5 requirements list

Workplan v6 (`valoria_master_workplan_v6.md:70`) maps M1 **juncture 1 = "Strategic decision (the season's posture)"** to "**FA decision-surface work (J-5) + `domain_actions` module home**". The three-question legibility bar (`:65`: what is at stake · who is acting and why · what changed) must be answerable on-screen. From the docs as they stand, a designer building this surface is missing:

1. **A single canonical verb list.** Three non-reconciled action vocabularies coexist: (i) `module_contracts.yaml:59-63` `da.*` consume-types (5: antinomian/covert_betrayal/diplomatic_alliance/economic_intervention/public_governance); (ii) `sim/faction_action.py` verbs (4: Conquest/Muster/Govern/faction-unique); (iii) `faction_layer_v30` §7 seven-priority Domain Actions (Parliamentary Motion, Embargo, Treaty, Suppress…). EP-2 (ED-FA-0002) already flagged that the "menu" is an outcome-classification schema — this is the same defect at oracle level. **Missing: one reconciled verb menu the player picks from.**
2. **`domain_actions` home doc.** `doc: null` (one of the 10; workplan `:109` calls it "smallest of the doc:null closures, highest M1 leverage"). **Missing: what a Domain Action *is*, its resolver, its cost.**
3. **Action economy.** The oracle grants exactly **one** stochastic action/season (`faction_action.py:48-77`, flat 30/35/20/15 mix = `M7_ASSUMPTION_SIX`, `:9`). Canon (`faction_layer_v30` §7) implies multi-slot priorities. **Missing: slots-per-season, sequencing, and the posture-selection policy for NPC factions (current mix is `[ASSUMPTION]`, not canon).**
4. **GD-2 mandatory-precedence spec.** `faction_action.py:52-54` docstring: *"GD-2: mandatory threat-response before stochastic selection. Currently simplified: probabilistic mix per v17."* **GD-2 is asserted but unimplemented** — the decision surface's "forced move when threatened" layer has no spec.
5. **The read-model (legibility inputs).** To answer "what is at stake," the screen must surface Mandate + threats + available actions — but **Mandate isn't computed** and the stat model is superseded (see Math table). **Missing: the derived read-model feeding the decision.**
6. **Fork-10 resolution.** FA lane (`:210-212`): fork 10 (faction count 4–8, ED-FA-0001) "blocks any faction-scope bank/binding table and needs its own ED + ruling." **A per-season surface can't enumerate actors/player-controllability until this is settled.**
7. **Strategic↔scene bridge.** `scene_dispatch.run_scene_phase` is "*side-effect-free on strategic stats until the context-derivation bridge lands*" (`mc_v18.py:79-83`). **Juncture 1's decision does not yet connect to juncture 2's resolution.**

---

## Degeneracy mechanisms (ranked, evidenced)

Candidate mechanisms for one-faction win-share collapse. Ranked by strength of code evidence. (Measurement is C-EMERGE's; these are mechanism hypotheses with code paths.)

**M1 — Faction-unique wiring asymmetry (strongest; near-dispositive).**
`faction_action._try_faction_unique` (`:80-129`) wires **only Crown and Church**. Crown → Crown Initiative (`crown_initiative.py:87,96,150,231` pump `Crown.L +1..+2` per success). Church → Excommunication (`excommunication.py:141` drops the **highest-L rival's** L — target selected `:213` `sort by f.L reverse`), Council (`council_solmund.py:71,78` `Church.L +2` **and** rival `L −1`), Absolution. **Hafenmark and Varfell return `'invalid'`** (`faction_action.py:128-129`, "BLOCKED on Pass 2d/2e"). Because selection uses a single roll with cumulative branches (`:58-77`), their 30% unique slot **silently falls through to Conquest** (`roll<0.30 ⟹ roll<0.65`). So Crown/Church each own a repeatable **self-L-pump + (Church) rival-L-suppress engine**; Hafenmark/Varfell own neither. The fallback winner score is `held*10 + f.L + len(territories)` (`mc_v18.py:125`) — **L directly enters the tiebreak.** Corroboration: the pinned regression golden is `{Crown:50, Church:50, Hafenmark:0, Varfell:0}` (`test_mc_v18_regression.py:38`) — exactly the two wired factions win, the two blocked ones never do.

**M2 — Undamped Military→Conquest snowball; the canonical damper guards a non-existent loop.**
`_try_muster` (`:192-206`) adds `Mil +3/+5` on success with `pool=Mil` — self-compounding. `Mil` is both the conquest gate (`:156` `Mil<3.0 → invalid`) and the battle power (`massbattle.py:1817` `power=int(faction.Mil)`; damage `= net×(1+power)`, `:966`). Win → take territory + defender `L −10` (`faction_action.py:181`) + defender loses territory. More territory → more adjacency (`:145-152`) → more conquest targets. **No rubber-banding, no catch-up, no leader-tax anywhere in the loop.** Meanwhile the doc-asserted damper that "closes L3 Mandate runaway" — saturating `7T/(T+6)` + mean-reverting L/PS drift, loop-safety ledger "per-cycle gain 0.966 < 1, DAMPED + BOUNDED (verified)" (`archives/audit/2026-06-04-loop-safety-ledger/loop_safety_ledger.md:39,106`) — operates on the **Mandate↔L/PS loop that is not in the oracle at all.** The loop that *is* in the oracle (territory→Mil→conquest→territory) is undamped. The "verified damped" claim does not protect the reference the port validates against.

**M3 — Winner-take-all victory over positive-feedback dynamics ⟹ single attractor.**
Victory requires **all 15** territories, Accord≥2 in all, sustained 2 seasons (`victory.py:27-30,52-84`); otherwise the fallback picks the **territory leader** (`mc_v18.py:118-127`). With M1+M2 supplying only positive feedback and starting asymmetry (Church I=6/L=5/W=5 richest, Crown L=5/I=5; Hafenmark/Varfell lower — `game_state.py:37-42`), each seed converges to one runaway; across seeds the best-positioned wired faction wins disproportionately. This is the standard signature of a system with reinforcing feedback and no negative feedback — a single dominant attractor, consistent with the ~87% figure C-EMERGE will quantify.

---

## Exploit arena

Two layers, because the doc-side dominant lines and the oracle diverge. The doc-side lines (LINE 1–4) are **KNOWN** from hunt_faction_minmax (PR #77) — listed for completeness with their safeguards, **not** re-scored as new. The oracle-side observation is the novel contribution.

| Line | Play | In-canon safeguard | Status |
|---|---|---|---|
| **Treaty-hegemony** (`hunt_faction_minmax.md:20-49`) | Sign qualifying treaties with all rivals; hold 1 province; treaty-bound territory counts toward 15 **and** is Accord-exempt (`strain §6 L432`) **and** drives Strain down | Treaty **consent gate** — NPC consent needs Mandate≥3 ∧ Stability≤3 (`victory §3.1`); Capitulation/Tributary need military subjugation. **Partial** — destabilizing a rival auto-yields consent | KNOWN-TRACKED |
| **Domain-Echo Mandate-farming** (`:51-68`) | N Debate scenes/season farm own Mandate up + rival Mandate down (cap is per-scene, not per-season) | Mean-reverting L/PS drift (+1/season) — but **1 debate/season outruns it**; safeguard is on the wrong axis (`§5.3` fixes timing not count) | KNOWN-TRACKED (P2, safeguard weak) |
| **Mandate saturation gaming** (`:70-78`) | Develop one metropolis to Mandate≥5; `7T/(T+6)` saturation makes further territory near-free for the hegemon-domination clause | The saturation **is** the safeguard (diminishing returns, Lesson-5 bound, `settlement §1.8:168`) — intended, N-grounded | KNOWN-TRACKED (P3, intended) |
| **Insurgency suppression by rote Enforce** (`:80-91`) | Strip −1 insurgency marker/season at trivial Ob 2 indefinitely | Enforce costs Order−1 → feeds Accord down → threatens own Accord≥2; Cell Resilience +1 Ob at 3+ settlements | KNOWN-TRACKED (P2, self-cost damper) |
| **Govern/Muster stacking** (oracle) | Muster self-compounds Mil (`faction_action.py:203`); Govern raises Accord toward the ≥2 victory gate (`:223-224`) | **None found** — no per-season cap beyond the 7.0 stat ceiling; no diminishing returns on repeated Muster | NEW angle (mechanism = M2) |

**The novel oracle-side observation (NEW):** the strongest *doc-side* dominant line — **Treaty-hegemony (LINE 1)** — **cannot occur in the port oracle at all.** `treaty.propose_treaty` raises `NotImplementedError` (`treaty.py:97-111`); the mc_v18 season loop never `register_treaty`s an in-loop treaty nor calls `process_treaty_expirations` for one; and Crown's faction-unique routes to Crown Initiative modes (`faction_action.py:90-104`), **not** the Senator-Outward treaty path. So treaties are **inert** in the campaign loop. The safeguard-hunt for the doc exploits is therefore moot for the oracle, while the oracle's *actual* dominant line (M1's wired-faction L-engines) has **no in-canon safeguard** — it's a raw implementation asymmetry, not a designed mechanic with a counter.

---

## Findings

Format: `C-FA-N: claim · Priority · Status · evidence`.

- **C-FA-1** · The faction oracle (`sim/`) implements a **pre-LPS-1 superseded model** — 5-stat L/Sta/W/I/Mil with faction-scalar Legitimacy, **no Mandate, no Popular Support, no per-settlement L/PS, no Treasury, no α/β/γ/λ**. The canonical accounting engine is entirely unimplemented in the Godot-port reference. · **P1** · **NEW** · `game_state.py:88-101` vs `faction_canon_v30.md:199,214`; `accounting.py:37-79`; the sim's faction-scalar L is the defect `faction_canon_v30.md:239 §5.3` says LPS-1 resolved (2026-05-30).
- **C-FA-2** · Treasury attribution has a **5× doc-internal contradiction**: `Prosperity×50` (`settlement_layer_v30.md:47`) vs `Prosperity×10` (`:169`), both citing derived_stats; and it's ABSENT in the oracle (prosperity accrues no income). · **P2** · **NEW** · `settlement_layer_v30.md:47,169,499`; `game_state.py:120`.
- **C-FA-3** · **"PS" acronym collision across the port boundary**: `victory.py:73` "PS" = Political Stability (Turmoil clock); docs "PS" = Popular Support. Direct port-transcription hazard. · **P2** · **NEW** · `victory.py:29,73` vs `faction_canon_v30.md:204`.
- **C-FA-4** · **Faction-unique wiring asymmetry** — only Crown/Church have unique-action engines; Hafenmark/Varfell `return 'invalid'` and fall through to Conquest; L (which those engines pump/suppress) enters the fallback winner score. Primary candidate mechanism for the win-share collapse. · **P1** · **NEW** (mechanism; 87% itself is KNOWN, C-EMERGE-owned) · `faction_action.py:80-129,125`; `crown_initiative.py:87`; `council_solmund.py:71,78`; `excommunication.py:141,213`; corroborated `test_mc_v18_regression.py:38`.
- **C-FA-5** · **Undamped Mil→conquest snowball; the "verified DAMPED" L3 loop is absent from the oracle.** The loop-safety ledger's 0.966-gain damper guards Mandate↔L/PS, which the sim doesn't have; the sim's real loop has no damper/rubber-banding. · **P1** · **NEW** · `faction_action.py:156,181,192-206`; `massbattle.py:966,1817`; `loop_safety_ledger.md:39,106`.
- **C-FA-6** · **faction_politics restructure stalled**: file moved but `restructure_ledger.md:165` still PENDING; 36 files/101 occurrences cite the dead `faction_politics_expanded_v1.md` path; `doc:null` never flipped; the CANONICAL doc is orphaned from CURRENT.md's faction row. (Deepens ep-14.) · **P2** · **NEW detail on KNOWN-TRACKED ep-14** · `restructure_ledger.md:165`; `module_contracts.yaml:707-725`; `faction_politics_v30.md:3`; `CURRENT.md:29`.
- **C-FA-7** · **λ Legitimacy integrators are unquantified canon** — `λ_continuity/procedural/expectation/violation` are named but given no values and no ΔL formula in any head. · **P2** · **NEW** · `faction_canon_v30.md:157` (contrast the fully-specified ΔPS at `faction_behavior_v30.md:232-250`).
- **C-FA-8** · **GD-2 mandatory threat-response is asserted but unimplemented** — action selection is a flat probabilistic mix (`M7_ASSUMPTION_SIX`), a self-declared simplification. · **P2** · **NEW** · `faction_action.py:9,52-54`.
- **C-FA-9** · **Dead/mismatched victory param** — `mc_v18.py:41` advertises threshold 11 (never passed); `victory.py:27` enforces 15; NERS dossier says "11+". Three values, one gate. · **P3** · **NEW** · `mc_v18.py:41`; `victory.py:27`; `dossier_faction_political.md:18`.
- **C-FA-10** · **The doc's top exploit (treaty-hegemony) is inert in the oracle** — `propose_treaty` raises, loop never forms treaties; safeguard analysis for LINE 1 is moot for the reference, while the oracle's real dominant line (C-FA-4) has no in-canon counter. · **P2** · **NEW** · `treaty.py:97-111`; `faction_action.py:90-104`; hunt LINE 1 `hunt_faction_minmax.md:20-49` (KNOWN).
- **C-FA-11** · **α glyph overloaded** — cascade-blend α (`faction_canon_v30.md:126`, base 0.4) vs temperament α-outcomes (`:162-168`) are different quantities under one symbol; a typed export would collide them. · **P3** · **NEW** · as cited.
- **C-FA-12** · **Verb-menu triple-vocabulary** — module_contracts `da.*` (5) vs sim verbs (4) vs faction_layer priorities are unreconciled; blocks J-5. (Extends EP-2/ED-FA-0002 to the oracle.) · **P2** · **NEW detail on KNOWN-TRACKED EP-2** · `module_contracts.yaml:59-63`; `faction_action.py:48-77`; `faction_layer_v30.md §7`.

---

## Honest gaps

- **Did not run any sim.** Read-only per charter; the ~87% and the golden's `{50,50,0,0}` are read from `test_mc_v18_regression.py:38` and the file's own docstring, not reproduced. Mechanism ranking (M1>M2>M3) is an argued inference from code paths, **not** an ablation — C-EMERGE should confirm M1 by disabling faction-unique dispatch and observing whether Hafenmark/Varfell win-share rises.
- **massbattle.py read to line 1026 of 1906 + the adapter tail (1788-1861).** The middle (multi-turn loop internals) was not fully read; my battle-asymmetry claims rest on the pool/power/damage formulas and the `_faction_to_unit` adapter, which are the load-bearing parts, but a defender home-advantage/fort bonus buried in the unread middle would soften M2. I found none in the adapter (`_GarrisonStub Mil=1.5` only; no fort_level term in the strategic adapter).
- **faction_politics_v30.md read to line ~265 of 1116 + full section map.** Coverage characterization is from the header/scope/section headers; I did not read Parts 3–9 prose in full, so "what it covers" is structural, not line-verified beyond Part 1.
- **λ / ΔLegitimacy formula:** I confirmed the λ terms are *named* in `faction_canon §3.4` and that `faction_behavior §3.4` fully specifies ΔPS; I did **not** exhaustively confirm a ΔL formula is absent — `faction_behavior_v30 §3.5` (Legitimacy) was not read in full. C-FA-7 should be verified against §3.5 before filing.
- **"Treasury income = Σ Prosperity×10" (settlement §1.8:169)** — the actual `derived_stats_v1 §8.1` source doc was not opened to determine which of the two values (×10 or ×50) is the true canon; I report the contradiction, not its resolution.
- **Citation count:** calibration says 57; I measured 36 files / 101 occurrences of the dead path (different counting units — files vs. citations vs. occurrences). Not reconciled to the exact 57.
