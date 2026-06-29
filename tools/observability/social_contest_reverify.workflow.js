export const meta = {
  name: 'social-contest-reverify',
  description: 'Re-run the rate-limit-errored 3-lens verifications for the 9 throttled social-contest findings plus the corrected Piety/Persuasion-track finding, in small waves',
  phases: [
    { title: 'Verify', detail: 'each errored finding re-checked by a 3-lens panel (literal / context / currency); majority confirms. Waves of 2 findings.' },
  ],
}

const CORPUS = [
  'SOCIAL CONTEST CORPUS (repo-relative paths, cwd = C:/Github/ttrpg):',
  '  designs/scene/social_contest_v30.md          - main design spec (sections 1-12). Header says CANONICAL.',
  '  designs/scene/social_contest_v30_infill.md   - prose infill for the spec.',
  '  designs/scene/social_contest_system_v2.md    - legacy v2 (self-declares SUPERSEDED).',
  '  params/contest.md                            - params file (formulas, tables, patch log).',
  '  params/contest_extensions.md                 - canonical post-v2 additions.',
  '  params/core.md                               - engine primitives + channel-reservation rule (Pool vs Ob).',
  '  designs/scene/derived_stats_v30.md           - CANONICAL derived-value spec. Section 14 = dated Jordan-ratified taxonomy.',
  '  designs/npcs/npc_behavior_v30.md             - NPC behavior (uses Piety Track for contests).',
  '  sim/personal/contest.py                      - Python sim implementing the contest pipeline.',
].join('\n')

const CANON_NOTE = [
  'CANONICAL HIERARCHY (for deciding which side of a contradiction is current):',
  '  - derived_stats_v30.md section 14 carries the most recent DATED, Jordan-ratified rulings (ED-902 2026-06-04,',
  '    PP-716/PP-717, Decision-C 2026-05-15). Treat section 14 as source of truth for derived-value formulas AND track names.',
  '  - params/core.md defines the engine channel reservation: actor-STATE degradation (wounds, Rattled, Spent) must be a',
  '    -1D Pool penalty; the Ob channel is reserved for non-actor-state mechanics. (PP-716 / Decision-B.)',
  '  - params/contest.md sometimes reflects NEWER decisions than the spec, but is STALE on others. social_contest_v30.md is',
  '    the design spec but lags on several propagations. The sim may implement a struck/older rule. A file labeled CANONICAL',
  '    can still contradict ITSELF across sections.',
].join('\n')

