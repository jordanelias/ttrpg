export const meta = {
  name: 'combat-system-critique',
  description: 'Intensive NERS + resolution + contract audit of personal-combat engine, corpus reconciliation, adversarial verify, distillation',
  phases: [
    { title: 'Module-NERS', detail: 'one agent per state-graph module cluster — NERS + IN/resolver/OUT contract + dead-data + churn' },
    { title: 'Resolution', detail: 'Instance-A rolling-engine property test (P-i..P-v) on core resolver + sub-resolvers' },
    { title: 'Reconcile', detail: 'one agent per uploaded corpus — curious extension + adversarial review of what improves the engine' },
    { title: 'Adversarial', detail: 'skeptics try to refute the top findings and NERS-vet every proposed addition' },
    { title: 'Distill', detail: 'synthesize the distillation proposal: cut / consolidate / minimal NERS-clean core' },
  ],
}

const ENG = 'C:/Github/ttrpg/designs/scene/combat_engine_v1'
const SUBSTRATE = 'C:/Github/ttrpg/tests/sim/v32-combat-balance'
const DL = 'C:/Users/Jordan/Downloads'

const SHARED = `
You are auditing the Valoria PERSONAL-COMBAT engine. The WORKING TREE is the source of truth — read the actual files; do not trust any summary, doc, or memory over the code. Static analysis only; DO NOT run the engine (it imports /home/claude/* sandbox paths that do not exist on this checkout — that is itself a finding).

ENGINE DIR: ${ENG}/  (core.py, wrapper.py, systems.py, combatant.py, config.py, tradition.py, geometry.py, ability_armature.md, README.md)
RESOLVER SUBSTRATE (imported by core.py via dead /home/claude paths, but the files physically live here): ${SUBSTRATE}/ (m1_dice_sigma_core.py = soft_cap/sigma_n/the net engine; r1_sigma_resolution.py = effective_ob/degree/resolution_pool; r8_parity_harness.py = roll wrappers/WoundTracker/stamina_max; damage_model.py).
CANON STATE MAP (audit companion, MAY BE STALE vs HEAD): C:/Github/ttrpg/designs/audit/2026-06-09-personal-combat-comprehensive/combat_engine_flow_and_state_map.md

NERS: N — Necessary (no roll/lever/edge redundant; an ADDED mechanic must itself be necessary; lever-pile is the canonical defect). R — Robust (holds at extremes: leverage in-band, no cliffs, floors/caps respected, loops bounded = damper<1 AND cap, graded recoverable output, ER-2 continuity sub-5D). S — Smooth (transitions clean across scales/phases; consistent with sibling engines; no role-conflation at seams). E — Elegant (player intuits outcomes from legible odds; one number doing more work beats a new subsystem).
Personal combat is INSTANCE A (sigma-leverage continuous engine). Five properties: P-i legible odds; P-ii uniform/in-band leverage (σ_N-scaled, NOT flat +X); P-iii bounded+monotonic, no cliffs, Ob>=1 floor, ER-2 continuity; P-iv graded recoverable (not fragile binary, underdog floor); P-v right engine for the pool regime.
MODULE CONTRACT lens: every mechanic = IN(consumed) -> resolver -> OUT(emitted) + owned state. Flag dead-data (computed/stored, never consumed), orphan emissions, role-conflation (one variable, >1 job), undamped+unbounded loops.
CHURN PRINCIPLE: every mechanic must generate churn that seeds emergent narrative & meaningful choice. Suspect any inert/unreachable mechanic, any lever that only tunes but never branches the path, any choice with a dominant answer.

ALREADY-VERIFIED FACTS (confirm against code; extend; find MORE):
- core.resolve does a μ-SHIFT not Ob-shift: net = roll_net(pool) + m1.soft_cap(net_sigma)*m1.sigma_n(pool); boost IS σ_N-scaled (sigma_n=0.8*sqrt(pool)) so leverage is pool-uniform by construction; r1.effective_ob is display-only. soft_cap = 1.5*tanh(x/1.5) (M_MAX=1.5).
- ER-2 continuity correction is INLINE in core.degree() (thresholds read at k-0.5).
- mass/pob_frac NOW consumed by core.p_auth (blunt heft) — state map "F5 dead" is STALE. BUT armor_defeat_sigma still reads HAND-SET w['percussion'] for blunt armour-defeat → TWO competing percussion sources for one physical quantity.
- geometry.bake produces {gap,thrust,cut,perc_conc,halfsword}; only gap consumed; WEAPONS[w]['geo'] stored but never read → thrust/cut/perc_conc/halfsword are DEAD baked data.
- eff_cw IS wired at many sites now — state map "channels inert/pending" is STALE. precommit IS consumed (feint_eval def_read) — but only that one defender feint-resist site.
- 'seize' lever has NO consumer in wrapper.py/systems.py (pre-contact seizure CUT 2026-06-05) → abilities 'vorschlag' AND 'sen_no_sen' (JAPANESE flagship) are DEAD; ability_armature.md still claims 'seize' is "live" → doc drift.
- 'clinch' weapon field — never consumed.
- Substrate m1/r1/r8 not in engine dir; imported via /home/claude & /home/claude/v32 (nonexistent here) → engine non-runnable on this checkout / CI / Godot.

STYLE: curious in extension, adversarial in review (assume it's broken), judicious in reconciliation (credit what works; don't manufacture fault). Cite file:line for every claim. Severity P1 (breaks play/correctness), P2 (ambiguity/inert/drift), P3 (polish). Your output IS structured data.
`

