export const meta = {
  name: 'social-contest-audit-verify',
  description: 'Adversarial 3-lens verification of pre-computed social-contest audit findings, batched to avoid rate-limit bursts, plus a completeness-critic pass',
  phases: [
    { title: 'Verify', detail: 'each pre-computed finding checked by a 3-lens panel (literal quote / context holds / canonical direction); majority confirms. Batched in small waves.' },
    { title: 'Complete', detail: 'completeness critic reads the infill + legacy v2 and checks cross-ref existence; surfaces missed findings' },
    { title: 'VerifyExtra', detail: 'completeness findings run through the same 3-lens panel' },
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
].join('\n')

const CANON_NOTE = [
  'CANONICAL HIERARCHY (for deciding which side of a contradiction is current):',
  '  - derived_stats_v30.md section 14 carries the most recent DATED, Jordan-ratified rulings (ED-902 2026-06-04,',
  '    PP-716/PP-717, Decision-C 2026-05-15). Treat section 14 as source of truth for derived-value formulas.',
  '  - params/core.md defines the engine channel reservation: actor-STATE degradation (wounds, Rattled, Spent)',
  '    must be a -1D Pool penalty; the Ob channel is reserved for non-actor-state mechanics. (PP-716 / Decision-B.)',
  '  - params/contest.md sometimes reflects NEWER decisions than the spec (Decision-B Rattled to -1D) but is STALE',
  '    on others. social_contest_v30.md is the design spec but lags on several propagations. The sim may implement a',
  '    struck/older rule. A file labeled CANONICAL can still contradict ITSELF across sections.',
].join('\n')

// ---- pre-computed findings (from a full read of the corpus) ----
const FINDINGS = [
  {
    id: 'C1-CONCENTRATION', dimension: 'derived-values', severity: 'critical',
    title: 'Concentration has two live formulas and two depletion rates; the ED-902-struck Focus×3 survives in 4 places',
    claim: 'Canonical Concentration (ED-902, 2026-06-04) is (3×Focus)+(2×Spirit) range 5-35, but the struck Focus×3 (range 3-21) still appears in derived_stats §5.2, social_contest §4/§8, contest_extensions PP-NEW-D, and the sim; depletion rate is also -3/exchange in the spec vs -1/exchange in params.',
    locations: [
      { file: 'designs/scene/derived_stats_v30.md', section: '§12', quote: 'supersedes the Focus×3 interim (2026-06-04, Jordan, ED-902)' },
      { file: 'designs/scene/derived_stats_v30.md', section: '§5.2', quote: 'Depletion rate | −3 per exchange; −3 additional on exchange loss' },
      { file: 'designs/scene/social_contest_v30.md', section: '§4', quote: 'Concentration = Focus × 3. Range 3–21. Depletes by 3 per exchange' },
      { file: 'params/contest.md', section: 'Derived Values', quote: '(3 × Focus) + (2 × Spirit)' },
      { file: 'params/contest.md', section: 'Concentration and Spent', quote: 'Depletes −1/exchange, −1 additional on loss.' },
      { file: 'params/contest_extensions.md', section: 'PP-NEW-D', quote: 'Concentration maximum = Focus × 3' },
      { file: 'sim/personal/contest.py', section: 'L52', quote: 'CONCENTRATION_MULTIPLIER = 3' },
    ],
    canonical_position: '(3×Focus)+(2×Spirit), range 5-35 per derived_stats §14.1 / §12 ED-902 (2026-06-04). Focus×3 is explicitly STRUCK.',
    conflict: 'Same canonical file (derived_stats) states both §14.1 new formula and §5.2 old Focus×3; spec and sim use struck formula; depletion rate -3 vs -1.',
    why_it_matters: 'Concentration drives the Spent penalty and the entire exchange economy. Different formula AND different drain rate produce materially different play and balance.',
    suggested_fix: 'Propagate (3×Focus)+(2×Spirit) and a single depletion rate to derived_stats §5.2, social_contest §4/§8, contest_extensions PP-NEW-D, and the sim.',
  },
  {
    id: 'C2-CHA-FOC-X3', dimension: 'derived-values', severity: 'critical',
    title: 'Charisma-modifier / Focus-defence ×3 scaling applied in the summary but not in the resolution rules that compute strain',
    claim: 'The strain-computing resolution rules use unscaled Cha-mod 0-2 / Foc-defence 0-3, but the derived summary and canonical derived_stats scale them ×3 to 0-6 / 0-9. Strain = margin + Cha-mod − Foc-defence, so a Cha-6 winner contributes +2 or +6 depending on which section is read.',
    locations: [
      { file: 'designs/scene/social_contest_v30.md', section: '§4 CLASH', quote: 'Cha 1–3: +0; Cha 4–5: +1; Cha 6–7: +2' },
      { file: 'designs/scene/social_contest_v30.md', section: '§4 CLASH', quote: 'Foc 1: 0; Foc 2–3: 1; Foc 4–5: 2; Foc 6–7: 3' },
      { file: 'designs/scene/social_contest_v30.md', section: '§8', quote: 'max(0, floor((Cha − 3) ÷ 2)) × 3 | 0–6' },
      { file: 'designs/scene/derived_stats_v30.md', section: '§5.1', quote: 'Strain per exchange: rescaled ×3.' },
      { file: 'params/contest.md', section: 'Derived Values', quote: 'max(0, floor((Cha − 3) ÷ 2)) | 0–2' },
    ],
    canonical_position: 'derived_stats §5.1 (canonical) mandates ×3 scaling (0-6 / 0-9) to match Composure ×3. The §4 resolution rules and params §Derived are stale at the unscaled 0-2 / 0-3.',
    conflict: 'The numbers used to compute strain (§4, params) are factor-of-3 smaller than the derived-summary/canonical values.',
    why_it_matters: 'A factor-of-3 swing on every strain calculation against a 3-21 Composure pool. Either strain barely registers or it dominates, depending on which page the GM/engine reads.',
    suggested_fix: 'Make §4 resolution rules and params §Derived state the ×3-scaled values (0-6 / 0-9) consistent with derived_stats §5.1.',
  },
  {
    id: 'C3-SIM-FIDELITY', dimension: 'sim-fidelity', severity: 'critical',
    title: 'The sim implements only a fraction of the spec (CLASH-only, no strain, unused Concentration, fatigue over-applied, tie bug)',
    claim: 'sim/personal/contest.py treats every exchange as a single margin-vs-resistance comparison (CLASH-only), implements no interaction types, strain/Composure/Rattled, genre/Recall/style dice, or Concentration depletion; over-applies Contest Fatigue on any Decisive win; and always moves ties toward side A.',
    locations: [
      { file: 'sim/personal/contest.py', section: 'resolve_exchange', quote: 'movement = max(0, margin - resistance)' },
      { file: 'sim/personal/contest.py', section: 'build_argue_pool', quote: 'pool = (primary * 2) + history + (-1 * wounds) + fatigue_penalty' },
      { file: 'sim/personal/contest.py', section: 'tie branch', quote: 'movement = +1   # toward A by convention if no first-to-speak override' },
      { file: 'designs/scene/social_contest_v30.md', section: '§4', quote: 'CROSS (different genres):' },
      { file: 'designs/scene/social_contest_v30.md', section: '§6', quote: 'Total Victory (Persuasion Track ≥ 9 or ≤ 1): losing primary orator gains Contest Fatigue' },
    ],
    canonical_position: 'Spec §4 defines CLASH/REINFORCE/CROSS/TIE with distinct resolution; §6 ties Contest Fatigue to Total Victory only; §4 ties tie-movement to the first-to-speak holder; §14.4 Argue pool includes +3 and style.',
    conflict: 'Sim omits all interaction-type branching, strain, and Concentration; applies Contest Fatigue on any Decisive win; hardcodes tie movement to A; likely drops the +3 pool constant and style dice.',
    why_it_matters: 'Any balance or stress-test conclusion drawn from this sim is invalid for the current ruleset — it is not simulating the documented system.',
    suggested_fix: 'Either bring the sim up to the §4/§6/§14.4 spec or explicitly mark it as a reduced model and stop citing it as validation.',
  },
  {
    id: 'M1-RATTLED-CHANNEL', dimension: 'channel-discipline', severity: 'major',
    title: 'Rattled still uses the reserved +Ob channel in the spec and in the canonical derived_stats §5.1',
    claim: 'Decision-B converted Rattled from +Ob to -1D for channel consistency, but +1 Ob per Rattled level still appears in social_contest §4/§6 and in canonical derived_stats §5.1, contradicting derived_stats §10.5 and the §4.1 channel-reservation rule.',
    locations: [
      { file: 'designs/scene/social_contest_v30.md', section: '§4', quote: 'All subsequent contest rolls: +1 Ob per Rattled level (cumulative)' },
      { file: 'designs/scene/derived_stats_v30.md', section: '§5.1', quote: 'Rattled: +1 Ob per Rattled level to all contest rolls (cumulative)' },
      { file: 'params/contest.md', section: 'Composure and Rattled', quote: 'Rattled converted from +Ob to −1D for channel consistency' },
      { file: 'designs/scene/derived_stats_v30.md', section: '§10.5', quote: 'Rattled to next exchange (contest, post-PP-716 −1D)' },
    ],
    canonical_position: 'Rattled = -1D to Pool per Decision-B (2026-05-15) / PP-716. The Ob channel is reserved for non-actor-state mechanics.',
    conflict: 'Spec and the canonical derived_stats §5.1 still impose +Ob, violating the channel-reservation invariant and contradicting derived_stats §10.5.',
    why_it_matters: 'Channel-reservation is an engine-wide invariant (the recent combat-wound work enforced it). A +Ob Rattled penalty composes differently with TN than a -1D pool penalty, changing outcomes.',
    suggested_fix: 'Change Rattled to -1D in social_contest §4/§6 and derived_stats §5.1.',
  },
  {
    id: 'M2-RECALL-LINGER', dimension: 'stale-struck', severity: 'major',
    title: 'Recall removed from Concentration (ED-694) but still present in the Appraise pool and the coalition Concentration pool',
    claim: 'ED-694 removed Recall as a sustained-focus input, yet Recall still appears in the Appraise pool (params) and in the §9.2 coalition Concentration shared pool (sum of Focus + Recall) in both spec and params.',
    locations: [
      { file: 'designs/scene/social_contest_v30.md', section: '§8', quote: 'Recall removed — no conceptual link to sustained focus' },
      { file: 'params/contest.md', section: 'Pools', quote: 'Appraise | Attunement + Recall' },
      { file: 'designs/scene/social_contest_v30.md', section: '§9.2', quote: "sum of all coalition members' (Focus + Recall)" },
    ],
    canonical_position: "Recall's only contest role is the +2D citation bonus in Argue; it is removed from Concentration per ED-694.",
    conflict: 'Recall still inflates the Appraise pool (params) and the coalition Concentration pool (both docs).',
    why_it_matters: 'Both are pool-size inputs; leaving Recall in changes Appraise reliability and coalition stamina inconsistently with single-actor Concentration.',
    suggested_fix: 'Resolve whether Appraise is Attunement-only (spec) or Attunement+Recall (params); strip Recall from the coalition Concentration pool to match ED-694.',
  },
  {
    id: 'M3-APPRAISE-POOL', dimension: 'derived-values', severity: 'major',
    title: 'Appraise (exchange Step 1) pool and Ob are specified three different ways',
    claim: 'The Step-1 read is specified as Attunement-only Ob 1 (spec), Attunement+Recall with Ob = opponent Charisma ÷ 2 (params Pools), and Attunement Ob 1 under the name "Read" (params Exchange Structure).',
    locations: [
      { file: 'designs/scene/social_contest_v30.md', section: '§4 Step 1', quote: 'Roll Attunement alone (no History), TN 7, Ob 1.' },
      { file: 'params/contest.md', section: 'Pools', quote: 'Ob = opponent Charisma ÷ 2 (round up), min 1' },
      { file: 'params/contest.md', section: 'Exchange Structure', quote: 'Read (Attunement, TN 7, Ob 1)' },
    ],
    canonical_position: 'Unresolved — needs a single ruling on pool (Attunement vs Attunement+Recall) and Ob (fixed 1 vs opponent Cha÷2).',
    conflict: 'Three incompatible specs for the same roll within the corpus.',
    why_it_matters: 'Appraise gates the information the orator acts on each exchange; pool and Ob both materially affect the read.',
    suggested_fix: 'Pick one Appraise spec and propagate; reconcile with M2 (Recall removal).',
  },
  {
    id: 'M4-NIFLHEL-STRUCK', dimension: 'stale-struck', severity: 'major',
    title: 'Niflhel social content was STRUCK (ED-764) but still appears as live rules in the spec',
    claim: 'params records the Niflhel strike (ED-764 / CR-STRIKE-2026-04-19), but social_contest §9.7 still carries a Niflhel Social Toolkit and the §2 faction-boost table still lists a Niflhel row.',
    locations: [
      { file: 'params/contest.md', section: 'Faction Boosts comment', quote: 'STRUCK per CR-STRIKE-2026-04-19 / ED-764' },
      { file: 'designs/scene/social_contest_v30.md', section: '§9.7', quote: 'Niflhel cannot participate in Formal or Grand Contests.' },
      { file: 'designs/scene/social_contest_v30.md', section: '§2 boost table', quote: 'Niflhel | — | GM picks one | Either' },
    ],
    canonical_position: 'Niflhel social-contest content is struck per ED-764; replacement is settlement-level intelligence-broker NPCs.',
    conflict: 'Struck content still presented as live rules in the design spec.',
    why_it_matters: 'A GM reading the spec would apply struck rules; the strike never propagated from params to the spec.',
    suggested_fix: 'Remove §9.7 and the Niflhel boost row from social_contest_v30, or mark them struck with a pointer to the replacement.',
  },
  {
    id: 'M5-FIRST-TO-SPEAK', dimension: 'stale-struck', severity: 'major',
    title: 'First-to-speak resolved to ROLLED (ED-581) in the spec, but params still shows the deterministic version with an open question',
    claim: 'The spec resolved Exchange-1 first-to-speak to a rolled Attunement contest (ED-581), but params still says "higher Attunement acts last" and tags it with the open ED-138 question.',
    locations: [
      { file: 'designs/scene/social_contest_v30.md', section: '§5', quote: 'rolled first-to-speak aligns with combat initiative for cross-system consistency' },
      { file: 'params/contest.md', section: 'First to Speak', quote: '[ED-138: deterministic vs rolled?]' },
    ],
    canonical_position: 'Rolled (Attunement vs Attunement, TN 7, Ob 1) per ED-581; ED-138 is resolved.',
    conflict: 'Params shows the deterministic rule and treats ED-138 as open; the sim implements neither.',
    why_it_matters: 'Determines who has the information advantage in Exchange 1 and is the seed for the whole exchange-winner cascade.',
    suggested_fix: 'Update params First-to-Speak to the rolled rule and close ED-138.',
  },
  {
    id: 'M6-RESIST-EROSION', dimension: 'resolution-logic', severity: 'major',
    title: 'Two unreconciled resistance-erosion mechanisms (ED-864 per-exchange vs ED-582 chain-Deadlock), plus a stale unresolved ED-295 block',
    claim: 'params ED-864 "Option D" erodes resistance every two exchanges in ALL contests; spec §6.3 ED-582 erodes resistance only in chain contests after two zero-movement exchanges. Neither references the other. params also still shows ED-295 as "User decision required" directly above its own resolved block.',
    locations: [
      { file: 'params/contest.md', section: 'P1 Findings Resolved (ED-864)', quote: 'Option D — audience resistance erodes per exchange' },
      { file: 'designs/scene/social_contest_v30.md', section: '§6.3', quote: 'Resistance stall-break (ED-582)' },
      { file: 'params/contest.md', section: 'P1 Findings Awaiting Resolution', quote: 'ED-295: Head-On movement stalls at median' },
    ],
    canonical_position: 'Unclear — the two erosion rules need explicit reconciliation (do they stack? is ED-582 subsumed by ED-864?).',
    conflict: 'Two different resistance-erosion rules live in different docs with no cross-reference; a contradictory ED-295 status persists in params.',
    why_it_matters: 'Resistance erosion governs whether long contests resolve; two competing rules can double-erode or disagree on when a contest breaks.',
    suggested_fix: 'State one resistance-erosion model in both docs; delete the stale "Awaiting Resolution" ED-295 block from params.',
  },
  {
    id: 'm1-TERMINOLOGY', dimension: 'terminology', severity: 'minor',
    title: 'Pervasive terminology drift between spec and params (interaction types, marker, styles, orientation, step name, ethical modes); "Coalition Push" undefined',
    claim: 'Spec and params use different names for the same concepts: CLASH/REINFORCE/CROSS vs Head-On/Echo Match/Cross-Time; Doubt Marker vs Suspicion Token; differing style and orientation labels and faction ethical-mode labels. "Coalition Push" is referenced in params but never defined in the Interaction Types table.',
    locations: [
      { file: 'designs/scene/social_contest_v30.md', section: '§4', quote: 'REINFORCE (same genre, same orientation):' },
      { file: 'params/contest.md', section: 'Interaction Types', quote: 'Echo Match | Same genre, same orientation' },
      { file: 'params/contest.md', section: 'P1 Findings Resolved', quote: 'Coalition Push produces ~5 movement/exchange' },
      { file: 'designs/scene/social_contest_v30.md', section: '§4', quote: 'Place a Doubt Marker on the opponent.' },
      { file: 'params/contest.md', section: 'Interaction Types', quote: 'place Suspicion Token on opponent' },
    ],
    canonical_position: 'No single naming authority; the system needs one canonical glossary.',
    conflict: 'Cross-document references break because the same mechanic has multiple names; "Coalition Push" has no definition.',
    why_it_matters: 'Harms usability and makes propagation error-prone; an undefined interaction type cited in balance findings is a latent gap.',
    suggested_fix: 'Adopt one term set in a glossary; define or rename Coalition Push to its REINFORCE/Echo-Match equivalent.',
  },
  {
    id: 'm2-COMPOSURE6', dimension: 'stale-struck', severity: 'minor',
    title: 'Composure = "Charisma + 6" survives in the spec changelog while the body uses Charisma × 3',
    claim: 'The §12 "Resolved by this version" table still states Composure = Charisma + 6, contradicting the §6/§8 body and canonical Charisma × 3.',
    locations: [
      { file: 'designs/scene/social_contest_v30.md', section: '§12 Resolved table', quote: 'Composure = Charisma + 6. Parallels Health = Endurance + 6.' },
      { file: 'designs/scene/social_contest_v30.md', section: '§8', quote: 'Composure | Charisma × 3' },
    ],
    canonical_position: 'Composure = Charisma × 3 (derived_stats §5.1, §14.1; social_contest body).',
    conflict: 'Stale changelog entry contradicts the current formula in the same document.',
    why_it_matters: 'A reader consulting the changelog gets the wrong formula; low impact but a true intra-doc contradiction.',
    suggested_fix: 'Update the §12 changelog line to Charisma × 3 (or annotate it as superseded).',
  },
  {
    id: 'm3-STRUCTURAL', dimension: 'resolution-logic', severity: 'cosmetic',
    title: 'Structural defects in social_contest_v30: step-numbering gaps and out-of-order sections',
    claim: '§2 jumps from Step 5 to Step 7 (no Step 6); §4 has a "Step 2b" with no "Step 2"; §11 has steps 1, 2, 4 (no 3); §7.1 and §10.1 are physically placed after §12; unassigned patch IDs like "PP-NEW, ED-617" appear.',
    locations: [
      { file: 'designs/scene/social_contest_v30.md', section: '§2', quote: 'Step 7 — Record all above in the hidden GM ledger.' },
      { file: 'designs/scene/social_contest_v30.md', section: '§4', quote: 'Step 2b — Corroborate (optional):' },
      { file: 'designs/scene/social_contest_v30.md', section: '§3', quote: 'Grand Contest Recall (PP-NEW, ED-617):' },
    ],
    canonical_position: 'N/A — editorial/structural hygiene.',
    conflict: 'Numbering and ordering imply deleted/relocated content not cleaned up.',
    why_it_matters: 'Signals incomplete edits; low risk but erodes confidence the doc is current.',
    suggested_fix: 'Renumber steps, relocate §7.1/§10.1 into sequence, assign real patch IDs.',
  },
  {
    id: 'm4-PANEL-PROVISIONAL', dimension: 'cross-system', severity: 'minor',
    title: 'Panel adjudicator type is "not yet designed" yet "accepted as canonical"',
    claim: 'The §2 setup table marks Panel mechanics as not yet designed (ED-137, use Expert Judge provisionally), while §3 lists Panel as a canonical adjudicator type accepted per the 2026-04-26 audit.',
    locations: [
      { file: 'designs/scene/social_contest_v30.md', section: '§2', quote: 'panel mechanics not yet designed. Use Expert Judge as provisional.' },
      { file: 'designs/scene/social_contest_v30.md', section: '§3', quote: 'accepted as canonical per 2026-04-26 audit' },
    ],
    canonical_position: 'Panel is provisional (= Expert Judge) until designed; calling it "canonical" overstates it.',
    conflict: 'Same type is both "not yet designed" and "accepted as canonical."',
    why_it_matters: 'A GM may treat Panel as a fully specified type when only Expert-Judge fallback exists.',
    suggested_fix: 'Pick one framing — provisional-pending-design — in both §2 and §3.',
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
          id: { type: 'string' },
          title: { type: 'string' },
          severity: { type: 'string', enum: ['critical', 'major', 'minor', 'cosmetic'] },
          claim: { type: 'string' },
          locations: {
            type: 'array',
            items: {
              type: 'object',
              properties: { file: { type: 'string' }, section: { type: 'string' }, quote: { type: 'string' } },
              required: ['file', 'quote'],
            },
          },
          canonical_position: { type: 'string' },
          conflict: { type: 'string' },
          why_it_matters: { type: 'string' },
          suggested_fix: { type: 'string' },
        },
        required: ['id', 'title', 'severity', 'claim', 'locations', 'why_it_matters'],
      },
    },
  },
  required: ['dimension', 'findings'],
}

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
      'LITERAL-EVIDENCE LENS. Open the cited file(s) and locate each quoted string. Minor differences are allowed: whitespace,',
      'and unicode-vs-ASCII equivalents (× vs x, − vs -, ÷ vs /, ≥ vs >=, ≤ vs <=). Set real=false only if a quote genuinely',
      'cannot be located near its cited section (fabricated/misattributed). Set real=true if the evidence quotes exist as',
      'written. This lens checks ONLY that the evidence is real, not whether the contradiction matters.',
    ].join('\n'),
  },
  {
    key: 'context',
    instruction: [
      'CONTEXT LENS. Read the FULL surrounding section of each cited quote. Decide whether the claimed contradiction ACTUALLY',
      'HOLDS in context, or whether nearby text nullifies it - a strike-through, a "deprecated"/"struck"/"superseded"/"STRUCK"',
      'marker, an HTML comment that deletes it, a scope qualifier, or an "except/exception" clause. Set real=true only if the',
      'contradiction genuinely holds once context is read. Default to real=false if context dissolves the claim.',
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

function verifyPanel(f, phaseName) {
  return parallel(LENSES.map((L) => () =>
    agent(
      'ADVERSARIAL VERIFICATION - ' + L.key + ' lens. A prior auditor reported this finding about the Valoria social contest subsystem. Apply your lens strictly and try to REFUTE it.\n' + CORPUS + '\n' + CANON_NOTE + '\n\n' + L.instruction + '\n\nFINDING (JSON):\n' + JSON.stringify(f, null, 2) + '\n\nReturn the lens schema. finding_id="' + f.id + '", lens="' + L.key + '".',
      { label: 'verify:' + f.id + ':' + L.key, phase: phaseName, schema: LENS_SCHEMA, effort: 'high' },
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

// Verify in small sequential waves to avoid bursting the rate limiter.
const CHUNK = 3
phase('Verify')
const primary = []
for (let i = 0; i < FINDINGS.length; i += CHUNK) {
  const slice = FINDINGS.slice(i, i + CHUNK)
  const res = await parallel(slice.map((f) => () => verifyPanel(f, 'Verify')))
  for (const r of res) { if (r) primary.push(r) }
  log('verified ' + Math.min(i + CHUNK, FINDINGS.length) + '/' + FINDINGS.length)
}

const confirmedPrimary = primary.filter((f) => f.confirmed)

// Completeness critic (single agent, runs alone).
phase('Complete')
const criticContext = confirmedPrimary.map((f) => '- [' + f.id + '] ' + f.title).join('\n')
const critic = await agent(
  [
    'You are the COMPLETENESS CRITIC for an audit of the Valoria social contest subsystem.',
    CORPUS, CANON_NOTE, '',
    'CONFIRMED findings so far (do NOT repeat these):',
    criticContext || '(none)',
    '',
    'Find what was MISSED:',
    '  (1) Read designs/scene/social_contest_v30_infill.md AND designs/scene/social_contest_system_v2.md. Do they contradict',
    '      the v30 spec, restate a struck rule, or contain mechanics inconsistent with the canonical spec?',
    '  (2) Use Grep/Glob to VERIFY EXISTENCE of cross-referenced docs and cited sections: clock_registry_v30;',
    '      npc_behavior_v30 / npc_behavior_system_v1 sec 3.3 / 5.2 / 1.2; scale_transitions sec 4.3.2; generational_transition_v30;',
    '      player_agency sec 4.2 / 5.2; faction_layer sec 1; baralta_crown_claim sec 2; fieldwork_investigation sec 2.3.',
    '      Report any document/section that does not exist.',
    '  (3) Any contradiction CLASS not represented above.',
    'Return NEW findings only, ids prefixed "CM-". dimension="completeness". Ground every finding in a verbatim quote or a',
    'concrete file/section-not-found result from your own Grep/Glob.',
  ].join('\n'),
  { label: 'completeness-critic', phase: 'Complete', schema: FINDINGS_SCHEMA },
).catch(() => null)

phase('VerifyExtra')
const criticFindings = (critic && critic.findings) ? critic.findings : []
const extra = []
for (let i = 0; i < criticFindings.length; i += CHUNK) {
  const slice = criticFindings.slice(i, i + CHUNK)
  const res = await parallel(slice.map((f) => () => verifyPanel(f, 'VerifyExtra')))
  for (const r of res) { if (r) extra.push(r) }
}

const all = primary.concat(extra)
const confirmed = all.filter((f) => f.confirmed)
const notConfirmed = all.filter((f) => !f.confirmed)
const countSev = (arr, s) => arr.filter((f) => f.severity === s).length

log('audit complete: ' + confirmed.length + ' confirmed / ' + all.length + ' raised (' + extra.length + ' from critic)')

return {
  summary: {
    total_raised: all.length,
    confirmed: confirmed.length,
    not_confirmed: notConfirmed.length,
    completeness_additions_raised: extra.length,
    completeness_additions_confirmed: extra.filter((f) => f.confirmed).length,
    confirmed_by_severity: {
      critical: countSev(confirmed, 'critical'),
      major: countSev(confirmed, 'major'),
      minor: countSev(confirmed, 'minor'),
      cosmetic: countSev(confirmed, 'cosmetic'),
    },
  },
  confirmed: confirmed.map((f) => ({ id: f.id, title: f.title, severity: f.severity, real_votes: f.real_votes, total_votes: f.total_votes, claim: f.claim, locations: f.locations, canonical_position: f.canonical_position, suggested_fix: f.suggested_fix })),
  not_confirmed: notConfirmed.map((f) => ({ id: f.id, title: f.title, real_votes: f.real_votes, total_votes: f.total_votes, votes: f.votes })),
}
