# Polearm close-quarters grounding: grip-asymmetry overhang & thrust-degradation

**Status:** Research/grounding memo only — no engine files edited, no decisions made. This
compiles a multi-angle research pass (four research angles + engine-model verification +
synthesis + skeptic refutation attempt + reconciliation) into one artifact for Jordan's
Track-2 ratification. Nothing here is greenlit; see §6 for what remains genuinely his call.

---

## 1. Jordan's original claim

> Both of Jordan's claims under test in this memo:
>
> **Claim A (grip asymmetry / overhang):** choking up on a spear or staff at close range
> carries a distinct handling penalty from managing a two-ended, asymmetric-mass object —
> it "can't swing/rotate/turn near as smoothly" as a naive single-pivot model would predict,
> because there is real mass and length trailing behind the grip that must clear space when
> the wielder is surrounded or in a tight formation.
>
> **Claim B (thrust degrades to shaft-strike):** at close range, with a high choke grip, a
> "thrust" from a polearm cannot actually extend to its full reach — it functionally
> degrades into a shaft/butt strike, because the point can no longer be brought to bear.
>
> Both claims were raised against the current engine's treatment of the spear, specifically
> against the numeric finding that `grip_choke_max = 1.0` for the spear (identical to the
> staff) with no additional handling or reach-degradation penalty — the suspected root cause
> of a reported 94–96% spear win-rate anomaly.

---

## 2. Research angle: European quarterstaff/short-staff HEMA doctrine

