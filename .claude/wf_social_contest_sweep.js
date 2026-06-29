export const meta = {
  name: 'social-contest-coherence-sweep',
  description: 'Operational/integration sweep of the social contest system: (A) internal logic & coherence, (B) integration with faction dynamics & political events, (C) Key-bus wiring, (D) player legibility & fun. One analyst per lens, each finding adversarially verified against the live working tree.',
  phases: [
    { title: 'Investigate', detail: '8 parallel analysts across 4 axes read the corpus and surface findings (defects, gaps, risks, strengths) with verbatim quotes + an axis verdict' },
    { title: 'Verify', detail: 'each finding adversarially re-checked against the cited + adjacent files (is it sound / already-handled / overstated / refuted?)' },
  ],
}

const CORPUS = [
  'CORPUS (repo-relative, cwd = C:/Github/ttrpg). Read what your lens needs; GREP adjacent files before claiming a gap.',
  '  -- THE SYSTEM --',
  '  designs/scene/social_contest_v30.md            main spec (S1-12: setup, exchange, resolution, asymmetric, BG, hybrid, obligations, succession, heresy).',
  '  designs/scene/social_contest_v30_infill.md     prose/rationale.',
  '  params/contest.md  params/contest_extensions.md  formulas, tables, patch log, Resonant Style targeting.',
  '  sim/personal/contest.py  sim/personal/tribunal.py  Python sim of the pipeline.',
  '  designs/scene/derived_stats_v30.md             CANONICAL derived-value spec; SECTION 14 is the dated Jordan-ratified taxonomy (source of truth for formulas/buckets).',
  '  params/core.md                                 engine primitives + channel-reservation rule (actor-state degradation = -1D Pool, NOT +Ob).',
  '  -- FACTION DYNAMICS & POLITICAL EVENTS --',
  '  designs/provincial/faction_state_authoring_v30.md  faction_layer_v30.md  faction_politics_v30.md  Mandate/Stability/L-PS/rank ladders/coalition/succession/Sacred Veto.',
  '  designs/provincial/ci_political_v30.md  victory_v30.md  CI milestones/Theocracy attempt; era transitions.',
  '  designs/npcs/npc_behavior_v30.md (+infill)     Stance Triangle, Resonant Style, Belief Revision (S3.2), Conviction Scars (S3.3/3.4), Obligation-priority-tree, arcs, Recruitment Offer (S9.5).',
  '  designs/architecture/player_agency_v30.md      Scene Slate, Domain Actions (Subversion/Diplomacy), Standing.',
  '  -- KEYS / ENGINE / SCALE --',
  '  designs/architecture/key_substrate_v30.md  key_type_registry_v30.md  references/module_contracts.yaml  the Key bus, types, emit/consume, resolver classes, seeding.',
  '  designs/architecture/scale_transitions_v30.md  zoom/handoff fabric, Mandatory Zoom-In triggers, targets[]/scale_signature.',
  '  designs/provincial/clock_registry_v30.md       Obligations/Investigations/CI as clocks.',
  '  -- LEGIBILITY / UI --',
  '  designs/articulation/articulation_layer_v30.md  the player-facing articulation surface (Bonds register, cut-scene triggers, chronicle).',
  '  designs/ui/valoria_ui_ux_v4_1.md  valoria_ui_ux_v4_2_workplan.md  UI spec (lobbying scene, contest surfacing).',
  '  -- PRIOR AUDITS (cross-reference, do NOT re-derive) --',
  '  designs/audit/2026-06-28-distillation-coherence/distillation_coherence_report.md  two-primitive engine map; flags contest unkeyed seams + MEDIUM ESCP tier.',
  '  designs/audit/2026-06-28-social-contest-deliberation-critique/critique.md (+ findings.json)  the deliberation-as-game design critique (different angle: design philosophy, not operational coherence).',
  '  tools/observability/social_contest_audit.workflow.js  the internal-consistency audit (spec-vs-params-vs-sim) lens set.',
].join('\n')

