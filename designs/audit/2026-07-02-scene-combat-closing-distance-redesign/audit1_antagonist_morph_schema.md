# Antagonist audit — MORPHOLOGY + SCHEMA lens — plan_corrected_r1.md

Ground truth: C:/Github/ttrpg-morph-rearch/designs/scene/combat_engine_v1/*.py
Phase0 source: designs/audit/2026-07-02-morphology-rearch-phase0/phase0_morphology_combined.json

## What the plan gets RIGHT (verified, do not attack)
- orient_deg/material/guard-type/element_ref ALL absent from weapons.py (grep=0). D0 correctly restores.
- Pull-vs-bind RETRACTION (repair 2 / D9 / JD-7) is CORRECT: phase0 orient bands interleave —
  pulls {guisarme 60, ji 90, guandao 100, poleaxe 180, bec -90, fauchard 90};
  binds {ranseur 45, spetum 55, partisan 50, dangpa 25, bear_spear 90, kama_yari 60}.
  |60| and |90| each appear in BOTH; type='lug' on guandao(pull)+dangpa/bear_spear(bind). No primitive separates.
- 53-weapon count exact. 7 silent-zip set {dangpa,spetum,partisan,guandao,fauchard,flamberge,hook_sword} EXACT+complete.
- Voulge count-mismatch real: 3 elements [1.1,1.55,0.65], 2 mode_elements; positional zip drops elements[2] (rear_fluke, mid-list). element_ref fix sound.
- reach underflow M-04 reproduces EXACTLY: nofloor poleaxe 3.44/staff 3.57/guisarme 3.28 (<L0=4.0); floored 5.35/5.35/5.54/spear 4.94 (>L0). Confirmed.
- Staff S_g(0)=0.00000 -> NaN hazard real; guard correct.
- S_g-collapse diagnosis correct: at_grip S_g=m|d_g|, d_g=PoB-u, u->PoB, so S_g->0 gathered. yes.
- sel_gap/sel_head object-confusion real: core.strike:171 passes w['gap']; adef_cap:219-220 w['gap']; approach_displace:448 w['head']; reach_threat:357 native head vs armor_defeat_sigma:345 sel_head. ji point 0.68 vs w 0.56 divergence confirmed.
- core.damage:153 blunt-ignores-heft_units confirmed; D2/D2b disjoint-channel claim accurate.
- select_mode ignores closed (systems.py:302) confirmed; reach_base ignores grip_position (systems.py:19) confirmed.
- state_graph descriptive; no Contact node; no 'contact' TRACE_KIND; contact.axis is '(WS-5, unbuilt)' metadata. All confirmed.
- name-literal test scans ONLY core/systems/wrapper for weapon-NAME string literals; a pull_capable data boolean in weapons.py is invisible. Plan's guard-hollowness argument CORRECT.
- halfsword forms in phase0; at_grip(w,0)['I_g']==derive['MoI'] EXACT for both -> I1 identity holds (plan over-cautious but not wrong).
- capabilities.py has halfsword/gap_thrust/percussive_blow gates w/ self-test; extensible pattern confirmed.

## DEFENSIBLE FINDINGS AGAINST THE PLAN

### F1 (SERIOUS) — "orient_deg cleanly gates arc-vs-thrust" is FALSE against phase0 data
Plan asserts (D0 L105-107; D5 L350-353; Appendix L793-794, all "verified"):
  "thrust modes all sit at orient≈0; swing/hook modes at ±60…180 — a CLEAN GATE for D5/D6."
Actual phase0: THRUST(point) orient ∈ {0,90,180}; SWING/CUT orient ∈ {0,15,25,30,...}.
~27 swords' cutting blades sit at orient_deg=0 (arming/longsword/greatsword/sabre/katana/glaive/scimitar/…),
PLUS staff blunt tip=0 and goedendag blunt club=0. The bands OVERLAP at 0 AND 90.
- goedendag: BOTH mode_elements at orient=0 (blunt club-swing AND spike-thrust) -> orient cannot separate.
- voulge cleaver (swing) orient=30, heel-spike (thrust) orient=5 — 25 deg apart, both low; not in ±60…180.
- fauchard blade (cut) orient=20; podao 15; bardiche 25; sparr_axe 30 — all cutters in the sub-60 "dead/thrust" zone.
Consequence: D5's close-efficacy cannot rely on |orient_deg| as the arc-vs-thrust discriminator as claimed;
it must fall back on pc (point_concentration), which ALREADY EXISTS and did not need the D0 re-ingestion.
The plan's stated justification that D0 makes D5/D6 "buildable" via a clean orient_deg gate is undercut.
Not BLOCKER: D5's formula is a conjunction incl. `low pc`, and pc DOES separate the contaminated cases
(goedendag club pc=0.3, voulge cleaver pc=0.42 << thrust pc), so the mechanism can still function via pc.
But the plan certifies a false premise about its own data as "verified."

### F2 (MINOR) — plan's cited spear ideal-reach (5.98) is wrong
D1 L151 lists "spear 5.98→4.94". Actual ideal reach (grip=0, current formula) = 7.80, not 5.98.
Floored value 4.94 is correct and reproduces; only the cited baseline is wrong. I3 L572 uses the correct 4.94.
Non-load-bearing factual slip in the plan's own numbers.

### F3 (MINOR) — bec_de_corbin gap anchor mis-framed
Plan (D5 L342, I4 L590) cites "bec_de_corbin (point 0.57 vs whole 0.82)" as an I4 regression anchor.
bec has TWO point-tokened mode_elements: curved beak geo[gap]=0.57 AND top spike geo[gap]=0.80.
afforded_heads takes max per token (systems.py:295) -> the SELECTED 'point' = 0.80, not 0.57.
So the real divergence for bec's selected point is 0.80 vs 0.82 (tiny), not 0.57 vs 0.82.
The ji anchor (0.68 vs 0.56) is a genuine clear divergence and survives; bec is a weak/mis-stated anchor.
Does not break the M-02 fix, but the plan should anchor on ji + a true single-point composite, not bec's beak.
