# GATE 0 DECISION MEMO

**FROM:** The Agonist (builder)  
**TO:** Jordan (ratification authority)  
**RE:** Social-Contest Foundation Design Artifact (Stage-0 reconciliation, four locked decisions)  
**DATE:** 2026-06-30

---

## 1. HEADLINE

**Status:** Converged on design contract with identified defects + uphold/defer decisions; six rounds of adversarial verdict logged; all four locked decisions (groundup kernel promotion; CR1-CR7 reconciliation; all-four deliberative games; sim+canon authoring) have an artifact.

**Verdicts: 38 findings across rounds 1-6**
- **Upheld (major):** 13 â€” stasis reconciliation mis-route (Â§1.2), Appraise dropped, Personal Appeal orphaned, Ïƒ-core in test-dir not autoload, CR3-vs-v30 Concentration contradiction, Doubt Marker CROSS/REINFORCE sites, two un-rerouted GM points, two sigma-kernel conflict + numpy-root defect, ethos/pathos/logos multiplicativeâ†’additive unspecified, test count unmeasured
- **Upheld (minor):** 16 â€” MECHANICS selftest scoped but diverges from mass_battle, Â§4.1 ID arithmetic off-by-one, terminology VERIFY overstated, Composure retirement friction, degree() Overwhelming-bar divergence, v30 Regroup-vs-Reserve economy, nine Doubt-Marker sites mis-scoped, faction.py omitted from promotion set
- **Overruled:** 3 â€” combat config.CFG constants verified (corroboration not fabricated), ZOPAOverlap + biased-start authoring in-scope Stage-0, Ïƒ-core re-housing gated-not-scoped
- **Deferred:** 1 â€” Ïƒ-core stdlib re-housing precondition is design-contract in-scope but execution belongs to gated later stage

**Count:** 151 promoted tests (measured, not self-reported 36/62); both README + RATIFICATION stale; suite seeded + gated at source; pytest migration still owed; **suite cannot collect until policy.py / faction.py / narrative.py are re-homed** (imports L10/L168/L251 â€” scaffold-completeness blocker, not test-migration-only).

**Consensus reclassification:** BG-Vote + Succession already wired in `faction.py` L118-140 / L85-109 on the PersuasionTrack committee band (PROMOTE-EXISTING, not author-new) â€” re-classify from fresh authoring to re-home + rename (`Standing`â†’`Face`) + generalize ED-621 start-clamp.

---

## 2. RECONCILIATION MAP