const FINDING = {
  type: 'object', additionalProperties: false,
  required: ['id', 'severity', 'claim', 'evidence', 'kind'],
  properties: {
    id: { type: 'string' },
    severity: { type: 'string', enum: ['P1', 'P2', 'P3'] },
    kind: { type: 'string', enum: ['dead-data', 'orphan-emit', 'role-conflation', 'loop', 'cliff', 'leverage', 'redundancy', 'gap', 'doc-drift', 'churn-inert', 'correctness', 'portability', 'balance', 'other'] },
    claim: { type: 'string' },
    evidence: { type: 'string', description: 'file:line citations' },
  },
}
const CRIT = { type: 'object', additionalProperties: false, required: ['verdict', 'reason'], properties: { verdict: { type: 'string', enum: ['pass', 'fail', 'partial'] }, reason: { type: 'string' } } }
const NERS_BLOCK = { type: 'object', additionalProperties: false, required: ['N', 'R', 'S', 'E'], properties: { N: CRIT, R: CRIT, S: CRIT, E: CRIT } }
const MODULE_SCHEMA = {
  type: 'object', additionalProperties: false,
  required: ['module', 'contract', 'ners', 'churn', 'findings', 'recommendations'],
  properties: {
    module: { type: 'string' },
    contract: { type: 'object', additionalProperties: false, required: ['consumes', 'emits', 'dead_data', 'orphans'], properties: { consumes: { type: 'array', items: { type: 'string' } }, emits: { type: 'array', items: { type: 'string' } }, dead_data: { type: 'array', items: { type: 'string' } }, orphans: { type: 'array', items: { type: 'string' } } } },
    ners: NERS_BLOCK,
    churn: { type: 'string' },
    findings: { type: 'array', items: FINDING },
    recommendations: { type: 'array', items: { type: 'string' } },
  },
}
const RESOLUTION_SCHEMA = {
  type: 'object', additionalProperties: false,
  required: ['properties', 'ners', 'loops', 'findings', 'verdict'],
  properties: {
    properties: { type: 'object', additionalProperties: false, required: ['P_i', 'P_ii', 'P_iii', 'P_iv', 'P_v'], properties: { P_i: CRIT, P_ii: CRIT, P_iii: CRIT, P_iv: CRIT, P_v: CRIT } },
    ners: NERS_BLOCK,
    loops: { type: 'array', items: { type: 'object', additionalProperties: false, required: ['name', 'damper', 'cap', 'verdict'], properties: { name: { type: 'string' }, damper: { type: 'string' }, cap: { type: 'string' }, verdict: { type: 'string' } } } },
    findings: { type: 'array', items: FINDING },
    verdict: { type: 'string' },
  },
}
const RECONCILE_SCHEMA = {
  type: 'object', additionalProperties: false,
  required: ['corpus', 'already_in_engine', 'improvements', 'reject', 'creative_layer', 'verdict'],
  properties: {
    corpus: { type: 'string' },
    already_in_engine: { type: 'array', items: { type: 'string' } },
    improvements: { type: 'array', items: { type: 'object', additionalProperties: false, required: ['id', 'what', 'mechanism', 'ners_impact', 'severity', 'adversarial_note'], properties: { id: { type: 'string' }, what: { type: 'string' }, mechanism: { type: 'string' }, ners_impact: { type: 'string' }, severity: { type: 'string', enum: ['high', 'medium', 'low'] }, adversarial_note: { type: 'string' } } } },
    reject: { type: 'array', items: { type: 'string' } },
    creative_layer: { type: 'array', items: { type: 'string' } },
    verdict: { type: 'string' },
  },
}
const VERIFY_SCHEMA = {
  type: 'object', additionalProperties: false,
  required: ['target_id', 'real', 'ners_compliant', 'severity_adjust', 'reasoning', 'revised'],
  properties: {
    target_id: { type: 'string' },
    real: { type: 'boolean' },
    ners_compliant: { type: 'boolean' },
    severity_adjust: { type: 'string' },
    reasoning: { type: 'string' },
    revised: { type: 'string' },
  },
}
const DISTILL_SCHEMA = {
  type: 'object', additionalProperties: false,
  required: ['cut', 'consolidate', 'keep_core', 'add_only_if', 'sequencing', 'headline'],
  properties: {
    cut: { type: 'array', items: { type: 'string' } },
    consolidate: { type: 'array', items: { type: 'string' } },
    keep_core: { type: 'array', items: { type: 'string' } },
    add_only_if: { type: 'array', items: { type: 'string' } },
    sequencing: { type: 'array', items: { type: 'string' } },
    headline: { type: 'string' },
  },
}

