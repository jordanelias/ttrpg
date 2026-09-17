# Working records — the three lens reports' full tables

## Status: WORKING RECORD (not canonical design text) — companion to `00_synthesis.md`
## Date: 2026-08-06 · Lane: SC

These are the tables the synthesis compresses. They are reproduced because the synthesis states
conclusions and a future reader needs the enumeration behind them. Provenance: three read-only
Fable 5 `valoria-critic` lenses run in parallel with disjoint mandates. **Claims here carry the
lenses' own confidence, not the orchestrator's** — only the claims re-verified in `00_synthesis.md §1`
are banked. Anything below not in that verification log should be re-checked before it is relied on.

---

## A — Lens 1: primitive verdict table (classification per primitive)

Classifications: **INERT** (defined, never read, or cannot change an outcome) · **DOMINATED** (never
using it is never worse) · **REDUNDANT** (a second primitive already does this job) ·
**CONFIGURATION-MASQUERADING-AS-MECHANISM** · **UNDERSPECIFIED** · **LOAD-BEARING**.

| Primitive | file:line | Class | Note |
|---|---|---|---|
| Persuasion Track 0–10 + bands | v30:91-95; resolver.py:79-93 | LOAD-BEARING | Only outcome-banding primitive; wired in kernel and stub |
| Audience resistance | v30:94; wrapper.py:42-55,74-77 | **INERT** | Derived, never consumed; registry self-declares PARTIAL |
| Per-exchange resistance erosion (ED-864/295) | v30:379 | **INERT** | No code anywhere — yet the doc used it to *retire* the live Deadlock drop |
| Face_max / Face_current (Gate A) | primitives.py:132-149 | **INERT** | Pure view nothing reads; would `TypeError` via public API (F2) |
| Standing (0–10, ethos-built) | primitives.py:31-47 | LOAD-BEARING | Feeds Readiness + Resonance.leak — the real Face substrate |
| Face strip / strain channel | resolver.py:404-419 | PARTIAL, doc **stale** | `strip_points` fires; doc says it never does (F3) |
| Rattled | v30:244-246 | **INERT** | Zero occurrences in any sim `.py` |
| Strain + Cha-modifier ×3 + Focus defence ×3 | v30:189-196,500-501 | **INERT** | Two derived stats parameterizing a formula no code evaluates |
| Concentration / Spent | v30:259-261; primitives.py:49-56 | **REDUNDANT ×3** | Three coexisting stamina models; kernel exhaustion → *clinch loss*, not a −2D turn |
| Doubt Marker | v30:212-216 | **INERT** + atomization defect | Trigger header lives only in infill:30; effect bullets dangle header-less in the skeleton |
| Terminal Doubt (ED-1060) | v30:217-220 | UNDERSPECIFIED (deliberate) | But cost-half wired, payoff-half not → dominance shipped **inverted** |
| CR5 self-Face backfire | rhetoric.py:413-454 | LOAD-BEARING | Wired, standing-bounded, cited==applied; reachable only bypassing the wrapper |
| Momentum spend | v30:172 | **INERT** | Only the post-contest *grant* exists (stub) — a different primitive |
| Recall +2D (+ ED-617 exhaustion) | v30:169-171 | **INERT / REDUNDANT** | `Dossier.present` already is "cite a source, per-source exhaustion, diminishing corroboration" |
| Corroborate +1D | v30:162 | **INERT / REDUNDANT** | Kernel `support` move is the working analogue |
| Prep +1D / Findings +2D | v30:533-546 | **INERT** + UNDERSPECIFIED | KU-1 cap adopted with no value and no guard |
| Faction boost + `guilds_boost_for` (ED-1061) | dictionaries.py:404-487 | **INERT / REDUNDANT with `Pressure`** | Consumed only by `_kernel_tests.py:1133` |
| Four Styles | dictionaries.py:90-134 | LOAD-BEARING in kernel, **API-unreachable** | See F1 |
| Genre via stasis (CR4) | rhetoric.py:91-243 | LOAD-BEARING (armature-gated) | Same reachability hole |
| Orientation | rhetoric.py:393-410 | PARTIAL | `orientation_channel()` self-documents as "RESOLVES NOTHING" |
| Stasis ladder | primitives.py:11-25 | LOAD-BEARING | `is_pre_merits`/`is_higher_order_reframe` have no consumer — JURISDICTION is a label |
| Adjudicator armature | armature.py:191-451 | LOAD-BEARING (kernel), [SEED] magnitudes | API-unreachable |
| Appraise ch.(a) audience read | v30:146-158 | **DOMINATED** — by the repo's own ED-SC-0012 ruling | Execute the fold |
| Appraise ch.(b) armature read | appraise.py:140-177 | UNDERSPECIFIED wiring | No `appraise` in `VALID_KINDS`; no cost, no Move |
| First-to-Speak | v30:268-272 | **INERT** (kernel) / **MISIMPLEMENTED** (stub) | Kernel iterates `(A,B)` forever; stub has the silent A-bias (F7) |
| CLASH/REINFORCE/CROSS/TIE | dictionaries.py:283-323 | **CONFIGURATION-MASQUERADING-AS-MECHANISM** | §4 Step 4 — the doc's centrepiece — is a table with no engine |
| Regroup / Concede | v30:228-230 | **REDUNDANT / INERT** + DOMINATED | |
| Obligations + interruption rule | v30:306-358 | UNDERSPECIFIED (engine) | No code object; binding fires with **no authority check** |
| Wager Obligations | v30:325-352 | CONFIGURATION | Correct as data post-DISTILL |
| Contest Fatigue | stub.py:80,126,250-257 | LOAD-BEARING (stub only) | The only post-contest consequence with working code |
| Chain Contests / Deadlock | v30:368-383 | **INERT** | Retirement rationale cites a rule that exists nowhere |
| Panel / weighted VoteAtClose | resolver.py:96-145 | LOAD-BEARING | Fully wired, proceeding-reachable |
| Evidence / Dossier | primitives.py:282-310 | LOAD-BEARING | The repo's real M3 seed |
| `Pressure` | contract.py:69-77 | LOAD-BEARING — **no canonical prose owner** | Mirror image of the doc's inert prose mechanics |
| §9.3/§9.4/§9.4b thread riders, Chamber Violence, Niflhel, Let It Ride | v30:551-585 | **INERT** | Let It Ride has no enforcement object — a Record is its natural carrier |
| §7 asymmetric numbers | v30:390-398,624-641 | CONFIGURATION (correctly) | But "halved resistance" halves a number nothing reads |