This last result (Stacy Clifford/ARMA webmaster quoting Silver directly: "the longer the
staff, the more the tail end causes problems when you start choking up toward the middle")
is a strong, directly-on-point corroboration, though it's a forum paraphrase of Silver rather
than a verified direct quote — flagged as unverified-to-primary.

### Findings (staff/spear close-range handling — grip-choke overhang and thrust-degradation)

**Claim A (grip asymmetry/overhang, trailing-end clearance cost) — partially supported at T2,
unverified at T0/T1:**
- **T0 (primary, indirect):** George Silver, *Paradoxes of Defence* (1599) and *Brief
  Instructions* (1605) — describes the standard quarterstaff grip as back hand near the butt,
  forward hand ~1–1.5 ft above it (i.e., an intentionally asymmetric, forward-loaded grip),
  not a centered one. Silver's short-staff material is grip-position-explicit but no
  independently verifiable direct Silver quote stating overhang causes handling problems could
  be found — only a paraphrase.
- **T2 (named-instructor commentary, unverified against primary):** ARMA webmaster (Stacy
  Clifford), forum post citing Silver: "the longer the staff, the more the tail end causes
  problems when you start choking up toward the middle." This is exactly Jordan's claim, but
  it's a forum paraphrase — flagged, not verified to T0.
- **T3 (enthusiast forum, directionally consistent):** ARMA forum poster Jay Vail: "At
  distance the half staff position has nothing to recommend it. It lacks reach"; Stuart
  McDermid notes the choked-up grip leaves "a nice long butt... to close with," implicitly
  conceding the trailing length is a separate management variable, not simply discarded mass.
- No source (T0–T2) gives a quantitative or biomechanical treatment of trailing-mass/clearance
  cost — this remains an inference from qualitative treatise commentary, not a grounded
  physical model. **No T1 (peer-reviewed) source was found** addressing polearm overhang
  biomechanics specifically; general biomechanics literature (tennis racquet MoI, golf grip
  studies) doesn't transfer.

**Claim B (thrust degrades to shaft-strike at close range) — supported at T2/T3, plausible T0
basis:**
- **T2:** R.G.A. Winn, *Broadsword & Singlestick* (19th c., named-instructor, secondary to
  older material): "points... may also be effected with the butt; and this is the case when
  the combatants have come to rather close quarters" — direct historical statement that
  close-range "thrusts" become butt-strikes.
- **T3 (Wikipedia, citing Silver/Swetnam/Wylde, 16th–18th c.):** the "half staff" grip (hands
  both near one end, e.g. one at bottom one near middle) is explicitly a close-range-only
  posture, "more vulnerable... but more useful very close in," used because standard
  quarterstaff reach can't be brought to bear at grappling distance.
- **T3 (forum consensus, ARMA):** near-unanimous agreement that half-staff trades reach for
  control at close range, consistent with Jordan's mechanism (can't extend the head, so you
  work with what's between your hands).

**Verdict for the engine:** Both claims are directionally grounded in period/secondary staff
literature but **not quantifiable from any source found** — nothing gives a formula or even a
comparative magnitude for overhang handling cost or thrust-to-shaft-strike transition
distance. This is real missing physics (confirmed against code: `at_grip` uses a single pivot
with no overhang/asymmetry term; `recoverability_factor` has no clearance term; spear
`grip_choke_max=1.0` at g=1.0 gives S_g→0, i.e., currently treats a fully choked spear as
costlessly retractable, which is the exact case Jordan disputes) but would require a
**[FIAT]-tier composite proposal** (e.g., an overhang-moment penalty using the already-known
head/butt mass split in `weapons.py`), not a literature-derived constant.

**Files verified this session (read-only, no edits made):**
`designs/scene/combat_engine_v1/weapon_physics.py` (`_gather_len`, `grip_choke_max`,
`grip_travel_max`, `at_grip`, lines 256-289), `designs/scene/combat_engine_v1/systems.py`
(`recoverability_factor` lines 89-119, `lunge_quality` lines 139-149),
`designs/scene/combat_engine_v1/weapons.py` (spear/staff dicts, lines 53-61). Confirmed
numerically: spear `grip_choke_max=1.0`, `travel_max=1.71m`; at g=1.0, spear `I_g=1.062`
(staff `I_g≈0.362` at any g — staff is already near-CoM-balanced by construction) and spear
`S_g→0`.

**Sources:**
- [Paradoxes of Defence, George Silver 1599](http://www.pbm.com/~lindahl/paradoxes.html)
- [Brief Instructions, George Silver 1605](https://www.pbm.com/~lindahl/brief.html)
- [Quarterstaff — Wikipedia](https://en.wikipedia.org/wiki/Quarterstaff)
- [A Brief History of the Quarterstaff, Docherty 2001, EJMAS](https://ejmas.com/jwma/articles/2001/jwmaart_docherty_0501.htm)
- [ARMA forum: why called quarterstaff](https://www.thearma.org/forum/viewtopic.php?t=3421)
- [Proposed Terminology for Gripping the Staff/Spear, Grauenwolf blog](https://grauenwolf.wordpress.com/2015/03/15/proposed-terminology-for-gripping-the-staff-spear-and-similar-weapons/)

---

## 3. Research angle: Chinese/Asian gun (staff) and qiang (spear) close-range doctrine

### Findings (research only, no files edited)

**Bottom line: the specific claim — that choking up on a spear/staff at close range carries a
distinct handling penalty from managing a two-ended, asymmetric-mass object, and that a
middle-grip thrust degrades to a shaft-strike — is NOT explicitly documented in the accessible
Chinese pole-weapon literature.** No passage in Qi Jiguang's *Jixiao Xinshu* (1560) or Wu
Shu's *Shoubi Lu* (手臂錄, c. 1678) content surfaced via search/fetch addresses grip-sliding
costs or close-range thrust degradation directly. This is a gap in *retrievable* secondary
summaries, not proof the primary texts are silent — neither treatise's full technical content
was available through web search; only Wikipedia/Grokipedia-level summaries (formations,
"king of weapons" epithets, general thrust/footwork emphasis) came back. **Grokipedia is an
AI-generated tertiary source and should be weighted near zero for fact claims.**

**What the search base does support, indirectly:**
- Gun-fa (staff) doctrine is generalized as "70% spear technique, 30% staff-specific
  sweeping," implying staff and spear share close-range handling logic — consistent with the
  existing engine axiom that poles are one class, but says nothing about a choke-penalty.
- **Duan gun (短棍, short staff/cudgel)** is treated as a *distinct, shorter weapon* for
  close-quarters work, not "a long staff choked up to short-staff length." This is
  circumstantial support for Jordan's intuition: the tradition's answer to closing distance is
  switching weapon class, not sliding grip on the same shaft — suggesting choke-up-in-place
  may not be presented as a clean substitute in the source tradition (absence of endorsement,
  not evidence of a penalty).
- Western/HEMA-adjacent comparative material (Grauenwolf's WMA terminology page, Sword STEM's
  "Why Do Polearms Hurt?") confirms the **shortened/half-staff grip is a documented real
  technique** (hands at "bottom and upper quarter... allowing greater leverage in the bind")
  but neither source models a trailing-mass handling cost or clearance requirement — Sword
  STEM explicitly computes rotational inertia for full-length staff swings but admits its own
  analysis doesn't address grip-position shifts, calling its treatment "wishy-washy."
- **Best corroboration found** is Japanese sōjutsu/kamayari doctrine (budojapan.com on
  Hozoin-ryu): the core anti-spear doctrine is "enter past the tip" because a long weapon is
  neutralized at close range, and close-range leverage is modeled as rear-hand-drives/
  front-hand-fulcrum with "1cm differences" being tactically decisive — supporting that
  close-range polearm control is a distinct, harder regime, but this is Japanese sōjutsu, not
  Chinese qiang/gun, and is a single enthusiast blog, not a peer-reviewed or primary source.

**Confidence assessment:** Low-to-moderate. The Chinese-tradition source base here is exactly
as thin and marketing-entangled as flagged — mostly Shaolin-tourism/wushu-competition sites
(shaolin-kungfu.com, taichiwuji.com, splinteredstaff.wordpress.com) with no primary-text
quotations, not scholarly translations. Full-text translations of Jixiao Xinshu ch. 10-12
(spear) or Shoubi Lu could not be accessed to verify firsthand. **Recommendation: do not
ground new engine constants in "documented Chinese doctrine" for claim A or B — neither is
sourced strongly enough.** Instead, ground the model in the physics directly (two-body/
dumbbell moment-of-inertia with mass on both sides of a moving pivot, and rear-clearance as a
geometric constraint = wielder's back-space minus rear-overhang length), citing existing
`recoverability_factor`/`at_grip` composite-derivation precedent rather than a martial-arts
citation that can't be adversarially verified.

**Files consulted this session (read-only):**
`C:\Github\ttrpg\designs\scene\combat_engine_v1\systems.py`, `weapon_physics.py`,
`weapons.py` (per session context) — no edits made.

---

## 4. Research angle: biomechanics of two-handed pole/lever grip dynamics

That's a strong direct hit — "it's difficult to turn the butt end of a spear around if you're
surrounded" is exactly the clearance/rotation constraint Jordan describes, sourced
independently.

### Findings (grounded, with citations)

**Question 1 — does scalar MoI (parallel-axis) fully capture handling difficulty, or is there
a real, citable cost from managing an asymmetric two-ended object beyond I_g?**

Yes, there is a real, citable gap, and it is *not* fully captured by I_g alone — but the
sports-science literature isolates it as a **kinematic/temporal cost** (slower average
velocity, altered torso/pelvis rotation, more elbow extension), not as a separate "control
tensor" term. Escamilla & Fleisig (2009, *Journal of Applied Biomechanics* 25(3):203-13,
"Effects of Bat Grip on Baseball Hitting Kinematics," 14 subjects, 120Hz motion capture) found
choke-up grip produced significantly *lower* bat velocity (28±5 m/s vs 31±4 m/s normal grip)
alongside more-closed pelvis, less torso/pelvis ROM, and altered elbow extension velocity —
i.e., choking up forces a compensatory whole-body kinematic adjustment, not merely a free MoI
win. DeRenne et al. (2010, *The Sport Journal* 19, 14 subjects) similarly found faster
swing/stride time with choke-up but did NOT show improved contact accuracy — "bat control"
was subjects' *stated belief*, not a measured accuracy gain. Kagan (2017, Hardball
Times/FanGraphs, "The Physics of Choking Up") shows the mechanism: choking up lowers I about
the new pivot but also lowers *average* bat speed because more of the object's trailing mass
(the knob end, moving backward relative to the new pivot) subtracts from average velocity — a
real physical drag that a naive "lower I ⇒ easier/faster" read misses. Critically, **none of
these bats are asymmetric-in-the-Jordan-sense** (mass concentrated at ONE end, like the
spear's head+counterweight-butt) — standard bats are barrel-heavy but single-ended. This means
the sports literature grounds "choking up costs average velocity/control," but doesn't yet
isolate the specific two-trailing-ends case.

For that specific case (a pivot with mass on BOTH sides), the physics is a real, separate
primitive: the engine already computes `I_cm` correctly via parallel-axis, but I_g is a
**scalar about a single axis** and says nothing about the **product of inertia / off-axis
wobble** or, more importantly, about **swept-volume/clearance** — an engineering/robotics-
standard concept (arxiv 2509.09325 on swept-volume computation notes clearance is required
specifically to prevent "unanticipated contacts of a part in motion with surrounding
objects"). That is exactly Jordan's claim: a choked pole has a butt overhang that needs real
rotational clearance behind the wielder, which a scalar I_g cannot represent — it's a
spatial/environmental constraint, not an inertial one.

**Direct martial-practice confirmation of both claims.** On claim A (overhang/clearance): an
ARMA forum discussion (thearma.org, "How to defeat the spear?") states plainly: *"it's
difficult to turn the butt end of a spear around if you're surrounded"* — independent
confirmation that a trailing butt specifically loses maneuverability in tight space, matching
Jordan's "can't swing/rotate/turn near as smoothly" claim almost verbatim. On claim B (thrust
degrades to shaft-strike at close range): historical quarterstaff manuals (English
Quarterstaff, c.1600, via hroarr.com) document that "half-staff" (center grip) sacrifices
reach specifically — "one who thrusts [holding rear-hand only] gains an extra 2 ft of reach"
versus the center/half-grip — and fighters are taught to switch grips as range closes
precisely because a center-gripped thrust cannot achieve full extension; Fiore dei Liberi's
spear material (fightlikefiore.wordpress.com) explicitly has fighters "turning the head of the
spears behind and striking with the butt" at close range rather than thrusting the point —
literal historical evidence that a "thrust" from a choked grip becomes a shaft/butt strike,
exactly as Jordan describes.

**Verdict: Jordan's claim is a real, citable, currently-unmodeled effect.** The engine's
`I_g`/`S_g` machinery correctly captures the *swing-arrest* and *thrust-retract* cost
reductions from choking toward CoM, but it has **no term for (a) trailing-end
overhang/clearance** (an ARMA-confirmed, physically-real close-quarters penalty scaling with
the length of shaft *behind* the grip, not ahead of it) or **(b) thrust-reach degradation into
a shaft-strike** at high choke + close range (confirmed by period quarterstaff/spear sources).
Both are currently invisible to the model: `at_grip` only returns the CoM-referenced
d_g/I_g/S_g, and nothing in `recoverability_factor` or `lunge_quality` reads rear-overhang
length (`d_g` for the trailing/butt segment) or an available-clearance/range budget. The
spear's own data (mass=2.0, head_len=5.5, butt_kg=0.25 counterweight) makes it the worst-case
exemplar: choked to g=1.0 its I_g (1.06) is ~3x the staff's I_g (0.36) at the same g —
confirming the file's own note that a choked spear is NOT equivalent to a centre-balanced
staff — but the overhang/clearance and thrust-degrades-to-shaft-strike penalties are separate,
currently-zero terms, not something already absorbed into that I_g gap.

**Sources:**
- Escamilla RF, Fleisig GS, et al. (2009). "Effects of Bat Grip on Baseball Hitting
  Kinematics." *Journal of Applied Biomechanics* 25(3):203-213.
  https://journals.humankinetics.com/view/journals/jab/25/3/article-p203.xml
- DeRenne C, et al. (2010). "A Choke-Up Grip Facilitates Faster Swing and Stride Times Without
  Compromising Bat Velocity and Bat Control." *The Sport Journal* 19.
  https://thesportjournal.org/article/a-choke-up-grip-facilitates-faster-swing-and-stride-times-without-compromising-bat-velocity-and-bat-control/
- Kagan D (2017). "The Physics of Choking Up." The Hardball Times / FanGraphs.
  https://tht.fangraphs.com/the-physics-of-choking-up/
- Cross R, Nathan A (2009). "Performance versus moment of inertia of sporting implements."
  *Sports Technology*, Wiley (paper fetched but binary-garbled; cited per prior engine
  grounding, not independently re-verified this session — flag for re-check).
  https://onlinelibrary.wiley.com/doi/abs/10.1002/jst.88
- ARMA Forum (Association for Renaissance Martial Arts), "How to defeat the spear? (and other
  polearms)." https://www.thearma.org/forum/viewtopic.php?t=24634
- English Quarterstaff manual, c.1600 (transcription/commentary).
  https://www.hroarr.com/manuals/01-polearms/Staff/Quarterstaff/Quarterstaff.pdf
- Fight Like Fiore, "Spear" (Fiore dei Liberi spear material commentary).
  https://fightlikefiore.wordpress.com/tag/spear/
- arxiv 2509.09325, "Swept Volume Computation with Enhanced Geometric Detail Preservation"
  (cited for the general engineering concept that clearance is required to prevent contact
  during rotational motion — used here as the formal analogue for the "space behind the
  wielder" constraint, not weapon-specific).

**Code locations verified this session** (read-only, no edits made):
`C:\Github\ttrpg\designs\scene\combat_engine_v1\weapon_physics.py` (`at_grip` lines 274-289,
`grip_choke_max`/`grip_travel_max` lines 256-272, `derive` at line 96),
`C:\Github\ttrpg\designs\scene\combat_engine_v1\systems.py` (`recoverability_factor` lines
89-119, `lunge_quality` lines 139-149, `grip_target`/`can_choke` lines 125-138),
`C:\Github\ttrpg\designs\scene\combat_engine_v1\weapons.py` (spear dict line 53, staff dict
line 58). Confirmed numerically: spear at g=1.0 gives I_g=1.062, S_g=0.0, d_g=0.0; staff at
g=1.0 gives I_g=0.362, S_g=0.0, d_g=0.0 — both S_g/d_g collapse to zero (identical
"recoverability" signal) despite the spear retaining ~3x the staff's I_g and a far more
extreme head/butt mass split, and neither retains any signal for rear-overhang length or
thrust-clearance at that grip.

---

## 5. Research angle: close-range thrust degrading to shaft-strike / half-staffing

### Findings: staff/spear/pollaxe mechanics at close range

**Both claims are documented, with the pollaxe evidence being strongest.**

**Claim B (thrust degrades to shaft-strike) — directly attested.** Le Jeu de la Hache (French
pollaxe treatise, c.1460-85) names the shaft segment between the hands the **"demy-hache"**
("half-axe"), one of three named zones of the weapon (tête/head, demy-hache, queue/butt)
defined *by hand position, not fixed geometry*. The treatise explicitly describes using this
middle segment to "hit and push... held in both hands" when the head can't be brought to bear
— this is not fringe interpretation, it's a named, canonical technique in the source, distinct
from striking with the head or queue.
[Le Jeu de la Hache – Wiktenauer](https://wiktenauer.com/wiki/Le_Jeu_de_la_Hache_(MS_Fran%C3%A7ais_1996));
[ARMA spotlight](https://www.thearma.org/spotlight/lejeudelahache.htm);
[talhoffer.blogspot.com pollaxe primer](http://talhoffer.blogspot.com/2009/05/what-is-pollaxe.html).
Fiore's spear material (Zogho Stretto / "narrow play") independently corroborates the general
pattern: once range closes past the point's effective zone, technique shifts to butt-strikes,
shaft-jams, and grappling — the point stops being the active weapon.
[Chicago Swordplay Guild — Wide and Close Play in Armizare](https://www.chicagoswordplayguild.com/wide-and-close-play-in-armizare-the-martial-tradition-of-fiore-dei-liberi).

**Claim A/analogy ("half-staffing") — attested but weaker and later.** A middle-of-staff +
quarter-point grip ("half-staff") is documented, explicitly described as trading reach for
close-range control: "more vulnerable to a weapon with good reach, but more useful very close
in," with fighters transitioning quarterstaff→half-staff as range closes
([Wikipedia: Quarterstaff](https://en.wikipedia.org/wiki/Quarterstaff)). Caveat found via
adversarial check: this specific two-hands-close-together "half-staff" grip is **not attested
in early-modern sources** (Silver, Swetnam, Wylde all use back-hand-at-butt +
forward-hand-18in-up) — it only appears in **Victorian-era (1880s) sport quarterstaff
manuals** (McCarthy). So "half-staffing" as a named technique is real but is a 19th-century
sportification, not a medieval combat attestation — don't cite it as equivalent-vintage
evidence to the pollaxe material.

**Not found:** no source explicitly frames the mechanism in biomechanical terms (rear-overhang
swing clearance, coordinated dual-mass management, MoI asymmetry cost). The martial sources
describe the *tactical* fact (thrust becomes shaft-strike; grip shifts trade reach for
control) but never the *why* in physics terms — that inference (a choked grip leaves mass
trailing both sides of the hands, costing clearance and control) is physically plausible and
consistent with the named "demy-hache" zone existing at all, but it's this memo's
extrapolation, not a treatise's stated reasoning. Flag it as such if it enters `systems.py`.

No files were edited — this is research only, per instructions and the Jordan-gate on
balance-affecting changes in `designs/scene/combat_engine_v1/`.

---

## 6. Engine-model verification findings (with file:line citations)

This confirms `grip_position` only feeds `wield_heft`, `weapon_tempo`/`close_tempo` (cadence
penalty), and `recoverability_factor` (via `at_grip`). It never touches
`select_mode`/`coupling`/`gap_prec`/`w['gap']` — no thrust-range or shaft-strike degradation
term.

### Findings

**1. No rear/trailing-overhang term, no independent front/rear hand-separation model, no
thrust-range-at-close-range degradation exists anywhere in the engine.**

- `WP.at_grip` (`weapon_physics.py:274-289`) models a **single working-hand pivot** sliding
  forward by distance `u` toward the CoM, returning `I_g` (re-pivoted MoI), `S_g` (static
  moment), `d_g` (CoM-to-hand distance), `u`. There is no second hand position, no
  length/mass remaining *behind* the pivot, no rear-overhang variable at all — the model is a
  scalar-slide re-pivot of the whole-weapon `derive()` output, nothing more
  (`weapon_physics.py:96-141` for `derive`, called by `at_grip` at line 282).
- `recoverability_factor` (`systems.py:89-119`) consumes only `I_g`, `S_g`,
  `point_concentration`, `grip_len` (fixed, not grip-position-dependent — confirmed at line
  113: `w['grip_len']`, not `at_grip`'s `d_g`/`u`), and `lunge_depth`. No term reads rear-hand
  separation or trailing mass/length independently of the single re-pivoted MoI.
- `lunge_quality` (`systems.py:139-149`) uses `point_concentration`, mass-based "lightness,"
  `PoB_frac` hand-balance, and a 1H/2H flag — no overhang/asymmetry term.
- `weapon_tempo`/`close_tempo` (`systems.py:35-60`) apply `CHOKE_TEMPO_PEN * grip_position` (a
  flat linear cadence cost for choking) and `POLE_CLOSE_K * close_unwieldiness *
  (1 - grip_position)` (reach-based close penalty that a chokes-up pole escapes
  proportionally to `grip_position`). Neither reads anything about a trailing butt/queue past
  the hands — the penalty is purely reach/MoI-derived, and it *decreases* monotonically as
  `grip_position→1`, with no compensating handling cost added back in for choking itself.
- `select_mode`/`afforded_heads` (`systems.py:220-275`) and `core.coupling` (`core.py:120-133`)
  determine which head is used and its damage coupling from `w['gap']` (a **static,
  grip-independent** primitive) — `grip_position` never threads into `select_mode`,
  `afforded_heads`, or `coupling`. **Nothing converts a thrust to a shaft-strike at high
  choke/close range**; the weapon always thrusts with its actual head at its actual
  `gap_precision`, regardless of grip position or closed/open state.

**2. Spear at g=1.0 vs staff at its natural grip are NOT treated as equivalent — they differ
sharply in raw magnitude, but not because of any overhang penalty.**

Computed directly: spear `derive()` gives `MoI=2.067, PoB_frac=0.353` (butt-heavy,
forward-balanced far from centre) vs staff `MoI=0.362, PoB_frac=0.0072` (already near its own
centroid by construction). At `g=1.0` (max choke): spear `I_g=1.062`, staff `I_g=0.362` — the
spear remains **~2.9× heavier in swing inertia** than the staff even fully choked, because
`at_grip` only re-pivots the *existing* mass distribution; it never equalizes two structurally
different weapons. So the model does *not* claim a choked spear becomes physically identical
to a staff — but the only thing separating them is raw MoI/static-moment magnitude, never a
handling-cost penalty for the asymmetry itself.

**3. `grip_choke_max`.** Both spear and staff return exactly **1.0**
(`weapon_physics.py:268-272`, confirmed by direct call), since `_gather_len` (line 256-262)
treats the spear's full `head_len` as grippable (`wclass=='hafted_tip'`), giving `Lu` far
above `GRIP_LONG=3.0` for both. This confirms the memory's suspicion precisely: **the model
currently assumes a fully-choked spear has unrestricted regrip freedom** identical to a
staff's, with the only downstream difference being the MoI-magnitude gap above — no separate
penalty for choking *itself* on an asymmetric weapon.

**4. Close-range thrust conversion.** Checked `select_mode` (`systems.py:242-275`),
`afforded_heads` (`systems.py:220-240`), `wrapper.py` (lines 66-124, including
`halfsword_target`), and `core.coupling`/`_transmit` (`core.py:106-133`) — `closed` (bool)
only gates `grip_target`/`halfsword_target`/`select_mode`'s armor-conditional legibility
label, never the thrust's `gap`/`point_concentration`/`coupling` magnitude. **No code path
degrades a thrust to a shaft-strike or reduces effective thrust range as a function of closed
distance or grip_position.**

**Conclusion:** both of Jordan's claims (A: grip-asymmetry/overhang handling cost, B:
thrust→shaft-strike at close range) are entirely unmodeled — confirmed, not just suspected.
`grip_choke_max=1.0` for the spear is the specific numeric root of the "94-96% win" complaint:
the engine grants a choked-up spear free, unlimited regrip with no asymmetry tax and no
thrust-range floor.

---

## 7. Synthesized proposal

### Findings: grip-asymmetry and thrust-degradation costs

**1. Grounding verdict — do not inflate.**
- **Claim A (grip asymmetry/overhang handling cost): partially grounded, form-only.** No
  T0/T1 source gives magnitude or formula. Best evidence is a T2/T3 qualitative consensus
  (ARMA: "difficult to turn the butt end of a spear around if you're surrounded";
  Silver-paraphrase on "tail end causes problems") plus a real biomechanical analogue
  (Escamilla & Fleisig 2009, *J. Appl. Biomech.* 25(3) — choking up measurably *lowers*
  average implement velocity via trailing-mass drag, not a free MoI win) and an engineering
  analogue (swept-volume/clearance is a real, separate primitive from scalar MoI). Enough to
  justify a **form**, not a magnitude.
- **Claim B (thrust degrades to shaft-strike at close range): well-grounded at T2, directly
  named in a primary-adjacent source.** *Le Jeu de la Hache* (c.1460-85) names the mid-shaft
  zone **"demy-hache"** as a distinct, canonical striking zone used precisely when the head
  can't be brought to bear; Fiore's *Zogho Stretto* and Winn's *Broadsword & Singlestick*
  independently corroborate "thrusts effected with the butt" at close quarters. This is
  strong enough to ground a **hard behavioral gate**, not just a magnitude tweak.

**2. Concrete proposal.**

New function `overhang_penalty(c, cfg)` in `systems.py`, alongside `at_grip`/
`recoverability_factor`:
- Reads: `w['head_len']`, `w['grip_len']`, `w['butt_kg']`/mass distribution (already in
  `weapons.py`), and the chosen `grip_position` `g` (via `WP.at_grip`'s `d_g`, extended to
  also return trailing length `L_behind = total_len*g - grip_len_from_butt`, i.e. shaft
  length *behind* the working pivot, not just `d_g` to CoM).
- Formula shape: `overhang_moment = m_trail * L_behind²` (a second, independent moment term
  for the mass trailing behind the hands, on top of `I_g`'s forward-referenced re-pivot) —
  this is the missing "two trailing ends" term the current single-pivot `at_grip` cannot
  express. Penalty enters `recoverability_factor` as a multiplicative `clearance_mult = 1 +
  [FIAT] K_OVERHANG * overhang_moment/I_ref`, gated by `closed` (only matters when there's no
  rear space) — closeness already exists as a bool/continuous signal in the wrapper.
- Thrust-degradation: a **hard cap**, not a continuous penalty —
  `select_mode`/`afforded_heads` should check `available_extension = measure_distance -
  (grip_len_from_grip_to_head_tip * (1-g))`; when `available_extension < [SIM-CALIBRATE]
  MIN_POINT_CLEARANCE`, the point head is simply unavailable and the weapon's only legal head
  at that grip+range is a shaft/butt strike (a new `wclass`-shared "shaft_strike" head,
  reusing `mace`'s blunt coupling as its analogue). This lives in `select_mode`
  (systems.py:242-275), the one place `gap`/`coupling` is chosen — currently `grip_position`
  never threads there; this closes exactly that gap.
- Flag explicitly: the **form** (two-body trailing moment; a hard reach-vs-extension gate) is
  grounded by the sources above; **all coefficients** (`K_OVERHANG`, `MIN_POINT_CLEARANCE`)
  are **[FIAT]** — no source gives a number.

**3. Double-counting check.**
- `ctrl_credit`'s force-couple term uses `w['grip_len']` (the weapon's **fixed, issued** grip
  length) — it never varies with chosen grip position, so it does not already capture a
  moving-pivot overhang cost. No overlap.
- `C_swing`/`C_mode` already penalize high `I_g`, but `I_g` is re-pivoted *forward-only*
  (single working-hand pivot toward CoM) — it has no independent term for mass trailing
  *behind* that pivot. No overlap; this is additive, not duplicative.
- `lunge_quality`'s `handbal` term uses whole-weapon `PoB_frac`, not grip-position-dependent
  trailing mass — also non-overlapping, though note it should also gate on
  `available_extension` if the new thrust-cap is added (a lunge target with no legal
  point-head is otherwise nonsensical) — flag as a required consistency check, not a
  duplicate.

**4. Qualitative effect estimate.**
Both terms hit the **spear specifically and asymmetrically vs. the staff** — exactly the
differentiation currently missing (spear `grip_choke_max=1.0` treats it as freely choke-able
like a staff). The spear's butt-counterweighted, forward-headed mass split (`butt_kg=0.25` vs.
real head mass ~0.40kg over `head_len=5.5`) gives it a large `m_trail * L_behind²` at high
choke that the staff (naturally centre-balanced, `head_len==grip_len`) mostly lacks — so
`overhang_penalty` should raise spear-choked recoverability cost well above staff-choked cost
even at matched `g`. The thrust-cap should specifically strip the spear of its point advantage
at close range/high choke (forcing shaft-strikes, coupling ≈ mace-tier), while the staff loses
little since it never had a point advantage to lose. Net expected direction: **reduces the
spear's close-quarters dominance and increases spear/staff differentiation**, directly
targeting the reported 94-96% win-rate anomaly — but the actual magnitude is untestable
without running the engine, and both new coefficients remain [FIAT] pending Jordan's
calibration pass.

No files were edited (research/proposal only, per instructions). Files re-verified this
session: `C:\Github\ttrpg\designs\scene\combat_engine_v1\systems.py` (lines 89-149),
`C:\Github\ttrpg\designs\scene\combat_engine_v1\weapons.py` (lines 45-63).

---

## 8. Skeptic's refutation attempt

This confirms the proposal's claim that `select_mode` (systems.py:242) never reads
`grip_position` at all — `select_mode`'s signature only takes `closed`, not grip state, and
`afforded_heads`/`select_mode` never reference `w['grip_len']` scaled by `g`. So the "thrust
degrades to shaft-strike" gap is real and correctly located.

### Refutation attempt — verdict: proposal survives

**Sources checked directly.** Escamilla & Fleisig 2009 (*J. Appl. Biomech.*, "Effects of bat
grip on baseball hitting kinematics") is real and does find choke-up grip reduces bat linear
velocity at contact — a genuine trailing-mass/leverage analogue, correctly used only as
qualitative support, not a magnitude source (the proposal doesn't misuse it that way). *Le
Jeu de la Hache*'s "demy hache" is real and is literally defined as "the portion of the shaft
between your hands," used to strike/push at close range when the head can't be brought to
bear — this is a strong, specific, verifiable primary-adjacent grounding for Claim B, stronger
than the proposal even undersells. Both citations check out.

**Formula/engine claims verified against actual code, not the proposal's line numbers.** The
file:line citations were slightly off (`at_grip`/`grip_choke_max`/`_gather_len` live in
`weapon_physics.py`, not `systems.py` — systems.py only calls `WP.at_grip`), but the
substantive claims hold:

- `at_grip(w,g)` (weapon_physics.py:274-289) confirmed: single forward-referenced pivot that
  slides toward CoM and **stops there** ("never past the inertia minimum"). There is
  genuinely no trailing-mass/rear-overhang term — `d_g = PoB - u` only ever shrinks toward 0,
  and `I_g = I_cm + m*d_g²` bottoms out at `I_cm`. No independent "mass behind the pivot"
  moment exists anywhere in this function or in `recoverability_factor`.
- `select_mode` (systems.py:242) confirmed to never read `grip_position` — its signature is
  `(c, defender_armor, closed, cfg)`, and neither it nor `afforded_heads` scales reach/gap by
  `g`. So the thrust-degrades-to-shaft-strike gate is genuinely absent, exactly as claimed.
- Numerically computed `at_grip` for spear vs. staff at g=0/0.5/1.0. At g=1.0: spear
  `I_g=1.062`, staff `I_g=0.362` — nearly 3x, confirming spear and staff are **not**
  dynamically equivalent even fully choked, contra the naive "poles are one class" reading.
  This is real and directionally supports the proposal's differentiation claim.
- `grip_choke_max(spear) = 1.0` confirmed (near-full choke freedom, since `_gather_len`
  includes the whole grippable head_len for `wclass=='hafted_tip'`) — so the model currently
  does treat a choked spear as reachable to any grip position with no penalty beyond MoI,
  exactly as the proposal states.

**Double-counting check.** Independently traced `ctrl_credit`'s `tau` term (line 113): it uses
`w['grip_len']` (the fixed record value), never `g` or `d_g`. `C_swing`/`C_mode` use
`I_g`/`S_g` only in the forward-CoM sense. No existing term reads anything resembling "length
behind the pivot." The proposal's non-overlap claim holds.

**Where the proposal is honest vs. where more pushback is warranted:**
- It correctly labels `K_OVERHANG` and `MIN_POINT_CLEARANCE` as pure [FIAT] with zero sourced
  magnitude — this is accurate; nothing in Escamilla/Fleisig or *Jeu de la Hache* gives a
  coefficient.
- The claimed **direction of effect** (spear penalized more than staff at matched g) is
  consistent with the formula shape as specified (`m_trail * L_behind²`, driven by the
  spear's counterweighted mass split vs. the staff's even distribution) — plausible and not
  contradicted by the engine's data (butt_kg=0.25 vs. staff's even head_len==grip_len), but
  this is still an assertion about a function that doesn't exist yet, not something
  verifiable by running code. It is a reasonable extrapolation, not a demonstrated result.
- One gap the proposal itself flags but underweights: `lunge_quality` would need a
  consistency gate too if the thrust-cap lands — it doesn't currently read `grip_position` at
  all, so a fully-choked spear lunging with an already-degraded point is a second latent
  inconsistency, not just the one flagged.

**Verdict:** The proposal survives. Both externally-checkable citations are real and say what's
claimed. The engine-code claims check out against the actual files (modulo a minor
line-citation error, not a substantive one). No double-counting was found. The magnitude
coefficients are honestly flagged as unsourced FIAT, not disguised as grounded. The
direction-of-effect claim is a reasonable, code-consistent extrapolation but remains untested
since no function was implemented or run.

---

## 9. Final reconciled recommendation

Confirmed: file locations, `SPEAR-BALANCE [Jordan A, 2026-06-30]` provenance note,
`grip_choke_max`/`at_grip` mechanics, and `select_mode`'s lack of grip-position
parameterization all match the skeptic's corrections.

### Final finding: grip-asymmetry and thrust-degradation costs

**1. Grounding verdict (unchanged, both claims survive skeptic scrutiny).**
- **Claim A (overhang/asymmetry handling cost) — form-only, not magnitude.** No T0/T1 source.
  T2/T3 consensus (ARMA on turning a spear's butt when surrounded; Silver-paraphrase on
  tail-end interference) plus a verified biomechanical analogue — Escamilla & Fleisig 2009
  (*J. Appl. Biomech.* 25(3)) confirmed to actually show choke-up grip lowers implement
  velocity via trailing-mass drag, not a free win — plus the generic engineering point that
  swept-volume/clearance is independent of scalar MoI. Sufficient to justify adding a **form**
  (a new penalty term), insufficient to justify any specific **coefficient**.
- **Claim B (thrust degrades to shaft-strike at close range) — well-grounded, verified
  directly.** *Le Jeu de la Hache*'s **"demy-hache"** is confirmed real and is literally
  defined as the shaft zone between the hands used to strike/push when the head can't be
  brought to bear — a primary-adjacent, directly on-point source. Fiore's *Zogho Stretto* and
  Winn's *Broadsword & Singlestick* corroborate independently. Strong enough for a **hard
  behavioral gate**.

**2. Engine-fact corrections accepted from the skeptic (verified independently this pass).**
`at_grip`, `grip_choke_max`, and `_gather_len` live in `weapon_physics.py` (lines 256, 268,
274), not `systems.py` — `systems.py` only calls `WP.at_grip`. `select_mode` is at
`systems.py:242`, signature `(c, defender_armor, closed, cfg)`, confirmed to never take or
reference `grip_position`. These are citation corrections only; every substantive claim they
attach to is unchanged. Re-verified independently: `at_grip`'s pivot slides only toward CoM
and stops there (no trailing-mass term exists anywhere in `recoverability_factor`), and
`weapons.py:55` confirms the spear's `butt_kg=0.25` is itself a prior Jordan-ratified design
decision (`SPEAR-BALANCE [Jordan A, 2026-06-30]`) establishing the forward-headed/
counterweighted mass split this proposal builds on.

**3. Double-counting — no overlap found, confirmed independently.** `ctrl_credit` uses the
weapon's fixed `grip_len`, never `g`/`d_g`. `C_swing`/`C_mode` use only forward-referenced
`I_g`/`S_g`. `lunge_quality`'s `handbal` uses whole-weapon `PoB_frac`, not grip-position
trailing mass. A new `overhang_penalty` term and a `select_mode` extension/reach gate are
additive, not duplicative, of anything existing.

**4. Skeptic's one addition — folded in.** The lunge-consistency gap (a fully choked spear
lunging with an already-degraded point head is a second latent inconsistency) is real and is
now part of the proposal: `lunge_quality` must also read `available_extension` if the
thrust-cap lands, or it will recommend lunges the new gate has made illegal.

**5. Direction-of-effect claim — status unchanged.** Spear penalized more than staff at
matched grip position is a reasonable, code-consistent extrapolation (numerically confirmed
spear `I_g=1.062` vs staff `I_g=0.362` at g=1.0 — nearly 3x, so they are not dynamically
equivalent even fully choked). This remains an untested prediction, not a demonstrated result,
since no function has been implemented or run.

### Recommendation — what's greenlight-ready vs. Jordan's call

Ready to greenlight as a concrete build task: implement `overhang_penalty(c, cfg)` in
`systems.py` (trailing-mass moment `m_trail * L_behind²`, feeding a `clearance_mult` into
`recoverability_factor`) and extend `select_mode`/`afforded_heads` with an
`available_extension` hard gate that strips the point head and substitutes a shaft-strike
coupling at high choke/close range, plus the matching `lunge_quality` consistency check. The
**form** of both is grounded to T2/T3-plus-analogue standard.

Remains genuinely Jordan's design call: the numeric values of `K_OVERHANG` and
`MIN_POINT_CLEARANCE` — no source of any tier supplies a magnitude, and both must be
[FIAT]/[SIM-CALIBRATE], set by playtesting against the 94-96% spear win-rate anomaly this
proposal targets, not derived further from literature.