const FINDINGS = [
  {
    id: 'C1-CONCENTRATION', severity: 'critical',
    title: 'Concentration has two live formulas and two depletion rates; the ED-902-struck Focus×3 survives in 4 places',
    claim: 'Canonical Concentration (ED-902, 2026-06-04) is (3×Focus)+(2×Spirit) range 5-35, but the struck Focus×3 (range 3-21) still appears in derived_stats §5.2, social_contest §4/§8, contest_extensions PP-NEW-D, and the sim; depletion rate is also -3/exchange in the spec vs -1/exchange in params.',
    locations: [
      { file: 'designs/scene/derived_stats_v30.md', section: '§12', quote: 'supersedes the Focus×3 interim (2026-06-04, Jordan, ED-902)' },
      { file: 'designs/scene/derived_stats_v30.md', section: '§5.2', quote: 'Depletion rate | −3 per exchange; −3 additional on exchange loss' },
      { file: 'designs/scene/social_contest_v30.md', section: '§4', quote: 'Concentration = Focus × 3. Range 3–21. Depletes by 3 per exchange' },
      { file: 'params/contest.md', section: 'Derived Values', quote: '(3 × Focus) + (2 × Spirit)' },
      { file: 'params/contest.md', section: 'Concentration and Spent', quote: 'Depletes −1/exchange, −1 additional on loss.' },
      { file: 'sim/personal/contest.py', section: 'L52', quote: 'CONCENTRATION_MULTIPLIER = 3' },
    ],
    canonical_position: '(3×Focus)+(2×Spirit), range 5-35 per derived_stats §14.1 / §12 ED-902 (2026-06-04). Focus×3 is explicitly STRUCK.',
    conflict: 'Same canonical file states both new formula (§14.1) and old Focus×3 (§5.2); spec and sim use struck formula; depletion rate -3 vs -1.',
    why_it_matters: 'Concentration drives the Spent penalty and the whole exchange economy. Different formula AND drain rate = materially different play.',
    suggested_fix: 'Propagate (3×Focus)+(2×Spirit) and one depletion rate to derived_stats §5.2, social_contest §4/§8, contest_extensions PP-NEW-D, and the sim.',
  },
  {
    id: 'C2-CHA-FOC-X3', severity: 'critical',
    title: 'Charisma-modifier / Focus-defence ×3 scaling applied in the summary but not in the resolution rules that compute strain',
    claim: 'The strain-computing resolution rules use unscaled Cha-mod 0-2 / Foc-defence 0-3, but the derived summary and canonical derived_stats scale them ×3 to 0-6 / 0-9. Strain = margin + Cha-mod − Foc-defence, so a Cha-6 winner contributes +2 or +6 depending on which section is read.',
    locations: [
      { file: 'designs/scene/social_contest_v30.md', section: '§4 CLASH', quote: 'Cha 1–3: +0; Cha 4–5: +1; Cha 6–7: +2' },
      { file: 'designs/scene/social_contest_v30.md', section: '§8', quote: 'max(0, floor((Cha − 3) ÷ 2)) × 3 | 0–6' },
      { file: 'designs/scene/derived_stats_v30.md', section: '§5.1', quote: 'Strain per exchange: rescaled ×3.' },
      { file: 'params/contest.md', section: 'Derived Values', quote: 'max(0, floor((Cha − 3) ÷ 2)) | 0–2' },
    ],
    canonical_position: 'derived_stats §5.1 mandates ×3 scaling (0-6 / 0-9). The §4 resolution rules and params §Derived are stale at unscaled 0-2 / 0-3.',
    conflict: 'The numbers used to compute strain (§4, params) are factor-of-3 smaller than the derived-summary/canonical values.',
    why_it_matters: 'A factor-of-3 swing on every strain calculation against a 3-21 Composure pool.',
    suggested_fix: 'Make §4 resolution rules and params §Derived state the ×3-scaled values consistent with derived_stats §5.1.',
  },
  {
    id: 'C3-SIM-FIDELITY', severity: 'critical',
    title: 'The sim implements only a fraction of the spec (CLASH-only, no strain, unused Concentration, fatigue over-applied, tie bug)',
    claim: 'sim/personal/contest.py treats every exchange as one margin-vs-resistance comparison (CLASH-only), implements no interaction types, strain/Composure/Rattled, genre/Recall/style dice, or Concentration depletion; over-applies Contest Fatigue on any Decisive win; and always moves ties toward side A.',
    locations: [
      { file: 'sim/personal/contest.py', section: 'resolve_exchange', quote: 'movement = max(0, margin - resistance)' },
      { file: 'sim/personal/contest.py', section: 'build_argue_pool', quote: 'pool = (primary * 2) + history + (-1 * wounds) + fatigue_penalty' },
      { file: 'sim/personal/contest.py', section: 'tie branch', quote: 'movement = +1   # toward A by convention if no first-to-speak override' },
      { file: 'designs/scene/social_contest_v30.md', section: '§6', quote: 'Total Victory (Persuasion Track ≥ 9 or ≤ 1): losing primary orator gains Contest Fatigue' },
    ],
    canonical_position: 'Spec §4 defines CLASH/REINFORCE/CROSS/TIE; §6 ties Contest Fatigue to Total Victory only; §4 ties tie-movement to the first-to-speak holder; §14.4 Argue pool includes +3 and style.',
    conflict: 'Sim omits interaction types, strain, Concentration; applies Contest Fatigue on any Decisive win; hardcodes tie movement to A; likely drops +3 and style dice.',
    why_it_matters: 'Any balance/stress-test conclusion from this sim is invalid for the current ruleset.',
    suggested_fix: 'Bring the sim to the §4/§6/§14.4 spec or mark it explicitly as a reduced model and stop citing it as validation.',
  },
  {
    id: 'M1-RATTLED-CHANNEL', severity: 'major',
    title: 'Rattled still uses the reserved +Ob channel in the spec and in the canonical derived_stats §5.1',
    claim: 'Decision-B converted Rattled from +Ob to -1D, but +1 Ob per Rattled level still appears in social_contest §4/§6 and in canonical derived_stats §5.1, contradicting derived_stats §10.5 and the §4.1 channel-reservation rule.',
    locations: [
      { file: 'designs/scene/social_contest_v30.md', section: '§4', quote: 'All subsequent contest rolls: +1 Ob per Rattled level (cumulative)' },
      { file: 'designs/scene/derived_stats_v30.md', section: '§5.1', quote: 'Rattled: +1 Ob per Rattled level to all contest rolls (cumulative)' },
      { file: 'params/contest.md', section: 'Composure and Rattled', quote: 'Rattled converted from +Ob to −1D for channel consistency' },
      { file: 'designs/scene/derived_stats_v30.md', section: '§10.5', quote: 'Rattled to next exchange (contest, post-PP-716 −1D)' },
    ],
    canonical_position: 'Rattled = -1D to Pool per Decision-B (2026-05-15) / PP-716. Ob channel reserved for non-actor-state.',
    conflict: 'Spec and canonical derived_stats §5.1 still impose +Ob, violating the channel-reservation invariant.',
    why_it_matters: 'Channel-reservation is an engine-wide invariant; +Ob composes differently with TN than -1D, changing outcomes.',
    suggested_fix: 'Change Rattled to -1D in social_contest §4/§6 and derived_stats §5.1.',
  },
  {
    id: 'M2-RECALL-LINGER', severity: 'major',
    title: 'Recall removed from Concentration (ED-694) but still present in the Appraise pool and the coalition Concentration pool',
    claim: 'ED-694 removed Recall as a sustained-focus input, yet Recall still appears in the Appraise pool (params) and in the §9.2 coalition Concentration shared pool (sum of Focus + Recall) in both spec and params.',
    locations: [
      { file: 'designs/scene/social_contest_v30.md', section: '§8', quote: 'Recall removed — no conceptual link to sustained focus' },
      { file: 'params/contest.md', section: 'Pools', quote: 'Appraise | Attunement + Recall' },
      { file: 'designs/scene/social_contest_v30.md', section: '§9.2', quote: "sum of all coalition members' (Focus + Recall)" },
    ],
    canonical_position: "Recall's only contest role is the +2D citation bonus; it is removed from Concentration per ED-694.",
    conflict: 'Recall still inflates the Appraise pool (params) and the coalition Concentration pool (both docs).',
    why_it_matters: 'Both are pool-size inputs; leaving Recall in changes Appraise reliability and coalition stamina inconsistently.',
    suggested_fix: 'Resolve Appraise pool composition; strip Recall from the coalition Concentration pool to match ED-694.',
  },
  {
    id: 'M3-APPRAISE-POOL', severity: 'major',
    title: 'Appraise (exchange Step 1) pool and Ob are specified three different ways',
    claim: 'The Step-1 read is Attunement-only Ob 1 (spec), Attunement+Recall with Ob = opponent Charisma ÷ 2 (params Pools), and Attunement Ob 1 under the name "Read" (params Exchange Structure).',
    locations: [
      { file: 'designs/scene/social_contest_v30.md', section: '§4 Step 1', quote: 'Roll Attunement alone (no History), TN 7, Ob 1.' },
      { file: 'params/contest.md', section: 'Pools', quote: 'Ob = opponent Charisma ÷ 2 (round up), min 1' },
      { file: 'params/contest.md', section: 'Exchange Structure', quote: 'Read (Attunement, TN 7, Ob 1)' },
    ],
    canonical_position: 'Unresolved — needs one ruling on pool (Attunement vs Attunement+Recall) and Ob (fixed 1 vs opponent Cha÷2).',
    conflict: 'Three incompatible specs for the same roll within the corpus.',
    why_it_matters: 'Appraise gates the information the orator acts on each exchange; pool and Ob both matter.',
    suggested_fix: 'Pick one Appraise spec and propagate; reconcile with the Recall-removal finding.',
  },
  {
    id: 'M5-FIRST-TO-SPEAK', severity: 'major',
    title: 'First-to-speak resolved to ROLLED (ED-581) in the spec, but params still shows the deterministic version with an open question',
    claim: 'The spec resolved Exchange-1 first-to-speak to a rolled Attunement contest (ED-581), but params still says "higher Attunement acts last" and tags it with the open ED-138 question.',
    locations: [
      { file: 'designs/scene/social_contest_v30.md', section: '§5', quote: 'rolled first-to-speak aligns with combat initiative for cross-system consistency' },
      { file: 'params/contest.md', section: 'First to Speak', quote: '[ED-138: deterministic vs rolled?]' },
    ],
    canonical_position: 'Rolled (Attunement vs Attunement, TN 7, Ob 1) per ED-581; ED-138 is resolved.',
    conflict: 'Params shows the deterministic rule and treats ED-138 as open; the sim implements neither.',
    why_it_matters: 'Determines Exchange-1 information advantage and seeds the exchange-winner cascade.',
    suggested_fix: 'Update params First-to-Speak to the rolled rule and close ED-138.',
  },
  {
    id: 'M6-RESIST-EROSION', severity: 'major',
    title: 'Two unreconciled resistance-erosion mechanisms (ED-864 per-exchange vs ED-582 chain-Deadlock), plus a stale unresolved ED-295 block',
    claim: 'params ED-864 "Option D" erodes resistance every two exchanges in ALL contests; spec §6.3 ED-582 erodes resistance only in chain contests after two zero-movement exchanges. Neither references the other. params also still shows ED-295 as "User decision required" directly above its own resolved block.',
    locations: [
      { file: 'params/contest.md', section: 'P1 Findings Resolved (ED-864)', quote: 'Option D — audience resistance erodes per exchange' },
      { file: 'designs/scene/social_contest_v30.md', section: '§6.3', quote: 'Resistance stall-break (ED-582)' },
      { file: 'params/contest.md', section: 'P1 Findings Awaiting Resolution', quote: 'ED-295: Head-On movement stalls at median' },
    ],
    canonical_position: 'Unclear — the two erosion rules need explicit reconciliation (stack? is ED-582 subsumed by ED-864?).',
    conflict: 'Two resistance-erosion rules in different docs with no cross-reference; a contradictory ED-295 status persists in params.',
    why_it_matters: 'Resistance erosion governs whether long contests resolve; two competing rules can double-erode or disagree.',
    suggested_fix: 'State one resistance-erosion model in both docs; delete the stale "Awaiting Resolution" ED-295 block from params.',
  },
  {
    id: 'm1-TERMINOLOGY', severity: 'minor',
    title: 'Pervasive terminology drift between spec and params; "Coalition Push" undefined',
    claim: 'Spec and params use different names for the same concepts: CLASH/REINFORCE/CROSS vs Head-On/Echo Match/Cross-Time; Doubt Marker vs Suspicion Token; differing style/orientation/ethical-mode labels. "Coalition Push" is referenced in params but never defined in the Interaction Types table.',
    locations: [
      { file: 'designs/scene/social_contest_v30.md', section: '§4', quote: 'REINFORCE (same genre, same orientation):' },
      { file: 'params/contest.md', section: 'Interaction Types', quote: 'Echo Match | Same genre, same orientation' },
      { file: 'params/contest.md', section: 'ED-297', quote: 'Coalition Push produces ~5 movement/exchange' },
      { file: 'designs/scene/social_contest_v30.md', section: '§4', quote: 'Place a Doubt Marker on the opponent.' },
      { file: 'params/contest.md', section: 'Interaction Types', quote: 'place Suspicion Token on opponent' },
    ],
    canonical_position: 'No single naming authority; the system needs one canonical glossary.',
    conflict: 'Cross-document references break because the same mechanic has multiple names; "Coalition Push" has no definition.',
    why_it_matters: 'Harms usability and makes propagation error-prone; an undefined interaction type cited in balance findings is a latent gap.',
    suggested_fix: 'Adopt one term set in a glossary; define or rename Coalition Push to its REINFORCE/Echo-Match equivalent.',
  },
  {
    id: 'CM5R-PIETY-PERSUASION', severity: 'major',
    title: 'Contest resolution track is "Persuasion Track" in spec/params/sim but the canonical name (derived_stats §14.2/§11, npc_behavior) is "Piety Track"',
    claim: 'The track the Argue pool moves is called "Persuasion Track" (0-10, ≥7/≤3) in social_contest_v30, params/contest.md, and the sim, but the canonical derived_stats_v30 §14.2 lists only a "Piety Track" (0-10) and §11 enumerates the social contest components as "Argue pools, genre/orientation, Piety Track, interaction types"; npc_behavior_v30 also resolves contests on the Piety Track. The canonical name is Piety Track; "Persuasion Track" is the stale label. (This is the corrected direction of the refuted finding CM-5.)',
    locations: [
      { file: 'designs/scene/social_contest_v30.md', section: '§6', quote: 'Persuasion Track ≥ 7 = Side A wins' },
      { file: 'designs/scene/derived_stats_v30.md', section: '§11', quote: 'Social contest: Argue pools, genre/orientation, Piety Track, interaction types' },
      { file: 'designs/scene/derived_stats_v30.md', section: '§14.2', quote: 'Piety Track | 0–10 | Oscillating | Per character | Personal religious standing' },
      { file: 'designs/npcs/npc_behavior_v30.md', section: 'contest resolution', quote: 'Piety Track ≥ 7 or ≤ 3' },
    ],
    canonical_position: 'Piety Track is canonical per derived_stats §14.2/§11 (Decision-C taxonomy) and is used by npc_behavior; "Persuasion Track" in social_contest/params/sim is the stale label.',
    conflict: 'social_contest_v30, params/contest.md, and the sim name the resolution track "Persuasion Track" while the canonical taxonomy and npc_behavior call it "Piety Track".',
    why_it_matters: 'Two names for the single resolution track break cross-doc references between npc_behavior (Piety) and the contest spec (Persuasion); an engine reading both could treat them as separate tracks.',
    suggested_fix: 'Rename "Persuasion Track" to "Piety Track" in social_contest_v30, params/contest.md, and the sim to match derived_stats §14.2/§11.',
  },
]