const CANON_NOTE = [
  'CANONICAL HIERARCHY: derived_stats_v30 SECTION 14 carries the most recent dated Jordan-ratified rulings (ED-902, PP-716/717) — source of truth for derived-value formulas/buckets. params/core.md defines channel reservation (actor-state degradation -> -1D Pool). params/contest.md is newer than the spec on some rulings and stale on others; the spec lags on propagations; the sim may implement struck rules. A file labeled CANONICAL can contradict itself across sections.',
  '',
  'STANDARD TO JUDGE AGAINST:',
  ' - COHERENCE: the pieces fit and produce sensible, non-degenerate outcomes; no orphaned states, no dead/dominant strategies, no contradictions, no provisional-treated-as-canonical in live resolution.',
  ' - INTEGRATION: contest outputs (track, Obligation, Domain Echo, Succession, Mandate) actually move faction state & political events in a bounded/DAMPED way (suspect any unbounded loop), and political events correctly drive/zoom into contests and back across scales.',
  ' - KEYS: every consequential contest event is a typed Key (key_substrate invariant); emit-closure (every emitted type registered) + consume-closure (every type consumed); cross-scale Keys populate targets[]/scale_signature/stat_deltas; replay-determinism preserved (no silent state writes off the bus).',
  ' - PLAYER EXPERIENCE: LEGIBLE (the player can see and understand the state and why an outcome happened — opacity is the project owner\'s stated core pain; the GM-hidden-ledger vs player-knowledge boundary matters) and FUN (meaningful, non-dominated choices each exchange; decision density; good pacing; stakes clarity; the "format follows context" variety actually yields distinct experiences).',
  '',
  'EVIDENCE RULE: every claim about the system MUST carry a SHORT VERBATIM QUOTE you actually read from a named file (file + section). No quote = not a finding. Before asserting a gap, GREP the adjacent files — a mechanic may live in npc_behavior/faction_*/key_type_registry/articulation/ui.',
  'ENGINE DISCIPLINE for fixes: reuse the two primitives (sigma resolver; armature dot-product), the Key bus, and the existing buckets (pool/track/clock/derived_value). No bolt-on parallel subsystems.',
  'SEVERITY: critical = breaks a core computation, a replay-determinism invariant, or makes the system unplayable/illegible at the table. major = a real defect/gap/unbounded-loop/blind-seam that degrades coherence, integration, or fun. minor = drift, stale label, inferable gap. cosmetic = numbering/ordering nits. Only report what you can ground in a quote; quality over quantity.',
].join('\n')

