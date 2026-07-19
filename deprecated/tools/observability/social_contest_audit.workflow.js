// RETIRED (2026-07-11, ED-IN-0033, Valoria Audit Ecosystem plan Phase 2 item 10 — Jordan's
// ruling). Moved from tools/observability/ to deprecated/tools/observability/ via `git mv`.
// Do not invoke; do not resurrect without re-authoring against current canon.
//
// Why:
//   - Never executed even once: no dated audit output anywhere in designs/audit/ cites this
//     workflow by name (confirmed by grep of designs/audit/ for "social_contest_audit.workflow").
//   - Its CORPUS constant cites `sim/personal/contest.py`, which no longer exists — the
//     2026-07-02 contest rebuild (Stage 3 / Gate C, PR #63) replaced it with the
//     `sim/personal/contest/` package (armature, rhetoric, appraise modules).
//   - Its CANON_NOTE source-hierarchy predates the entire ED-SC-0002..0015 lane-tagged
//     ruling sequence and no longer reflects the live canonical-precedence ordering.
//   - The SC lane already has a ratified, dated, executed subsystem audit covering this exact
//     ground: designs/audit/2026-07-05-fable5-social-contest-audit/ (PR #80).
//
// See deprecated/skills/README.md for the retirement-batch precedent this follows.
export const meta = {
  name: 'social-contest-audit',
  description: 'Multi-agent consistency audit of the Valoria social contest subsystem (spec vs params vs canonical derived-stats vs sim), with adversarial verification of every finding',
  phases: [
    { title: 'Find', detail: '7 parallel auditors, one per dimension, read the contest corpus and surface findings with verbatim quotes' },
    { title: 'Verify', detail: 'each finding adversarially re-checked against the cited text by an independent agent' },
  ],
}

const CORPUS = [
  'SOCIAL CONTEST CORPUS (repo-relative paths, cwd = C:/Github/ttrpg):',
  '  designs/scene/social_contest_v30.md          - main design spec (sections 1-12). Header says CANONICAL.',
  '  designs/scene/social_contest_v30_infill.md   - prose infill for the spec.',
  '  designs/scene/social_contest_system_v2.md    - legacy v2 (may be superseded/renamed source).',
  '  params/contest.md                            - params file (formulas, tables, patch log).',
  '  params/contest_extensions.md                 - canonical post-v2 additions (PP-NEW, Resonant Style).',
  '  params/core.md                               - engine primitives + channel-reservation rule (Pool vs Ob).',
  '  designs/scene/derived_stats_v30.md           - CANONICAL derived-value spec. Section 14 is the dated,',
  '                                                 Jordan-ratified 4-bucket authoritative taxonomy.',
  '  sim/personal/contest.py                      - Python sim implementing the contest pipeline.',
  '  sim/personal/tribunal.py                     - related sim (tribunal/asymmetric).',
].join('\n')

const CANON_NOTE = [
  'CANONICAL HIERARCHY (for deciding which side of a contradiction is current):',
  '  - derived_stats_v30.md section 14 carries the most recent DATED, Jordan-ratified rulings (ED-902 2026-06-04,',
  '    PP-716/PP-717, Decision-C 2026-05-15). Treat section 14 as source of truth for derived-value formulas.',
  '  - params/core.md defines the engine channel reservation: actor-STATE degradation (wounds, Rattled, Spent)',
  '    must be a -1D Pool penalty; the Ob channel is reserved for non-actor-state mechanics. (PP-716 / Decision-B.)',
  '  - params/contest.md sometimes reflects NEWER decisions than the spec (Decision-B Rattled to -1D) but is STALE',
  '    on others. Do not assume any single file is uniformly current.',
  '  - social_contest_v30.md is the design spec but lags on several propagations.',
  '  - The sim (contest.py) cites the spec but may implement a struck/older rule.',
  '  IMPORTANT: a file labeled CANONICAL can still contradict ITSELF across sections, or contradict the section-14',
  '  taxonomy. Intra-file contradictions are valid, high-value findings.',
  '',
  'EVIDENCE RULE: every location you cite MUST include a SHORT VERBATIM QUOTE you actually read from that file.',
  'No quote = not a finding. Cite file + section/line context for each.',
  '',
  'SEVERITY:',
  '  critical = makes a core resolution computation ambiguous or wrong (two live formulas for a value used in',
  '             strain/track math; sim computes materially wrong outcomes).',
  '  major    = a real rule contradicts another live rule (spec-vs-spec, spec-vs-canonical, spec-vs-sim);',
  '             struck content still presented as live; a channel-reservation violation.',
  '  minor    = terminology drift, stale changelog entry, a cross-ref gap where the mechanic is still inferable.',
  '  cosmetic = step-numbering gaps, out-of-order sections, label nits.',
  'Only report defects you can ground in quotes. Quality over quantity.',
].join('\n')