---

## B — Lens 1: the P1–P45 / M1–M14 delta

`PRESENT` / `PARTIAL` / `ABSENT` / `CONTRADICTED-BY-OURS`.

| P# | Verdict | Evidence |
|---|---|---|
| P1 Standing (per-body) | PARTIAL | Per-*bout*, resets at contest end; not record-derived |
| P2 Precedence | ABSENT | First-to-Speak is a 2-party info edge, itself unimplemented |
| P3 Commitment | PARTIAL | Beliefs reward consistency; nothing makes a past position citable *against* you |
| P4 Immunity | **CONTRADICTED** | Exists only as entity special-cases (PP-349 Church shield v30:646; Niflhel v30:581) — scripting drift where the uploads have an `Office.immunities` config |
| P5 Stasis Gate | PARTIAL | Ladder wired, but upward-only *reframe*, not win-to-advance; no per-stasis victory; **no raise-JURISDICTION-at-a-cost trade — we fail exactly the "fails when" clause** |
| P6 Claim | PARTIAL | `EvidenceItem(ground, weight, appeal)`; no premises/warrant/provenance |
| P7 Attack ×3 | **ABSENT** | One `rebut` verb, venue-gated off, pure capped attrition. The uploads' entire anti-collapse device |
| P8 Critical Question | ABSENT | No burden-shifting question verb |
| P9 Burden token | PARTIAL | Frozen inside win-conditions (`ProofBar`); never moves during play |
| P10 Forum Challenge | **CONTRADICTED** | v30:39 makes an adjudicator shift *end the contest*, where the uploads make *translatio* a costed move |
| P11 Evidence Array | PARTIAL | Weights hidden, but symmetric-hidden; no probe verb, no count/category reveal |
| P12 Agenda Control | ABSENT | Proceeding fixes the question; framing is never a move |
| P13 Speaking Order | ABSENT | Hardcoded `(A,B)` |
| P14 Division | PARTIAL | Vote counts exist; chair's motion-order power absent |
| P15 Veto | ABSENT in-lane (Stay ≈ strategic partial) |
| **P16 Recorded Defeat** | **ABSENT** | Nothing persists a lost position as a citable object. Chain Contests carry a *scalar* |
| P17 Clock Consumption | PARTIAL | `Venue.budget` is the scarce container; `pass` is a *fault* — burning clock is punished, never tactical |
| P18 Enactment Clock | ABSENT (cousin: Obligation durations) |
| P19 Competence/Quorum | PARTIAL | No overlapping competences, no quorum |
| P20 Drafting Right / P21 Return-Unsigned | ABSENT |
| P22 Sortition / P24 Narrow-Widen / P25 Quota / P26 Term | ABSENT | Succession is selection-by-single-contest |
| P23 Threshold Election | PARTIAL | Majority only; no supermajority parameter |
| P27 Avoidance | PARTIAL (conceptual) | The armature asymmetric gate-off is a conflict-of-interest rule for the judge |
| P28 Standing Report | ABSENT | v30:95's "permanent knowledge" is asserted; no object, no decay |
| P29/P30/P31 | ABSENT in-lane (FI/WR) |
| P32–P34, P36–P38 | ABSENT in-lane (SE/FA); P34's shape appears degenerately as flat violation tables with **no detection dial** |
| P35 Hostage/Bond | PARTIAL | Wager is a future-conditional pledge; no held-asset forfeiture |
| P39 Reservation Value | **ABSENT — self-admitted** (v30:702) |
| P40 Side Payment | ABSENT in-lane |
| P41 Scaled Compromise | **CONTRADICTED** | Our compromise is a GM-narrated band; Total Victory *rewards* the clean winner (+1 Momentum). Nothing charges a winner for what winning cost |
| P42/P43 Cheap talk / costly signal | ABSENT / PARTIAL | Every outcome auto-binds; no non-binding default |
| P44 Positional Pricing | ABSENT |
| P45 Shared Loss | **ABSENT — correctly.** Upload 3 §9 deletes it for single-player. Do not add |