const LENSES = [
  {
    key: 'A1-resolution-math',
    axis: 'A · Logic & coherence',
    brief: [
      'AXIS A (LOGIC & COHERENCE) — the resolution kernel. Audit whether the per-exchange math produces sensible, non-degenerate outcomes.',
      'Check: (1) the interaction matrix (CLASH/REINFORCE/CROSS/TIE) and margin-vs-resistance movement — does it stall, swing wildly, or have a DOMINANT/DEAD strategy? Trace the known prior findings: ED-295 (CLASH stalls at median margin), ED-296 (REINFORCE negative movement floor), ED-297 (Coalition Push ~5/exchange dominates solo ~0) — are the RATIFIED fixes (per-exchange resistance erosion ED-864 Option D; max(0,..) floor; coalition-dominance-as-intended) coherent, or do they interact badly (e.g. erosion + Deadlock drop double-counting; coalition dominance making solo advocacy pointless)?',
      '(2) Strain/Composure/Concentration/Spent/Doubt-Marker math: is it internally consistent (x3 scaling everywhere), does Spent stay reachable, does the channel-reservation hold (-1D not +Ob)?',
      '(3) SIM FIDELITY (operational coherence): does sim/personal/contest.py actually implement the canonical kernel, or a simplified/struck one? (It is documented to treat all exchanges as one margin-vs-resistance compare — i.e. NO interaction types, NO genre/Recall/Corroborate/Momentum dice, NO strain/Concentration, Contest Fatigue on any Decisive not just Total Victory, tie always toward side A.) Enumerate each divergence with the sim line + canonical quote, and state whether the sim can be trusted to validate balance at all.',
      'Deliver an AXIS VERDICT: is the resolution logic coherent and non-degenerate?',
    ].join('\n'),
  },
  {
    key: 'A2-lifecycle-coherence',
    axis: 'A · Logic & coherence',
    brief: [
      'AXIS A (LOGIC & COHERENCE) — the sub-system state machines. Audit whether the contest\'s lifecycle pieces fit together without contradiction, orphaned states, or dead ends.',
      'Check the coherence of: Obligations + Wager edge cases (S6.1/6.1.1 — counterparty death/collapse/impossible, PC death holding/owing); Chain Contests + Deadlock + cold-equilibrium (S6.3); Succession Contest + faction split (S7.2/7.2.1); Heresy Investigation lifecycle (S7.3, 8 closure conditions) + Excommunication Tribunal (S7.1) + Parliamentary Stay (S10.1). Look for: states with no exit, transitions that contradict each other, two mechanisms doing the same job (e.g. ED-864 erosion vs S6.3 Deadlock resistance-drop), PROVISIONAL content used in live resolution (Panel ED-137), out-of-order/struck content presented as live, and cross-references to undefined mechanics.',
      'Also assess STRUCTURAL coherence of the doc itself only insofar as it affects usability (e.g. S7.1/S10.1 placed after S12; step-numbering gaps) — but focus on LOGIC coherence (do the rules cohere) over cosmetics.',
      'Deliver an AXIS VERDICT: do the lifecycle sub-systems form coherent state machines?',
    ].join('\n'),
  },
  {
    key: 'B1-contest-to-faction',
    axis: 'B · Faction dynamics',
    brief: [
      'AXIS B (FACTION DYNAMICS) — does a contest outcome move the faction world coherently and in a BOUNDED way?',
      'Trace every contest->faction output: Mandate +1 (Domain Echo, decisive+Memory), the +1D Domain Action bonus (decisive+Projection), Total-Victory Mandate -1, the Obligation -> NPC priority-tree block (S6.1), the Succession faction-split stat inheritance (S7.2.1), BG Parliamentary Vote -> Mandate -1. For each: confirm the receiving faction stat/mechanic actually EXISTS in faction_state/faction_layer/faction_politics (grep), and that the magnitude is coherent with that stat\'s scale and caps.',
      'Critically assess LOOP DAMPING (the distillation report flagged this): the npc_behavior <-> social_contest 2-cycle (opinion oscillation) and the concern->opinion->concern cycle have NO specified damper; Mandate has a saturating damper (7T/(T+6)) — does the contest\'s Mandate writes respect it? Is there any runaway (a faction that keeps winning contests -> more Mandate -> bigger pool -> wins more)? Are Domain Echo / Obligation grants capped per season?',
      'Also: does a contest LOSS for the player meaningfully constrain them (Player Obligations are violable) and does an NPC loss meaningfully constrain the AI (priority-tree block) — i.e. is the political consequence real and legible, not a stat bump that evaporates?',
      'Deliver an AXIS VERDICT: does the contest integrate coherently and bounded-ly with faction dynamics?',
    ].join('\n'),
  },
  {
    key: 'B2-political-events',
    axis: 'B · Political events',
    brief: [
      'AXIS B (POLITICAL EVENTS) — does the contest drive and get driven by the setting\'s political-event machinery coherently?',
      'Map the event loops: Heresy Investigation / Excommunication Tribunal / Parliamentary Stay (contest as the resolution venue) and their coupling to CI (Church Influence) milestones (ci_political_v30: the CI<55 Stay gate, CI thresholds, the Theocracy attempt) and to faction crises. Succession Contest triggered by leader removal (npc arcs / faction_politics). Domain Echo shifting Institutional Tendency. Check: are the trigger conditions and closure conditions coherent and REACHABLE (no event that can never fire or never end)? Does a contest outcome correctly advance the political timeline (CI up, arc transition, Scene Slate crisis), and do political events correctly spawn contests?',
      'Grep ci_political/victory/npc_behavior arcs to verify the cross-references the contest spec makes (e.g. scale_transitions S4.3.2 Mandatory Zoom-In on active Heresy Investigation; baralta_crown_claim Crown succession; CI political-pool bonus floor(CI/20) making the Stay unpassable at 55+).',
      'Deliver an AXIS VERDICT: does the contest cohere with the political-event lifecycle of the setting?',
    ].join('\n'),
  },
  {
    key: 'B3-scale-integration',
    axis: 'B · Scale integration',
    brief: [
      'AXIS B (SCALE INTEGRATION) — does the faction-scale <-> personal-scale bridge cohere?',
      'Audit the three modes: BG Parliamentary Vote (S10, faction Mandate-pool roll), TTRPG personal contest (S1-9), and Hybrid (S11, BG layer -> capped offset -> TTRPG layer). Check: the Lobby Cap (S10/S11, PP-256/ED-621 clamps the starting track to 4-6) — is it coherent across BG and Hybrid? Does the Hybrid hand-off (BG offset clamped to compromise zone, then run TTRPG from there) preserve meaning, or can the BG layer pre-decide / be wasted? Does scale_transitions actually define the zoom that takes a faction-scale political vote down to a personal contest and propagates the result back up (targets[]/scale_signature)? Is the BG vote math (sum of Mandate, genre/audience boost, resistance) coherent with the personal kernel, or a separate untested formula (SIM-DEBT)?',
      'Deliver an AXIS VERDICT: do BG/TTRPG/Hybrid cohere as one system across scales?',
    ].join('\n'),
  },
  {
    key: 'C1-key-integration',
    axis: 'C · Key integration',
    brief: [
      'AXIS C (KEYS) — does the contest live correctly on the Key bus? This is the most concrete, verifiable lens.',
      'For every consequential contest event, determine whether it EMITS a typed Key registered in key_type_registry_v30, and whether that Key is CONSUMED by >=1 system: contest resolution (track outcome / decisive / total victory), Obligation creation, Domain Echo faction-stat grant, Conviction Scar, Belief Revision (state.belief_revised — the registry has a STUB/under-attribution at this; ED-937/workplan #32), Succession faction-split, BG vote result. The distillation report explicitly flags these as UNKEYED "delivers-blind" down-seams (Domain-Echo DA-bonus and Obligation creation unkeyed; Thread->settlement writes silent; cross-system wound impairment read from state not carried by a Key). VERIFY each against key_type_registry + module_contracts (grep for the event type).',
      'Then assess the consequences: (1) REPLAY DETERMINISM — does any contest consequence write game-state silently (off the bus), breaking save=initial+Key-log/replay=re-run-log? (2) CHRONICLE/ARTICULATION VISIBILITY — does the articulation layer see contest events (it consumes Keys; an unkeyed Obligation/Belief-revision is invisible to the chronicle/cut-scenes)? (3) CROSS-SCALE — do contest Keys populate targets[]/scale_signature/stat_deltas, or deliver blind? (4) SEEDING — is any contest RNG (the contest.py random, succession draws) seeded per-Key-emission for replay?',
      'Deliver an AXIS VERDICT: is the contest emit-closed, consume-closed, and replay-safe on the Key bus?',
    ].join('\n'),
  },
  {
    key: 'D1-legibility',
    axis: 'D · Player experience',
    brief: [
      'AXIS D (LEGIBILITY) — can the player SEE and UNDERSTAND the contest? Opacity is the project owner\'s stated core pain.',
      'Audit what is hidden vs visible. The Persuasion Track and exchange results are recorded on a HIDDEN GM LEDGER (S2 Step 7 "Record all above in the hidden GM ledger"; S4 Step 7 "GM records exchange on hidden ledger"; S6 "GM reveals ledger"). The audience boost must be discovered by Appraise; the adjudicator/opponent Resonant Style must be Appraised; Obligations and Scars have deliberately partial visibility (S6.2 "the player does not learn the Scar count"). Assess: can a player form a correct mental model of WHERE THEY STAND and WHY an outcome happened, or is the contest a black box whose result feels arbitrary? Is the hidden-ledger a deliberate fog-of-war that creates tension, or genuine opacity that makes choices unguided? What does the articulation_layer / valoria_ui_ux surface actually show the player about a live contest (track position, resistance, available styles, what an outcome will cost)? Is there a plain-language read of state, or only GM-side numbers?',
      'Weigh both: some hiddenness is good design (you should not see the NPC\'s exact Scar count); some is opacity debt (the player cannot tell a winning line from a losing one). Distinguish them.',
      'Deliver an AXIS VERDICT: is the contest legible enough for a player to make informed decisions?',
    ].join('\n'),
  },
  {
    key: 'D2-fun-agency',
    axis: 'D · Player experience',
    brief: [
      'AXIS D (FUN / AGENCY) — does the contest offer meaningful, non-dominated choices and good pacing?',
      'Audit decision density and dominance. Each exchange the player picks: a style (genre x orientation -> Precedent/Suppression/Vision/Insinuation), whether to cite Recall (+2D), Corroborate, spend Momentum, or Forfeit (Regroup/Concede). Assess: are these REAL choices or is there a dominant line (e.g. always match the audience-boosted axis for +1D; always Obscuring for the free Doubt Marker; Coalition Push dominating solo per ED-297)? Are any options DEAD (never worth picking)? Does Appraise->target the audience/Resonant-Style create a satisfying recon->tailor loop, or is it bookkeeping? Is the genre/orientation choice a meaningful read of the room or a lookup?',
      'PACING & GRIND: exchange counts (Formal 3 / Grand 5 / Tribunal 1-5 / max-10 stalemate), the Spent loop, Chain Contests (up to 3) + 4-season lockout, long Heresy lifecycles (4-6 seasons). Does a contest resolve in a satisfying arc, or grind? Does "format follows context" actually deliver DISTINCT experiences across venue types, or the same dice game with a different primary attribute?',
      'STAKES CLARITY: does the player know what they are playing for (S2 Step 6 stakes) and what each outcome band (decisive/compromise/total) will concretely cost/grant, before committing?',
      'Deliver an AXIS VERDICT: is the contest fun — meaningful choices, good pacing, distinct venues, clear stakes?',
    ].join('\n'),
  },
]