const LENS_SCHEMA = {
  type: 'object',
  properties: {
    finding_id: { type: 'string' },
    lens: { type: 'string' },
    real: { type: 'boolean' },
    reasoning: { type: 'string' },
    evidence_quote: { type: 'string' },
    severity_assessment: { type: 'string', enum: ['critical', 'major', 'minor', 'cosmetic'] },
  },
  required: ['finding_id', 'lens', 'real', 'reasoning'],
}

const LENSES = [
  {
    key: 'literal',
    instruction: [
      'LITERAL-EVIDENCE LENS. Open the cited file(s) and locate each quoted string. Minor differences allowed: whitespace,',
      'markdown bold markers, and unicode-vs-ASCII equivalents (× vs x, − vs -, ÷ vs /, ≥ vs >=, ≤ vs <=). Set real=false only',
      'if a quote genuinely cannot be located near its cited section (fabricated/misattributed). Otherwise real=true. This lens',
      'checks ONLY that the evidence is real, not whether the contradiction matters.',
    ].join('\n'),
  },
  {
    key: 'context',
    instruction: [
      'CONTEXT LENS. Read the FULL surrounding section of each cited quote. Decide whether the claimed contradiction ACTUALLY',
      'HOLDS in context, or whether nearby text nullifies it - a strike-through, a deprecated/struck/superseded marker, an HTML',
      'comment that deletes it, a scope qualifier, or an except/exception clause. Set real=true only if the contradiction holds',
      'once context is read. Default to real=false if context dissolves the claim.',
    ].join('\n'),
  },
  {
    key: 'currency',
    instruction: [
      'CANONICAL-DIRECTION LENS. Using the canonical hierarchy (section-14 dated rulings, Decision-B, ED-902, PP-716), judge',
      'whether the finding correctly identifies which statement is CURRENT vs STALE. Set real=true if the canonical_position is',
      'correct, OR if this is a genuine unresolved contradiction with no clear canonical winner. Set real=false only if the',
      'finding misidentifies the canonical side (flags the CURRENT rule as the error).',
    ].join('\n'),
  },
]