| M# | Verdict |
|---|---|
| M1 Standing | PARTIAL (not per-body, not record-derived) |
| **M2 Scope** | **ABSENT** — the spine, per upload 3 §4 |
| M3 Concealed Value | PARTIAL — two instances (Dossier weights, hidden `armature_position` with banded reveal); no per-actor `Estimate`, no decay, no unification |
| M4 Probe | PARTIAL — `appraise_armature` is a probe with no Move, no cost, no burden side-effect |
| M5 Claim / M6 Attack | PARTIAL / ABSENT |
| M7 Gate | PARTIAL — stasis yes; burden-as-parameter no; escape no |
| M8 Floor / M9 Block | ABSENT in-lane (Stay partial) |
| **M10 Record** | **ABSENT** — Obligation-clocks persist but are not citable; no `cite()` verb |
| M11 Clock | PARTIAL — durations exist ad hoc; no tiered clock |
| M12 Compliance | ABSENT in-lane (the NPC priority-tree block is a binary degenerate case) |
| M13 Settlement | ABSENT — negotiation stub; scaled compromise contradicted |
| M14 Selection | PARTIAL — Succession selects by agôn + institutional vote; no method/threshold/quota/avoidance config, no investiture-confers |

---

## C — Lens 2: reachability table

| Branch | Reachable in the 8 canonical proceedings? | Why not |
|---|---|---|
| FACT stasis | Church Tribunal only (start) | — |
| DEFINITION stasis | **Doc: never** — the doc has no reframe action at all. Code: only from the FACT start via `Move("shift")`, used only by `fallback_ladder`, never on the live path | Doc-side the ladder above the start value is decorative |
| JURISDICTION / CONSEQUENCE / FEASIBILITY | Doc: never. Code: kernel-direct only | **Projection-primary (+1D for Vision/Insinuation) is unreachable in all 8 proceedings under the doc's own procedure.** ED-1062 fixed Memory and left Projection identically broken |
| CR4 +1D at all | Never on any production path | Armature-gated; wrapper never builds one |
| Armature δσ; CR5 backfire | Kernel-direct / tests / harness only | Zero production callers |
| Asymmetric gate-off | Fires nowhere; the only armature caller leaves it False even for church_tribunal | Known since Gate C (`verdict_log.json:317`), unfixed |
| Panel / VoteAtClose | **YES** — guild_arbitration | The one Gate-B closure genuinely reachable |
| Attunement- / Cognition-primary pools | Never — `primary_attribute` is display metadata | §3's whole character-differentiation design fires nowhere (ED-SC-0004) |
| Doubt Marker / Terminal Doubt | Never (no code) | |
| Appraise as a costed action | Never | |
| `rebut` | Never in the 8 (all inherit `allow_rebuttal=False`) — and `counterpuncher` auto-clinches there (F4) | |
| `hard` before an Expert Judge | Never licit (`learned=True, hostile=False`) → always a barred-device clinch loss. Defensible; undocumented in canon | |
| Evidence dossiers | Never on the live path (dispatch builds bare-faculty contestants) | |
| §7.1 Excommunication, §7.2 Succession, §7.3 Heresy, §11 Hybrid | No personal-scale code | |