const FINDINGS_SCHEMA = {
  type: 'object',
  properties: {
    lens: { type: 'string' },
    axis: { type: 'string' },
    axis_verdict: { type: 'string', description: 'one-paragraph answer to this lens\'s core question: does this aspect work? (coherent/integrated/key-clean/legible/fun?) with the headline reason.' },
    findings: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          id: { type: 'string', description: 'short stable id, e.g. A1-1' },
          type: { type: 'string', enum: ['strength', 'defect', 'gap', 'risk'] },
          title: { type: 'string' },
          severity: { type: 'string', enum: ['critical', 'major', 'minor', 'cosmetic'] },
          claim: { type: 'string', description: 'the issue (or strength) in one or two sentences' },
          locations: {
            type: 'array',
            items: {
              type: 'object',
              properties: {
                file: { type: 'string' },
                section: { type: 'string' },
                quote: { type: 'string', description: 'verbatim text actually read' },
              },
              required: ['file', 'quote'],
            },
          },
          impact: { type: 'string', description: 'concrete effect on logic / faction-integration / keys / player-experience' },
          fix: { type: 'string', description: 'concrete remedy reusing engine primitives. Empty for pure strengths.' },
        },
        required: ['id', 'type', 'title', 'severity', 'claim', 'locations', 'impact'],
      },
    },
  },
  required: ['lens', 'axis', 'axis_verdict', 'findings'],
}