const DIMENSIONS = [
  {
    key: 'derived-values',
    title: 'Derived-value formulas (Composure / Concentration / Cha-mod / Foc-defence)',
    prompt: [
      'Audit DERIVED-VALUE CONSISTENCY across the contest corpus.',
      'For EACH of: Composure, Concentration, Charisma modifier, Focus defence, and the Concentration depletion/Spent rate -',
      'collect EVERY formula / numeric range / depletion-rate statement wherever it appears (social_contest_v30 sec 4/6/8/9.2,',
      'derived_stats_v30 sec 5 and 14, params/contest.md Derived/Concentration/Composure, params/contest_extensions PP-NEW-D,',
      'sim/personal/contest.py). Then for each value: list competing statements with verbatim quotes, decide which is canonical',
      'per the dated section-14 rulings, and flag every stale/contradicting statement (formula mismatch, range mismatch,',
      'x3-scaling applied in one place but not another, depletion -1 vs -3).',
      'Pay special attention to: (a) Concentration = (3xFocus)+(2xSpirit) [ED-902] vs Focus x3 - and whether the SAME canonical',
      'file states both; (b) Charisma modifier / Focus defence appearing as 0-2 / 0-3 in the resolution rules but 0-6 / 0-9',
      '(x3-scaled) in the derived summary - since strain is computed with these, the swing changes outcomes; (c) whether the',
      'sim implements a struck formula.',
    ].join('\n'),
  },
  {
    key: 'channel-discipline',
    title: 'Channel discipline (Pool -1D vs +Ob) for actor-state degradation',
    prompt: [
      'Audit CHANNEL DISCIPLINE. First confirm, with a quote, the engine channel-reservation rule from params/core.md and/or',
      'derived_stats_v30 (actor-state degradation = -1D to Pool; Ob channel reserved for non-actor-state). Then find EVERY place',
      'in the contest corpus where an actor-state penalty (Rattled, Spent, Concentration loss, wounds) is still expressed as',
      '"+1 Ob" / "+Ob" instead of "-1D to Pool". Check social_contest_v30 sec 4/6, params/contest.md (note its Decision-B',
      '"Rattled converted from +Ob to -1D"), AND derived_stats_v30 sec 5.1 itself (its Composure row Depleted-at cell).',
      'Report each violation with a quote, name the canonical channel, and state whether the violating file otherwise claims',
      'to be canonical.',
    ].join('\n'),
  },
  {
    key: 'terminology',
    title: 'Terminology / naming consistency',
    prompt: [
      'Audit TERMINOLOGY consistency. Build a variant map (with quotes) for each concept and flag inconsistent or ambiguous',
      'usage across files:',
      '  - Interaction types: CLASH vs Head-On; REINFORCE vs Echo Match vs Coalition Push; CROSS vs Cross-Time. Specifically',
      '    resolve: is Coalition Push a 4th interaction type or a rename of REINFORCE? Is it defined anywhere?',
      '  - The penalty marker: Doubt Marker vs Suspicion Token (same mechanic, two names?).',
      '  - Argument style names: Precedent/Suppression/Vision/Insinuation vs Cite Precedent/Bury Precedent/Propose Vision/Imply Consequence.',
      '  - Orientation labels: Revealing/Obscuring vs Direct/Indirect.',
      '  - The exchange Step-1 action name: Appraise vs Read vs Judge.',
      '  - System name: Debate vs Contest. Faction ethical-mode labels (Church Divine Command vs Faith; Crown Virtue Ethics vs',
      '    Virtue; Restoration Rawlsian vs Equity).',
      'Report each term used inconsistently across files, with the variants and quotes.',
    ].join('\n'),
  },
  {
    key: 'stale-struck',
    title: 'Stale / superseded / struck content still presented as live',
    prompt: [
      'Audit for STALE / STRUCK content still presented as a live rule. Investigate at least:',
      '  (a) Niflhel social toolkit - params says STRUCK (ED-764 / CR-STRIKE-2026-04-19); is it still present as live rules in',
      '      social_contest_v30 sec 9.7 and/or the sec-2 faction-boost table?',
      '  (b) Recall removed from Concentration (ED-694) - does Recall still appear in the Appraise pool and/or the sec-9.2',
      '      coalition Concentration pool?',
      '  (c) Composure = Charisma + 6 surviving anywhere (a changelog/Resolved table) while the body says x3.',
      '  (d) First-to-speak: spec resolved to ROLLED (ED-581) but does params still show the deterministic version and an OPEN ED-138?',
      '  (e) PP-NEW-D referencing a formula/section since struck.',
      'For each, quote both the stale text and the superseding canonical text, and name which document is out of date.',
    ].join('\n'),
  },
  {
    key: 'resolution-logic',
    title: 'Resolution logic, edge cases, and structural defects',
    prompt: [
      'Audit RESOLUTION LOGIC and STRUCTURE (social_contest_v30 + params/contest.md + extensions).',
      '  - Resistance erosion: there appear to be TWO mechanisms - params ED-864 Option D (per-exchange erosion,',
      '    Stab_resistance_t = max(0, Stab_resistance_0 - floor(exchange/2)), applies to ALL contests) and social_contest_v30',
      '    sec 6.3 ED-582 Deadlock (chain contests, resistance drops by 1 after 2 zero-movement exchanges). Determine whether',
      '    they conflict, stack, or duplicate, and whether the spec omits the ED-864 mechanic entirely (or vice versa).',
      '  - Edge logic: TIE/CROSS no-strain precedence (sec 4 / PP-236); Spent timing (checked after Step 4, penalty next',
      '    exchange); CROSS net-movement direction; Total Victory (>=9/<=1) vs Decisive (>=7/<=3) thresholds.',
      '  - Structural defects: step-numbering gaps (sec 2 jumps Step 5 to Step 7; sec 4 has Step 2b but no Step 2; sec 11 has',
      '    steps 1,2,4 but no 3); out-of-order sections (sec 7.1 and sec 10.1 physically placed AFTER sec 12); unassigned patch',
      '    IDs (PP-NEW). Report concrete defects only, each with a quote.',
    ].join('\n'),
  },
  {
    key: 'sim-fidelity',
    title: 'Sim fidelity - contest.py vs canonical spec',
    prompt: [
      'Audit SIM FIDELITY: sim/personal/contest.py (and sim/personal/tribunal.py) vs the canonical contest spec',
      '(social_contest_v30 sec 1-9, params/contest.md, derived_stats_v30 sec 14.4 Argue Pool). Enumerate every canonical',
      'mechanic the sim OMITS or implements INCORRECTLY, each with the sim line/symbol and the canonical rule quote. Verify:',
      '  - Interaction types: does resolve_exchange implement CLASH/REINFORCE/CROSS/TIE, or treat ALL exchanges as one',
      '    margin-vs-resistance comparison (CLASH-only)?',
      '  - Missing dice inputs: genre/orientation bonus, Recall +2D, Corroborate, Momentum spend, style dice.',
      '  - Strain/Composure/Rattled: implemented at all?',
      '  - Concentration: constant CONCENTRATION_MULTIPLIER = 3 - is it ever USED? does it match canonical (3xFocus)+(2xSpirit)?',
      '  - Argue pool: sim uses (primary*2)+history; canonical sec 14.4 is (Primary*2)+History+3+style. Is the +3 present or lost?',
      '  - Contest Fatigue: sec 6 ties it to TOTAL VICTORY (>=9/<=1); does the sim apply it on ANY Decisive win?',
      '  - Tie movement: sec 4 says +1 toward the FIRST-TO-SPEAK holder; does the sim always move toward side A regardless?',
      '  - Resistance erosion / Spent / Doubt marker: implemented?',
    ].join('\n'),
  },
  {
    key: 'cross-system',
    title: 'Cross-system integration & dangling references',
    prompt: [
      'Audit CROSS-SYSTEM INTEGRATION and DANGLING REFERENCES. The contest spec references many other documents/sections.',
      'For each reference, use Grep/Glob to verify the target document AND the cited section actually exist in the repo; flag',
      'dangling or broken references and rules that depend on an undefined external mechanic. Check at least: clock_registry_v30',
      '(Obligations as clocks, sec 6.1); npc_behavior sec 3.3 / 5.2 / 1.2 (Resonant Style, Scars, Edeyja Arc E); scale_transitions',
      'sec 4.3.2 (Mandatory Zoom-In trigger); generational_transition_v30 (Obligation transfer on PC death, sec 6.1.1);',
      'player_agency sec 4.2 / 5.2 (Scene Slate, Standing>=5); faction_layer sec 1 (dissolution); baralta_crown_claim sec 2',
      '(Crown succession); fieldwork_investigation sec 2.3 (Findings). ALSO flag rules marked PROVISIONAL or "not yet designed"',
      'that are nonetheless treated as canonical (Panel adjudicator ED-137; any other open item used in live resolution).',
      'Each finding needs a quote.',
    ].join('\n'),
  },
]