---

## D — Lens 2: the no-GM defect register

Valoria has no GM — the engine resolves everything. Every entry is a resolution-authority hole.

| Site | Text | Engine rule needed |
|---|---|---|
| infill:19 | "The Game Master (GM) sets the format at setup" | Superseded by `modes.PROCEEDINGS` — **stale prose contradicting a shipped rule; delete** |
| infill:20 | "GMs should not call for a contest when…" | Slate/dispatch predicate exists; delete prose |
| infill:23 | "If the question does not clearly favour one genre, the GM assigns" | **Directly contradicts CR4.** Doc-internal conflict; delete |
| v30:93 | Track start "GM-set" | Exists in code (`CANONICAL_TRACK_START`); rewrite |
| v30:104, 450 | "Inquisitor sets" exchange count 1–5 | **No rule anywhere**; code hardcodes max. Needs length = f(Evidence Track, CI, target Standing) |
| v30:113, 264, 278 | Hidden GM ledger / records / reveals | `Bout(record=True)` log exists; rewrite as engine log |
| v30:153 | "GM identifies a wrong boost" on failed Appraise | Deterministic wrong-axis rule exists (`appraise.py:154-163`); rewrite |
| v30:279 | "GM narrates partial outcome proportional to final position" | Needs a compromise renderer — and P41 scaled compromise is the mechanic behind it |
| v30:302 | "Reputation shift (**GM-set magnitude**)" | **No rule anywhere.** Needs band→magnitude, per the ED-SC-0002 composition pattern |
| v30:308 | Obligation cap "GM guidance note" | Ledger config |
| v30:330 | Wager "Condition partially met: **GM judgment**" | The row supplies its own default ("no advance, no decay") — promote the default to the rule |
| v30:350 | "require the GM/engine to confirm" | Strike "GM/" |
| v30:409, 429 | Succession length "Adjudicator may set 3-7"; "Adjudicator decides ties" | length = f(claimant-support spread); tie rule deterministic (mirror `select_censure_target`) |
| v30:485 | "Inquisitor death … is a **Game Master event**" | Route to the mortality/NPC-AI layer — as written this closure condition can never fire |
| v30:546 | Findings citation "GM sets scope: the Finding must be relevant" | **The kernel already has the engine-shaped answer:** `EvidenceItem.ground == live stasis` |
| v30:567 | §9.4b C3 "curiosity or fear, GM judgment" | Truth-indexed Disposition-shift rule |