function verifyPanel(f) {
  return parallel(LENSES.map((L) => () =>
    agent(
      'ADVERSARIAL VERIFICATION - ' + L.key + ' lens. A prior auditor reported this finding about the Valoria social contest subsystem. Apply your lens strictly and try to REFUTE it.\n' + CORPUS + '\n' + CANON_NOTE + '\n\n' + L.instruction + '\n\nFINDING (JSON):\n' + JSON.stringify(f, null, 2) + '\n\nReturn the lens schema. finding_id="' + f.id + '", lens="' + L.key + '".',
      { label: 'verify:' + f.id + ':' + L.key, phase: 'Verify', schema: LENS_SCHEMA, effort: 'high' },
    ).catch(() => null),
  )).then((votes) => {
    const valid = votes.filter(Boolean)
    const realVotes = valid.filter((v) => v.real).length
    return Object.assign({}, f, {
      votes: valid,
      real_votes: realVotes,
      total_votes: valid.length,
      confirmed: realVotes >= 2,
      panel_severities: valid.map((v) => v.severity_assessment).filter(Boolean),
    })
  })
}

const CHUNK = 2
phase('Verify')
const out = []
for (let i = 0; i < FINDINGS.length; i += CHUNK) {
  const slice = FINDINGS.slice(i, i + CHUNK)
  const res = await parallel(slice.map((f) => () => verifyPanel(f)))
  for (const r of res) { if (r) out.push(r) }
  log('verified ' + Math.min(i + CHUNK, FINDINGS.length) + '/' + FINDINGS.length)
}

const confirmed = out.filter((f) => f.confirmed)
const notConfirmed = out.filter((f) => !f.confirmed)
const countSev = (arr, s) => arr.filter((f) => f.severity === s).length

log('reverify complete: ' + confirmed.length + ' confirmed / ' + out.length + ' re-checked')

return {
  summary: {
    rechecked: out.length,
    confirmed: confirmed.length,
    not_confirmed: notConfirmed.length,
    confirmed_by_severity: {
      critical: countSev(confirmed, 'critical'),
      major: countSev(confirmed, 'major'),
      minor: countSev(confirmed, 'minor'),
      cosmetic: countSev(confirmed, 'cosmetic'),
    },
  },
  confirmed: confirmed.map((f) => ({ id: f.id, title: f.title, severity: f.severity, real_votes: f.real_votes, total_votes: f.total_votes, panel_severities: f.panel_severities })),
  not_confirmed: notConfirmed.map((f) => ({ id: f.id, title: f.title, real_votes: f.real_votes, total_votes: f.total_votes, votes: f.votes })),
}
