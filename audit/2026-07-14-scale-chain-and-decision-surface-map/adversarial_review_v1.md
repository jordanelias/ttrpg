# Adversarial Review — Scale-Chain & Decision-Surface Docket (2026-07-14)

## Status: FILED (analysis) — 2026-07-14 · Lane: IN · ED-IN-0064

**What this is.** An independent, refute-by-default antagonist pass (Opus 4.8, read-only tools)
over the five docket artifacts — `chain_map_v1.md`, `decision_surface_census_v1.md`,
`churn_event_opportunity_map_v1.md`, `gap_register_v2.md`, `decision_queue_delta_v1.md`. Every
load-bearing edge classification and count was **re-checked against the actual `sim/` working tree
and the cited design docs** (caller sites grepped, not inferred). The binding constraint — *Mandate
of Heaven must not appear as a proposed Valoria mechanic* — was scanned across the whole docket and
the re-groundings were verified against `research/governance/conflicts_power_struggles.md`.

**Attack surface (per charter):** (1) edge misclassification, (2) MoH leakage, (3) surface-analogy
resolutions, (4) census count errors, (5) unsupported claims.

**Headline.** The docket's structural spine is **sound and unusually well-evidenced**: I independently
confirmed the four headline gaps (scale enum 4-of-6, FI zero-dispatch, L/PS 100/100 inert, V2 the one
live vertical aggregation) and the "orphan mutator" correction's *direction* against code. The MoH
binding is **satisfied — clean**. The defects are concentrated in one balance-relevant firing-frequency
overstatement, one internally self-contradictory caller count, and a cluster of citation imprecisions.
None overturns a headline gap; all are correctable in place. **Overall: SOUND_WITH_FIXES.**

---

## §0 · What survived the attack (confirmed against code — not findings, but the basis for the verdict)

These were the highest-value claims to break, and they held:

- **scale_signature enum is 4-of-6.** `sim/substrate/keys.py:62` — `SCALES = ("personal", "settlement",
  "territory", "peninsula")`. Confirmed. And `keys.py:355-359` **actively raises `KeyValidationError`
  on any non-canonical scale** — so V4 (territory→province→duchy→country) BROKEN-at-substrate is not
  merely a doc claim; the substrate genuinely rejects the stamp. (See F-3 for a citation correction that
  *strengthens* this.)
- **FI has zero live dispatch.** `sim/cross_scale/scene_dispatch.py:137` `if st == "combat"`, `:146`
  `elif st == "contest"`, `:214` else "not live". No `fieldwork`/`investigation` branch. Confirmed.
  `sim/personal/investigation.py` and `fieldwork.py` exist (1101 / 1071 bytes) with **zero external
  importers** — genuine import-orphans. NG-2 / H6 BROKEN confirmed.