---

## E — Lens 3: the record-spine trace

Every contest output in the wired campaign loop → its consumer → verdict.

| # | Output | Producer | Consumer | Verdict |
|---|---|---|---|---|
| 1 | §10 vote loser Mandate −1 | `parliamentary_vote.py:207-218` | `Faction.L` scalar | **MODIFIES** — and permanently (F6) |
| 2 | Winner Domain Echo (band→degree, genre→stat) | `parliamentary_bridge.py:205-213` → `echo_transport` | `Faction.adjust` | **MODIFIES.** Nothing downstream ever asks *why* L moved |
| 3 | Emergency-council verdict echo | `scene_dispatch.py:334-343` | same | **MODIFIES** — `actor_faction == target_faction`; the faction debates itself |
| 4 | **Projection channel "+1D on first Domain Action"** | — | **not implemented**; flattened to an `I` stat delta | **DEAD-ENDS — the most damning row.** The one canonical output with a genuine *guard* shape was the one the stat-delta-only interface could not carry |
| 5 | `scene.contest_resolved` Key → KeyLog | `echo_transport.py:416-438` | **tests only** | **DEAD-ENDS.** A write-only ledger |
| 6 | Chronicle (turning point, decisive appeal) | `narrative.py:112-154` | nothing stores it | **DEAD-ENDS** |
| 7 | Succession split ratio | `faction.py:86-118` | none — docstring says consequences "NOT modelled here" | **DEAD-ENDS** |
| 8 | Territory-transfer motion | `parliamentary_bridge.py:165-177` | territory ownership | **MODIFIES** (strongest strategic consequence). But no producer of `world.casus_belli` exists — a contest cannot mint a CB |
| 9 | `parl_transfer_used_this_arc` | `parliamentary_bridge.py:143` | blocks a second attempt | **GUARDS — the only genuine instance in the entire wired loop, and it is a frequency limiter** |

