# Refutation — Content Feasibility (adversarial skeptic lane)

## Status: WORKING NOTES (not canonical). Role: break the synthesis on CONTENT FEASIBILITY.
## Author: opus adversarial-skeptic subagent, 2026-07-05.
## Method: charter method rules — cite file+§ for every claim; KNOWN NERS items are context; [OPEN — Jordan] numbers are calibration.

Sources compared: `synthesis.md` (esp. §6, §8, fork 6), `dossier_content_economics.md`
(§2.1/§2.2/§3/§5), `dossier_nlg_graduation.md` (§4 bake pipeline, §6 open decisions),
`00_engine_charter.md` (Q4 anti-oatmeal items 1-3, capstones #10/#11), `01_arc_corpus.md`
(a: 5 fixed seeds; c: gm_ref corpus).

---

## Attack 1 — The bake-volume headline contradicts the synthesis's own default fork. (BLOCKER-severity claim)

Synthesis §6 states: "Content-economics dossier: **~350-450 authored units** under orthogonal
composition **(feasible)**; the Certainty axis is a fork (§7 fork 6)."

Synthesis fork 6 default: "**include it (charter authority)** — swings the bake ~5-6×
(dossier_content_economics); fallback if bake cost prohibitive = Certainty as a runtime
lexicon-swap, not a frozen-pool axis."

The 350-450 figure is the dossier's factored estimate (`dossier_content_economics §2.2`) computed
*without* Certainty as a frozen-pool axis. The dossier is explicit (`§3 item 3`, echoed in `§5
item 2`): "if Certainty must gate the FROZEN FRAGMENT pool (not just a runtime lexicon swap),
§2.2's backbone estimate should multiply by up to ~5-6×, **pushing the low-hundreds estimate into
the low-thousands**."

So: the synthesis presents "~350-450 (feasible)" as the bake number, while its own default fork
resolution (include Certainty in the pool) is precisely the choice the dossier says invalidates
that number by 5-6×. Under the stated default the honest figure is **low-thousands**, not 350-450.
The "(feasible)" verdict is attached to the fallback's number but the default's fork choice. This
is not a wording nit — the whole "C1 authored-templates is affordable" story rests on the
low-hundreds figure, and the synthesis's own default breaks it.

Note also the dossier's verdict (`§5`) is CONDITIONAL-feasible: "FEASIBLE at the anti-oatmeal bar
— **but only** under the factored discipline … **and only if** two open items get closed"
(Certainty discrepancy + per-NPC/per-arc authoring effort). Synthesis §6 strips the "but only if"
and presents an unconditional "(feasible)".

REQUIRED FIX: State both figures against both fork-6 resolutions explicitly — "~350-450 units
holds ONLY if Certainty is a runtime lexicon-swap (fork-6 fallback); under the fork-6 DEFAULT
(Certainty in the frozen pool) the bake is low-thousands per `dossier_content_economics §3.item3`."
Either flip fork 6's default to lexicon-swap (making 350-450 honest) or carry the low-thousands
number as the headline. Do not present 350-450 as "feasible" while defaulting to the 5-6× choice.

---

## Attack 2 — "Anti-oatmeal is STRUCTURAL" conflates data-divergence with prose-distinctiveness. (BLOCKER-severity claim)

Synthesis §6: "**Anti-oatmeal #1 is STRUCTURAL here**: because arc_vectors are DATA, two seeds
diverge in named actors / stakes / outcomes (capstone #11), **verifiable because vectors are data
not prose**."

This proves the wrong thing. That vectors are data guarantees the *slot fillers* (proper nouns,
stakes tags, outcome states) differ across seeds. It does NOT guarantee the *rendered prose* reads
differently. If two seeds fire the same `(key_type × significance_band × coherence × certainty ×
focalizer)` cell and differ only in `targets[].actor_id`, the chronicle is structurally identical
prose with a name swapped — which is *exactly* Compton's oatmeal failure.

The dossier says this in as many words (`§3 item 2`): generic slot-fill "risks producing
structurally-identical prose across arcs that only differ in proper nouns — exactly Compton's
oatmeal risk," and the register's existing `Direction:`-sentence substitution model is "good
enough for a mechanical register, **not obviously good enough for player-facing prose without
additional arc-specific authored color beyond simple substitution**."

The charter's actual anti-oatmeal bar is not data-divergence and not two seeds. Q4 anti-oatmeal
item 3: "the arc_test_batch seed method as NARRATIVE regression — **5 seeds must yield chronicles
differing in named actors, stakes, outcomes**" (5 fixed seeds [42,77,99,137,201] per
`01_arc_corpus §a`). The instrument that actually measures prose variance is Expressive Range
Analysis, which `dossier_nlg_graduation §4 step 5` / `§6 item 7` flags as an **unbuilt method**
("currently unbuilt"), and which `03_articulation_nlg_architecture §9` lists as unresolved. So the
one gate that could substantiate "anti-oatmeal met" does not exist yet, and the synthesis asserts
the capstone met "by construction" anyway.

The synthesis also argues the weaker case: capstone #11 is a two-seed *sketch*, but the standing
anti-oatmeal regression gate (Q4 item 3) is 5-seed prose distinctiveness. Two-seed data-divergence
is neither the 5-seed bar nor a prose bar.

REQUIRED FIX: Downgrade the §6 claim from "anti-oatmeal is STRUCTURAL / verifiable because vectors
are data" to: "vector-as-data guarantees slot-filler divergence; **prose distinctiveness is NOT
structural** and must be certified by the ERA bake gate (`dossier_nlg_graduation §4 step 5`) over
the 5 fixed seeds. ERA is currently an unbuilt method — building it is a Stage-5 blocker for the
anti-oatmeal capstone, and arc-specific authored color beyond name-substitution is a distinct bake
line item (`dossier_content_economics §3 item 2`)." Do not assert capstone #11/Q4-item-3 met "by
construction."

---

## Attack 3 — Per-NPC voice is budgeted at the name-swap floor of a range the dossier says has no per-unit ceiling. (MAJOR)

Synthesis §2.2 folds per-NPC into the factored total as "~100-175 units" (dossier §2.2c: 3-5
micro-units × 35 Active NPCs). The synthesis carries this optimistic figure into the "350-450"
headline and does not carry forward the dossier's flagged risk.

The dossier is explicit that 100-175 is the FLOOR, not the estimate (`§3 item 1`): the 35-NPC cap
"bounds the COUNT but not the AUTHORING EFFORT PER NPC — if each Active NPC genuinely needs several
idiolect-specific fragment variants across the ~10 triggers that can fire for them, effort is
closer to **35 × 10 × (a few variants)** than 35 flat … bounded in cardinality (good), **NOT
bounded in per-unit authoring cost (open risk)**." 35 × 10 × 3 ≈ 1,050 units for per-NPC alone —
i.e. the per-NPC axis by itself can exceed the entire "350-450" total.

Charter Q3 makes the higher bar mandatory, not optional: "**Recognizable-yet-dynamic NPCs** …
per-NPC lexicon overlays," and "two Bonded NPCs both getting `state.scar_acquired` cut scenes must
not read as the same template with a name swapped in" (`dossier_content_economics §3 item 1`).
Name-swap-level overlays (the 100-175 figure) are exactly what that bar forbids.

REQUIRED FIX: Split per-NPC into a distinct bake line item with a range whose top end reflects
`35 × (triggers-that-fire-per-NPC) × variants`, not the 3-5×35 floor. State that hitting Q3
"recognizable-yet-dynamic" without oatmeal is an authoring-craft cost the combinatoric factoring
does NOT certify (dossier §5 item 3), and that the "feasible" verdict is conditional on this being
budgeted — mirror the dossier's conditional verdict rather than absorbing per-NPC into a flat
optimistic total.

---

## Attack 4 — No minimum-viable fragment corpus for the capstone slice; Stage 0 "near-zero cost" is unbacked. (MINOR–MAJOR)

Synthesis §7 Stage 0: render-gap close "**Closes ED-IN-0004 + C6 at near-zero cost** … Unblocks
capstone #10." Capstone #10 = ARC-S07 (Torben Loyalty Clock) compiled end-to-end with template
slots + trace; capstone #11 = two-seed chronicle sketch.

Neither the synthesis nor `dossier_content_economics` states how many fragments the capstone slice
actually needs. The dossier gives a full-corpus factored estimate (§2.2) but no MVP number for
rendering even ONE arc (ARC-S07) end-to-end across the Coherence/Certainty/focalizer cells S07
touches, at a distinctiveness sufficient for the two-seed sketch. `dossier_nlg_graduation §5`
correctly names ARC-S07 as "the proof the schema … actually closes on a real arc" and §4 step 2
leaves per-cell count "N = a count budget — open (§6)". So "near-zero cost" is asserted for a stage
whose fragment count is unscoped.

This is softened by capstone #11 being a "sketch" (charter #11) — a design-level demonstration may
not require full rendered prose — but Stage 0's job includes an actual ARC-S07 *trace* (#10) and a
working realizer, which do require concrete fragments. "Near-zero cost" conflates "the *code edit*
(add triggers, graduate schema) is cheap" with "the *fragment authoring* to render the capstone is
cheap." Only the former is near-zero.

REQUIRED FIX: Scope an explicit MVP fragment count for the capstone slice — the ARC-S07
key-types × reachable cells needed for the #10 trace, plus the minimum arc-specific authored color
for a #11 sketch that differs in prose (not just data). Restate Stage 0 as "the code/schema edits
are near-zero cost; the capstone *fragment authoring* is a separate, non-zero Stage-0/Stage-5 line
item" rather than a blanket "near-zero cost."

---

## Where the synthesis is CORRECT (concede, so the critique is honest)

- It correctly rejects the naive 31k–5.4M cross-product (`synthesis §6` / dossier §2.1) and adopts
  the "product becomes a sum" factoring (`03_… §2`). The *structure* of the bake strategy is sound.
- The 35-Active-NPC cap (dossier §1.8, PP-661) genuinely bounds cardinality — the count cannot
  explode without limit; the risk is per-unit effort, not runaway N.
- Fork 6 correctly identifies the Certainty-in-bake-key discrepancy as a real Jordan call and
  provides a lexicon-swap escape hatch that WOULD keep the bake at low-hundreds. The defect is
  which side is the default and how the headline number is framed, not that the fork was missed.

## Verdict

**SOUND-WITH-FIXES.** The architecture is not content-infeasible — it IS buildable IF (a) Certainty
is a runtime lexicon-swap (fork-6 fallback) and (b) arc-specific and per-NPC distinguishing color
is genuinely authored and budgeted, with (c) the ERA gate built to certify the 5-seed prose bar.
But the synthesis as written overstates feasibility: it prints the low-hundreds number while
defaulting to the 5-6× fork choice (Attack 1), asserts anti-oatmeal is structurally met when the
certifying gate is unbuilt and the claim only proves data-divergence (Attack 2), budgets per-NPC at
the floor of an uncapped-effort range (Attack 3), and calls the capstone-fragment authoring
"near-zero cost" without a count (Attack 4). All four are fixable by honest restatement + explicit
budget line items; none break the spine.