- **Only Stability Crisis is live among the zoom-in triggers, and it routes to `contest`.**
  `scene_dispatch.py:64-83` fires on `Faction.Sta <= 2`, `scene_type: "contest"`; `evaluable =
  {"Stability Crisis"}`, all others deferred. `_emergency_council_parties` (`:104-122`) derives
  `side_a = round(f.L)`, `side_b = round(7.0 - f.Sta)` — exactly the "L / 7−Sta" claim. Confirmed. The
  canonical scene content *does* offer a fieldwork option (`scale_transitions_v30.md:137`: "social
  contest **or fieldwork** scene… assess (Fieldwork Evidence +2…)"), so the "routes to contest, never
  FI, despite a canonical fieldwork option" claim is supported.
- **L/PS 100/100 inert.** `Settlement.legitimacy`/`popular_support` appear in `sim/` **only** as field
  definitions (`sim/territory/registry.py:64-65`) and in comments/string-literals (`faction_action.py:331`,
  `npe.py:72`, `scene_dispatch.py:112`). Zero non-definition reads/writes. `lps_inert_check` red is
  supported; the scalar `Faction.L`-as-Mandate placeholder is real (`parliamentary_vote.py:~168`:
  `mandate = sum(int(world.factions[d.faction_name].L) for d in decls)`, PRE-LPS-1/PORT-BLOCKING note
  at `:~20`). V3 / NG-3 SPEC-ONLY confirmed.
- **V2 is the one live vertical aggregation.** `sim/territory/registry.py:124-130`
  `province_accord = math.floor(sum(m.order for m in members) / len(members))`. Confirmed WIRED,
  exactly as described.
- **The echo path is flag-gated / INERT-by-default.** `echo_transport.py:emit_scene_echo` fires only
  when `world.echo_scheduler is not None` **and** `ctx` carries an `echo` block; returns `{}` (byte-exact
  no-echo) otherwise, and hardcodes `scale_signature=["personal"]` (`:~145`, "enriched in the PR-3 keying
  wave"). `mc_v18.py:109-113` gates `parliamentary_bridge.run_parliamentary_scene` on the same scheduler.
  V8 / H2′ / H3 INERT-under-flag confirmed.
- **`parliamentary_transfer` is never called from the live loop.** Only references are a doc-comment
  (`__init__.py`) and `test_f7_smoke_oracle.py` — whose own docstring says "the only restoration path,
  parliamentary_transfer, is never called." GAP-A1 (territory one-way ratchet) confirmed.
- **`parliamentary_stay` is an import-orphan.** No live caller. Confirmed.

---

## §1 · Findings (ranked most-severe first)

### F-1 · [edge-misclassification · CONFIRMED] The H2 Censure edge is labeled "unconditional / every season"; it is neither.

**Where.** `chain_map_v1.md §0.4` ("`run_parliamentary_vote` is reached **every season,
unconditionally**"), the §2.2 caller-graph (`PC ==>|UNCONDITIONAL — WIRED| RPV`), the §2.1 H2 row
("Unconditional, applies §5.4 Censure"); `gap_register_v2.md §3 H2` ("`parliamentary_vote` mutates
live state **every season**").

**What the code actually does.** `sim/provincial/faction_action.py:176-245` (`faction_take_action`):
the four action buckets carry PRIOR weights **30/35/20/15** (unique/Conquest/Muster/Govern), are
state-reweighted, renormalized, and resolved by a **single selection draw** — `if roll < cum_unique:`
where neutral `cum_unique = 0.30`. So the unique slot (which contains the Censure fallback) is entered
**~30% of the time in a neutral state**, not every season. Inside it, `_try_faction_unique` (`:265`)
reaches `propose_censure` only when (a) `faction.parliamentary` is true **and** (b) the faction-specific
unique first returns `_NOOP` (Crown/Church frequently do not), and `propose_censure` then **self-gates
on GD-3 + the §5.4 proposer-minimum**, returning `_NOOP` when unavailable.

**Why it matters.** This is not a labeling nicety — the docket uses "mutates live strategic state every
season" to argue the §10 vote is a live balance force. The real firing rate is *probabilistic and
quadruple-gated*, materially lower than "every season." The docket even contradicts itself in the same
sentence ("every season, unconditionally … in the **30%-prior unique slot**").

**Correction.** Relabel H2: **WIRED but conditional/probabilistic** — reached via the ~30% (neutral,
state-reweighted) unique slot, gated on parliamentary-eligibility + specific-unique-fallthrough +
GD-3/§5.4 proposer-minimum. The *substantive* correction the docket makes (retire "orphan mutator":
`parliamentary_vote` has a live, non-echo-gated caller) **stands and is correct** — only the
"unconditional / every season" firing claim is wrong. Drop "UNCONDITIONAL" from the caller-graph edge.

### F-2 · [count-error · CONFIRMED] The `run_parliamentary_vote` caller count is both wrong and internally self-contradictory.

**Where.** `chain_map_v1.md §0.4` says "**three** live/near-live callers plus **two** orphan wrappers"
(3+2). `chain_map_v1.md §2.2` says "**five** call sites: **two** live … and **three** orphaned" (2+3).
These disagree on the live/orphan split while both asserting a total of five.

**What the code actually shows** (`grep run_parliamentary_vote sim/ --include=*.py`, excluding
tests/doc-comments): **four** real call sites —
1. `parliamentary_action.py:136` (`propose_censure`) — **live**, conditional (F-1).
2. `parliamentary_bridge.py:104` (`run_parliamentary_scene`) — **live**, flag-gated (H2′).
3. `parliamentary_transfer.py:151` — **orphan**.
4. `parliamentary_stay.py:85` — **orphan**.

The emergency-council contest, counted in §2.2 as the third "orphaned call site," **is not a caller of
`run_parliamentary_vote` at all** — the docket itself says it "routes through `sim.personal.contest`,
not this function." Counting a self-admitted non-caller inflates the total to five.

**Correction.** `run_parliamentary_vote` has **4 call sites: 2 live** (propose_censure — conditional;
parliamentary_bridge — flag-gated) **+ 2 orphan** (parliamentary_transfer, parliamentary_stay). The
emergency-council path is **not** a caller of this function (it is a caller of `sim.personal.contest`)
and should be dropped from the count entirely, not filed as an "orphaned call site." Reconcile §0.4 and
§2.2 to this single number.

### F-3 · [unsupported-citation · CONFIRMED, self-strengthening] V4/NG-1 attribute the scale-canonicity rejection to doc "invariant 7," which does not contain it.

**Where.** `chain_map_v1.md §1.1` — "the substrate would reject or mis-stamp them
(`doc:key_substrate_v30.md:122` invariant 7: `scale_signature` non-empty *and* members must match the
canonical set)." `gap_register_v2.md NG-1` — "`audit:key_substrate_v30 §12 invariant 7 rejects
non-canonical members`."

**What the doc actually says.** `key_substrate_v30.md:122` invariant 7 reads, in full: "`scale_signature`
non-empty." There is **no** "members must match the canonical set" clause, and it is in §2.3, not §12.
The canonicity constraint lives in the §2.1 enum definition.

**The behavior is nonetheless real** — enforced in **code**: `keys.py:355-359` iterates the signature
and raises `KeyValidationError(f"…non-canonical scale {scale!r} (§2.1)")`. So the V4 BROKEN
classification is **correct and, in fact, understated by its own citation** — there is live code
enforcement, not just a doc invariant.

**Correction.** Re-cite the rejection to `code:keys.py:355-359` (enforcing the §2.1 enum), not doc
invariant 7. Strike "members must match the canonical set" from the invariant-7 paraphrase. V4 / NG-1
classification is unchanged (BROKEN).

### F-4 · [grounding-thinness · PLAUSIBLE] Two of the non-MoH re-groundings are real but thinly/imprecisely cited.

**Context.** The binding re-grounding of GAP-B2 (relief-valves) and GAP-B4 (decay) leans on
*recusatio/Ambrose* (self-reproach) and *Polybian anacyclosis* (decay, confirmatory). Both are
genuinely present in the corpus and genuinely non-MoH — the binding is satisfied — but:

- **Self-reproach (recusatio + imperial penance under Ambrose)** appears **only** in the consolidated
  hooks table (`research:41`), with **no dedicated Roman body section**. The Roman detail §§1-9 covers
  Gracchi, Marius/Sulla, Caesar, the Year of Four Emperors, Didius Julianus, the Third Century,
  Tetrarchy, adoptive succession, and the Jewish revolts — but never develops recusatio/penance. By
  contrast the collision groundings (GAP-E1/E2) each have full body sections (§1, §4). The self-reproach
  valve is therefore the **least-substantiated** re-grounding — a single hooks-table line.
- **Polybian anacyclosis** is cited by `gap_register_v2.md §7` and `decision_queue_delta_v1.md §C` as
  "`research` synthesis." It actually lives in the **Han/Three-Kingdoms §3.6 (Dong Zhuo)** section
  (`research:363-365`), where it is explicitly framed "**non-MoH**… rather than dynastic-cycle framing."
  The precedent exists and is clean; the section-pointer is wrong.

**Correction.** (a) Cite recusatio to `research` hooks-table row "Ritual self-abasement," and flag that
the self-reproach valve wants a dedicated body paragraph before it grounds a ratified mechanic — do not
represent it as body-attested. (b) Re-cite anacyclosis to `research:§3.6` (Dong Zhuo), not "synthesis."
Neither correction affects the MoH binding (both are non-MoH).

### F-5 · [methodology · PLAUSIBLE] The census's ~4-5 bar sits *at* the scene-action budget, but the doc's own "surplus is the point" logic requires the menu to *exceed* it.

**Where.** `decision_surface_census_v1.md §0` derives the "~4-5 meaningful verbs" bar from
`player_agency_v30.md §6.1`'s Scene Action Budget (confirmed: `player_agency_v30.md:55` "3–5 scene
actions per season"; `:308` "The surplus is the point"). The method text itself says a decision is real
only "when affordable moves are numerous enough to force triage and **the menu exceeds the budget**."

**The tension.** If the budget is 3-5 and the menu must *exceed* it to force triage, the pass bar for a
"real decision surface" should be **> 5**, not "≈4-5" (which is merely *at* budget, i.e. near-zero
surplus). The proposed fills (council ~5, bureaucrat ~5, Parliament ~4 — NG-4/DS-1/DS-2/DS-3) are
authored **to the ≈4-5 floor**, so if implemented at exactly that count they clear the census's own
"surplus" rationale only marginally.

**Correction.** State the fills' ~4-5 as a **floor, not a target** — or raise the target to menu-exceeds-
budget (≥6) so the authored surfaces deliver the surplus the method is built on. The census flags its
bar as "deliberately soft," so this is a calibration note, not a broken verdict; the THIN/OK verdicts
themselves are unaffected.

### F-6 · [count-inflation · PLAUSIBLE] The governor "~11-13" double-counts method sub-choices as standalone verbs.

**Where.** `decision_surface_census_v1.md §3(b)` — "~11-13 (8 core verbs + ~5 expansions + 3 Directive
responses)."

**Check.** The 8 core verbs are confirmed (`governance_play_redesign_v1.md §1.3:53-60`: Develop,
Fortify, Keep Order, Hold Court, Sponsor, Treat, Levy, Investigate). But of the "~5 expansions," several
are **method/branch sub-choices of existing verbs, not standalone verbs**: Survey and Negotiate Quota
are §1.3a method branches; Ordenanza is "three-branch **under Hold Court**." Only Retain Clerks (§1.3:39)
and Bind the Cells (§1.3b) are genuinely new standalone verbs. Counting sub-choices as separate
"meaningfully distinct" actions contradicts the census's own overlap discipline (§0: "where two words
mean the same thing they are noted as overlaps").

**Correction.** The defensible standalone count is ≈**10** (8 core + Retain Clerks + Bind the Cells +
3 Directive responses, net of method-branches). The **OK verdict is robust regardless** — 8 standalone
verbs already clear any reading of the bar — so this is a count hygiene note, not a verdict change.

---

## §2 · MoH binding — explicit verdict: CLEAN (no finding)

The charter's hard constraint is that **Mandate of Heaven must not appear as a proposed Valoria
mechanic.** I grepped every MoH-shaped token (`mandate of heaven`, `MoH`, `zaiyi`, `heaven`) across all
five docket files and read every hit in context:

- **Every** MoH occurrence is in a binding-notice, the §7/§C re-grounding apparatus, or a
  "**historical grounding only**" / "**do not port**" / "**never MoH warlordism**" tag. **Zero** MoH
  mechanics are proposed in any Valoria-mechanic column.
- The two previously MoH-grounded items are re-grounded on non-MoH precedent, and I verified **each
  cited precedent exists in `research/governance/conflicts_power_struggles.md` and is non-MoH**:
  - GAP-E1/E2 collision → Roman Gracchi (`research:§1`, lines 103-105), Year of Four Emperors
    (`§4`, 115-117), Ottoman Janissary + Şeyhülislam fatwa (`Ottoman §Janissary/§fatwa`, 67-86),
    Carolingian 887-888 (`§3.8`, 179-181). The Roman brief carries an explicit verifier verdict
    "**MoH leakage: NONE — confirmed clean**" (`research:97`); mechanism framed as army-loyalty fission.
  - GAP-B2 scapegoat → Venetian graduated-removal ladder + procurator sinecure **and** Ottoman
    grand-vizier-as-scapegoat (`research:26,40`). Self-reproach → Roman recusatio + Ambrose penance
    (`research:41`; see F-4 on its thinness). Decay → Polybian anacyclosis (`research:363-365`,
    explicitly "non-MoH"; see F-4 on the section-pointer).
- **Terminology guard for readers:** the docket's pervasive term **"Mandate"** (as in "Mandate =
  Σ settlement L/PS," `settlement_layer §1.5`; "Mandate-collapse relief-valve") denotes Valoria's
  **endogenous aggregate stat**, *not* the Mandate of Heaven. This is handled correctly throughout —
  the research row even labels it "Mandate-collapse relief-valve (scapegoat)… **no MoH**" (`research:40`).
  A naive reviewer might flag "Mandate"; it is not a leak.

**No MoH leakage found.** The binding is satisfied.

---

## §3 · Surface-analogy audit (charter attack #3) — no unflagged violations

I checked whether any proposed fix is justified by *resemblance* rather than a *read/write dependency*:

- The thin-surface fills (NG-4/DS-1/DS-2/DS-3) and Parliament verbs (NG-5) import HRE/Roman/Venetian
  precedent — but they are **correctly classified `[GENUINE-GAP]`**, which the docket's own doctrine
  defines as precisely the case where "an imported-and-adapted precedent [is] load-bearing." Each fill
  additionally carries the read/write guard "must **emit a down-tier Key** or it is decorative." That is
  a dependency requirement, not an analogy. **Not a violation.**
- The one edge that *is* resemblance-not-dependency — §6.2 event→Parliament/SC ("opening Ob from the Key
  magnitude") — is **self-flagged AT-RISK** by the docket and routed to "earn (`stakes.source_key`
  consume-edge) or weaken," never resolved by analogy. Correct handling.
- The collision primitive and relief-valves are each defined as concrete co-firing/spend **Key
  dependencies** (two independent Keys co-fire; an appointee's Standing Key absorbs the delta; an
  L/PS-priced ritual spends the ruler's own resource), with the histories as illustration. Legitimate.

No fix in the docket rests on surface analogy without either (a) a stated read/write dependency or
(b) an explicit AT-RISK "earn-or-weaken" flag.

---

## §4 · Overall verdict

**SOUND_WITH_FIXES.**

The docket's four headline structural claims survived independent code verification, the "orphan
mutator" correction is directionally right, and the **MoH binding is clean** with all re-grounding
precedents confirmed present and non-MoH in the research corpus. The surviving defects are bounded and
in-place-correctable: one balance-relevant firing-frequency overstatement (F-1, "unconditional" →
conditional ~30% gated), one self-contradictory and inflated caller count (F-2, 5 → 4 call sites), one
mis-cited-but-real invariant (F-3, cite `keys.py:355-359` not doc invariant 7), and three lower-severity
citation/methodology/count-hygiene notes (F-4/F-5/F-6). None overturns a gap classification, a THIN/OK
verdict, or the ranked decision queue. Apply F-1 through F-3 before the DESIGN pass leans on the H2/§10
"live every season" framing or the caller-graph; F-4 through F-6 are cleanups.