const VERDICT_SCHEMA = {
  type: 'object',
  properties: {
    finding_id: { type: 'string' },
    verdict: { type: 'string', enum: ['sound', 'already-handled', 'overstated', 'refuted', 'uncertain'] },
    corrected_severity: { type: 'string', enum: ['critical', 'major', 'minor', 'cosmetic'] },
    reasoning: { type: 'string', description: 'why. If already-handled, name WHERE in the corpus the mechanic actually lives, with a quote.' },
    evidence_quote: { type: 'string', description: 'a key verbatim quote you independently located' },
    fix_assessment: { type: 'string', description: 'is the proposed fix engine-disciplined and correct? tighten if needed.' },
  },
  required: ['finding_id', 'verdict', 'reasoning'],
}

phase('Investigate')
const results = await pipeline(
  LENSES,
  (l) => agent(
    [
      'You are a senior game-systems engineer auditing the Valoria TTRPG social contest system for OPERATIONAL COHERENCE and PLAYER EXPERIENCE (not design philosophy).',
      'Axis: ' + l.axis + '. Lens: ' + l.key + '.',
      '', CORPUS, '', CANON_NOTE,
      '', 'YOUR LENS:', l.brief,
      '', 'Read the relevant files yourself (Read/Grep/Glob). Return the schema. lens="' + l.key + '", axis="' + l.axis + '". Give the axis_verdict as a crisp does-this-work judgement. 3-7 sharpest findings (include strengths where real), each grounded in a verbatim quote. Do not invent gaps without grepping adjacent files first.',
    ].join('\n'),
    { label: 'investigate:' + l.key, phase: 'Investigate', schema: FINDINGS_SCHEMA, effort: 'high' },
  ),
  (review, l) => {
    const findings = (review && review.findings) ? review.findings : []
    return parallel(findings.map((f) => () =>
      agent(
        [
          'ADVERSARIAL VERIFICATION of an operational-coherence finding about the Valoria social contest system. Pressure-test it; open the cited files AND grep the adjacent corpus yourself.',
          CORPUS,
          '', 'FINDING (JSON):', JSON.stringify(f, null, 2),
          '', 'Verdict: "sound" (holds as described) / "already-handled" (the gap is actually addressed somewhere — NAME WHERE with a quote; the corpus is large, this is the key check) / "overstated" (partly true, severity too high) / "refuted" (quote not locatable or out of context) / "uncertain". Independently locate an evidence_quote. Assess corrected_severity honestly. Judge whether the fix is engine-disciplined (reuses sigma resolver / armature dot-product / Key bus / existing buckets; no bolt-on). finding_id="' + f.id + '".',
        ].join('\n'),
        { label: 'verify:' + l.key + ':' + f.id, phase: 'Verify', schema: VERDICT_SCHEMA, effort: 'high' },
      ).then((v) => Object.assign({}, f, { lens: l.key, axis: l.axis, verdict: v })).catch(() => null),
    ))
  },
)