const FINDINGS_SCHEMA = {
  type: 'object',
  properties: {
    dimension: { type: 'string' },
    findings: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          id: { type: 'string', description: 'short stable id, e.g. DV-1' },
          title: { type: 'string' },
          severity: { type: 'string', enum: ['critical', 'major', 'minor', 'cosmetic'] },
          claim: { type: 'string', description: 'the defect in one or two sentences' },
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
          canonical_position: { type: 'string', description: 'which statement is current/correct and why' },
          conflict: { type: 'string', description: 'what contradicts it' },
          why_it_matters: { type: 'string' },
          suggested_fix: { type: 'string' },
        },
        required: ['id', 'title', 'severity', 'claim', 'locations', 'why_it_matters'],
      },
    },
  },
  required: ['dimension', 'findings'],
}

const VERDICT_SCHEMA = {
  type: 'object',
  properties: {
    finding_id: { type: 'string' },
    verdict: { type: 'string', enum: ['confirmed', 'refuted', 'uncertain'] },
    corrected_severity: { type: 'string', enum: ['critical', 'major', 'minor', 'cosmetic'] },
    reasoning: { type: 'string', description: 'why confirmed/refuted - reference what you actually found' },
    evidence_quote: { type: 'string', description: 'the key verbatim quote you independently located' },
    fix_assessment: { type: 'string' },
  },
  required: ['finding_id', 'verdict', 'reasoning'],
}