const CLUSTERS = [
  { key: 'measure_reach', title: 'Measure & reach', focus: `reach_base & reach_sigma (systems.py:11,167), HEAD_REACH/LONG/HANDS2/reach_adj, REACH_W armour-rotation, the standing reach-disadvantage term in net_sigma. Reach is the dominant weapon driver (r=+0.83). Check: reach over-weighted vs delivery? point +1.0 reach makes thrusting rapier out-reach a greatsword? paired_short +1.4 reach_adj defensible? FOOT_MEASURE_K double-counting balance?` },
  { key: 'tempo_approach', title: 'Tempo, approach & stop-hit', focus: `weapon_tempo/close_tempo (systems.py:17,32), approach_displace (209), close_rate & stop-hit (wrapper.py:66-85), ACT_THRESHOLD/BURST_MAX, CLOSE_TEMPO_COMPRESS. Check: is tempo a real second axis or compressed away? stop-hit pool=resolution_pool(history) only — fair sub-resolver? burst ceiling churn-positive?` },
  { key: 'reopen_recovery', title: 'Reopen / measure-recovery', focus: `reopen_moment creation a/b/c (wrapper.py:217-225), reopen_prob (systems.py:217), push_avail. Check: are all three creation paths reachable & churn-positive? is longer-weapon reopen dominant or dead? does a spear actually re-make distance, or is it inert?` },
  { key: 'commit_disposition', title: 'Commit-depth & disposition', focus: `commit draw + disposition skew (wrapper.py:98-106), disp_lean (systems.py:62), act_cost (47), OOB, three DISP hooks (config). Check: act_cost diverges from derived_stats §4.2 (state map F3)? disposition truly ~neutral (both poles cost)? is commit-depth a meaningful choice or RNG?` },
  { key: 'read_feint', title: 'Read, legibility & feint', focus: `reading (systems.py:53), legibility (177), feint_eval (194), familiarity (tradition.py:62), mental_fat, read_win logistic (wrapper.py:133). Check: reading DOUBLE-weighted (Cog AND Att)? feint loop NERS-necessary or bolt-on? is precommit's ONLY consumption (def feint-resist) enough to justify the channel? legibility mode-shift correctness.` },
  { key: 'defence_modes', title: 'Defence modes (parry/dodge/wind)', focus: `mode_sigma (systems.py:88), GATE table (74), guards, NEUTRALIZE_* fixed shapes, mode pick (wrapper.py:135-137). Check: is mode selection churn-positive or argmax-deterministic? GATE caps justified per weapon? does neutralize double-count defender skill (C-2 claims not — verify)?` },
  { key: 'initiative_vor', title: 'Initiative / Vor + Indes steal + counter', focus: `initiative_sigma/clamp/decay/hold (systems.py:248-279), Vor loop (wrapper.py:41-46,148-154,229-230), Indes steal + INDES_SCALE, single-time counter (158,186-198), init_steal_factor/init_overcommit_loss. Check: Vor loop bounded (DECAY damper + CAP)? steal+counter a lever-pile or churn-rich? counter SUCCESS clamp [.05,.92]. ATTACKER_BIAS=0.12 vs mirror-fairness sound?` },
  { key: 'poststrike', title: 'Outcome map, overcommit, bind/kuzushi, riposte, displace', focus: `outcome mapping (wrapper.py:168-198), overcommit_exposure (163), bind loop + bind_sigma + KUZUSHI (systems.py:228; wrapper.py:233-252), poise_factor (systems.py:282), displace-and-step-inside (204-213), riposte/role-flip (253-261). Check: bind bounded (<=3 iters)? is poise churn-positive or a thin multiplier? is displace-inside reachable? overcommit→riposte loop check.` },
  { key: 'damage_armour', title: 'Damage chain & armour-defeat', focus: `core.py damage/coupling/p_auth/strike (34-99), RESIST/DELIVERY/QUAL/overwhelming tail, armor_defeat_sigma (systems.py:110). Check: TWO percussion sources (p_auth vs hand-set w['percussion']) — drift? dead geo coefficients. linear (no-tanh) damage robust at extremes (no one-shot)? HEFT categorical {light:0,heavy:3} vs continuous MoI. ADEF_CUT=-0.9 a cliff?` },
  { key: 'tradition_layer', title: 'Tradition channel-weights & abilities', focus: `tradition.py whole file: TRADITIONS vectors, eff_cw wiring, ABILITIES (dead 'seize' → vorschlag/sen_no_sen inert; Japanese flagship can't fire), familiarity/ADJACENT, ability_armature.md drift. Check: do channel weights ROUTE the path or only tune σ? which traditions have ZERO live abilities (chinese/filipino)? is a native-tradition layer present at all? is 0.85/0.93/1.0 familiarity churn-positive?` },
  { key: 'wrapper_structure', title: 'Wrapper / loop / harness / portability', focus: `wrapper.py engagement() loop & terminals, fight() harness (275), role-object A/B architecture, mirror-fairness (tie coin-flip, alternating aggressor, ATTACKER_BIAS), beats<24, UPSET_FLOOR. Check: /home/claude & /home/claude/v32 imports (core.py:3, wrapper.py:4, systems.py:5, combatant.py:4) — engine NON-RUNNABLE on this checkout/CI/Godot (substrate in tests/sim/v32-combat-balance). fight()(sim) vs single-engagement(game) boundary clean? unreachable code (stamina<=-4 aborts)?` },
]