const all = results.flat().filter(Boolean)
const axisVerdicts = results.map((r, i) => ({ lens: LENSES[i].key, axis: LENSES[i].axis, axis_verdict: (r && r.axis_verdict) || '(no verdict returned)' }))
const surviving = all.filter((f) => f.verdict && (f.verdict.verdict === 'sound' || f.verdict.verdict === 'overstated' || f.verdict.verdict === 'already-handled'))
const refuted = all.filter((f) => f.verdict && f.verdict.verdict === 'refuted')
const sevOf = (f) => (f.verdict && f.verdict.corrected_severity) ? f.verdict.corrected_severity : f.severity

log('sweep complete: ' + all.length + ' findings raised; ' + surviving.length + ' survive (' + refuted.length + ' refuted). critical=' + surviving.filter(f=>sevOf(f)==='critical').length + ' major=' + surviving.filter(f=>sevOf(f)==='major').length)

return {
  totals: { raised: all.length, surviving: surviving.length, refuted: refuted.length,
    by_severity: { critical: surviving.filter(f=>sevOf(f)==='critical').length, major: surviving.filter(f=>sevOf(f)==='major').length, minor: surviving.filter(f=>sevOf(f)==='minor').length, cosmetic: surviving.filter(f=>sevOf(f)==='cosmetic').length } },
  axis_verdicts: axisVerdicts,
  findings: surviving,
  strengths: surviving.filter(f => f.type === 'strength'),
  refuted,
  uncertain: all.filter((f) => f.verdict && f.verdict.verdict === 'uncertain'),
}