phase('Find')
const results = await pipeline(
  DIMENSIONS,
  (d) => agent(
    'You are auditing the Valoria TTRPG social contest subsystem - dimension: ' + d.title + '.\n' + CORPUS + '\n' + CANON_NOTE + '\n\nYOUR LANE:\n' + d.prompt + '\n\nRead the relevant files yourself (Read/Grep/Glob). Return findings in the schema. dimension="' + d.key + '". If you genuinely find no defect in your lane, return an empty findings array - do not invent.',
    { label: 'find:' + d.key, phase: 'Find', schema: FINDINGS_SCHEMA },
  ),
  (review, d) => {
    const findings = (review && review.findings) ? review.findings : []
    return parallel(findings.map((f) => () =>
      agent(
        'ADVERSARIAL VERIFICATION. A prior auditor reported this finding about the Valoria social contest subsystem. Your job is to REFUTE it if you can. Open the cited files yourself and independently locate the quoted text.\n' + CORPUS + '\n' + CANON_NOTE + '\n\nFINDING (JSON):\n' + JSON.stringify(f, null, 2) + '\n\nRules:\n- If any cited quote cannot be located in the named file, or the quote is out of context such that the claimed contradiction does not actually hold, verdict = refuted.\n- If the contradiction/defect genuinely holds as described, verdict = confirmed.\n- If you cannot resolve it from the files, verdict = uncertain.\n- Independently assess corrected_severity (do not just copy). Provide the key evidence_quote you located yourself.\nReturn the verdict schema. finding_id = "' + f.id + '".',
        { label: 'verify:' + d.key + ':' + f.id, phase: 'Verify', schema: VERDICT_SCHEMA, effort: 'high' },
      ).then((v) => Object.assign({}, f, { dimension: d.key, verdict: v })).catch(() => null),
    ))
  },
)

const all = results.flat().filter(Boolean)
const sevOf = (f) => (f.verdict && f.verdict.corrected_severity) ? f.verdict.corrected_severity : f.severity
const confirmed = all.filter((f) => f.verdict && f.verdict.verdict === 'confirmed')
const uncertain = all.filter((f) => f.verdict && f.verdict.verdict === 'uncertain')
const refuted = all.filter((f) => f.verdict && f.verdict.verdict === 'refuted')

log('audit complete: ' + confirmed.length + ' confirmed, ' + uncertain.length + ' uncertain, ' + refuted.length + ' refuted (of ' + all.length + ' raised)')

return {
  summary: {
    total_raised: all.length,
    confirmed: confirmed.length,
    uncertain: uncertain.length,
    refuted: refuted.length,
    confirmed_by_severity: {
      critical: confirmed.filter((f) => sevOf(f) === 'critical').length,
      major: confirmed.filter((f) => sevOf(f) === 'major').length,
      minor: confirmed.filter((f) => sevOf(f) === 'minor').length,
      cosmetic: confirmed.filter((f) => sevOf(f) === 'cosmetic').length,
    },
  },
  confirmed,
  uncertain,
  refuted,
}