const CORPORA = [
  { key: 'weapon_physics', title: 'Weapon physics & balance', files: [`${DL}/weapon_physics_calibration_and_wiring_2026-06-22.md`, `${DL}/weapon_physics_preliminary_pob_2026-06-22.md`, `${DL}/weapon_tradition_state_analytical_ledger_2026-06-22.md`, `${DL}/weapon_physics.py`, `${DL}/combat_analysis_rev2.md`], lens: `These derive reach/heft/tempo/str-demand/damage from physical primitives (mass, pob_frac, pommel_kg, MoI) and RETIRE categorical reach/wt. Some is ALREADY partly wired (p_auth). Claims: continuous MoI/heft replaces categorical {light,heavy}; new pommel_kg primitive; K_* gains UNCALIBRATED (need sim gate: mirror=50, attribute-tier spread, no-one-shot). Adversarial: is continuous heft NERS-Necessary or does categorical already deliver churn? Does wiring fix the two-percussion-source drift? Are the dead geo coefficients (thrust/cut/perc_conc) the natural consumers to wire? Is the analytical ledger's gap register (short-blunt class, dead levers, "traditions tune but never route") accurate vs HEAD or stale?` },
  { key: 'martial_morphology', title: 'Martial morphology (4 vols)', files: [`${DL}/martial_morphology_distilled.md`, `${DL}/martial_morphology_vol3_efficacy.md`, `${DL}/martial_morphology_vol2.md`, `${DL}/martial_morphology.md`], lens: `A morphology of martial traditions: 14 dimensions in 3 classes (efficacy-bearing / culture-framing / decisive variable = aliveness), the governing-analogue thesis, and a FOUR-AXIS evaluation standard (coherence / epistemic status / analogue-coherence / efficacy). tradition.py models traditions as cognitive-mode channel-vectors. Candidates: (a) four-axis standard as design discipline for the native-tradition layer; (b) skeleton-before-culture / efficacy-first order; (c) governing-analogue as the FLAVOUR layer — map to channel vectors? Be HARD-adversarial & judicious: vol3 says most of this is efficacy-NEUTRAL meaning, not mechanics. What is actually MECHANICALLY load-bearing for the resolver vs pure creative-layer? Does the aliveness axis even apply where every fighter is "alive"? Resist importing a 14-dim scheme the morphology's own distillation says should be cut to a few variables.` },
  { key: 'engagement_psych', title: 'Engagement psychology', files: [`${DL}/combat_engagement_engine_proposal_refined.md`, `${DL}/combat_engagement_engine_proposal_unified.md`, `${DL}/combat_engagement_psychology_findings.md`], lens: `These self-audited down to ONE proposed mechanic: 'wariness' (commit-depth only, scaled by 1-familiarity), plus a regime-contest lens and a clinch/disengage-on-overcommit hook. They claim the engine ALREADY encodes disguise(legibility)/deception(feint)/overcommit-exploit faithfully — verify vs HEAD. Adversarial on the ONE addition: is 'wariness' NERS-Necessary or does disposition+familiarity already cover it? Is the regime-contest a real engine gap (no clinch/disengage contact axis — confirm) or out of scope? Is the §2 "convergence" circular (shared Silver + shared synthesizer)? Judge whether even the one mechanic earns its place.` },
  { key: 'deliberation', title: 'Deliberation-as-game', files: [`${DL}/deliberation-as-game-synthesis.md`], lens: `About DEBATE/TRIAL/NEGOTIATION as rule-governed games — NOT personal combat directly. Direct relevance likely to a parallel SOCIAL-contest engine (repo has one, git J-31). Be judicious: extract only what transfers. Candidates: (a) COMMITMENT STORE / game-state ledger (Hamblin) ↔ the engine's initiative/Vor ledger as a commitment record; (b) information-contest frame (sense more, reveal less) ↔ read/feint/legibility; (c) constitutive vs regulative rules, magic-circle/bounded-arena, adjudicator-as-resolver; (d) mixed-motive vs zero-sum (combat is zero-sum; deliberation often not) — implication for whether the SAME resolver serves both. Strongest honest output: does this argue for a SHARED resolver architecture across personal-combat + social-contest, and what would that share? Do NOT force combat-specific mechanics out of it.` },
]

