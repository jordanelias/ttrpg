# 03 · INQUIRY — discern a truth

## Status: **PROPOSED — nothing ratifies.** 2026-09-04. Branch `claude/social-contest-system-review-dn2y5d`, HEAD `1e163ee`.
## Grade per `CLAUDE.md` §0.2: **PAPER.** Nothing in this document runs. Its parts run — `ProofBar`, the inquisition venue, `formal_grounds_check`, `invoke_stay`, `Dossier`, `LedgerTag` all execute today in isolation — and the sequence that composes them does not. The grade changes when §9's falsifiers execute, not when this file is merged.
## Consumes `00_BRANCH_SHAPES.md` §2 (the shared spine). The spine is owned by `01_SPINE.md`; where this document names a spine object it is a **consumer**, and any disagreement is reported here, not resolved here.
## Compliance target: `architecture/meta/04_CODE_ARCHITECTURE.md` (PR #362) and `architecture/` (PR #357) — both **PROPOSED, HELD BACK IN FULL**. A shape constraint, not canon (`CLAUDE.md` §0.05).

**What a PR #362 veto costs this branch.** The three things this branch actually needs from the kernel — `burden` selecting `ProofBar` on the `church_tribunal` row, the restored three-way grounds check, and the finding write — are all **kernel-local or SE-local** and survive a veto unchanged. What dies with a veto is the *vocabulary*: `Act.actor`/`Act.via`, the `Seat`-remit eligibility on `open_case`/`determine`, `Receipt`, the write gate, and the degree-keyed `writes:` column. Without them the branch reverts to a direct `ledger_add` from the resolver's caller and an eligibility check written in Python rather than declared in a table. **The mechanics are unaffected; the accountability is.** That is a claim about a future veto, not a measured one.

**Jordan's ruling, 2026-09-04 (verbatim):** *"negotiated agreement bind in scene. in fact, everything that occurs within a scene should bind or else it's as if time doesn't exist within a season."* This branch is written to satisfy it, and §4/§5/§6 below say where each write lands and when. On current evidence there is **no conflict with PR #362 for this branch** — see §4.6, which works the one hard case (the Stay) out with anchors. The architectural verdict for all three branches belongs to `01_SPINE.md`; this document reports what it found and does not legislate.

---

## §0 · Method, and what was read

**Read in the working tree, in full:** `systems/social_contest/sim/contest/{wrapper,resolver,primitives,contract,modes,rhetoric,armature,appraise,degree_extension}.py` (the sections cited), `systems/social_contest/sim/parliamentary_stay.py`, `systems/factions/sim/{tribunal,excommunication}.py`, `systems/settlements/sim/ledger.py`, `systems/fieldwork/sim/fieldwork.py`, `engine/cross_scale/{scene_dispatch,echo_transport}.py`, `engine/substrate/keys.py` (registry + `KeyLog`), `engine/autoload/scene_slate.py`, `systems/social_contest/social_contest_v30.md` §7/§7.1/§7.3/§10.1, `references/KEY_INDEX.md`, `engine/engine_params/key_types.json`, `systems/npcs/npc_behavior_v30.md` §3.2, `references/id_reservations.yaml`. **Research:** `research/rhetoric_oratory_contest/rhetoric_oratory_contest_research.md` §1.4, §5.1–5.3, §7.2, §9.3, §9.7, §12.3, §12.4. **Snapshot** (`v30-snapshot-2026-06-28`, not in `main`): the deliberation critique, `AUDIT_RECONCILED.md`, `VENUE_VALIDATION.md`, `BALANCING_PASS_2026-06-05.md`. **Live audit:** `audit/2026-08-06-social-contest-three-lens-audit/` (00, 01, 02, 04). **Held-back proposals:** PR #362 `01_AXIOMS.md`, `04_CODE_ARCHITECTURE.md`, `09_WORKED_EXAMPLES.md`; PR #357 `verb_table.yaml`, `rosters.yaml`, `hole_register.yaml`.

**Discipline.** No `pytest` was run (instructed). Nothing under `systems/`, `engine/`, `canon/` or `registers/` was edited. This is the only file created. Every `path:line symbol` below was read this session; where the shape spec's anchor and the tree disagreed, the tree wins and the row is marked AMENDED or REFUTED. Every invented number carries `[SEED]`. Every "no dominant option" statement is an **upper bound** — no AI-vs-AI best-response sweep was run (`04_ners_audit.md`'s rule, and ED-SC-0021's falsifier is still unrun).

---

## §1 · Verification of `00_BRANCH_SHAPES.md` §4, element by element

Twelve elements. **Five CONFIRMED, six AMENDED, one REFUTED.** The amendments are the useful part: three of them are defects that would have shipped.