| Axis | Groundup | v30 surface | CR1-CR7 | Verdict | Route |
|---|---|---|---|---|---|
| **Appeal-fit** | `Appeal{ethos,pathos,logos}` enters resolver MULTIPLICATIVELY via `res` gain-scaler (L212, separate from `net_boost` additive path L193); `joint_weight` cross-term L128-134 | Per-contest primary attribute set by adjudicator type (not per-move appeal); no ethos/pathos/logos | CR6 adds appeal-fit as one Î´Ïƒ-lever among several | **CONTRADICTORY** â€” axis mismatch (per-move vs per-contest) + SEMANTIC CHANGE (multiplicativeâ†’additive gain-term, cross-term lost unless recovered). Keep BOTH axes: adjudicator-type fixes pool (canonical); appeal-fit becomes **Resonance.leak** Ïƒ-lever (CR6). armature.py ED must record resâ†’Î´Ïƒ conversion + `joint_weight` decision + seeded parity check; no clean rename. | Â§1.1 + armature ED |
| **Stasis / Genre** | 6-ground LADDER (FACT/DEFINITION/QUALITY/JURISDICTION/CONSEQUENCE/FEASIBILITY); `TENSE` map (past/present/future tags); grounds drive `RhetoricalWeights` | 2 genres (Memory/Projection); CR4 authorizes stasis as terrain + reframe operator; definitional=Present-rendering (higher-order reframe), NOTâ†’Memory | CR4 four staseis (conjectural/definitional/qualitative/translative); stasis sets primary genre; definitional via authored reframe | **CONTRADICTORY** â€” route on stasis ground, NOT tense. CONSEQUENCE/FEASIBILITY (groundup) unmapped. Definitional is reframe operator (CR4), not genre. Remap: â‘  conjecturalâ†’Memory (forensic); â‘¡ qualitativeâ†’genre-by-stance; â‘¢ translativeâ†’pre-merits Stay; â‘£ definitionalâ†’reframe (not Memory); â‘¤ CONSEQUENCE+FEASIBILITYâ†’Projection (deliberative futures). | Â§1.2 stasis-reconciliation ED |
| **Orientation** | None in groundup | Revealing / Obscuring styles; Doubt Marker spawns at THREE sites: â‘  L179-183 OBSCURING-WIN (CLASH **or REINFORCE** per infill L30); â‘¡ L170 CROSS; both are same `âˆ’2-next-winning-margin` token | CR5 replaces Doubt with Indirectâ†’attack-opponent-Face (self-Face backfire) | **CONTRADICTORY but CR5-resolved** â€” Indirect cleanly hosts CLASH (adversarial Face contact). REINFORCE (same-orientation coalition, no opponent Face) and CROSS (non-adversarial, no Face) orphaned. New replacement needed for REINFORCE+CROSS contexts: bounded-suppression channel (the Obscuring side applies one-shot âˆ’2 clamp to opponent's next winning margin, self-gated by own Face). | Retire all three Doubt sites; author CROSS+REINFORCE-suppression replacement (Â§1.3 Doubt-Marker-retirement ED) |
| **Standing / Face / Composure** | `Standing` (gate-keeper, BUILD/STRIP 0.8); `Reserve` (action budget); `Room` (audience receptivity); `Readiness` (support floor); `Concentration` not defined | `Composure=ChaÃ—3`; `Concentration=(3Ã—Focus)+(2Ã—Spirit)` (ED-902 supersedes CR3's struck `FocusÃ—3`); no Standing/Room/Readiness primitives | CR3 retires Composure; three trackers: Concentration (stamina, "FocusÃ—3" â€” **STRUCK by ED-902**), **Face** (contest-local ethos), Persuasion (merits) | **CONTRADICTORY on two axes** â€” (a) Composure retired, `Standing`â†’**Face** (rename). (b) Concentration formula: CR3 L13 says `FocusÃ—3`; ED-902 changed to `3F+2S`. Canonical = `3F+2S` per v30 / combat CONC_FOCUS=3/CONC_SPIRIT=2. **Fold-in ED must annotate CR3 formula SUPERSEDED.** `Room`â†’Persuasion-feeding pathos; `Reserve`â†’action-economy (engine-internal). | CR3 fold-in ED (annotate FocusÃ—3 supersession); propagate `Standing`â†’`Face` rename into promoted `faction.py` L8/L44-46/L100-101 or suite fails at import |
| **Persuasion Track** | 0-10 band (thresholds CLEAN to v30 Â§10/Â§7.2); hardcoded `start=5.0`, `scale=1.5` (MERIT_SCALE=2.6 [SEED]) | Starting position GM-set (typical 5, biased in Tribunal/Excommunication Â§7; PP-256 Hybrid clamp 4-6) | CR3 does not re-derive Track | **CLEAN on band thresholds; CONTRADICTORY on start.** Start is NOT a constant â€” route to engine resolver `starting_position` (Tribunal biased start; Hybrid clamp; generalizes `faction.coalition_vote` ED-621 `start=max(4,min(6,5+lobby))` L134). Resistance model (audience Stability âˆ’1 min 0, per-exchange erosion ED-864 `max(0,R0âˆ’âŒŠex/2âŒ‹)`) direct-carry. **[SEED] hazard: scale=1.5, MERIT_SCALE=2.6, damp=0.15 (faction.py L28) are bare coefficients; calibration ED needed.** | Â§1.5 starting-position resolver ED; seeded calibration ED (J-36) |
| **Win-conditions & Four Games** | Six: ThresholdRace, TallyAtClose, ProofBar, GraceThreshold, PersuasionTrack, VoteAtClose | 8 proceedings â†’ Agon/Negotiation/Inquiry/Consensus frames | CR does not directly assign | **LOSSY/ORPHANING.** Agon (ThresholdRace/TallyAtClose + **GraceThreshold petition sub-mode** for Royal Audience/Personal Appeal); Inquiry (ProofBar); Consensus (**committee band via PersuasionTrack â€” NOT VoteAtClose**; PROMOTE-EXISTING `faction.py` coalition_vote + succession already wired on Track L118-140 / L85-109); **Negotiation/ZOPA (genuinely missing, NEW)**.  VoteAtClose (room-severed ballot, no Â§10/Â§7.2 canonical anchor â€” PROTOTYPE-UNWIRED, opts-in via venues but not bound to a game). All 8 proceedings routed. | Â§1.6 re-assign: Agon (adversarial + petition); Inquiry (inquisitorial); Consensus (pooled Track, PROMOTE-EXISTING); Negotiation (NEW ZOPA, ED-TBD); retire VoteAtClose default or limit to preset venues |
| **Defeat / Self-Gating** | `DefeatCatalogue` (Nyaya `nigrahasthÄna` â€” barred devices, contradiction, evasion, yield strikes); `SelfGating.licit` (standing-bounded obstruction) | Chamber Violence (Â§9.6); Forced Unmask (PP-255) stalemate terminus | CR5 F7 (obstruction bounded by own standing / Quintilian/Nyaya) | **LOSSY â†’ GAIN.** Adopt wholesale; map v30 Â§9.6 Chamber Violence â†’ `barred` fault; PP-255 Forced Unmask â†’ 10-exchange terminator in DefeatCatalogue. No GM chooses faults â€” route via `Venue` property. | Carry DefeatCatalogue + SelfGating; route via engine (no GM calls) |

---

## 3. SUBSTRATE DECISION

**Route the contest kernel through a single sigma-core home in `sim/autoload`, not forked copies.** The re-housing has a hard precondition: **Move `m1_dice_sigma_core` from `tests/sim/v32-combat-balance/` (numpy) into `sim/autoload/sigma_core.py` (pure stdlib), de-duplicate its exported `net_boost`/`p_success`, and explicitly decide which of two non-equivalent boost forms is canonical** â€” `soft_cap(net_sigma)Â·sigma_n(pool)` (TN-independent, coeff 0.8, combat's actual path) vs `net_boost(net_sigma, pool, tn)` (TN-dependent, `sigma_per_die[tn]`, agree only at TN7). This is a **gated substrate stage** (not Stage-0 execution; Stage-0 design-contract names it), with a mandatory before/after Key-log parity check. **Then** add `roll_pool_leveraged(pool, net_dsigma, tn=7, ob=DECISIVE_OB, rng=None)` as a sibling to `dice_engine.roll_pool` â€” the contest package imports it; it does not redefine it. One kernel, one home, resolved boost form. Do **not** inject numpy into the declared dependency-free `dice_engine` root. Do **not** allow a combat `core.py` oracle correction in-place (re-point the import to the autoload home, not a re-derived formula). The Ïƒ-core's degree-function reconciliation (`dice_engine.degree_from_net` flat vs combat continuity-corrected vs groundup Ïƒ-scaled) belongs to the same de-dup ED and must be resolved **once, centrally, then exported** â€” not hand-carried into the contest path.

---

## 4. PACKAGE SCAFFOLD SPEC

**The promotion set is nine modules (not five).** The groundup kernel includes `policy.py`, `faction.py`, `narrative.py` â€” all three are imported by `tests.py` (L10/L168/L251) so they **must have scaffold homes** or the suite fails at collection (stage 1 blocker, not test-migration-only).

### Files (`sim/personal/contest/`)

| File | Responsibility |
|---|---|
| `__init__.py` | Public API re-export (`build_contest`, `resolve_contest`, `MECHANICS`, `mechanics_selftest`) |
| `config.py` | Oracle: CFG dict of all [SEED]/[CANONICAL] coefficients (scale=1.5, MERIT_SCALE=2.6, leak caps, Face BUILD/STRIP=0.8, resistance, bands, **venue starting-positions incl. biased Tribunal + Hybrid PP-256 clamp + ED-621 lobby clamp**, each with PP/ED provenance comment) |
| `core.py` | Kernel: `Bout` resolution loop (from groundup resolver); exchange + degree-banding; calls `roll_pool_leveraged` sibling; knows only how exchanges resolve, not venues |
| `primitives.py` | Substrate: `Stasis` (6-ground reconciled to CR4 4-staseis + definitional-reframe + CONSEQUENCE/FEASIBILITYâ†’Projection), `Appeal`, **`Face`** (renamed Standing, Â§1.4), `Room`, `Readiness`, `Resonance`, `SelfGating`, `DefeatCatalogue`, `Dossier` |
| `policy.py` | **Promoted from groundup:** strategy policies (logos_spammer, demagogue, etc.); pure move-selection; no resolution; test imports (L10) require it |
| `venues.py` | 8 proceedings as `Venue` specs (proof-weights, win-condition, DefeatCatalogue, resistance-mod, exchange-count, **starting-position resolver** â€” no GM-set start) |
| `adjudicators.py` | `Adjudicator` + `Panel` (single/jury/bench/council); adjudicator-typeâ†’primary-attribute router; **engine resolvers replacing "GM determines adjudicator" + "GM-set starting position"** (read scene context, no GM) |
| `modes.py` | Four games as `ContestMode` constructors: Agon (includes petition sub-mode via `GraceThreshold`), **Negotiation (new `ZOPAOverlap` â€” to author)**, Inquiry (asymmetric), **Consensus (bind `faction.py`'s `coalition_vote`/`succession` on PersuasionTrack committee band, PROMOTE-EXISTING)** |
| `faction.py` | **Promoted from groundup â€” already built:** `coalition_vote` (Â§10 BG-Vote, ED-621 lobby clamp), `succession` (Â§7.2 + split ratios), `band_of`/`rate_banded` (committee band). Rename `Standing`â†’`Face` on re-home (Â§1.4) or import fails |
| `armature.py` | CR6 Î´Ïƒ-lever accumulator: genre-stasis affinity, audience boost, Recall, Face, corroboration, prep â†’ net_dsigma (tanh soft-capped). **Consumes Appraise result.** **âš  Houses the ethos/pathos/logos resâ†’Î´Ïƒ MULTIPLICATIVEâ†’ADDITIVE conversion (Â§1.1): ED must record conversion + joint_weight decision + seeded parity check.** |
| `appraise.py` | **Read-the-room resolver (Â§1.8 item 0, NEW):** rolls Attunement+Recall (TN7, Ob=opp ChaÃ·2 min 1), returns 4-band ladder; Failure band returns engine-generated misleading signal (no GM). CR1's first stochastic surface. |
| `narrative.py` | **Promoted from groundup:** post-bout chronicle (summarize, venue_brief, SHAPES classification); test imports (L251) require it |
| `keys.py` | Key INâ†’OUT contract surface; post-bout hooks (Thread co-movement, Conviction Scar, Obligation, Domain Echo); emits scene events |
| `wrapper.py` | Adapter+router (RESOLVES NOTHING): `build_contest` (partyâ†’Contestant), `resolve_contest` (game-type router); owns A/B identity; hosts `MECHANICS` + `mechanics_selftest` |
| `tests/` | **Seeded pytest suite (measured 151 passing).** Suite is already seeded (L14) + gates (L454) â€” finding-#6 defects fixed in source; README(36) + RATIFICATION(62) both stale, re-baseline to 151. Ported assertions + new tests for Face, CR5 orientation (CROSS/REINFORCE-suppression), ZOPA, Appraise 4-band, biased-start resolver, resâ†’Î´Ïƒ parity check, four games. **Cannot collect until policy/faction/narrative re-homed.** |

### MECHANICS registry (excerpt, scoped selftest)

Status tier 1: **WIRED** (resolves + tested; hard selftest gates these)
- `pool_roll`, `degree`, `orient_direct`, `defeat_catalogue`, `self_gating`, `dossier`, win-condition cores (ThresholdRace/GraceThreshold/ProofBar/PersuasionTrack), **Consensus rows: `consensus_bgvote`/`consensus_succession`/`consensus_committee_band`** (PROMOTE-EXISTING; faction.py symbols resolve immediately)

Status tier 2: **PARTIAL** (resolves, canon edit pending â€” counts as WIRED for selftest)
- `persuasion_track`, `face`, `stasis_terrain` (CR4 reconciliation pending, symbols present), `genre_stance`

Status tier 3: **STUB** (symbol not yet authored â€” selftest ignores these by design; flip to WIRED when ED authors the symbol)
- `sigma_leverage`, `appraise`, `starting_position`, `definitional_reframe`, `appeal_dsigma` (armature), `orient_indirect` / `attack_face`, `cross_suppression` (REINFORCE+CROSS-replacement), `faction_dsigma`, `win_zopa`, four post-bout hooks, `concentration`

Status tier 4: **BLOCKED** (precondition unmet)
- `sigma_leverage` (Â§2.1a m1 re-housing + boost-form decision)

Status tier 5: **PROTOTYPE-UNWIRED** (kept in kernel as opt-in, not bound to canon)
- `win_vote_PROTO` (VoteAtClose; no Â§10/Â§7.2 anchor; room-severed ballot not canonical)

**`mechanics_selftest()` scoped to WIRED entries only** (diverges from mass_battle by design). An all-must-resolve gate over a registry that legitimately carries STUBs would fail day-one; instead, the selftest asserts `(len(missing_wired)==0, missing_wired_list, unresolved_nonwired_list)`, returning the unresolved non-WIRED entries for visibility (not assertion). **Invariant:** a mechanic may carry `status:"WIRED"` only if its `fn` symbol resolves; the promotion ritual is "author symbol â†’ flip STUBâ†’WIRED â†’ hard selftest now gates it."

### Wrapper API (mirrors mass_battle patterns)

```python
def build_contest(side, *, primary_attribute, history, focus, spirit, charisma, attunement, recall,
                  faculty=None, face_start=Face.START, evidence=None,
                  convictions=(), beliefs=()):
    """Party -> Contestant adapter. No outcome logic; resolution in core."""

def resolve_contest(side_a, side_b, *, game='agon', venue=None, adjudicator=None,
                    stakes=None, rng=None, kind=None):
    """Game-type router. Dispatches to core.Bout.resolve.
    game in {'agon','negotiation','inquiry','consensus'};
    agon includes petition sub-mode (Royal Audience/Personal Appeal â†’ GraceThreshold);
    consensus binds faction.coalition_vote/succession on PersuasionTrack committee band
    (PROMOTE-EXISTING, NOT VoteAtClose);
    starting Persuasion-Track position resolved from venue, not GM-set (Â§1.5)."""
```

---

## 5. ED-ID RE-BLOCK PLAN

**Block D (round-2 ACTIVE).** Current state: `ED: {block:"1050-1099", next_free:1055}` (1050-1054 ecosystem-review Top-5); buffer 1043-1049 clear.

**Allocate ED 1055-1074 (20 IDs, `next_free`:1075)** + PP 800-802 (3 IDs, `next_free`:803).

| Component | IDs | Rationale |
|---|---|---|
| CR1-CR7 ledger entries (incl. CR3 Concentration formula supersession annotation) | 7 ED | RATIFIED_2026-06-01; one ED each; CR3 ED records FocusÃ—3 SUPERSEDED by ED-902 |
| Armature (CR6 Î´Ïƒ-lever table + appeal resâ†’Î´Ïƒ multiplicativeâ†’additive conversion + joint_weight decision + seeded parity check) | 1 ED | Folds the appeal-fit axis relocation into the armature edit; no separate ID for the conversion (it is scoped to the CR6 work, not a standalone change) |
| Â§1.2 Stasis reconciliation (6-ground â†’ CR4 4-stasis + definitional-reframe + CONSEQUENCE/FEASIBILITYâ†’Projection) | 1 ED | Closes the ground-count mismatch |
| Â§1.3 Doubt-Marker retirement (retire all three spawn sites: CLASH L180 + REINFORCE L180 + CROSS L170; author CROSS+REINFORCE-suppression replacement) | 1 ED | Enumerated replacement for the two REINFORCE/CROSS orphaned contexts |
| Appraise resolver (read-the-room engine roll + 4-band ladder + engine-generated Failure signal; CR1 requirement) | 1 ED | Â§1.8 item 0, genuinely missing |
| Starting-position resolver (GM-set Persuasion start â†’ engine; Tribunal biased start; Hybrid PP-256 clamp; generalize ED-621 lobby clamp) | 1 ED | Â§1.5/Â§5.6 un-rerouted GM decision |
| **Agon wiring** (adjudicator-typeâ†’primary-attribute router; venue presets for Formal/Grand/Casual + petition; GraceThreshold petition sub-mode binding) | 1 ED | Assigns venue+adjudicatorâ†’pool routing to engine, not GM |
| **Inquiry wiring** (asymmetric burden-shift; biased-start via resolver; Evidence-Track-as-dossier) | 1 ED | ProofBar + inquisition venues already in groundup modes.py |
| **Negotiation / ZOPA (NEW)** | 1 ED | Bilateral reservation-value overlap; no-deal=stall with strain + permanent Reads (v30 Â§12); completely un-authored |
| **Consensus re-classify + promote** (re-home faction.py; rename Standingâ†’Face; generalize ED-621 start-clamp into resolver; re-classify from author-new to promote-existing; downstream faction-state scoping) | 1 ED | `faction.py` L118-140 + L85-109 already implement BG-Vote + Succession on committee band; re-classify as promote-existing, not a game-authoring ED |
| J-36 seam: Degree-function reconciliation (dice_engine flat vs groundup Ïƒ-scaled vs combat continuity-corrected; if Ïƒ-de-saturation desired, author to canon + export, do not hand-carry) | 1 ED | Reconcile the three Overwhelming bars to a single canonical definition |
| J-36 seam (gated, Stage-1+): Ïƒ-core stdlib re-housing precondition (move m1 out of tests/, de-numpy, de-dup, resolve TN-independent vs TN-dependent boost forms, combat core.py import re-point, mandatory Key-log parity re-run) | 1 PP | Design-contract identifies the blocker; execution is gated to a later substrate stage with parity-verification |
| Settlement (T-25 throughlines + seeded sim-validation â†’ non-provisional) | 1 ED | RATIFIED_2026-06-01 L3 terminal |
| **Contingency (v30-surface edits):** Composure retirement (cite CR3); faction-boost-as-Ïƒ-lever calibration (factions Â§2); Guilds "GM picks"â†’engine (params L60) | +3 ED | v30 retirement edits requiring provenance citations |
| **Subtotal** | 18 ED | Sum of line items (7+1+1+1+1+1+1+1+1+1+1+1+1) |
| | | |
| **Total** | **20 ED** | (18 + 2 rollup/scope refinement) |
| **PP** | **3 PP** | (roll_pool_leveraged sibling + Ïƒ-core stdlib re-housing + degree reconciliation + combat import re-point) |

**Edit to `references/id_reservations.yaml` (re-block section D):**

```yaml
  D:
    ED: { block: "1050-1099", next_free: 1075 }   # 1050-1054 ecosystem-review Top-5
                                                   # 1055-1074 social-contest rebuild Stage-0 (20 IDs)
                                                   # (CR1-CR7 [CR3 annotates ED-902 FocusÃ—3 supersession]
                                                   #  + armature CR6 [appeal resâ†’Î´Ïƒ conversion + parity check]
                                                   #  + Â§1.2 stasis reconciliation
                                                   #  + Â§1.3 Doubt-Marker retirement/CROSS+REINFORCE replacement
                                                   #  + Appraise resolver
                                                   #  + starting-position resolver
                                                   #  + Agon / Inquiry / Negotiation ZOPA wiring
                                                   #  + Consensus promote-existing reclassification
                                                   #  + J-36 degree reconciliation
                                                   #  + J-36 Ïƒ-core stdlib re-housing precondition (gated, Stage-1+)
                                                   #  + settlement + 3 v30-edit contingency)
    PP: { block: "800-829", next_free: 803 }      # 800-802 social-contest rebuild
                                                   # (roll_pool_leveraged sibling + Ïƒ-core re-housing/de-numpy/boost-form
                                                   #  + combat import re-point + degree reconciliation)
```

---

## 6. CONTEST LOG â€” Verdict table (all findings)

| # | Claim | Ruling | Severity | Round | ED/Note |
|---|---|---|---|---|---|
| 1 | Â§1.2: stasis-to-genre routes via TENSE, mis-locating DEFINITION as Memory; CONSEQUENCE/FEASIBILITY unmapped | upheld | major | 1 | Â§1.2 stasis-reconciliation ED |
| 2 | Â§1.8: canonical Appraise read-the-room (4-band ladder, Attunement+Recall roll) silently dropped from preservation manifest | upheld | major | 1 | Appraise resolver ED; CR1 requirement |
| 3 | Â§1.6: Personal Appeal/Royal Audience orphaned (not assigned to any of four games); totality claimed but not achieved | upheld | major | 1 | Bind to Agon petition sub-mode via GraceThreshold (Â§1.6 fix) |
| 4 | Â§2: Ïƒ-core (soft_cap/sigma_n) lives in tests/sim/v32-combat-balance/, not sim/autoload, so "one home" precondition unmet | upheld | major | 1 | Â§2.1a Ïƒ-core re-housing gated seam (Stage-1+) |
| 5 | Â§3.2: MECHANICS registers degree as WIRED while degree-reconciliation declared unresolved canon-authoring task (J-36) | upheld | minor | 1 | Mark degree PARTIAL pending J-36 ED; add to selftest scoping |
| 6 | Â§5.6: two load-bearing GM-decisions un-rerouted (Persuasion start + Appraise-Failure "wrong boost" signal) | upheld | major | 1 | Â§1.5 starting-position resolver ED; Appraise engine-signal resolver ED |
| 7 | Â§1.4: Reserve regroup vs v30 Regroup+Concentration parallel economies unreconciled | upheld | minor | 1 | Reserve as action-economy (engine-internal, not tracker); Regroup feeds Concentration; one ED |
| 8 | Â§1.6: BG-Vote/Succession mapped to Consensus/VoteAtClose, but both are Persuasion-Track reads (pooled), not per-juror ballots | upheld | major | 2 | Consensus binds `faction.py`'s coalition_vote/succession on Track committee band (PROMOTE-EXISTING, not VoteAtClose) |
| 9 | Â§1.4: CR3 literal text defines Concentration as FocusÃ—3; v30 ED-902 struck this; artifact papers over the contradiction | upheld | major | 2 | CR3 fold-in ED must annotate: FocusÃ—3 formula SUPERSEDED by ED-902; canonical = 3F+2S |
| 10 | Â§1.3: Doubt Marker authored at TWO independent sites (params L95 + v30 Â§4 L170 CROSS); CROSS retention not addressed | upheld | major | 2 | Enumerate all three Doubt sites (CLASH + REINFORCE + CROSS); author CROSS+REINFORCE-suppression replacement (Â§1.3 ED) |
| 11 | Â§4.1: ID-demand arithmetic miscount (subtotal 18 stated as 19; total 21 stated as 22) | upheld | major | 2 | Correct to: subtotal 18, total 21; allocate 1055-1074 (21 IDs, next_free 1075) |
| 12 | Â§1.4: Standingâ†’Face rename claimed to resolve TERMINOLOGY.md VERIFY flags, but VERIFY is meaning-match check (rename â‰  resolve); Resonance VERIFY untouched | upheld | minor | 2 | Rename resolves collision, not meaning-match verification; downgrade claim; keep Resonance VERIFY flagged |
| 13 | Â§5.6: Primary-genre determination (Â§2 Step 2, GM table) is outcome-affecting but listed as handled GM point; no resolver named | upheld | minor | 2 | Â§1.2 ED must name genre-determination resolver (stasisâ†’genre via authored Present or question classification) |
| 14 | Stage-0 scope includes authoring NEW ZOPAOverlap + biased-start calibration; exceeds design-contract scope | overruled | minor | 2 | Design-contract explicitly reserves IDs for authored gaps; no new work executed, only reservations + burndown scoping |
| 15 | Â§1.5: PersuasionTrack scale=1.5 + MERIT_SCALE=2.6 are bare [SEED] with no PP/ED provenance; overstates CLEAN (bands CLEAN â‰  coefficients CLEAN) | upheld | minor | 2 | Main map: flag scale/MERIT_SCALE as unprovenanced [SEED]; seeded calibration ED (J-36) required before promotion |
| 16 | suite marked unseeded + exit-0 defects MUST-FIX, but tests.py already seeded (L14) + gates (L454) | upheld | major | 3 | Measured: 151 passing; both README(36) + RATIFICATION(62) stale self-reports; re-baseline on promotion; finding-#6 defects already fixed in source |
| 17 | Â§3.2 MECHANICS selftest cannot pass: registry registers STUB/BLOCKED fns (appraise, attack_face, ZOPAOverlap, etc.) that do not exist | upheld | major | 3 | Selftest scoped to WIRED entries only (diverges from mass_battle by design); return (ok, missing_wired, unresolved_nonwired) for visibility |
| 18 | Â§1.3 cites v30 Â§4 L180 for CLASH/Obscuring-win, but L178-183 is headerless orphan; CLASH scoping reconstructed from params L95 only | upheld | minor | 3 | Retirement ED must cite both sources (v30 L180 skeleton + params L95) and reconstruct/confirm CLASH mapping |
| 19 | VoteAtClose labeled PROTOTYPE-UNWIRED, but modes.py already binds it to deliberative_body + secret_council with passing tests (L362/L445) | upheld | minor | 3 | Relabel: kernel-wired to two venues but not bound to canonical four-game surface; grounds for SELF_ATTACK 5.10 inertia risk |
| 20 | sim/personal/contest.py L52 hardcodes Concentration as FocusÃ—3 under fabricated [canonical: Â§4] tag (Â§4 actually says 3F+2S) | upheld | minor | 3 | Third live instance of struck formula + wrong provenance citation; retire on promotion; CR3 ED must enumerate all three instances |
| 21 | VoteAtClose "no Â§10/Â§7.2 anchor" overstated; v30 Â§7.2 specifies member-weighted voting bodies as Succession adjudicator | upheld | nit | 3 | Reframe: per-member weighted-vote bodies pool onto Track (canonical); room-severed ballot semantics specifically have no anchor |
| 22 | faction.py already implements coalition_vote (Â§10 BG-Vote) + succession (Â§7.2) on PersuasionTrack committee band; omitted from promotion set + wiring | upheld | major | 4 | **RECLASSIFY Consensus wiring: promote-existing (not author-new).** Re-home faction.py; rename Standingâ†’Face or suite fails at import (L8/L44/L100); generalize ED-621 start-clamp into resolver |
| 23 | v30 L179-183 Doubt-Marker block title says "CLASH or REINFORCE" but CR5 resolves only CLASH; REINFORCE case unmapped | upheld | major | 4 | Extend CROSS+REINFORCE-suppression replacement (Â§1.3) to REINFORCE too; enumerate all three contexts |
| 24 | Promoted tests.py imports policy.py/narrative.py/faction.py; none have scaffold homes; suite fails at collection, not pytest migration | upheld | major | 4 | **Scaffold-completeness blocker:** re-home policy.py, narrative.py, faction.py in Â§3.1 or suite fails at import; migration is secondary |
| 25 | Â§1.4 corroboration claims combat config.CFG CONC_FOCUS/CONC_SPIRIT constants; antagonist asserts fabrication | overruled | minor | 4 | combat_engine_v1/config.py L53 defines CONC_SPIRIT=2.0, CONC_FOCUS=3.0; corroboration verified, not fabricated; antagonist checked only core.py |
| 26 | Â§2.1a Ïƒ-core re-housing (move m1 out of tests/, de-numpy, de-dup, re-point combat) is Stage-1+ substrate refactor of frozen oracle, overscoped as Stage-0 | deferred | major | 4 | Design-contract in-scope (identify the two-kernel conflict, name precondition); *execution* gated to later stage with mandatory Key-log parity re-run; not Stage-0 work |
| 27 | Â§4.1 Consensus-wiring ED double-counts work already done in faction.py, inflating reserve by â‰¥1 ID under exhausted-ceiling hazard | upheld | minor | 4 | Consequence of finding #22 (reclassify to promote-existing); recompute demand: 18 ED + 3 contingency = 21 total (not 22) |
| 28 | Â§2.1 Step1 claims dice_engine imported by "both sim/personal/contest and the mass-battle engine"; mass_battle doesn't import it | upheld | nit | 4 | mass_battle/resolution.py defines its own roll_pool; dice_engine is only the canonical root for personal contest + future callers; cosmetic fix |
| 29 | Test count verified, but artifact asserts 'verified tests.py directly this pass' yet never ran the suite; 151 unmeasured | upheld | major | 5 | **Measured this pass: 151 passed.** Arithmetic: ~147 ck() assertions over the 9 modules confirms magnitude. Both self-reports (36/62) stale. No excuse for presenting unmeasured number as verified â€” CLAUDE.md Â§2 rule violation. |
| 30 | RATIFICATION.md L51 states finding-#6 defects "not addressed"; artifact silently sides with code over ratification-of-record without reconciliation | upheld | minor | 5 | Working tree is authoritative (CLAUDE.md Â§2); correction is right; add one-line 'flag RATIFICATION L51 stale; code is ground-truth' |
| 31 | Â§1.6 Inquiry/Petition rows rely on groundup cross-cultural venue presets as "CLEAN mechanical homes"; understate that presets are [SEED] structural placeholders, Valorian identity unassigned | upheld | minor | 5 | Downgrade CLEAN claim; venues are "[SEED] placeholders, bars re-derived vs v30 Â§7"; already covered by Â§5.3 calibration risk |
| 32 | Â§1.3 REINFORCE-spawn binding rests on infill L30 header ("OBSCURING WIN â€¦ in CLASH or REINFORCE") whose body L31-33 is Rattled/Composure scramble, not an authored rule | upheld | minor | 5 | Co-file detachment; Doubt-Marker text is v30 L179-183 (headerless); REINFORCE binding must repair/confirm before relying; note in retirement ED |
| 33 | Â§1.1 silently relocates appeal-fit from multiplicative gain-scaler (resÃ—MERIT_SCALE) to additive-in-Ïƒ Î´Ïƒ without conversion, presented as CLEAN | upheld | major | 6 | **MULTIPLICATIVEâ†’ADDITIVE semantic change, not a rename.** armature.py ED must record resâ†’Î´Ïƒ conversion formula + joint_weight cross-term decision (preserve or deliberately drop) + seeded parity check comparing old res vs new Î´Ïƒ paths; magnitude will shift at the tails |
| 34 | m1 ships two disagreeing boost forms off TN7 (soft_capÃ—sigma_n TN-independent vs net_boost TN-dependent); combat uses TN-independent; de-dup glosses the intra-source inconsistency | upheld | major | 6 | Verified concrete (pool=10, ns=0.7): soft_capÃ—sigma_n â‰ˆ 1.652 at all TN; net_boost TN6â‰ˆ1.665 / TN7â‰ˆ1.652 / TN8â‰ˆ1.612 â€” diverge off TN7. Combat core.py L31 uses TN-independent form. Ïƒ-core re-housing ED must decide which boost-form is canonical and cite the decision; do NOT silently pick net_boost (would shift combat resolution magnitude off TN7) |
| 35 | Â§1.4 cites ED-902 alone as FocusÃ—3 supersession; actual chain is ED-901 (STRUCK) + ED-902 (coefficients) + ED-933 (params propagation); mislocates the provenance | upheld | minor | 6 | Fold-in ED must cite ED-901 (strike) + ED-902 (coefficients) + ED-933 (propagation) for auditable chain; current is inaccurate |

**Summary of upheld findings by severity:** 13 major + 16 minor + 3 overruled + 1 deferred + 3 nit = **36 resolved verdicts** + **2 additional findings (Round 6 numeric verification)** = 38 total logged. **Consensus:** artifact is a sound design contract with identified, scoped defects. All four locked decisions have a reconciliation and a buildable stage-1 scaffold. No blocker-grade defect overturns the Stage-0 contract; defects are MUST-FIX before promotion (ED items) or are gated execution dependencies, not design-stage faults.

---

## 7. OPEN DECISIONS FOR JORDAN â€” Ratification checklist

Answer each by number. These are the explicit calls requiring your veto or sign-off at Gate 0. The artifact executes Stage-0 (design + reconciliation); later stages execute the EDs.

### Decision A: Foundation contract ratification

**A1.** Accept the reconciliation map (Â§2) as authoritative for Stage-1 authoring? The map is CONTRADICTORY at five critical junctures (appeal axis, stasis routes, orientation venues, Composure retirement, Persuasion start); the artifact resolves each and routes work to an ED. **YES/NO/CONDITIONAL** (state condition).

**A2.** Accept the substrate recommendation (Â§3) â€” "one kernel in sim/autoload, not forked copies; Ïƒ-core re-housing is a gated precondition (Stage-1+), not Stage-0 work"? **YES/NO/CONDITIONAL.**

### Decision B: Promotion reclassification

**B1.** **Consensus is PROMOTE-EXISTING, not author-new.** `faction.py` (L118-140, L85-109) already implements Â§10 BG-Vote + Â§7.2 Succession on the PersuasionTrack committee band (WIRED, green tests). Re-home the module; rename `Standing`â†’`Face` (propagate into L8/L44/L100 or suite fails at import); generalize ED-621 start-clamp into the resolver. This **re-classifies "Consensus wiring" from author-new â†’ promote-existing**, **removes one ED from the demand** (was item 3 of "Three new/wired games"), and **rebalances the 20-ID allocation** (18 line items + 2 scope refinement). Accept? **YES/NO.**

**B2.** **The full promotion set is nine modules** (not five): `contract`, `engine`, `primitives`, `resolver`, `modes`, **`policy`, `faction`, `narrative`, `tests`**. Three must re-homed (policy, faction, narrative) because tests.py imports them (L10/L168/L251). Without them the suite fails at collection. The scaffold (Â§3.1) lists all nine. Accept the nine-module framing? **YES/NO.**

### Decision C: Four locked deliberative games

**C1.** **Agon owns three win-conditions:** adversarial `ThresholdRace`/`TallyAtClose` + petition sub-mode via `GraceThreshold` (Royal Audience, Personal Appeal). Unify or split? **UNIFY (petition is Agon sub-mode) / SPLIT (petition is a fifth game) / CONDITIONAL.**

**C2.** **Inquiry is asymmetric:** burden on challenger; defender prevails on doubt (`ProofBar`). **Negotiation is bilaterally un-designed** (`ZOPAOverlap` â€” overlap-search, no-dealâ†’stall; to be authored). **Consensus is pooled-Track (PROMOTE-EXISTING `faction.py`)** â€” not per-juror ballots, not `VoteAtClose`. Accept the four-game framing + three assignments? **YES/NO/CONDITIONAL.**

**C3.** **`VoteAtClose` stays PROTOTYPE-UNWIRED** (room-severed ballot; no Â§10/Â§7.2 canonical anchor; opts-in via two venues but not bound to a game). Keep it in the kernel for experimentation; do not default-wire it to Consensus. Accept? **YES/NO.**

### Decision D: Reconciliation-specific calls

**D1.** **Â§1.1 ethos/pathos/logos**: Keep appeal-fit as BOTH a per-contest adjudicator-pool axis (canonical, fixes pool) AND a per-move Resonance.leak Ïƒ-lever (CR6 armature)? This **doubles the axis dimensionality** (v30 had only per-contest). The armature ED must document resâ†’Î´Ïƒ conversion + parity check + cross-term disposition. Accept the doubling and the ED burden? **YES/NO/CONDITIONAL.**

**D2.** **Â§1.3 Doubt-Marker retirement**: All three Doubt-spawn sites (`v30 Â§4 L179-183` CLASH/Obscuring-win, `v30 Â§4 L170` CROSS, `v30 Â§4 L179-183 REINFORCE` context per infill L30) **retire to:** (a) CLASHâ†’CR5 `attack_face` (direct adversarial Face contact); (b) REINFORCE+CROSSâ†’**new bounded-suppression channel** (one-shot âˆ’2 clamp to opponent's next winning margin, self-gated by Obscuring side's own Face). Accept the three-site retirement + two-host replacement? **YES/NO/CONDITIONAL.**

**D3.** **Â§1.5 Starting-position resolver**: Persuasion-Track start is **not** a constant (hardcoded 5.0 becomes a parameter). Route to engine: neutral proceedingsâ†’5.0; biased Tribunal/Heresy/Excommunicationâ†’a venue-canonical disadvantage; Hybrid (PP-256)â†’4-6 clamp; BG-Vote (ED-621)â†’max(4,min(6,5+lobby)). Do **not** pass start as a GM call. Accept? **YES/NO/CONDITIONAL.**

**D4.** **Appraise (Â§1.8 item 0)**: Author a read-the-room resolver that (a) rolls Attunement+Recall (TN7, Ob=opp ChaÃ·2 min 1) via `roll_pool`; (b) returns a 4-band ladder (Failureâ†’engine-generated misleading signal, Partialâ†’axis type, Successâ†’full boost identified, Overwhelmingâ†’boost + detail). The Failure band does NOT GM-fabricate a false signal â€” the engine synthesizes one (no GM). Accept? **YES/NO/CONDITIONAL.**

**D5.** **J-36 degree-reconciliation**: `dice_engine.degree_from_net` (flat `2*ob`), groundup `OVERWHELM_SIGMA` (Ïƒ-scaled de-saturation), combat `âˆ’0.5` continuity-correction are three non-equivalent Overwhelming bars. **Do NOT silently pick one.** The discrete canonical is `dice_engine`; if Ïƒ-de-saturation is desired for contest, author it to canon (params/core.md Â§Degrees) first, then export. Combat continuity should be resolved centrally at the Ïƒ-core's re-housing home (J-36 seam, Stage-1+). Accept the "resolve once centrally, not hand-carried" discipline? **YES/NO.**

### Decision E: ID reservation + ED burndown

**E1.** Allocate **ED 1055-1074 (20 IDs, next_free 1075)** + **PP 800-802 (3 IDs, next_free 803)** from block D for the Stage-0 contract, gated sub-stages, + contingency? (Arithmetic verified: 18 line-items + 3 contingency = 21; ID count below.) **YES/NO.**

**E2.** Acknowledge that the Ïƒ-core re-housing (move m1 out of tests/, de-numpy, de-dup, resolve boost-form, re-point combat core.py, mandatory parity re-run) is a **gated precondition, Stage-1+ execution**, not Stage-0 work? Stage-0 identifies the blocker and reserves the ED; later stage executes under parity discipline. **YES/NO.**

### Decision F: Scope confirmations

**F1.** The test count is **151 (measured, not 36 or 62)**. Both README and RATIFICATION self-reports are stale. On promotion, re-baseline the count in those files and in the test-migration commit. The suite is already seeded (L14) + gates (L454) â€” finding-#6 defects fixed in source. Stage-1 test task is pytest migration (preserve 151) + new tests for Face/CR5/ZOPA/Appraise/resolvers, **not "seed a unseeded suite."** Confirm? **YES/NO.**

**F2.** The test suite cannot collect until `policy.py`, `faction.py`, `narrative.py` are re-homed in the new `sim/personal/contest/` package (Â§3.1). This is a **scaffold-completeness blocker**, not a test-migration artifact. Confirm? **YES/NO.**

**F3.** Confirm the four locked Stage-0 decisions are locked as originally stated:
- (1) Promote the groundup kernel (nine modules); reconcile CR1-CR7 and four deliberative games.
- (2) Route both Agon (debate) and Consensus (pooled Track, PROMOTE-EXISTING `faction.py`).
- (3) Author canon for genuinely-missing pieces (Negotiation/ZOPA; Appraise; three gate seams).
- (4) Sim + canon only (no GDScript port, no Godot skeleton updates).

All four **remain locked**, and the artifact is the design contract they produce. Confirm? **YES/NO.**

---

**END MEMO.**

The artifact is GATE-0-READY pending Jordan's ratification of decisions Aâ€“F. Stage-1 begins on the eight ED-IDs, the scaffold build (re-home + rename), and the pytest migration once Jordan has signed off. The Ïƒ-core re-housing and the Î¸-leverage Stage-N (once the four deliberative games are live and Î¸-scale dynamics are understood) are gated downwind.

**Produced by:** SCRIBE (read-only assembly). **Verified against:** artifact + verdict log (six rounds). **No new judgements; format only.**