// resume hardening: opus-tier stages (resolution/reconcile/adversarial/distill) errored on an opus
// availability blip in run 1. A() retries on null; RESUME_SALT changes their cache key so they re-run
// live on resume (the Sonnet module agents keep raw agent() → identical key → cache-hit, instant).
const RESUME_SALT = '\n\n[resume-pass:2 — re-run opus stage]'
async function A(p, o) {
  for (let i = 0; i < 3; i++) {
    const r = await agent(p + RESUME_SALT, o)
    if (r) return r
    log(`retry ${(o && o.label) || 'agent'} (attempt ${i + 1} returned null)`)
  }
  return await agent(p + RESUME_SALT, o)
}

phase('Module-NERS')
const round1 = await parallel([
  ...CLUSTERS.map(c => () => agent(
    `${SHARED}\n\n=== YOUR MODULE: ${c.title} (${c.key}) ===\nAudit ONLY this cluster. Read the cited files/functions in full first.\nFOCUS: ${c.focus}\n\nProduce: the IN->resolver->OUT contract (consumes, emits, dead-data, orphans); a per-criterion NERS verdict (N/R/S/E each pass/fail/partial with a one-line reason grounded in code); a churn assessment (does it branch the path / create meaningful choice, or only tune a number / sit inert?); a findings list (severity, kind, claim, file:line) — hunt for MORE than the verified facts; and concrete recommendations. Be adversarial: assume the module is broken and prove it or clear it.`,
    { schema: MODULE_SCHEMA, label: `module:${c.key}`, phase: 'Module-NERS', model: 'sonnet' }
  )),
  (() => A(
    `${SHARED}\n\n=== RESOLUTION DIAGNOSTIC (Instance A property test) ===\nRun valoria-resolution-diagnostic on the CORE RESOLVER and every embedded sub-resolver. READ FIRST: core.py (resolve/degree/roll_net/damage), and the substrate at ${SUBSTRATE}/ (m1_dice_sigma_core.py for soft_cap & sigma_n & the net distribution; r1_sigma_resolution.py for effective_ob & degree & resolution_pool; r8_parity_harness.py for WoundTracker). Then sub-resolvers in wrapper.py: read_win logistic (133), stop-hit roll (75-82), bind logistic loop (243-252), counter-success clamp (188-192), mode fallback (137), net_sigma assembly (140-144).\n\nTest P-i..P-v. Verify: (1) leverage σ_N-scaled uniform (soft_cap*sigma_n) — confirm by reading m1; (2) ER-2 continuity present in degree() and CORRECT; (3) wound-reduced pool regime — pool=max(1, resolution_pool(history)-wounds) can fall to ~1-2D (sub-5D) → does continuity cover it, or does a low-history wounded fighter hit a fidelity/cliff zone?; (4) μ-shift vs Ob-shift consequences for the degree ladder (overwhelming/failure rates); (5) Ob>=1 floor; (6) the embedded LOGISTIC sub-resolvers (read_win, bind, counter) — legible (P-i) or opaque secondary draws stacked on the main roll?; (7) loops: Vor (damper INIT_DECAY=.75, cap INIT_CAP=1.5), poise (recover+floor), burst (BURST_MAX) — each damped AND bounded?; (8) right engine for the pool regime (P-v)? Give a NERS verdict + loops table.`,
    { schema: RESOLUTION_SCHEMA, label: 'resolution-diagnostic', phase: 'Resolution', effort: 'high' }
  )),
  ...CORPORA.map(c => () => A(
    `${SHARED}\n\n=== CORPUS RECONCILIATION: ${c.title} ===\nRead these uploaded docs IN FULL:\n${c.files.map(f => '  - ' + f).join('\n')}\nThen read the relevant engine files to check what's ALREADY done vs proposed.\nLENS: ${c.lens}\n\nProduce: (a) already_in_engine — what the corpus proposes that HEAD already does (credit; flag where the corpus is STALE vs HEAD); (b) improvements — concrete NERS-assessed engine changes (what; mechanism as file/function/lever IN->OUT; ners_impact; severity; strongest case AGAINST); (c) reject — ideas NOT worth adopting + reason; (d) creative_layer — Jordan-only flavour; (e) verdict. Curious in extension, ADVERSARIAL in review (every addition risks lever-pile / NERS-N failure), judicious in reconciliation.`,
    { schema: RECONCILE_SCHEMA, label: `reconcile:${c.key}`, phase: 'Reconcile' }
  )),
])