| # | element (§4 of the shape spec) | verdict | anchors |
|---|---|---|---|
| **E1** | `inquiry` is a STUB row in `GAMES`, sourced to v30 §7 | **CONFIRMED** | `wrapper.py:236 GAMES`; the row at `wrapper.py:243-244` (`"inquiry": {"resolve": _stub("inquiry"), "status": "STUB", "source": "social_contest_v30 §7 Church Tribunal / Inquisition (author-new — later stage)"}`); `_stub` at `wrapper.py:220`; pinned by `_kernel_tests.py:696-703` |
| **E2** | `ProofBar` supplies burden = ACCUSER, and the burden-holder loses on a stall | **CONFIRMED** | `resolver.py:67 ProofBar(bar, challenger=A)`; `:70 net = s.adv[ch] - s.adv[df]`; `:71` challenger wins iff `net >= bar`; **`:72 if closing: return df`** — the defender takes the close. This is exactly `00_synthesis.md:346-348`'s "burden family in disguise" |
| **E3** | The biased track start is a handicap that cannot express *silence convicts*, and becomes derivable under `burden` | **CONFIRMED** | `modes.py:476 CHURCH_TRIBUNAL_TRACK_START = 6.0`, consumed at `modes.py:497 track_start=`; the canon it cites is real (`social_contest_v30.md:396` "Persuasion Track starts biased at 6") and **disagrees with §7.1's own "starts at 7"** (`:629`) — one canonical number, two canonical values, already a live drift |
| **E4** | `tribunal.py` dropped the three-way grounds check; v30 has all three | **CONFIRMED** | `tribunal.py:73 formal_grounds_check` returns `ci >= 40 and church.L >= 4` and nothing else; its own docstring at `:78-81` says the Evidence/Obligation/2-convictions clause "is one of three alternative gates … not yet ported"; canon at `social_contest_v30.md:626` carries all three |
| **E5** | `support` dodges the silence clinch with no fault (the shape spec's I-I6 / F-I2) | **CONFIRMED, AND WORSE THAN STATED** | `resolver.py:345-348` (`pass` → `fault.yields += 1`, then `regroup()`); `resolver.py:349 c.reserve.spend(mv.kind)`; `resolver.py:350-351 if mv.kind == "support": c.reserve.regroup(); c.build_ethos(1); return` — **no fault of any kind**. `primitives.py:51 COST["support"] = 2` and `:52 REGAIN = 4`, so `support` is **net +2 reserve** and **+0.8 Standing** (`:33 BUILD = 0.8`) per exchange. Independently recorded three months earlier: `v30-snapshot-2026-06-28:designs/audit/2026-06-03-contest-groundup/AUDIT_RECONCILED.md:184-185` — *"`ProofBar` lets the defender win only by timeout, creating a stall incentive that interacts with the silence-clinch. **Not systematically explored.**"* Two independent rediscoveries; see §10 for how much worse it is in this venue specifically |
| **E6** | The Case is a `LedgerTag` + a recurring `SceneSlot`; the stage is a `KeyLog` Query, not a store | **CONFIRMED, and the reasoning strengthened** | `ledger.py:35-36 LedgerTag(kind, key, value, created_season, ttl)`; `:47 ledger_add`; `:69 ledger_sweep`; `scene_slate.py:25 SceneSlot`, `:34 queue_scene`; `keys.py:336 KeyLog`, `:367 append`, `:459 content_hash`. **The strengthening:** the shape spec cut `Record.stages` on the ground that an aggregate cannot be stored (`T-a`). That is right but incomplete — canon *does* require one stored decision, the **declared duration** (`social_contest_v30.md:450`: "2-4 seasons (**Inquisitor declares duration at filing**)"), which is not derivable from anything. The clean split: *the declared term is stored* (`LedgerTag.ttl` + `created_season`, or PR #362's `Tenure.term`, `01_AXIOMS.md:1138 T-n`); *the stage reached is derived* (a count over the log). §7 records the consequence: `verb_table.yaml:349`'s `writes: ["Record.exists", "Record.stages"]` carries a field whose job is already done twice over |
| **E7** | `PROCEEDINGS["church_tribunal"]` gains `burden: "ACCUSER"`, `win = ProofBar(bar)` | **AMENDED — the edit is a MERGE OF TWO VENUES, not the addition of a field** | `PROCEEDINGS["church_tribunal"]` (`modes.py:495-499`) resolves through `proceeding_venue` (`:536`), whose only branches are panel → `VoteAtClose`, tracker-on → `PersuasionTrack(start=6.0)`, else `TallyAtClose` (`:556-562`). **It has never used `ProofBar`.** The venue that does is `inquisition_hearing_venue` (`modes.py:181`, `win=ProofBar(bar=2.5)` at `:196`), reachable only through `CROSS_CULTURAL_VENUES` (`:318`) — and `build_contest` **rejects any string venue not in `PROCEEDINGS`** (`wrapper.py:127-130`). So the tree carries **two inquisition surfaces with different win-conditions and different fault configurations, and the reachable one has no burden.** The branch's core edit is to collapse them onto one row |
| **E8** | "silence convicts" is carried by `evasion_strikes=1` | **AMENDED — wrong fault** | `DefeatCatalogue.check` (`primitives.py:272-279`) maps `evasion_strikes` → clinch reason **`"evasion"`** (raised by *arguing off the live issue*, `resolver.py:381`) and `yield_strikes` → clinch reason **`"silence"`** (raised by *declining to answer*, `resolver.py:346`). `inquisition_hearing_venue` sets `evasion_strikes=1, yield_strikes=2` (`modes.py:197-198`). **Silence therefore convicts on the SECOND refusal, not the first**; the `1` the shape spec cites belongs to a different nigrahasthāna. Both faults have Nyāya names in the code — `ananubhāṣaṇa` (`:347`) and `arthāntara` (`:381`) — and they are different offences in the doctrine too (research §5.1 `:206`) |
| **E9** | S1.1's grounds expression `ledger_get("Leverage", f"evidence:{accused}").value ≥ 3` and `count(ledger_get("Precedent", f"conviction:{accused}")) ≥ 2` | **AMENDED — neither clause can execute** | `ledger_get(ledger, kind)` (`ledger.py:65`) takes **no key argument and returns a list**; `.value` on it is a type error. Worse, the conviction count **cannot exceed 1**: `ledger_add` dedupes by `(kind, key)` and **refreshes in place** (`ledger.py:53-57`), so a second `Precedent("conviction:<accused>")` overwrites the first. The shape spec's own S4 writes exactly that key, making its own S1.1 clause permanently false. Fix by the spec's own §2.3 rule (E6): the conviction count is an **aggregate** → a `KeyLog` Query over `scene.investigation_resolved` with `finding == "guilty"` and matching `subject_id`. The evidence count is a **declared scalar** → `LedgerTag.value`, read with an exact-key scan |
| **E10** | I-I5 "one active case per accused per jurisdiction" is MECHANICAL via `ledger_add` dedupe | **AMENDED — dedupe is a silent overwrite, not a refusal** | `ledger.py:53-57` replaces the prior tag and returns `None`. A second `open_case` would therefore **succeed and silently reset the case clock**, which is worse than a duplicate. MECHANICAL requires an explicit `ledger_has(ledger, "Leverage", f"case:{accused}")` pre-check (`ledger.py:61`) returning `Refusal(duplicate)`. Canon backs the rule at `social_contest_v30.md:472` (§7.3.3, one Investigation per target per Cardinal Justice's jurisdiction; cross-jurisdictional may run in parallel) |
| **E11** | The finding rides `KEY_TYPE_BY_SCENE` gaining `"inquiry": "scene.investigation_resolved"` (spine §2.1) | **REFUTED — the transport cannot carry this key** | Three independent blocks. (i) `emit_scene_echo` hardcodes the payload as `{scene_id, outcome, participants}` (`echo_transport.py:436-440`), while `scene.investigation_resolved` **requires `scene_id`, `subject_id`, `finding`** (`references/KEY_INDEX.md:958`, `engine/engine_params/key_types.json`), and `KeyLog.append` → `TypeRegistry.validate_payload` **raises `KeyValidationError` on a missing required field** (`keys.py:367,378,308-320`). (ii) the whole emission is inside `if er.fires and … er.delta != 0` (`echo_transport.py:421`) — a **faction stat delta**, which a tribunal against a Person need not produce. (iii) `_OUTCOME_BY_DEGREE` (`echo_transport.py:114`) has no `inquiry` family, and the map's own comment (`:106-107`) calls adding a scale without its resolver "shape-divergence (guardrail)". **The finding is emitted by `determine`, not by the echo transport** — which is also what Jordan's in-scene ruling requires, so the refutation and the ruling point the same way |
| **E12** | S2.3 routes the Evidence Track through `advance_evidence` | **AMENDED — that function is a stub and writes nothing** | `fieldwork.py:54 advance_evidence` returns `stubwire.stub_resolve(...)`, design-gated on ED-916. It is a typed no-op. The evidence scalar must be written by the inquisitor's own act onto the case tag |

**Two further amendments, minor but concrete.** (a) The shape spec's S4.1 payload `{subject_id, finding, public, sentence}` **omits the required `scene_id`** and would fail `validate_payload`. (b) `references/id_reservations.yaml:195` **does** carry the SC lane's `next_free: 33` — §6 of the shape spec reports it could not be located.

**And one finding neither document has, which is the counterweight to E5.** Canon's only mechanical concession to the accused — *"Disadvantaged party (accused, petitioner) faces halved resistance (round up)"* (`social_contest_v30.md:392`, restated at `:632`) — **is inert.** `_derive_resistance` computes it (`wrapper.py:43-57`) and `Contest` carries it (`wrapper.py:169,194`), but `wrapper.py:331-332` states plainly that *"the resolver has zero 'resistance' references; `Venue.base_ob` is never set from it"*, and the `MECHANICS` row grades it `PARTIAL` (`wrapper.py:337`). So the venue currently implements **neither** canonical asymmetry: not the accused's halved resistance, and not the bar on accused corroboration (`social_contest_v30.md:630`). It does implement a free stall the accused was never meant to have. Both are missing, in opposite directions, which is why §10's dominance reading is not simply "the prosecution is too strong".

---

## §2 · What conflict class this resolves, why `agon` cannot — and whether this is a game at all

### §2.1 The class

**Asymmetric, burden-bearing, judged by a third party, about a past act.** The output is a *finding* — a truth-claim the institution will act on — not a right-claim and not a bargain. `01_AXIOMS.md:111 AX-3` is the axiom that makes the class distinct: *what is true and what is right are different kinds of thing … evidence moves what is held true.* An inquiry is the procedure that converts evidence into an institutional holding about what is true.

### §2.2 Why `agon` cannot

Not because `agon` is weak, but because three of its properties are wrong here, each verifiable:

1. **No burden.** The symmetric track is a race between two accumulators (`resolver.py:87 PersuasionTrack.track` = `start + scale·(adv[A] − adv[B])`). Nothing distinguishes *the party who must prove* from *the party who need only not lose*. `ProofBar:72` does exactly that in one line.
2. **No stall semantics.** The biased start (E3) is a **handicap**: it changes expected value and can be out-argued. `00_synthesis.md:350` states the distinction the tree cannot currently express: *"A handicap changes expected value; it cannot express silence convicts."* Under `PersuasionTrack` an accused who does nothing loses slowly; under `ProofBar` an inquisitor who proves nothing loses **at the close, by rule**.
3. **The bar is a dial the track has no analogue for.** Measured in the snapshot: `VENUE_VALIDATION.md:9` — equal skill → acquittal **1.00**; passive defence → conviction **0.97**; `bar 2` plus a skill gap → conviction **0.56** ("preponderance"), `bar 4` ≈ beyond-reasonable-doubt. The standard of proof is a first-class parameter of a `ProofBar` venue and has no representation on a track start.

### §2.3 The critique says Belief Revision already supplies the inquiry game. It is right, and the honest conclusion is that this branch is small.

The 2026-06-28 deliberation critique files inquiry under **already-handled**:

> `four-games FG-2/FG-3/FG-5` (low / already-handled): … **Belief Revision** (`npc_behavior §3.2` …) **already provides the inquiry game** … The residue is narrow: close the `state.belief_revised` Key emission … and optionally apply the existing **Sincerity Gate** so an instrumental win can't fake a conversion. **Editorial, not structural.**
> — `v30-snapshot-2026-06-28:…/critique.md:111`

I confirm the mechanism it names: `systems/npcs/npc_behavior_v30.md:391 §3.2` — an NPC revises a Belief when a Contest produces a decisive outcome against them **and** the winning argument used their Resonant Style. That is a working discern-a-truth outcome and this branch **adds no conversion mode, no second resolver, and no competing belief channel**. The Sincerity Gate is FI-owned (`systems/fieldwork/fieldwork_v30.md:419 §5.3`, Spirit TN 7 Ob 1) and is not duplicated here.

**Where the critique's framing is nonetheless too narrow, stated as a distinction and not as a rescue of the branch.** Belief Revision changes *what a mind holds*. A finding is *what an institution holds*, and it binds whether or not any mind was changed. The two are separately typed in the tree already, and the separation is not mine:

| | Belief Revision | a finding |
|---|---|---|
| key | `state.belief_revised` (`KEY_INDEX.md` state_transition family) | `scene.investigation_resolved` (`KEY_INDEX.md:948`) |
| carries | a revised belief | `subject_id`, `finding ∈ exonerated\|guilty\|inconclusive`, optional `sentence` |
| permanence | persistent | **indelible** (`KEY_INDEX.md:956`) |
| gate | decisive band **and** the loser's Resonant Style | the bar was met, or was not |
| can revoke a seat | no | yes — `01_AXIOMS.md:1160 T-o` is what a sentence *is* |

An unconvinced heretic who is nonetheless excommunicated is the ordinary historical case, and it is unrepresentable if the only output of a truth-contest is a change of mind.

**So: is this a game or a venue row?** **A venue row.** The later audit reached the same verdict independently and more bluntly — `04_reductive_audit_primitives_and_foundations.md:334`: *"**ABANDON THE FRAMING.** Keep `settle()` as the one genuinely new build; **Inquiry and Consensus are venue rows, not games**"*, with `:224` placing `church_tribunal`, `inquisition_hearing`, `excommunication_court` and `GAMES inquiry` in one type whose *"differences are track bias (EV-only) and judge `[SEED]`s"* and where *"burden is the one variety-bearing parameter."* Two documents, ten weeks apart, on different evidence, agree.

**What that leaves this branch, said plainly and without inflation:**

- **one field** on one `PROCEEDINGS` row (`burden`), consumed by the spine's win-condition selector;
- **one venue merge** (E7) — the ProofBar inquisition venue folded onto the reachable canonical row, deleting the second surface;
- **one restored guard** in FA (`tribunal.py:73`);
- **one existing module wired** (`parliamentary_stay.py:101 resolve_stay_lift`, zero callers today);
- **one fault-configuration fix** in the kernel (E5/E8), which is not inquiry-specific and benefits every bar venue;
- **one write** — the finding — and it is the only genuinely new behaviour;
- **zero** new resolvers, new keys, new descriptors, new stores, new Move kinds, new tracker classes.

That is a venue row plus a write. Anyone reading this document as licence to build an `inquiry.py` has misread it.

---

## §3 · Historical grounding, with tiers, and where the corpus's confidence is low

Tier codes are the corpus's own: `[PRIM]` primary text · `[PR]` peer-reviewed · `[REF]` scholarly reference · `[TER]` tertiary, corroborating only. **`§9.7` binds throughout** (`research/…:365-367`): *"history validates the structure … never the numbers."* No constant in §5 is derived from a source below.

### §3.1 The spine — the romano-canonical *ordo iudiciarius*

`[PRIM]` `research/…:288` (§7.2): Tancred's *Ordo iudiciarius* (c. 1216) — **libellus** (written complaint) → ***litis contestatio*** (joinder of issue) → a **graded hierarchy of proof** ("two witnesses = full proof", confession as "queen of proofs") → **sentence**, with *positiones/articuli* as the formal assertions to be proved. `research/…:351` (§9.3) draws the mapping this branch implements: *"The **romano-canonical ordo iudiciarius** supplies a historically exact structure — libellus (charge) → litis contestatio (issue joined) → graded proof hierarchy → verdict."*

The mapping Valoria canon licenses, and no more:

| *ordo* stage | Valoria | anchor |
|---|---|---|
| *libellus* | `open_case` — the filing, which declares the term | `social_contest_v30.md:450` "Inquisitor declares duration at filing" |
| *litis contestatio* | the live stasis is fixed at FACT when the bout opens | `modes.py:64 CHURCH_TRIBUNAL_START_GROUND = Stasis.FACT` (ED-1062) |
| *positiones/articuli* + proof accumulation | the Evidence scalar on the case tag, presented as `EvidenceItem`s | `primitives.py:283`, `:291 Dossier`; `research/…:351` names the *positiones* pattern as the model for the Evidence clock |
| graded proof hierarchy | **the `ProofBar` height** — the one place the hierarchy is expressible | `resolver.py:67`; `research/…:351` flags this as *"a possible Evidence-weighting refinement — Jordan call"*, i.e. **proposed, not licensed** |
| *sententia* | `determine` → the finding | `verb_table.yaml:156` |

`[PRIM]` **Bernard Gui's *Practica inquisitionis heretice pravitatis*** (1323–24) supplies the interrogation and category structure (`research/…:290`), and the corpus notes it maps directly onto *"the heresy-investigation lifecycle already in the repo"* — which is `social_contest_v30.md:441 §7.3`. The venue factory already cites peer-reviewed work on the accusatorial/inquisitorial tension (Eichbauer 2014 `doi:10.1111/hic3.12130`, Taliadoros 2018) in its own docstring (`modes.py:190-192`), so this grounding is not new to the branch — it is already in the code.

### §3.2 The stasis ladder as the forensic defence tree — and the correction that matters

`research/…:351` (§9.3): *"The classical stasis ladder **is** the forensic defence tree: deny the fact (conjectural) → contest the label (definitional) → justify/mitigate (qualitative) → **challenge the venue (translative = the Stay)**."*

**The corpus corrects its own reading of this, and the correction is load-bearing.** `research/…:495-497` (§12.4, `[PR]`, Heath 1994 *CQ* 44 **read directly**) records three things this branch must respect:

1. **Hermagoras *excluded* the legal/textual questions (*nomika zētēmata*) from the staseis.** The *status legales* as a co-equal second axis is **later Latin/Hermogenic systematization**, not native. So the branch does **not** claim a two-axis status model, and a statutory-dispute layer (ambiguity, letter-vs-intent, conflicting edicts) is flagged there as `[Proposed — Jordan call]` and is **not built here**.
2. The tree is **more exactly a "strongest-tenable-rung fallback ladder"** (Lausberg's *Kampflage*): deny the act → deny the law applies → admit-but-justify. That reading is *already how the kernel behaves* — `Stasis.stronger_than` (`primitives.py:23`) permits a shift only **upward** along `LADDER` (`:14`), so a side that cannot hold FACT may fall back to DEFINITION or QUALITY and can never retreat. The kernel implements the fallback ladder without naming it.
3. **The 13 *status* of Hermogenes/Zeno were declamation inflation**, tailored for fictional school exercises after the imperial forum had declined, while *"Quintilian sought a **practicable reduction**"*. The corpus states the design consequence itself: this is *"a NERS-Elegance guardrail with historical authority."* It is the reason §7's false-N-line hunt is run against this branch's own additions and not only against the shape spec's.

**Independent corroboration for the venue challenge, from a different tradition.** `research/…:493` (§12.3, French, `[REF]`): the *évocation* plus the medieval maxim *"it is the **jurisdiction**, more than the justice of the cause, that decides the outcome"* — the corpus explicitly says this *"independently corroborate**s** CR4's translative-stasis = **the Stay**, now from French legal history, not classical rhetoric."* And Valoria canon says the same thing in its own words: the Stay *"represents **Parliament asserting civil jurisdiction over an ecclesiastical proceeding**"* (`social_contest_v30.md:649`). Three sources, one mechanic, and the code already carries it: `rhetoric.py:172 is_pre_merits` returns True for JURISDICTION, with the docstring *"contested BEFORE the merits and has no primary genre until settled."*

### §3.3 The Indian axis — the defeat machinery and when the accused's silence is a loss

`[PRIM]` `research/…:204-206` (§5.1): *kathā* splits into **vāda** (truth-seeking), **jalpa** (victory-seeking, any device permitted) and **vitaṇḍā** (*"pure refutation with no counter-thesis of one's own"*); victory is awarded **against the side that incurs a *nigrahasthāna*** — a clinching point of defeat. `[PRIM]` `research/…:210-217` (§5.2, Caraka *Vimānasthāna* 8): before agreeing to debate, assess the opponent's relative standing and the assembly's disposition, and **condition strategy on that triage**. `[PRIM]` `research/…:219-221` (§5.3, Vācaspatimiśra): *"Obstruction is bounded by your own standing and the situation."*

This is the doctrine `SelfGating` (`primitives.py:213`) and `DefeatCatalogue` (`:262`) already implement, and the kernel cites the Sanskrit terms at the fault sites: `ananubhāṣaṇa` (`resolver.py:347`), `apratibhā` (`:347`), *pratijñā-hāni* (`:354`), *apasiddhānta* (`:357`), *arthāntara* (`:369`, `:381`), *chala/jāti* (`:377`). **The finding this grounds:** an accused who answers nothing substantive but never formally declines is running ***vitaṇḍā*** — refutation with no counter-thesis — and the doctrine treats sustained failure to engage the question as a clinching defeat, not as a legitimate defensive posture. `support` (E5) is that posture with no fault attached. So the fix is not an invention; it is the fault catalogue reaching a move it already covers everywhere else.

### §3.4 Where confidence is low, stated rather than glossed

- The **proof hierarchy as an Evidence-weighting refinement** is explicitly `[Jordan call]` in the corpus (`research/…:351`). This branch uses only the *bar height*, which the kernel already has; it does **not** implement graded proof kinds (two-witness vs confession vs *fama*).
- The **clean four-stasis scheme** is `[CONFIDENCE: medium]` — *"Hermagoras's own system was more elaborate and the tidy four owes much to Ciceronian transmission"* (`research/…:99`). The kernel's six-rung ladder (four forensic + two deliberative, `primitives.py:14`) is already a Valorian construction, not a historical reconstruction, and this branch does not add a rung.
- The venue's numeric profile (`ProofBar(2.5)`, `evasion_strikes=1`, the proof weights) is `[SEED]` in the source — `modes.py:194` says so verbatim: *"[SEED] all numeric values."* Nothing in §3 licenses any of them.
- **A doc/code drift found in the grounding itself, worth one row:** `inquisition_hearing_venue`'s docstring (`modes.py:182-184`) says *"must accumulate evidence to ProofBar(3.0) … Lower bar than civil court (4.0)"*, while the code sets `ProofBar(bar=2.5)` (`:196`) and `court_venue` sets `ProofBar(bar=2.0)` (`:69`) — so the docstring is wrong about its own number **and** about the comparison (2.5 is *higher* than 2.0, not lower). Under `CLAUDE.md` §0.05 the code is the mechanism; the docstring is reference and is wrong. Fix the prose, not the number, unless Jordan rules the number.

---

## §4 · THE SEQUENCE

Idiom: `systems/_architecture/subsystem_flow_skeletons_v1.md:94` — steps `S1`, `S2`, branches nested one level as `S2.1`, tagged `[gate] [branch] [loop] [emit] [write]`, each step naming reads, writes and the owner of the write.

**Two proceedings, not one.** Canon separates the **Heresy Investigation** (§7.3, 4–6 seasons, one interrogation per season, verdict ∈ Acquittal / Insufficient Evidence / **Tribunal Recommended**, `social_contest_v30.md:451`) from the **Excommunication Tribunal** (§7.1, the sentencing proceeding, `:624`). The shape spec's S4 maps an Overwhelming investigation result straight onto `attempt_excommunication`; **canon puts a second proceeding in between** — a further amendment to §4 of the shape spec, stated here because it is a property of the sequence rather than of any one element. Both are inquiry-class; each produces its own finding; each binds at its own close.

```
S1  [gate][write] open_case  — actor: a Person holding a seat whose remit reaches `determine`
    S1.1 [gate] eligibility        Refusal(eligibility)                       verb_table.yaml:347; H-52 (§11 F1)
    S1.2 [gate] formal grounds — RESTORED to the canonical three-way alternative:
             CI >= 40  AND  church.L >= 4  AND
             (  evidence_value(place, accused) >= 3                 -- LedgerTag scan, exact key
              ∨ ledger_has(place.ledger, "Debt", violated_key)      -- ledger.py:61
              ∨ conviction_count(log, accused) >= 2 )               -- KeyLog Query, NOT a tag count (§1 E9)
             reads: world.clocks['CI'], Faction.L, Settlement.ledger, KeyLog
             writes: nothing.  Refusal(grounds).                    tribunal.py:73; social_contest_v30.md:626
    S1.3 [gate] uniqueness — EXPLICIT, because ledger_add's dedupe silently overwrites (§1 E10)
             ledger_has(place.ledger, "Leverage", f"case:{accused}")  ->  Refusal(duplicate)
             one active case per accused PER JURISDICTION; cross-jurisdictional cases run in parallel
                                                                     ledger.py:61; social_contest_v30.md:472
    S1.4 [write] the ONE stored scalar — the case, with its DECLARED term
             LedgerTag(kind="Leverage", key=f"case:{accused}", value=<evidence count at filing>,
                       created_season=world.season, ttl=<declared 2..4>)
             owner of the write: the SE ledger primitive, called through the write gate by open_case.
             The term is stored because the Inquisitor DECIDED it; the stage is not, because it is
             an aggregate over the log (§1 E6).                      ledger.py:47; social_contest_v30.md:450
    S1.5 [emit] case.opened  +  queue_scene("inquiry", ctx={accused, inquisitor, jurisdiction, place})
             recurs once per season for the declared term.           scene_slate.py:34; social_contest_v30.md:450
             ⚠ requires a new `st == "inquiry"` branch in scene_dispatch._resolve_slot (§5.6) —
               without it the slot falls through to the total-mapping stub.  scene_dispatch.py:361

S2  [loop over seasons <= term]  the Interrogation scene — ONE per season (canon, not a choice)
    the bout: Bout(venue = church_tribunal (ProofBar/ACCUSER, FACT), adjudicator = expert_judge,
                   armature = ArmatureConfig(styles=..., opponent_is_adjudicator=True, cr5=True),
                   rng = <injected>)                                 resolver.py:238; modes.py:495
    S2.1 [branch] moves, alternating, roles NOT alternating (inquisitor proposes)
             side A = inquisitor (the burden-holder), side B = accused
             the accused may not corroborate (canon :630) and may not `support` (§5.4, I-I6)
    S2.2 [gate] faults -> DefeatCatalogue.check; a clinch ENDS the bout
             against the accused  -> the burden was met, not a veto
             against the inquisitor -> a veto: it DEMOTES, it never promotes   §C.5 "the veto can only demote"
                                                                     primitives.py:272; resolver.py:341
    S2.3 [write] the Evidence scalar — refreshed on the case tag by the INQUISITOR'S OWN ACT,
             not by fieldwork.advance_evidence, which is a stub that writes nothing (§1 E12)
             ledger_add(place.ledger, LedgerTag(... value=new_count, created_season, ttl unchanged))
             owner: the SE ledger primitive; actor: the inquisitor.  fieldwork.py:54; ledger.py:47
    S2.4 [emit] beats (Bout(record=True).log); this scene's outcome BINDS at this scene's close —
             the evidence write lands here, in this RESOLVE, not next season.   §4.6

S3  the Stay — NOT a step of this sequence.  A SEPARATE act, by a DIFFERENT actor, in a DIFFERENT
    venue, whose only couplings to the case are an availability band and a clock write.  §4.6 works
    this out; it is where the shape spec's S3/S3.1 would have created an architectural conflict.
    S3.1 [gate] availability is a BAND ON A QUERY, never a stored flag:  CI < 55
                                                                     parliamentary_stay.py:37,61-67
    S3.2 [branch] the Stay is itself a §10 BG Parliamentary Vote — Side A = invoker + >=2
             parliamentary factions, Side B = the Church.  It can be LOST.       parliamentary_stay.py:85
    S3.3 [write] on `granted`: the case tag's clock gains one season.  Multiple Stays are lawful,
             one per filing per season; a Stay SUSPENDS, it never closes.
             ⚠ AMENDED: the write lands in the STAY's own scene.  invoke_stay today RETURNS the
             suspension "for the caller to apply" (parliamentary_stay.py:19-21) and has had ZERO
             callers since 2026-05-31 — a deferred write nobody ever applied.  Under Jordan's ruling
             it binds where it is decided.                            social_contest_v30.md:465,653
    S3.4 [gate] resolve_stay_lift(stay, world) is the lift; wiring it is this branch's only
             new call site into an existing, uncalled module.         parliamentary_stay.py:101

S4  [branch][write][emit]  determine — the Investigation Verdict.  Actor: the Person in the judging
    seat.  margin = ProofBar.margin (net − bar); veto from S2.2.  THREE canonical outcomes, not four:
             guilty-band      -> finding "guilty",  and the verdict is TRIBUNAL RECOMMENDED,
                                 which opens a §7.1 proceeding — it does NOT sentence   :451
             inconclusive     -> finding "inconclusive"; the case SUSPENDS; may resume if the
                                 evidence scalar reaches 3 within 4 seasons              :451
             exonerated       -> finding "exonerated"; case closed; Renown +1 in non-Church
                                 factions; re-filing the same charge REQUIRES FRESH EVIDENCE
                                 ("cannot recycle prior testimony")                      :466
    S4.1 [emit] scene.investigation_resolved{scene_id, subject_id, finding, public?, sentence?}
             emitted BY `determine`, not by echo_transport (§1 E11).  Permanence: indelible.
                                                                     KEY_INDEX.md:948; keys.py:367
    S4.2 [write] the record of the finding: LedgerTag(kind="Precedent",
             key=f"conviction:{accused}:{case_id}", ttl=None) on guilty; f"acquitted:{accused}"
             on exonerated.  ⚠ the case_id suffix is REQUIRED — without it ledger_add refreshes in
             place and the 2-prior-convictions gate can never fire (§1 E9).      ledger.py:53-57
    S4.3 [write] the case tag is closed: ledger_sweep on ttl, or removed by the closing act.

S5  [branch] the §7.1 Excommunication Tribunal — a SECOND inquiry-class proceeding, opened only by
    S4's guilty finding.  Same shape, different row: excommunication_court (ProofBar 3.0, ethos-
    dominant, Panel).  Its own determine writes the SENTENCE.                      modes.py:200,215
    S5.1 [write] on success: Tenure closes on the accused's seat (T-o, via = the judge's seat, and
             `via` MUST be present) and/or attempt_excommunication.  01_AXIOMS.md:1160; excommunication.py:78
    S5.2 the sentence's REACH is not this scene's business — PR #362 09_WORKED_EXAMPLES.md:147:
             "excommunication is not a flag … it lands as a compliance contest, per person."
             Each executor's compliance is a different scene and binds in THAT scene.  §4.6.

S6  [branch] closures at any phase, each an Event that ends the case tag, none of them MATTER:
    inquisitor death / demotion / reassignment; accused death / defection / faction-conversion /
    faction protection (a Stay, which suspends rather than closes); acquittal by verdict.
    Eight rows, all specified.                                        social_contest_v30.md:455-470
```

### §4.6 · The one hard case: does the Stay nest an act inside another act's resolution?

The coordinator asked this precisely, because it is the only place in this branch where Jordan's in-scene-binding ruling could collide with PR #362. **Worked out with anchors: it does not — provided the Stay is built as canon describes it, and the shape spec's S3.1 wording is what would have made it collide.**

**What PR #362 actually forbids.** Two clauses, narrower than "outcomes wait a season":
- `04_CODE_ARCHITECTURE.md:871` (PART D row 49): *"the roster resolves once from `proj` (§C.5.1); `commit` moves only through an Act, and **no Act resolves inside another's resolution**."* — a ban on **nesting**.
- `04_CODE_ARCHITECTURE.md:509`: `scenes = deliberate(frozen)` — *"a MAP. **No token exists in this scope**"* — a ban on **reacting inside RESOLVE to RESOLVE**.

Neither forbids a verdict binding within the RESOLVE that produced it. The driver (`:502-514`) runs `calendar → matter → deliberate → resolve → witness → census` and advances the season **once**, at `:514`. The RESOLVE fold (`:573-582`) is explicit: `if row.contests: degree, evs = seam.contest(...)` and then, **in the same iteration**, `receipts = [gate.write(...) for (k,f) in row.writes_at(degree)]`. **The degree-keyed write of a contested verb lands in the same RESOLVE that resolved the contest.** For `determine` that is the whole of what the ruling asks.

**And there is no second act to defer.** A determination is *computed by the proceeding*; it is not assented to by a counterparty. The judge determines; nobody has to agree. That is the structural difference between this branch and negotiation, and it is why the ruling is cheap here.

**Now the Stay.** Is it "a challenge to the venue raised inside the proceeding"? **No — and canon says so three times:**

1. `parliamentary_stay.py:54-98` — `invoke_stay` runs a **§10 BG Parliamentary Vote** (`:85 run_parliamentary_vote`) with Side A = the invoker plus at least two *parliamentary factions* (`:37-38, :72-73`) and Side B = the Church (`:77-80`). **Different actors, different venue, different resolver.** The accused Person is not among them.
2. `social_contest_v30.md:649` — it *"halts an active Church Tribunal **filing** for 1 season."* It acts on the *filing*, not on an exchange in progress.
3. `social_contest_v30.md:634`, canon's own strategic note: *"The correct strategic counter is **preventing the filing, not defending at Tribunal**."* Canon explicitly places the Stay outside the proceeding.

So the Stay is **its own Act, in its own scene, resolved in the same RESOLVE as every other act of that season, binding at its own close.** Nothing nests. D-49 is not engaged. Its coupling to the case is exactly two facts: the availability band `CI < 55` (a Query, `parliamentary_stay.py:61-67`) and a write to the case tag's clock.

**Where the collision would have come from, and it is worth recording as a near miss.** `00_BRANCH_SHAPES.md` §4(d) S3 puts `invoke_stay` inside the tribunal sequence, and S3.1 says *"a passed Stay = shift to JURISDICTION stasis … for one season."* Implemented literally, that resolves **a parliamentary vote inside a tribunal's `Bout.resolve`** — which is precisely the shape D-49 forbids, and it would also have made the tribunal's outcome depend on a roster resolved after the seam boundary, breaking `§C.5.1`. **The conflict is created by the conflation, not by the architecture.** Keeping the two apart costs nothing and is what canon describes.

**But the conflated reading points at something real, which should be kept.** There *is* an in-bout venue challenge, and it already executes: `Stasis.LADDER` (`primitives.py:14`) places JURISDICTION above FACT, `Stasis.stronger_than` (`:23`) permits an upward `shift`, and `resolver.py:352-358` applies it — so **the accused can spend 4 reserve to move the live ground to JURISDICTION**, at which point `rhetoric.py:172 is_pre_merits` is True and no side earns CR4's primary-genre bonus (`rhetoric.py:160-170`). Because `Stasis.relevant` (`primitives.py:21`) forces every subsequent move onto the live ground, an inquisitor whose policy keeps arguing FACT then accrues `evasion` — and `evasion_strikes=1` (`modes.py:198`) clinches the bout **against the inquisitor**. The translative status is a live, dangerous, in-bout move today, unremarked anywhere, and it is the *correct* mechanical home for "challenge the venue" (research §9.3 `:351`).

**So the vocabulary needs splitting, and this is the branch's contribution to it:**

| | in-bout | out-of-bout |
|---|---|---|
| name | the **jurisdictional plea** (translative stasis) | the **Parliamentary Stay** (§10.1) |
| who acts | the accused, inside the scene | the invoker's faction, in Parliament |
| mechanism | `Move(kind="shift", ground=JURISDICTION)` | `invoke_stay` → a BG vote |
| binds | at the move, inside the bout | at the close of the Stay's own scene |
| nests? | no — a Move is not an Act | no — a separate Act |
| exists today | **yes, and it is reachable** | yes, and it has **zero callers** |

**Consequence for the multi-season case, stated plainly.** A stayed case genuinely spans seasons — **and that is canon, not an architectural tax.** `social_contest_v30.md:450` already makes the Investigation 2–4 seasons with one interrogation per season; `:465` adds one season per Stay and permits multiple Stays; `:453` puts the nominal total at 4–6 seasons. The season-spanning shape is the design. What the in-scene ruling changes is only **where each season's write lands**: the interrogation's evidence write lands in the interrogation's scene, the Stay's clock write lands in the Stay's scene, the verdict lands in the verdict's scene. Nothing is handed back to a caller to apply later — which is the convention `invoke_stay`'s own docstring adopted (`:19-21`) and which produced, since it was implemented on 2026-05-31 (`parliamentary_stay.py:5`), **no applier anywhere in the tree**. The ruling retires that convention for this branch, and the evidence that it should be retired is that it never worked.

**One residual worth naming without inflating it.** A *negotiated abjuration* — the historically ordinary tribunal outcome, and the composition `00_synthesis.md:328` says the subsystem is missing — is a write on the **accused's own** relation (their `commit` to the heretical proposition, released). Under `§C.2:529-534` a Tenure write requires `actor == subject(id)` or one of three declared exceptions, none of which is "the subject consented in this scene". So abjuration is the one inquiry outcome whose in-scene binding is not obviously spelled today. **It is not in this branch's scope** — abjuration needs `settle()`, which is negotiation's build — and I am not proposing an amendment on a case my branch does not build. The spine document owns the architectural verdict; this is a pointer to the one place it is worth checking.

---

## §5 · THE SHAPE

Everything below is **consumed from** the spine except §5.4 and §5.6, which are this branch's own. `[SEED]` marks a number this document invented; there are three, and all three are dials rather than mechanisms.

### §5.1 · The `PROCEEDINGS` row — one row, replacing two venues

```python
# modes.py:495-499 — the merged row.  DELETED: track_start, tracker, tracker_mode (all derivable
# from `burden` once the win-condition is selected by it — spine §2.1, ED-SC-0020 Fork A).
"church_tribunal": dict(
    exchanges   = (1, 5),                    # canon :396 "Exchange count set by Inquisitor (1–5)"
    roles       = "inquisitor_proposes",     # unchanged; drives opponent_is_adjudicator (§5.5)
    resistance  = "halved_accused",          # unchanged — and INERT today (§1, tail); see F-I7
    adjudicator = "expert_judge",            # unchanged; answers H-32 for this venue (§11 F2)
    start_ground = Stasis.FACT,              # unchanged (ED-1062, modes.py:64)
    burden      = "ACCUSER",                 # NEW.  The one field.
    bar         = 2.5,                       # [SEED] — inherited verbatim from the venue this row
                                             # absorbs (modes.py:196), NOT newly invented.  It is the
                                             # standard-of-proof dial (VENUE_VALIDATION.md:9).
    faults      = DefeatCatalogue(barred=True, contradiction=True,
                                  evasion_strikes=1, yield_strikes=1),
                                             # AMENDED from yield_strikes=2 (§1 E8).  ONE refusal to
                                             # answer convicts, matching evasion.  This is what
                                             # "silence convicts" actually requires.
    restricted  = {"B": ("support",)},       # NEW.  §5.4.  The accused may not stall.
)
```

**Deleted with the row:** `CHURCH_TRIBUNAL_TRACK_START` (`modes.py:476`), the `church_tribunal` entry's `tracker`/`tracker_mode`, and — once no proceeding needs it — `_use_tracker` (`modes.py:521`) and the `use_tracker` parameter threaded through `build_contest` (`wrapper.py:110`) and `proceeding_venue` (`:536`). **Also deleted: `inquisition_hearing_venue` (`modes.py:181`) and its `CROSS_CULTURAL_VENUES` row (`:319`)**, whose entire content is now the canonical row's — that is the merge, and it is a net deletion of one venue factory, one registry row, one constant and one tri-state.

### §5.2 · The `ProofBar` binding — consumed from the spine, one line of glue

```python
# resolver.py — the spine adds margin() to every WinCondition; this branch binds burden -> class.
_WIN_BY_BURDEN = {
    "ACCUSER":        lambda spec: ProofBar(bar=spec["bar"], challenger=A),
    "RESPONDENT":     lambda spec: ProofBar(bar=spec["bar"], challenger=B),
    "LOWER_STANDING": lambda spec: GraceThreshold(bar=spec["bar"], petitioner=A),
    "NONE":           lambda spec: TallyAtClose(),          # or PersuasionTrack, per the spine
}
class ProofBar(WinCondition):                                # resolver.py:67, unchanged
    def margin(self, s) -> float:                            # NEW (spine-owned)
        return (s.adv[self.ch] - s.adv[other(self.ch)]) - self.bar   # sign == burden met
```

`challenger=A` is correct for `roles="inquisitor_proposes"`: side A is the inquisitor, who bears the burden. **The stall semantics ED-SC-0020 asks for are already at `resolver.py:72`** — `if closing: return df`. Fork A's stall clause needs no new code for this venue; it needs the row to select the class.

### §5.3 · The restored grounds check (FA-owned)

```python
# systems/factions/sim/tribunal.py:73 — replaces the two-clause check with canon's three-way form.
def formal_grounds_check(church, world, *, accused=None, place=None, log=None) -> bool:
    """§7.1: CI >= 40 AND Church Mandate >= 4 AND one of three alternatives
       (social_contest_v30.md:626).  The third clause was 'not yet ported' (this file's own
       docstring, :78-81) because the Evidence Track was personal-scale; it now resolves against
       the SE ledger and the KeyLog, both of which exist."""
    if world.clocks.get('CI', 0.0) < TRIBUNAL_PREREQ_CI_FORMAL:  return False   # :44
    if church.L < TRIBUNAL_PREREQ_L_FORMAL:                      return False   # :45
    if accused is None or place is None:                         return False   # typed, never a crash
    led = place.ledger
    if evidence_value(led, accused) >= TRIBUNAL_PREREQ_EVIDENCE: return True    # NEW const = 3, canon :626
    if ledger_has(led, "Debt", obligation_key(accused)):         return True    # ledger.py:61
    if conviction_count(log, accused) >= TRIBUNAL_PREREQ_PRIORS: return True    # NEW const = 2, canon :626
    return False

def evidence_value(ledger, accused) -> float:
    """The stored scalar.  ledger_get takes NO key (ledger.py:65) — scan for the exact key."""
    return next((t.value for t in ledger_get(ledger, "Leverage")
                 if t.key == f"case:{accused}"), 0.0)

def conviction_count(log, accused) -> int:
    """An AGGREGATE, therefore a Query and never a stored counter (T-a; spine §2.3).  A ledger
       count CANNOT work here: ledger_add dedupes by (kind,key) and refreshes in place
       (ledger.py:53-57), so the tag count is capped at 1 (§1 E9)."""
    return sum(1 for k in log.of_type("scene.investigation_resolved")
               if k.payload.get("subject_id") == accused
               and k.payload.get("finding") == "guilty")
```

Both new constants are **canon-cited, not `[SEED]`** — `social_contest_v30.md:626` gives 3 and 2 verbatim.

### §5.4 · `restricted` — the accused may not stall (this branch's only new Venue field)

The shape spec routes I-I6 through `SelfGating.licit`. **That does not work:** `licit(kind, my, opp, learned, hostile)` (`primitives.py:219`) takes no side and no venue, and returns `True` for every kind but `"hard"`. Routing a per-side venue restriction through it would change the signature of a function whose whole job is the standing gradient. The composing shape is a Venue field consumed at the top of `_apply`, beside the kind check that is already there:

```python
# resolver.py — Venue gains one field (class Venue, :151)
restricted: dict = field(default_factory=dict)      # {side: (kind, ...)} — venue-forbidden moves

# resolver.py:342, immediately after the VALID_KINDS check
if mv.kind in self.v.restricted.get(side, ()):
    c.fault.evasion += 1
    c.fault.reason = "the accused may not merely affirm (vitanda)"   # research §5.1 :206
    return
```

**Why a fault and not a refusal.** A `Refusal` would let a policy probe the venue for free and re-choose; a fault makes the attempt cost something, which is what every other illicit move in this kernel does (`resolver.py:369, :377, :381`). And it is what the doctrine says: *vitaṇḍā* is a mode you may adopt and be defeated in, not a move the assembly prevents.

**⚠ This is a KERNEL-WIDE change wearing an inquiry costume, and it should be said rather than hidden.** `support`'s free net-+2 regroup is available in **every** venue; the tribunal is only where it is decisive (§10). The `restricted` field fixes the *symptom in this venue*. The *cause* — a move that spends 2 and regains 4 with no fault — is `primitives.py:51-52`, and whether `REGAIN` should exceed `COST["support"]` is a kernel question this branch does not own. **F-I2 measures the symptom; §11 F6 records the cause and routes it to the spine.**

### §5.5 · The armature passthrough — precisely what it buys here

The spine adds `build_contest(..., armature=)`. For this venue, `roles="inquisitor_proposes"` derives `opponent_is_adjudicator=True` (`armature.py:374 position_of`), and **that gates the δσ channel entirely off**: `:388-390` returns `ArmaturePosition.zero()`, so `ArmatureConfig.dsigma` (`:436`) returns `0.0` before it computes anything. This is deliberate and correct — the inquisitor both argues and judges, so a judge-aimed dot-product would double-count the opponent-aimed Resonant Style (`armature.py:378-383`, the critique's own caveat).

**So the passthrough buys two channels here, not three:** CR4's `+1D` primary-genre pool bonus, which fires only when a Style is chosen and is therefore *armature-gated* (`resolver.py:399-403`, `rhetoric.py:221`), and CR5's self-Face backfire (`rhetoric.py:413`, enabled by `ArmatureConfig.cr5`). The spine's §2.2 N-line for `armature=` names "the adjudicator's convictions" as one of the possibilities lost; **for inquiry that third one is zero by construction.** A precision on the N-line, not a refutation of it — CR4 and CR5 are alone sufficient, because without the armature the accused has no Style choice at all and the terrain does nothing.

### §5.6 · The two verbs, the scene branch, and the Stay

```python
open_case(actor: PersonId, via: SeatId, accused: PersonId, jurisdiction: PlaceId,
          term: int) -> Receipt | Refusal
    # Refusal kinds: eligibility | grounds | duplicate | depth_cap
    # writes: LedgerTag("Leverage", f"case:{accused}", value, created_season, ttl=term)
    # emits:  case.opened   +   queue_scene("inquiry", ctx)
    # ⚠ `writes: Record.stages` (verb_table.yaml:349) is DROPPED — §1 E6, §7.3

determine(actor: PersonId, via: SeatId, case: LedgerTag) -> Receipt
    # contests: "a finding"                     <- rosters.yaml prizes gains ONE row
    # degree:   read off ProofBar.margin via the ONE ladder, veto may only demote
    # writes:   DEGREE-KEYED (04_CODE_ARCHITECTURE.md:573 F6) — §6.4
    # emits:    scene.investigation_resolved{scene_id, subject_id, finding, public?, sentence?}
    #           on EVERY band, including exonerated: an acquittal is a finding, not a non-event

invoke_stay(motion, invoker: PersonId, world, supporters, ...) -> StayResult   # EXISTS, :54
resolve_stay_lift(stay: StayResult, world) -> bool                            # EXISTS, :101, 0 callers
    # AMENDED: the suspension write lands in the Stay's own scene, through the gate, rather than
    # being returned "for the caller to apply" (:19-21) — a convention that produced no applier
    # in the entire tree.  §4.6.
```

**The scene branch (`engine/cross_scale/scene_dispatch.py`).** A new `elif st == "inquiry":` arm beside `st == "contest"` (`:279`), building with `venue="church_tribunal"` and the injected `rng` rather than the global-reseed dance at `:299`. Without it the slot falls through to the total-mapping stub at `:361` and the branch is unreachable. **This is work the shape spec's §4 does not name**, and it is the difference between "the venue row exists" and "a case runs".

**Three `[SEED]`s, and they are all this document invents:** `yield_strikes=1` (E8's correction — canon says silence convicts, canon does not say after how many refusals); `restricted={"B": ("support",)}` as a **set membership**, not a number; and nothing else. `bar=2.5` and `evasion_strikes=1` are inherited verbatim from `modes.py:196-198` and are that file's `[SEED]`s, not new ones. **No number in this document comes from history** (research §9.7).

---

## §6 · Keys, state, ownership, the write path, and the degree column

### §6.1 Keys

| key | direction | new? | anchor |
|---|---|---|---|
| `scene.investigation_resolved` | **written** by `determine` | **no** — exists, `finding ∈ exonerated\|guilty\|inconclusive`, permanence **indelible**, scale `territory` | `KEY_INDEX.md:948`; `key_types.json` |
| `state.belief_revised` | not written here | no — FI/NPC-owned; the conversion outcome is Belief Revision's, not inquiry's (§2.3) | `npc_behavior_v30.md:391` |
| `scene.contest_resolved` | not written by this branch | no — the echo transport's key, and it is the wrong shape for a finding (§1 E11) | `echo_transport.py:108` |

**New key types: zero. New descriptors: zero.** One registry edit rides along: `KEY_INDEX.md:960` producers gain `social_contest` (today: `faction_politics`, `scene_slate`). That is an IN-lane row, not code.

⚠ **One honest tension in reusing the existing key.** Its declared scale is `territory` while a tribunal against a Person is personal-scale, and `emit_scene_echo` hardcodes `scale_signature=["personal"]` on the keys it builds (`echo_transport.py:431`). Since `determine` emits directly (E11), it sets the scale itself and the mismatch is visible rather than inherited — but *which* scale a finding about a Person that revokes a seat carries is a real question I am not answering. It is not a blocker (the registry supplies a default, `keys.py:322`), and it should not be papered over.

### §6.2 State changes and who owns each write

| state | R/W | owner of the write | when it lands |
|---|---|---|---|
| `Settlement.ledger` — the case `LedgerTag` | W | `systems/settlements/sim/ledger.py:47 ledger_add`, single-owner | in `open_case`'s scene (S1.4) |
| the same tag's `value` (evidence) | W | same primitive; **actor = the inquisitor** | in each interrogation scene (S2.3) |
| the same tag's clock | W | same primitive; **actor = the Stay's invoker** | in the **Stay's** scene (S3.3) |
| `Settlement.ledger` — `Precedent(conviction:…\|acquitted:…)` | W | same primitive | in `determine`'s scene (S4.2) |
| `world.clocks['CI']` | R only | Church/faction layer | — |
| `Faction.L` | R only | `engine/autoload/game_state.py:153 Faction.adjust` | — |
| `Tenure.until` (the sentence) | W | **only** under `T-o` with `Act.via` present, in the §7.1 proceeding | in S5's scene |
| `KeyLog` | W (append) | `engine/substrate/keys.py:367 KeyLog.append` | at each emission |

**No new store.** The case is a `LedgerTag`; the stage is a Query; the evidence count is that tag's `value`; the schedule is a `SceneSlot`. **This branch owns no state of its own** — which is the strongest single argument that it is a venue row.

⚠ **The custody gap is real and is SE's, not mine.** `LedgerTag` has no holder: tags live on `Settlement.ledger` (`ledger.py:15-17`), never on a Person. A finding *about a Person* filed on a *settlement's* ledger is a compromise, and PR #362 names the missing property exactly — a Record is *"the fact that can leave the head that holds it"* (`01_AXIOMS.md:857 §D.4`). Until an owner-side `holder: PersonId | None` exists, this branch writes to the ledger at `place`. **Named, not hidden, and not fixed here.**

### §6.3 The write path

Every write goes `Act → gate.write(token, kind, field, id, change, actor, via) → Receipt` (`04_CODE_ARCHITECTURE.md:520`). The seam has no token (`§C.5`), so **the contest cannot write** — it returns a margin and the calling verb writes. Under the ruling, that write lands in the same RESOLVE iteration that resolved the contest (`:573-582`), which is §4.6's whole argument. Under a PR #362 veto the same writes are direct `ledger_add` calls from the verb's caller: the same writes, unreceipted.

### §6.4 The degree-keyed consequence column, on `determine`

Per `04_CODE_ARCHITECTURE.md:573 F6` and the 2026-09-03 ruling in the same section — *"the degree is READ OFF THE SUBSYSTEM, never mapped onto it by the table … a verb may not declare a band its subsystem cannot report"* — the column carries **three branches, because canon distinguishes three findings** (`social_contest_v30.md:451`; `key_types.json` `finding ∈ exonerated|guilty|inconclusive`). A fourth is registered as having no source in the data.

```yaml
- verb: "determine"                       # amends verb_table.yaml:156
  contests: "a finding"                   # NEW — the row has no `contests:` today
  writes:                                 # NEW — degree-keyed, replacing writes: [Tenure.degree]
    Overwhelming: [LedgerTag.Precedent, Case.closed]   # finding guilty; §7.1 tribunal OPENS
    Success:      [LedgerTag.Precedent, Case.closed]   # finding guilty; §7.1 tribunal OPENS
    Partial:      []                                   # inconclusive: the case SURVIVES, ttl unchanged
    Failure:      [LedgerTag.Precedent, Case.closed]   # exonerated; re-filing needs fresh evidence
  emits:                                  # keyed too — the same-shaped defect as writes (F6's second half)
    Overwhelming: [scene.investigation_resolved]
    Success:      [scene.investigation_resolved]
    Partial:      [scene.investigation_resolved]
    Failure:      [scene.investigation_resolved]
```

Two things this makes visible. (a) **`Partial` writes nothing and still emits** — the `Failure: []` shape `:625` calls *"the only place in this architecture where writing nothing is correct"*, and an inconclusive verdict is exactly that: the attempt happened, was witnessed, cost a scene, and left the case open. (b) **`Failure` is not an empty row.** An acquittal is a *positive* institutional fact with consequences — Renown +1 in non-Church factions, and re-filing barred without fresh evidence (`social_contest_v30.md:466`). A design that writes nothing on Failure loses double-jeopardy protection, which canon specifies. **This is the concrete counter-example to reading `F6` as "losing writes nothing".**

`determine`'s existing `writes: ["Tenure.degree"]` (`verb_table.yaml:162`) is dropped: `Tenure.degree` is PR #362's own `§F.4` hole — *a field with a writer and no reader*. Writing into it is not a consequence.

---

## §7 · Reuse ledger, and the false-N-line hunt over this branch's own additions

### §7.1 What this composes on (nothing here is new)

| composed on | anchor | what it supplies |
|---|---|---|
| `ProofBar` | `resolver.py:67-72` | burden = ACCUSER **and** the stall rule, in six lines |
| `DefeatCatalogue` | `primitives.py:262-279` | the four venue-configured clinches, with Nyāya names |
| `Stasis` / `LADDER` / `stronger_than` | `primitives.py:11-24` | the fallback ladder and the jurisdictional plea (§4.6) |
| `is_pre_merits` | `rhetoric.py:172` | translative status, already named "the Stay" in its own docstring |
| `EvidenceItem` / `Dossier` | `primitives.py:283, :291-295` | hidden weights, relevance gating, corroboration saturation |
| `armature` / CR4 / CR5 | `armature.py:415`, `rhetoric.py:221, :413` | Style choice as terrain reward; the eristic backfire |
| `appraise_armature` | `appraise.py:140` | the accused may read the judge — the critique's residue, no new mechanic |
| `excommunication_court_venue` | `modes.py:200-217` | S5's second proceeding, already built |
| `formal_grounds_check` / `run_excommunication_tribunal` | `tribunal.py:73, :87` | the §7.1 gate and its single-roll abstraction |
| `attempt_excommunication` | `excommunication.py:78` | the sentence |
| `invoke_stay` / `resolve_stay_lift` | `parliamentary_stay.py:54, :101` | the venue challenge, built and uncalled |
| `LedgerTag` + `ledger_add/has/get/sweep` | `ledger.py:35-72` | the Record primitive, single-owner, durable across succession |
| `queue_scene` / `SceneSlot` | `scene_slate.py:25, :34` | the multi-season recurrence |
| `KeyLog` + `content_hash` | `keys.py:336, :459` | the stage Query and the determinism falsifier |
| `degree_from_net` + `CONTEST_DEGREE_EXTENSION` | `dice_engine.py:227`, `degree_extension.py:87` | the one ladder; the extension may only demote |
| Belief Revision, Sincerity Gate | `npc_behavior_v30.md:391`, `fieldwork_v30.md:419` | the conversion outcome — **consumed, never duplicated** |

### §7.2 What is genuinely new, and why each survives

| new thing | N-line: *cut it, and the emergent possibility lost is…* | verdict |
|---|---|---|
| `burden` on the row | *silence convicts.* No handicap expresses it; `00_synthesis.md:350` says so in one sentence and `resolver.py:72` implements it in one line | **survives** — and it is the only field the audit calls "variety-bearing" (`04_reductive…:224`) |
| `restricted` on `Venue` | *an accused who is convicted for saying nothing while appearing to speak.* Without it the accused's dominant line is a free stall (§10) and the burden is decorative | **survives, with a caveat** — it fixes a symptom whose cause is kernel-wide (§5.4, §11 F6) |
| the restored third grounds clause | *a filing that must be earned by prior work* — fieldwork, an unpaid obligation, a history of convictions. Cut it and any Church at CI 40 with Mandate 4 can file on anyone, and the whole investigation layer becomes free | **survives** — and it is a restoration, not an addition (`tribunal.py:78-81`) |
| the `st == "inquiry"` dispatch branch | *the case running at all.* Without it every slot falls to the stub at `scene_dispatch.py:361` | **survives** — it is wiring, not a mechanism |
| the finding write | *an institutional fact that binds whether or not anyone was convinced* (§2.3). Cut it and inquiry collapses into Belief Revision, and the critique is simply right | **survives — and it is the one genuinely new behaviour in this branch** |

### §7.3 The false-N-line hunt, run against MY OWN additions

`14_NERS.md` §3: the pattern is *a mechanism was named, a **store** was proposed for it, and the store's job was already being done by an object the design had ruled in.* Six candidates, hunted deliberately. **Four cut, two kept.**

| candidate | its claim | verdict |
|---|---|---|
| **`Case` object with `stages`** | a multi-season investigation needs staged state | **CUT — and it is a live false N-line in the tree, not a hypothetical.** `verb_table.yaml:349` declares `writes: ["Record.exists", "Record.stages"]` and PR #362 `09_WORKED_EXAMPLES.md:137` says *"the act declares the stages and their terms."* The field's job is done **twice** by things already ruled in: the *declared term* by `LedgerTag.ttl`/`Tenure.term` (`T-n`), and the *stage reached* by a count over `KeyLog` — an aggregate, which `T-a` forbids storing. **Feedback owed to PR #357's verb table, and this branch's most concrete deletion.** |
| **an `Evidence` tracker class** | the Evidence Track is a named canonical mechanic (§7.1, §7.3) and needs a carrier | **CUT.** Its carrier is one float: `LedgerTag.value` on the case tag. `TRACKERS` (`primitives.py:154`) is the roster of *in-bout* trackers; the Evidence Track is *cross-season* and belongs to the record, not the bout. `Dossier`/`EvidenceItem` already carry the in-bout half with hidden weights. |
| **a `Stay` state object / a `stayed: bool` on the case** | a suspended case needs a suspension flag | **CUT.** Availability is a band on a Query (`CI < 55`, `parliamentary_stay.py:61-67`); the suspension itself is one integer already in the tag (`created_season` + `ttl`). `StayResult` (`:43`) is a *return value*, not state, and it should stay that way. A boolean would be a second home for a fact the clock holds. |
| **a `verdict` enum owned by social_contest** | the three findings need a vocabulary | **CUT.** `key_types.json` already declares `finding ∈ exonerated \| guilty \| inconclusive` for `scene.investigation_resolved`. A second enum is `ID-2` — two homes for one fact. |
| **`restricted` on `Venue`** | the accused's forbidden moves need a carrier | **KEPT, at medium confidence, and watched.** The honest attack: `DefeatCatalogue` is *already* the venue's per-move fault policy, so a second per-move venue field looks like the pattern. It survives because `DefeatCatalogue` is keyed by **fault**, not by **move × side**, and there is no side dimension anywhere in it (`primitives.py:267-279`). Folding a side-keyed restriction into a fault-keyed catalogue would widen the object more than adding the field does. **If the spine finds a side dimension it already needs elsewhere, cut this and use that.** |
| **`bar` on the row** | the standard of proof needs a home | **KEPT, high confidence.** It is not a new store — it is the constructor argument `ProofBar` already takes (`resolver.py:68`), moved from a venue factory's body to the row that selects the venue. Net objects: zero. |

**Vocabulary delta.** Added: `burden`, `bar`, `restricted`. Removed: `CHURCH_TRIBUNAL_TRACK_START`, `track_start` on this row, `tracker`, `tracker_mode`, `_use_tracker`, `use_tracker` (the parameter), `inquisition_hearing_venue`, the `inquisition_hearing` registry row, `Record.stages`, `determine.writes: [Tenure.degree]`. **Three in, ten out.** The `14_NERS.md` meta-rule benchmark — *three edits, two of them deletions, and the vocabulary got shorter* — is met on the count. It is **not** met on effort: the dispatch branch and the finding write are real new code, and saying otherwise would be the arithmetic dressed as a result.

---

## §8 · Invariants, graded per PR #362 §0's honest rule

Grades per `04_CODE_ARCHITECTURE.md:66-95`: **STRUCTURAL** = the defect has no spelling · **MECHANICAL** = one path exists and it refuses · **CONVENTION** = a reader notices, *stated as such, never dressed up*. Where the grade differs before and after this branch, both are given — an invariant that is CONVENTION today and claimed STRUCTURAL tomorrow is the defect class §0 names.

| id | invariant | today | after this branch |
|---|---|---|---|
| **I-I1** | the burden-holder loses the stasis on a stall | **MECHANICAL, already** — `resolver.py:72 if closing: return df`. One path, and it refuses | unchanged; the row selects the class |
| **I-I2** | a finding is written by `determine`, never by the seam | **n/a** (no finding exists) | **STRUCTURAL** — the seam has no token (`§C.5`), so it cannot write · **MECHANICAL** at the gate under a PR #362 veto · **CONVENTION** if both are vetoed, and then it should be said |
| **I-I3** | a stage exists only as an act's key in the log | **CONVENTION** — nothing stores a stage, and nothing prevents one | **CONVENTION, honestly.** No type forbids adding `stages`; `verb_table.yaml:349` currently *declares* it. A scan could see it, but no scan exists and §0.1 pt 5's predicate does not license minting one for a proposal-layer field. **Graded CONVENTION and left there** |
| **I-I4** | the Stay's availability is a band on a Query, never a stored flag | **MECHANICAL** — `parliamentary_stay.py:61-67` reads `world.clocks['CI']` at invocation; there is no flag to set | unchanged |
| **I-I5** | one active case per accused per jurisdiction | **not held** — no case exists; and `ledger_add`'s dedupe **silently overwrites** rather than refusing (§1 E10) | **MECHANICAL**, and only via the explicit `ledger_has` pre-check in S1.3. **Not by dedupe** — the shape spec's grade here was wrong and the correction is the point |
| **I-I6** | the accused never `support`s (and never corroborates) | **CONVENTION and violated.** Canon says no corroboration (`social_contest_v30.md:630`); the kernel implements neither that nor any bar on `support` (`resolver.py:350-351`) | **MECHANICAL** — `restricted` is checked on the one path every move takes (`_apply`, `resolver.py:341`), and a bypass must go around `_apply` |
| **I-I7** | **silence convicts** — the signature invariant | **CONVENTION, and dodgeable, and the dodge is free.** Graded honestly: the clinch exists (`primitives.py:278`) but three separate holes let the accused past it — `support` costs nothing (E5), `yield_strikes=2` gives a free refusal (E8), and canon's compensating halved resistance is **inert** (`wrapper.py:331-332`). An invariant with three live bypasses is not MECHANICAL | **MECHANICAL** once all three close: `restricted` blocks the stall, `yield_strikes=1` removes the free refusal, and the burden makes the close a loss for whoever failed to prove. **F-I2 is what tells you whether the grade is earned; until it runs, the claim is a plan** |
| **I-I8** | the veto may only demote | **MECHANICAL** by signature — `§C.5` *"veto : bool and the ladder takes the minimum"* | unchanged. Note the asymmetry this branch depends on: a clinch **against the accused** is *not* a veto — it is the burden met (`resolver.py:71`) |
| **I-I9** | an acquittal is a finding, not a non-event | **not held** | **MECHANICAL** — `determine`'s `emits:` is keyed on every band including `Failure` (§6.4), and the Renown/re-filing consequences are canon (`:466`). Without the keyed `emits:`, `F6`'s own second-half defect (*"a wound emitted `person.died`"*) recurs here as *an acquittal emitting nothing* |
| **I-I10** | each scene's outcome binds at that scene's close | **not held** — `invoke_stay` returns its effect "for the caller to apply" (`:19-21`) and has had zero callers since it was implemented on 2026-05-31 | **MECHANICAL** at the gate: the write is a `gate.write` in the same RESOLVE iteration (`§C.4:573-582`). Under a veto: **CONVENTION** |

**Count, per `§0`'s own rule** (rows whose grade names no `CONVENTION` term and no scan): **6 of 10 after, 3 of 10 today.** Command: read the "after" column and count rows containing neither "CONVENTION" nor "scan".

---

## §9 · Falsifiers

Per `CLAUDE.md` §0.1 pt 3 (name the falsifier in the same commit as the result) and pt 2 (**an assertion must be able to observe the failure it excludes**). Each carries its control. Numbers marked *(control)* come from the snapshot's measured run and are **not canon** — they are what a correct implementation must reproduce.

**F-I1 · The bar reproduces the presumption of innocence.**
`python -m pytest tests/valoria/test_inquiry_proofbar.py -q`, seeded, N ≥ 200 per arm, `ProofBar(2.5)`.
- equal-faculty inquisitor vs actively-defending accused → acquittal ≥ 0.90
- accused playing `pass` throughout → conviction ≥ 0.90
- **Control:** `VENUE_VALIDATION.md:9` measured 1.00 and 0.97 on the same venue. A run landing outside the band means the merge (E7) changed the venue, not that the venue is wrong.
- **Observes:** a merged row that silently kept `PersuasionTrack` — under a track both arms converge toward the compromise band and neither bound holds.

**F-I2 · The stall is closed, and by how much.** *This is the falsifier that can embarrass the branch.*
Three arms, same seed, N ≥ 200: accused plays (a) `pass` every exchange, (b) `support` every exchange, (c) `advance` on the live ground every exchange.
- **Before the fix:** assert arm (b) produces **zero faults and zero clinches** — i.e. reproduce the defect. If it does not, E5 is wrong and this branch loses a plank.
- **After the fix:** assert arm (b) accrues an evasion fault on the first `support` and clinches, and that `conviction(b) ≥ conviction(a) − ε`, `ε = 0.05` `[SEED]`.
- **Control:** arm (a) against `VENUE_VALIDATION.md`'s 0.97.
- ⚠ **Stated as an upper bound.** *Whether the dodge changes the conviction RATE is unmeasured.* Under `ProofBar` the accused's `support` adds nothing to `adv[df]`, so a competent inquisitor may clear the bar regardless — in which case the dodge buys survival to close and nothing more. **The clinch is certainly dodged; the verdict may not be.** Reporting arm (b)'s rate *before* the fix is the honest measurement, and it must be reported even if it shows the dodge was harmless — an attack that fails is a result.

**F-I3 · The grounds check is genuinely three-way.**
Direct calls, no campaign: `(CI=40, L=4, evidence=2, no obligation, priors=1)` → **False**; `(…, evidence=3)` → **True**; `(…, priors=2)` → **True**; `(…, obligation present)` → **True**; `(CI=39, evidence=9)` → **False** (the AND is not weakened by the OR).
- **Observes:** the exact defect it replaces — a check that returns True on CI and Mandate alone (`tribunal.py:73`) passes the first case and fails this test.
- **And the specific trap:** `(priors=2)` must be constructed by **two guilty findings in the log**, not two ledger tags. Build it with two tags and the test passes vacuously against a `conviction_count` that reads the ledger — which is the bug E9 found. **The fixture is the falsifier here.**

**F-I4 · The Stay: availability, repetition, and the lift.**
`invoke_stay` at `CI = 55` → `status == "unavailable"`, no key, case `ttl` unchanged. At `CI = 54` with a passing vote → `resume_season == season + 1` and the case clock gains one season. **Two Stays in consecutive seasons both take effect** (`social_contest_v30.md:465`: "Multiple Stays possible"). `resolve_stay_lift` returns False before `resume_season` and True at or after it.
- **Control:** at `CI = 54` with Side A of one faction → `status == "invalid"` and the clock does **not** move. A test that only checks the happy path cannot see a Stay that grants unconditionally.

**F-I5 · Uniqueness refuses; it does not overwrite.**
`open_case` twice on one accused in one jurisdiction → the second returns `Refusal(duplicate)`, the ledger holds **one** tag, and **that tag's `created_season` and `ttl` are unchanged**.
- **Observes the exact failure E10 names:** with dedupe alone the second call succeeds and resets the clock, and a test asserting only `len(tags) == 1` **passes while the bug is live**. The `created_season` assertion is what makes this falsifier able to see it.
- Third arm: the same accused in a *different* jurisdiction → succeeds, two tags (canon `:472`).

**F-I6 · The case is multi-season, deterministic, and each write lands in its own scene.**
A seeded 6-season run: case opened season 0 (term 3), interrogated 1 and 2, stayed at 2, determined at 4.
- Same seed twice → identical `finding` **and** identical `KeyLog.content_hash()` (`keys.py:459`; the `m1_acceptance` row-2 instrument, reused).
- **Per-scene binding:** after the interrogation scene at season 1 and *before* season 2 begins, the case tag's `value` already reflects that scene's evidence write. After the Stay's scene and before the next, the clock already reflects it. **A deferred-commit implementation fails this and a same-season implementation passes it** — that is what makes it able to observe the failure the ruling excludes.
- **Control:** the two campaign goldens must not move (`engine/tests/test_mc_v18_regression.py` n=2/seed-0, `test_f7_smoke_oracle.py` n=8/seed-42). No production caller queues a `church_tribunal` slot today, so an inquiry build is **campaign-unreachable** and both goldens are identical by construction. ⚠ **That makes them a weak control, and saying so matters** — `CLAUDE.md` §7 records exactly this trap (*"for a change that is campaign-unreachable both arms are identical by construction and running it would be a fake control; ED-MB-0066 is the worked example"*). The **real** control for this branch is `engine/tests/test_contest_kernel.py` at its new `_KERNEL_EXPECTED` (today 389, `:93`), because the venue merge and `yield_strikes` change **do** move kernel checks.

**F-I7 · The accused's canonical protections exist at all.** *(a falsifier for a claim this branch does not yet make)*
Assert that a `church_tribunal` bout built with `world={"stabilities": [...]}` produces a **different** outcome distribution from one built with `world=None`.
- **It fails today**, and it should be recorded as failing: `wrapper.py:331-332` states the derived resistance *"is NOT yet plumbed into resolution"*. Canon's only mechanical concession to the accused (`social_contest_v30.md:392`) is inert.
- **Why it is here rather than in a later branch:** tightening `yield_strikes` and blocking `support` both move the balance **toward the prosecution**. Shipping those without recording that the accused's canonical counterweight is missing would be exactly the asymmetric skepticism `04_ners_audit.md` warns about — banking the change that helps my thesis and not measuring the one that complicates it.

---

## §10 · Fairness and playability

### §10.1 The exploit surface a forensic venue invites

A forensic venue is where a fabricated citation and an eristic dodge pay best; the critique's `fallacies FG-2` and the Nyāya *jalpa*/*vitaṇḍā* distinction (research §5.1 `:204-206`) both say so. What the kernel already has: `EvidenceItem.weight` is **hidden** from the player (`primitives.py:284-286`) so evidence cannot be shopped by value; `Dossier.best` only returns items whose `ground` matches the live stasis (`primitives.py:300-302`) so irrelevant evidence has nothing to present; and CR5's self-Face backfire (`rhetoric.py:413`) charges the eristic move. **Fabrication is not modelled at all** — a forged document is a Record property (`01_AXIOMS.md:857` names *forgeable* as constitutive of a Record) and there is no forge verb. That is a gap, it is not this branch's, and inventing one here would be exactly the scripting the guardrails forbid.

### §10.2 The dominant-strategy risk, and it is worse than the shape spec states

I enumerated the accused's move set against the reachable venue's actual configuration. **Six of the seven `VALID_KINDS` are losing or unavailable:**

| the accused's move | what happens | anchor |
|---|---|---|
| `hard` | `SelfGating._hard_licensed` requires `(not learned or hostile)`; `expert_judge` is `learned=True, hostile=False`, so it is **never licensed** → `fault.barred` → **instant clinch** (`barred=True`) | `primitives.py:216-219`; `modes.py:438`; `resolver.py:376-377` |
| `rebut` | `Venue.allow_rebuttal` defaults False and the venue does not set it → `fault.evasion += 1` → with `evasion_strikes=1`, **instant clinch** | `resolver.py:165, :367-369`; `modes.py:196-198` |
| `advance` off the live ground | `Stasis.relevant` fails → `fault.evasion` → **instant clinch** | `resolver.py:380-381` |
| `shift` to a non-stronger ground | `fault.contradicted` → **instant clinch** | `resolver.py:355-357` |
| `pass` | `fault.yields` — **two** refusals to clinch today, one after E8's fix | `resolver.py:345-348` |
| `evidence` | legal, but canon says the accused has **no corroboration** (`:630`) — unimplemented, so today it works | `resolver.py:359-366` |
| `advance` on the live ground | the real move | `resolver.py:375-403` |
| **`support`** | **no fault, +2 net reserve, +0.8 Standing, every exchange, forever** | `resolver.py:349-351`; `primitives.py:51-52` |

**So `support` is not merely a dodge — in this venue it is the only move that is both legal and riskless**, and it is strictly better than `pass`, which is the *only other* move that engages nothing. Against `ProofBar`'s `if closing: return df`, an accused who plays `support` every exchange guarantees reaching the close without a clinch and wins unless the inquisitor independently cleared the bar. That is a **dominant defensive line**, and the shape spec understates it by treating it as one hole rather than as the residue of eliminating every alternative.

The snapshot corroborates that a zero-fault line is reachable: `BALANCING_PASS_2026-06-05.md:59-60` records *"counterpuncher in a rebuttal venue takes zero faults / zero reserve-exhaustion"* — and the inquisition venue has rebuttal **off**, so the counterpuncher's route is closed and `support` is what remains.

**⚠ This is an UPPER BOUND on the fix, not an estimate of it.** No best-response sweep has been run for any policy in this venue, ED-SC-0021's falsifier is still unrun, and F-I2 explicitly allows the answer *"the dodge was harmless to the verdict."* What is certain is the **move-set analysis above** (each row read from the code); what is uncertain is the **rate**.

### §10.3 What the player decides, per step, and the consult load

| step | the accused's decision | the inquisitor's decision |
|---|---|---|
| before filing | **prevent it** — canon's own stated counter (`:634`): suppress CI below 40, discharge the obligation, avoid a second conviction | file now or accumulate more evidence (raising the case `value`) |
| at filing | — | **declare the term, 2–4 seasons** (`:450`) — long enough to gather, short enough to survive |
| each exchange | ground, appeal, and **whether to plead jurisdiction** (§4.6) — a 4-reserve gamble that traps a rigid inquisitor and wastes an exchange against a flexible one | which evidence to present, and when |
| once per season | Style choice (CR4's `+1D`, armature-gated) | Style choice |
| between seasons | **seek a Stay** — needs ≥2 parliamentary allies and `CI < 55` | continue, or withdraw before the next season (`:449`, at a Disposition cost) |

**Per-decision consult load at the accused's seat: ≤ 5 moves per interrogation + 1 Stay decision per season ≈ 6/season**, against a case that runs 4–6 seasons. That is the right order for a subplot that is not the player's whole season.

**⚠ `R` is not scorable until "is this seat playable?" is answered per seat** (`14_NERS.md` Rule 3). For inquiry the answer differs by seat and I will not average them: **the accused's seat is plainly playable** and the table above is its decision set; **the inquisitor's seat is NPC-driven in every named case in canon** (`:441` — an Inquisitor at rank ≥ 2, a Church office), so a dominant inquisitor line is a **portrait**, not a defect, *unless* Jordan rules the inquisitor playable. **That is the one thing that changes the reading of §10.2**, and it is a live question, not a settled one.

### §10.4 Drama, and one number that should not be re-opened

`BALANCING_PASS_2026-06-05.md:48` measures `inquisition_hearing` at drama **0.14** against a 0.20–0.35 target, and `:68-72` gives the reason: *"REVERSAL/NAIL-BITER are momentum phenomena; a burden-of-proof bar produces threshold dynamics, not lead-changes. The low drama is **largely intrinsic to the venue type**. Recommendation: exempt asymmetric venues from the target … **Not a tuning bug.**"* **Held for Jordan; not re-opened here, and not treated as a defect this branch should fix.** The `COLLAPSE% 0.99` in the same row is a **reachability pass** (the target was *"COLLAPSE reachable with fault-prone policies"*, `:38-39`), not a base rate — I misread it once and record the correct reading so the next reader does not.

---

## §11 · Open forks, each run through the five tests

`CLAUDE.md` §0 (2026-08-24): **superseded → irrelevant → answered by a design document → answered by precedent → answered by what makes sense for the architecture.** Escalate only survivors. The shape spec predicted nothing on this branch survives all five. **I agree — with one row I want to record as a genuinely close call, and one that is not mine.**

| # | fork | closed at | citation |
|---|---|---|---|
| **F1** | `open_case` eligibility (H-52, `hole_register.yaml:594`, graded `absent`) — `remit:determine` is invented; the closed five remit acts do not include it | **test 4 — precedent** | `rosters.yaml:102` lists `remit_acts: [issue, determine, confer, revoke, dispatch, convene]`, and `09_WORKED_EXAMPLES.md:131-138` puts the case-opening in the inquisitor's seat: *"here the office bites: it needs the `determine` remit."* **A seat that may determine a matter may open the matter it will determine.** Provisional on PR #362's status; **not escalated** |
| **F2** | judging set (H-32, `hole_register.yaml:346`, `assumption`; PR #362 `§F.8`) | **test 5 — architecture, then test 3** | For this venue it is *answered by code*: `PROCEEDINGS["church_tribunal"]["adjudicator"] == "expert_judge"` (`modes.py:497`), and H-32's own default — *live holders of a `hold` on an Office whose `remit.acts` includes `determine`* — resolves to exactly that seat. **Not escalated** |
| **F3** | *silence convicts* — should it convict on one refusal or two? | **test 4 — precedent** | Every other fatal fault in this venue clinches on **one** (`barred`, `contradiction`, `evasion_strikes=1`, `modes.py:197-198`). `yield_strikes=2` is the outlier, and Nyāya treats *ananubhāṣaṇa* as a *nigrahasthāna* like any other (research §5.1 `:206`). Follow the venue's own pattern. **Not escalated** — but the number is `[SEED]` and F-I1/F-I2 measure it |
| **F4** | restore the tribunal's third grounds clause | **test 3 — design document** | `social_contest_v30.md:626` carries all three; `tribunal.py:78-81` says so about itself and names the reason it was deferred (Evidence Track "not yet ported"), which no longer holds. **Not escalated** |
| **F5** | single-scene vs multi-season | **test 3 — design document** | `social_contest_v30.md:445-452` specifies the phases, durations and one-interrogation-per-season cadence. **Not escalated** |
| **F6** | `support`'s free net-+2 regroup — fix the symptom in this venue, or the cause in the kernel? | **test 5 — architecture, and it routes rather than escalates** | The cause is `Reserve.COST["support"]=2` against `REGAIN=4` (`primitives.py:51-52`) and affects **every** venue. §0.1 pt 5's signature — *the broken code was correct when written and stopped working because something else changed* — fits: `support` was written for a momentum-race venue and became free when `ProofBar` made the close a defender's win. **The pattern fix belongs to the spine, not to a venue row.** This branch ships the venue-local `restricted` because the inquiry outcome is unrepresentable without it, and hands the kernel-wide question to `01_SPINE.md` with F-I2's measurement attached. **Not escalated to Jordan — routed to a sibling** |
| **F7** | the venue merge deletes `inquisition_hearing` (a `CROSS_CULTURAL_VENUES` row) | **test 5 — architecture** | Two venues modelling one institution with different numbers is `ID-2` (two homes for one fact), and the unreachable one is the duplicate: `build_contest` cannot name it (`wrapper.py:127-130`). The canonical row is reachable and canon-cited. **Not escalated** |
| **F8** | *(close call — recorded, then closed)* the `church_tribunal` **bar height** 2.5 vs the excommunication court's 3.0, and canon's two different track starts (6 at `:396`, 7 at `:628`) | **test 5 — architecture** | Tempting to escalate as a Jordan number-call. It closes because the branch does not need it decided: the bar is **inherited verbatim** from `modes.py:196`, and the two track starts become **moot** the moment `burden` replaces `track_start` (E3) — a contradiction that dissolves rather than resolves. **If a later pass keeps a track start on this row, this fork re-opens as a genuine escalation.** Not escalated now |
| **F9** | a `Case` object with stages | **dissolved** — a false N-line (§7.3), and the tree carries it at `verb_table.yaml:349`; feedback owed to PR #357, not a decision | — |
| **F10** | *(not mine)* Record **custody** — a finding about a Person filed on a Settlement's ledger | **SE-owned, named not escalated** | `ledger.py:15-17`; `01_AXIOMS.md:857 §D.4`. One optional `holder: PersonId \| None` on `LedgerTag` would close it, default `None` preserving today's semantics byte-for-byte. **Not proposed here; named for the SE lane** |

**Nothing from this branch escalates to Jordan.** The two things that come closest — the inquisitor seat's playability (§10.3) and the drama floor (§10.4) — are both **already** in front of him: the second is `BALANCING_PASS`'s finding 1, held since 2026-06-05, and the first is a scope question about who plays a Church office that this branch does not need answered to build. Re-filing either would be the queue-growth `CLAUDE.md` §0 forbids.

---

## §12 · The strongest case against this proposal, and the attacks I ran

### §12.1 The strongest case against it

**"This is a fault-catalogue patch and a registry edit, dressed as a branch."** That is close to true and §2.3 concedes it: strip the prose and the branch is one field, one merge, one restored `if`, one dispatch arm, one write. A reader could reasonably conclude the entire document should have been a four-line commit against `modes.py` plus a `tribunal.py` fix — and that the venue row would then be *done* in the §0.2 sense, which nothing in this document is.

**The counter, and it is only partly satisfying.** The four lines are not the hard part; **knowing which four** is. Three of them (E7, E8, E9) contradict the shape spec, and one of those (E9) would have shipped a grounds clause that can never fire. The document's product is those corrections, not the design. That is a defence of the *work*, not of the *format*, and I do not have a defence of the format.

**The second strongest case: the branch tightens the screws on the accused without restoring their protections.** `yield_strikes: 2→1` and blocking `support` both help the prosecution. Canon's two counterweights — halved resistance and no corroboration — are one inert (`wrapper.py:331-332`) and one unimplemented. **On current evidence, building this branch alone makes the tribunal harsher than canon specifies.** F-I7 exists precisely to keep that visible rather than to argue it away.

**The third: it bets on a PROPOSED shape twice over.** `Act`, `Seat`, `remit`, `Receipt`, the write gate and the degree-keyed column are all PR #362/#357, held back in full. §0 states what a veto costs. What §0 does **not** state, because it cannot, is whether the *decomposition* survives a veto — I claim the mechanics are kernel-local and therefore do, but that is an argument, not a measurement.

### §12.2 Attacks run, and their results — an attack that fails and is reported as failed is a result

| attack | result |
|---|---|
| "Belief Revision already provides the inquiry game, so this branch is unnecessary" | **PARTLY SUCCEEDS, and it is the most important result here.** It is right that no *conversion mode* is needed and right that this is not a game. It fails only against the narrower claim that a **finding is a different object from a changed mind** — different key, different permanence, different gate, and only one of them can revoke a seat (§2.3). **The branch shrank to a venue row because of this attack, and it should have** |
| "`PROCEEDINGS['church_tribunal']` already uses `ProofBar`, so E7 is invented work" | **FAILS.** `proceeding_venue` (`modes.py:536-562`) builds `PersuasionTrack(start=6.0)` for that row; `ProofBar` lives only in `inquisition_hearing_venue` (`:196`), which `build_contest` cannot name (`wrapper.py:127-130`). Two surfaces, verified by reading both |
| "*Silence convicts* is already MECHANICAL via `evasion_strikes=1`" | **SUCCEEDS against the shape spec, twice.** Wrong fault (E8: silence is `yield_strikes`), and dodgeable anyway (E5). The second half was found independently in 2026-06 (`AUDIT_RECONCILED.md:184-185`) and left unexplored |
| "The Stay nests an act inside another act's resolution, so it conflicts with D-49" | **FAILS — and the failure is the §4.6 result.** The Stay is a separate proceeding with different parties in a different venue (`parliamentary_stay.py:85`), which canon states three times (`:634, :649, :465`). Nothing nests. **What the attack did find** is that the shape spec's own S3.1 wording *would* have created the conflict, and that a genuine in-bout venue challenge already exists as a `shift` to JURISDICTION — unremarked anywhere |
| "A `Case` needs stages, so a `Record` with stages is necessary" | **FAILS, against PR #357's live verb table.** `KeyLog` supplies the stage reached; `ttl`/`Tenure.term` supplies the declared duration. `verb_table.yaml:349` carries the field anyway (§7.3) |
| "`ledger_add`'s dedupe gives uniqueness for free" | **SUCCEEDS against the shape spec.** Dedupe **refreshes in place** (`ledger.py:53-57`); a duplicate `open_case` would silently reset the case clock. And it takes the conviction-count clause down with it (E9) |
| "The finding can ride the existing echo transport" | **SUCCEEDS against the spine's §2.1.** Three independent blocks (E11), of which the payload-validation one is fatal: `KeyLog.append` raises |
| "Blocking `support` is a false N-line — `DefeatCatalogue` already carries venue fault policy" | **INCONCLUSIVE, and kept at medium confidence.** `DefeatCatalogue` is keyed by fault, not by move × side, and has no side dimension at all (`primitives.py:267-279`). But if the spine introduces a side dimension for another reason, `restricted` should be cut and folded into it. **Watched (§7.3)** |
| "The campaign goldens are the control for this branch" | **SUCCEEDS against my own first draft.** No production caller queues a `church_tribunal` slot, so an inquiry build is campaign-unreachable and both golden arms are identical **by construction** — the fake-control trap `CLAUDE.md` §7 names. The real control is `_KERNEL_EXPECTED` (F-I6) |
| "The venue is already balanced — `BALANCING_PASS` passed it" | **FAILS as a defence of the venue, and I nearly mis-cited it in the other direction.** The 0.99 in that row is COLLAPSE *reachability*, which was a target and passed. The genuine finding there is the drama floor 0.14, which the same document says is intrinsic and not a tuning bug (§10.4) |

### §12.3 Asymmetric-skepticism check, and the self-review bias

I applied a harder standard to the shape spec's claims (each read against the tree, six amended) than to the **snapshot's measured numbers**, which I accepted from `VENUE_VALIDATION.md` and `BALANCING_PASS` without re-running anything — I was instructed not to run tests, so this is a bounded limitation rather than a lapse, but the asymmetry is real and those numbers are therefore **controls, not verified facts**. Under the same rule, F-I1's bands are `[SEED]`-grade until a run reproduces them.

This document also audits a document produced in the same session for the same coordinator (`CLAUDE.md` §8.6 of the brief: the branch proposals are themselves under audit). **The limitation an independent reviewer would add, and which I cannot supply:** every claim in §10 rests on reading the move set out of `_apply` and reasoning about it. **Nobody has run a policy against this venue in this configuration.** A single seeded 200-bout run of the three F-I2 arms would settle in minutes what §10.2 argues at length — and if it showed `support`-spam converts at the same rate as active defence, §10.2's "dominant defensive line" would be wrong in its consequence while remaining right in its mechanism. **That run is the highest-value next action on this branch, and it is not in this document.**

### §12.4 The grade, restated last and plainly

**PAPER.** `ProofBar`, the inquisition venue, `formal_grounds_check`, `invoke_stay`, `Dossier`, `LedgerTag`, `queue_scene` and `KeyLog` all execute today, each in isolation. **The sequence in §4 does not exist, no scene queues a tribunal, no finding has ever been written, and no falsifier in §9 has been run.** Under `CLAUDE.md` §0.2 that is the grade that matters, and it does not change when this file merges — it changes when F-I1..F-I7 execute and something runs them.

---

*End. One file. Nothing else was created or edited.*