**Doc-side outputs with zero code:** Obligations incl. NPC-priority-tree blocking · Disposition and
Reputation shifts (`mc_v18.py:198-209`: Disposition "does not exist anywhere on the aggregate
strategic World") · Conviction Scars persisting across chain contests · chain-contest track carry-over ·
Excommunication → Standing −1 / Dishonored · MS +1.

**Note:** the legacy stub carried Contest Fatigue and the §6.2 Scar hook and was retired from dispatch
by ED-SC-0006 — **kernel promotion narrowed the consequence surface.**

---

## F — Lens 2: the special-case register (config vs mechanism)

| Bespoke rule | Collapses to a config field? |
|---|---|
| Royal Audience roles / halved resistance; Church Tribunal track 6 / FACT start | Already config ✔ |
| Church Tribunal + Excommunication "no accused corroboration" | One field: `corroboration: false` |
| **§7.1 Excommunication Tribunal wholesale** | A Proceeding row (track 7, budget 1–3, halved, no corroboration) + a consequence table. Differs from Church Tribunal in **numbers only** — upload 3 §8's "two fields" observation, confirmed. Currently ~20 lines of prose |
| §7 "advantaged orator takes 0 strain from CROSS" | A flag — but the strain system is doc-only; symptom, not config |
| Grand-only per-source Recall (ED-617) | `recall_scope` field — or one rule everywhere; the Formal exemption is rationalized as "impractical", i.e. not load-bearing |
| Succession §7.2 per-faction adjudicators / Standing ≥ 5 / length 3–7 | Data table ✔; eligibility is exactly upload 3's `Body.entryGate`; length needs a rule |
| §7.2.1 split ratios | Data table (and internally incoherent — tracked, ED-SC-0016) |
| **§7.3 Heresy lifecycle, 8 closure conditions** | A Clock + Record + interruption-rule composition. **ED-SC-0012's own interruption generalization was never applied here** — ~49 lines of bespoke state machine |
| §9.7 Niflhel bar + bespoke Ob | **Scripting drift.** The config exists: `Faction.parliamentary=False` |
| §9.2 coalition shared Concentration | Config on a doc-only system |
| ED-1060's banded/tally split | A special case *created by* two win-condition families exposing different quantities. Both share `adv`; one rule on `adv` generalizes |
| Tracker tri-state + `use_tracker` ValueError machinery | Dissolves entirely under a burden-parameterized gate (Fork A) |

---

## G — Lens 2: dominance arithmetic (doc-side §4 algebra)

Baseline: equal orators, 11D each, TN7 (μ 0.40/die, σ 0.80/die). E[net] = 4.40, sd = 2.65;
margin D = netA − netB ~ N(0, 3.75); E[m | win] ≈ 2.99.

**Obscuring vs Revealing:**

| | Immediate | Marker EV | Total |
|---|---|---|---|
| Revealing win, R=1 | E[(m−1)⁺ \| win] ≈ **2.1** + strain + initiative | — | **2.1+** |
| Obscuring win, exchange 1 of Formal | 0 | ≈1.55 × P(opp wins ≥1 of 2) ≈ 0.75 | **≈1.2** |
| Obscuring win, final exchange | 0 | 0 | **0** |

Revealing dominates at every resistance value (at R=2: 1.4 vs 0.7 — resistance discounts the marker
identically). Only surviving niche: a heavy underdog (8D vs 13D) early — 1.0 vs 1.4 — and CR5 charges
min(2, Face) on a deg-0 Obscuring move, whose probability is *maximal for exactly that underdog*.

**CROSS** is a real verb for underdogs only: 8D vs 13D, CLASH drifts ≈1.4 track/exchange to the
favourite plus strain; CROSS caps the favourite at ≈1.0 and zeroes strain. A legitimate matching game
— but on QUALITY terrain (7 of 8 proceedings) genre carries no +1D, so the four Styles reduce to one
bit (match?) plus a dominated bit.

**Forfeits:** Concede a Point pays 1 track + 1 strain for +1D ≈ +0.25 expected track — never correct.
Regroup pays 1 track + a forfeited exchange to refill a pool whose exhaustion costs ≈1.2 once, and in
a 3-exchange Formal, Spent first bites at exchange 3 — when the refill has no future to pay for.

*Confidence: medium — analytic approximations. The falsifier is a ~10-minute Monte Carlo over the doc
algebra; it was not run.*

---

## H — Lens coverage and honest gaps

- **Lens 1** read all listed docs and the kernel package; `agon_harness.py`/`_kernel_tests.py` by
  targeted grep; `policy.py`/`faction.py`/`narrative.py` and `engine/cross_scale/*` not read (its
  Domain Echo row is marked [UNVERIFIED] — the orchestrator closed it).
- **Lens 2** read the full kernel package, `sigma_leverage.py`, the duality doctrine, all four
  uploads; `parliamentary_stay.py` header-level; `narrative.py` unread; `_kernel_tests.py`
  spot-checked.
- **Lens 3** read the canonical doc, the cross-scale bridges, the faction sim, the duality doctrine,
  and all three prose uploads in full; `resolver.py` internals and the Gate-C modules left to lenses
  1/2; `season_manager.py` not read — **the orchestrator read it and closed F6.**
- **All three** were instructed that `audit/2026-07-05-fable5-social-contest-audit/` was the prior
  ratified audit. **It does not exist** (evacuated 2026-08-05). Every "already ratified" claim rests
  on `registers/editorial_ledger_sc.jsonl` and the Gate-A/B/C packets instead.