const moduleResults = round1.slice(0, CLUSTERS.length).filter(Boolean)
const resolutionResult = round1[CLUSTERS.length] || null
const reconcileResults = round1.slice(CLUSTERS.length + 1).filter(Boolean)

const targets = []
for (const m of moduleResults) {
  for (const f of (m.findings || [])) {
    if (f.severity === 'P1' || f.severity === 'P2') targets.push({ id: `${m.module}:${f.id}`, kind: 'finding', payload: f, ctx: `module ${m.module}` })
  }
}
if (resolutionResult) for (const f of (resolutionResult.findings || [])) targets.push({ id: `resolution:${f.id}`, kind: 'finding', payload: f, ctx: 'resolution diagnostic' })
for (const r of reconcileResults) {
  for (const imp of (r.improvements || [])) {
    if (imp.severity === 'high' || imp.severity === 'medium') targets.push({ id: `${r.corpus}:${imp.id}`, kind: 'addition', payload: imp, ctx: `corpus ${r.corpus}` })
  }
}
targets.sort((a, b) => {
  const score = t => (t.kind === 'addition' ? 2 : 0) + (t.payload && t.payload.severity === 'P1' ? 1 : 0)
  return score(b) - score(a)
})
log(`Adversarial targets: ${targets.length} (${targets.filter(t => t.kind === 'addition').length} additions, ${targets.filter(t => t.kind === 'finding').length} findings)`)
const MAX_TARGETS = 40
const capped = targets.slice(0, MAX_TARGETS)
if (targets.length > MAX_TARGETS) log(`NOTE: capped adversarial verification at ${MAX_TARGETS}/${targets.length} targets (additions + P1s prioritized)`)

phase('Adversarial')
const verdicts = (await parallel(capped.map((t, i) => () => A(
  `${SHARED}\n\n=== ADVERSARIAL VERIFICATION (target ${i + 1}) ===\nFrom: ${t.ctx}. Target kind: ${t.kind}.\nTARGET (JSON): ${JSON.stringify(t.payload)}\n\nRun to BREAK it, not bless it. Read the cited code yourself.\n- FINDING: is the claim true against HEAD? severity right? could it be a deliberate, safeguarded design choice (intent gate)? stale (already fixed)?\n- ADDITION (corpus improvement): the bar is NERS-Necessary. Does the engine ALREADY deliver this churn another way? Would it be a lever-pile (E/N fail)? Does it preserve mirror-fairness & invariants? Gated on an UNRUN sim? Default to skepticism — most additions should be rejected or deferred unless they CONSOLIDATE or fix a real dead/broken path.\nReturn target_id="${t.id}", real, ners_compliant, a severity adjustment, adversarial reasoning (what survived the attack), and a revised recommendation.`,
  { schema: VERIFY_SCHEMA, label: `verify:${t.id}`, phase: 'Adversarial' }
)))).filter(Boolean)

phase('Distill')
const compact = {
  modules: moduleResults.map(m => ({ module: m.module, ners: m.ners, churn: m.churn, findings: m.findings, recs: m.recommendations })),
  resolution: resolutionResult,
  reconcile: reconcileResults.map(r => ({ corpus: r.corpus, already: r.already_in_engine, improvements: r.improvements, reject: r.reject, creative: r.creative_layer, verdict: r.verdict })),
  verdicts,
}
const distill = await A(
  `${SHARED}\n\n=== DISTILLATION SYNTHESIS ===\nYou have all module audits, the resolution diagnostic, corpus reconciliations, and adversarial verdicts (JSON below). Produce a DISTILLATION PROPOSAL in the spirit of the martial-morphology "distilled core": cut the elaborate to the few load-bearing variables.\n\nGovern by NERS and the churn principle. Use the adversarial verdicts to DISCARD findings that did not survive and additions that failed NERS-N.\nProduce: cut (dead-data / inert levers / redundancy to remove — specific, file/lever); consolidate (two-into-one: percussion sources, categorical->continuous heft, redundant difficulty levers); keep_core (the minimal NERS-clean load-bearing core that MUST stay — what actually generates churn); add_only_if (corpus additions worth it ONLY under stated gates — e.g. weapon-physics wiring gated on mirror/tier/no-one-shot sim); sequencing (ordered plan: portability/import fix → dead-data cull → consolidation → gated additions); and a one-paragraph headline.\n\nALL RESULTS (JSON):\n${JSON.stringify(compact)}`,
  { schema: DISTILL_SCHEMA, label: 'distill', phase: 'Distill', effort: 'high' }
)

return { modules: moduleResults, resolution: resolutionResult, reconcile: reconcileResults, adversarial: verdicts, distillation: distill }
