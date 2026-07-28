export const meta = {
  name: 'social-contest-deliberation-critique',
  description: 'Critique the Valoria social contest system against the deliberation/politics-as-game research corpus (4 senses of game, Caillois families, commitment stores, mechanism design, the meta-game). One analyst per theoretical lens; each finding adversarially verified against the actual system files (checking whether claimed gaps are filled elsewhere).',
  phases: [
    { title: 'Critique', detail: '8 parallel analysts, one per theoretical lens, hold the system against the research and surface strengths + under/mis-configurations with verbatim quotes' },
    { title: 'Verify', detail: 'each finding adversarially re-checked: is the critique sound, and is the claimed gap actually unfilled across the whole corpus?' },
  ],
}

// ==== VALORIA WF HARNESS v1 — GENERATED FROM tools/wf_harness.js — DO NOT EDIT HERE ====
// Re-sync after editing the owner:  python tools/ci_wf_harness_check.py --fix
// Report-only by ruling (Jordan 2026-07-28): every signal records and the run CONTINUES.

// P3 · the closed set. A reason outside it is itself a defect, representable without throwing.
const H_STOP_REASONS = [
  'completed',                   // nothing fired
  'null_result',                 // P7: a lens/critic returned zero findings
  'critic_starved',              // a stage produced findings that no critic ever saw
  'disagreement_unadjudicated',  // P8: a dispute reached the return with no ruling
  'repetition',                  // P3: a round reproduced the previous round's finding set
  'round_cap',                   // P3: the loop hit its cap
  'invalid_signal',              // a caller passed a reason outside this set
]
// Reported stop_reason = the worst signal seen, ordered by how much it should make a READER
// distrust the run — not by the severity of any underlying finding.
const H_STOP_RANK = H_STOP_REASONS
const H_ROUND_CAP = 3

// P8 · closed vocabularies for a disagreement. Deliberately small; each value is a distinction
// this repo's critics actually draw (see the uphold/overturn/soften/sharpen funnel).
const H_DISPUTE_LAYERS = ['evidence', 'interpretation', 'severity', 'scope', 'method']
const H_ROOT_CAUSES = [
  'different-sources-read',     // agonist and critic opened different files
  'stale-canon',               // one side read a superseded head
  'ambiguous-spec',            // the doc genuinely admits both readings
  'severity-calibration',      // same facts, different weight
  'scope-boundary',            // in-lane vs out-of-lane, or in-scope vs out-of-scope
  'measurement-vs-assertion',  // one side measured, the other asserted
]

// The cross-lens identity of a finding (P7's rediscovery key, P3's repetition key).
// Bespoke: two lenses that independently hit one defect cite the SAME FILE and describe it in
// different words, usually a line or two apart — so the key is (first cited file path, line
// dropped) + the first content words of the claim. Line numbers are dropped on purpose; keeping
// them would split one rediscovered defect into N singletons, which is the failure this exists
// to prevent.
const H_STOPWORDS = ['the', 'a', 'an', 'is', 'are', 'was', 'were', 'and', 'or', 'but', 'of', 'to',
  'in', 'on', 'at', 'for', 'with', 'that', 'this', 'it', 'its', 'as', 'by', 'from', 'has', 'have',
  'not', 'no', 'be', 'been', 'does', 'do', 'never', 'only', 'any']

function hClaimText(f) {
  if (!f || typeof f !== 'object') return ''
  return String(f.claim || f.title || f.what || f.summary || '')
}

function hFirstFile(f) {
  if (!f || typeof f !== 'object') return ''
  // social-contest shape: locations[{file, quote}]
  if (Array.isArray(f.locations) && f.locations.length && f.locations[0] && f.locations[0].file) {
    return String(f.locations[0].file).split(':')[0].trim()
  }
  // combat / attribute shape: `evidence` is free-text "file:line" citations
  const src = String(f.evidence || f.surface || f.defining_surface || '')
  const m = src.match(/[A-Za-z0-9_./-]+\.(?:md|py|ya?ml|json|jsonl|gd|js|html)/)
  return m ? m[0] : ''
}

function hContentWords(f) {
  const seen = []
  for (const w of hClaimText(f).toLowerCase().replace(/[^a-z0-9\s]/g, ' ').split(/\s+/)) {
    if (w.length > 2 && H_STOPWORDS.indexOf(w) < 0 && seen.indexOf(w) < 0) seen.push(w)
  }
  return seen
}

// The EXACT key: same file, same claim wording. Used by the repetition breaker, where the question
// is "did this stage produce literally the same output again", so exactness is what is wanted.
function hFindingKey(f) {
  return (hFirstFile(f) || '?') + '#' + (hContentWords(f).slice(0, 6).join('-') || '?')
}

// The FUZZY match, used only by rediscovery. Two lenses that independently hit one defect describe
// it in different words — "dead geo coefficients are never consumed" and "the geo coefficients are
// dead, never consumed" are one finding. An exact key splits them into singletons and silently
// zeroes out the entire corroboration signal, which is worse than not computing it: the output
// still has a `rediscovery` column, it just always reads 1.
// So: same file, and one claim's content words substantially contained in the other's.
// Containment, not Jaccard — a thorough lens writes a longer sentence about the same defect, and
// Jaccard punishes exactly that. The absolute floor stops a two-word claim matching everything.
function hSameFinding(a, b) {
  if (hFirstFile(a) !== hFirstFile(b)) return false
  const wa = hContentWords(a), wb = hContentWords(b)
  if (!wa.length || !wb.length) return false
  const shared = wa.filter(w => wb.indexOf(w) >= 0).length
  const smaller = Math.min(wa.length, wb.length)
  if (smaller < 3) return shared === smaller && wa.length === wb.length
  return shared >= 3 && shared / smaller >= 0.6
}

// P3 · the run recorder. One per workflow; every stage reports through it.
function hRun(name) {
  const run = {
    name: name,
    rounds: 0,
    cap: H_ROUND_CAP,
    signals: [],          // append-only; nothing is ever removed (no-silent-disappearance)
    trace: [],            // the JSONL run trace, emitted by hSummary()
    disagreements: [],
    _lastRoundKeys: null,
  }

  run.trace_ = function (event, data) {
    run.trace.push(Object.assign({ seq: run.trace.length, event: event }, data || {}))
    return run
  }

  // NEVER throws. An unknown reason is recorded as 'invalid_signal' carrying what was asked for,
  // because a harness that crashes the run it is policing is worse than the drift it detects.
  run.signal = function (reason, detail) {
    const known = H_STOP_REASONS.indexOf(reason) >= 0 && reason !== 'completed'
    const rec = { reason: known ? reason : 'invalid_signal', detail: String(detail || ''), round: run.rounds }
    if (!known) rec.requested = String(reason)
    run.signals.push(rec)
    run.trace_('signal', rec)
    log('[harness] ' + rec.reason + ': ' + rec.detail)
    return run
  }

  // Round accounting + the repetition breaker. Report-only: past the cap it still returns true
  // and the caller decides; the SIGNAL is the deliverable, not a forced exit.
  run.round = function (label, findings) {
    run.rounds += 1
    const keys = Array.isArray(findings) ? findings.map(hFindingKey).sort() : null
    run.trace_('round', { label: String(label || ''), n: run.rounds, findings: keys ? keys.length : 0 })
    if (run.rounds > run.cap) {
      run.signal('round_cap', 'round ' + run.rounds + ' exceeds cap ' + run.cap + ' (' + label + ')')
    }
    if (keys && run._lastRoundKeys && keys.length && keys.join('|') === run._lastRoundKeys.join('|')) {
      run.signal('repetition', 'round ' + run.rounds + ' (' + label + ') reproduced the previous round\'s '
        + keys.length + ' finding(s) with no change — further rounds are unlikely to add anything')
    }
    if (keys) run._lastRoundKeys = keys
    return run
  }

  // P7a · the null-result alarm. Ships with hRediscover (P7b) and is meaningless without it:
  // an alarm for "you found nothing" with no way to see WHICH findings were corroborated is
  // pressure to manufacture findings. Both are called in every script; the checker enforces it.
  run.lens = function (lensKey, findings) {
    const n = Array.isArray(findings) ? findings.length : 0
    run.trace_('lens', { lens: String(lensKey), findings: n })
    if (n === 0) {
      run.signal('null_result', 'lens/stage "' + lensKey + '" returned zero findings — either the '
        + 'surface is genuinely clean, or the agent failed to read it. Check its coverage notes '
        + 'before crediting the silence.')
    }
    return findings || []
  }

  // A stage produced findings that no critic ever saw. The relay is the method (CLAUDE.md §10);
  // an unrefuted finding is a draft, not a result.
  run.critiqued = function (stage, produced, reviewed) {
    run.trace_('critique-coverage', { stage: String(stage), produced: produced, reviewed: reviewed })
    if (produced > 0 && reviewed < produced) {
      run.signal('critic_starved', stage + ': ' + reviewed + '/' + produced + ' finding(s) reached a '
        + 'critic; ' + (produced - reviewed) + ' returned unrefuted')
    }
    return run
  }

  // P8 · a disagreement record. `adjudication` starts empty ON PURPOSE — hSummary() signals if
  // it is still empty at the return, which is the no-silent-disappearance rule.
  run.dispute = function (rec) {
    const d = {
      finding_id: String((rec && rec.finding_id) || '?'),
      layer_disputed: H_DISPUTE_LAYERS.indexOf(rec && rec.layer_disputed) >= 0 ? rec.layer_disputed : 'interpretation',
      positions: (rec && rec.positions) || [],
      root_cause: H_ROOT_CAUSES.indexOf(rec && rec.root_cause) >= 0 ? rec.root_cause : 'ambiguous-spec',
      resolution_model: (rec && rec.resolution_model) || 'adjudicated-by-synthesis',
      cross_domain: !!(rec && rec.cross_domain),
      adjudication: '',
      status: 'open',
    }
    // CROSS-DOMAIN OBSERVATION, NOT JUDGMENT: a critic reaching outside its own lens/lane may
    // report what it saw but may not rule on it. Encoded, not merely asked for — the record
    // cannot leave this branch in a state that a later ruling would silently overwrite.
    if (d.cross_domain) {
      d.status = 'observation'
      d.resolution_model = 'observation-only (out-of-lens: report, do not rule)'
    }
    run.disagreements.push(d)
    run.trace_('dispute', { finding_id: d.finding_id, layer: d.layer_disputed, root_cause: d.root_cause, cross_domain: d.cross_domain })
    return d
  }

  run.adjudicate = function (findingId, ruling, by) {
    let n = 0
    for (const d of run.disagreements) {
      if (d.finding_id !== String(findingId) || d.status === 'observation') continue
      d.adjudication = String(ruling || '')
      d.adjudicated_by = String(by || 'synthesis')
      d.status = d.adjudication ? 'resolved' : 'open'
      n += d.status === 'resolved' ? 1 : 0
    }
    run.trace_('adjudicate', { finding_id: String(findingId), resolved: n })
    return n
  }

  run.summary = function () {
    const unadj = run.disagreements.filter(d => d.status === 'open')
    if (unadj.length) {
      run.signal('disagreement_unadjudicated', unadj.length + ' dispute(s) reached the return with no '
        + 'ruling: ' + unadj.map(d => d.finding_id).join(', '))
    }
    let worst = 'completed'
    for (const s of run.signals) {
      if (H_STOP_RANK.indexOf(s.reason) > H_STOP_RANK.indexOf(worst)) worst = s.reason
    }
    return {
      run: run.name,
      stop_reason: worst,
      degraded: worst !== 'completed',
      rounds: run.rounds,
      round_cap: run.cap,
      signals: run.signals,
      disagreements: run.disagreements,
      unadjudicated: unadj.map(d => d.finding_id),
      trace_jsonl: run.trace.map(t => JSON.stringify(t)).join('\n'),
    }
  }

  return run
}

// P7b · rank by INDEPENDENT REDISCOVERY. Practice 7 (one agent per lens) already produces this
// signal and every script threw it away. A defect three unrelated lenses hit independently is
// worth more than one a single lens hit hard, and this is the only cheap corroboration signal a
// read-only audit has. `lensOf` extracts the lens/cluster key so a lens cannot corroborate itself.
function hRediscover(findings, lensOf) {
  const groups = []
  for (const f of (findings || [])) {
    if (!f) continue
    const lens = String((lensOf && lensOf(f)) || f.lens || f.cluster || f.module || '?')
    let g = null
    for (const cand of groups) {
      if (hSameFinding(cand.findings[0], f)) { g = cand; break }
    }
    if (!g) { g = { key: hFindingKey(f), lenses: [], findings: [] }; groups.push(g) }
    if (g.lenses.indexOf(lens) < 0) g.lenses.push(lens)
    g.findings.push(f)
  }
  return groups
    .map(g => ({ key: g.key, rediscovery: g.lenses.length, lenses: g.lenses, findings: g.findings }))
    .sort((a, b) => b.rediscovery - a.rediscovery || a.key.localeCompare(b.key))
}

// P4 · the read-only critic. Independence is STRUCTURAL, not a sentence in a prompt: the
// agentType below is defined in .claude/agents/valoria-critic.md with a tools list that has no
// Write/Edit. Passing it is the whole mechanism — a critic stage that omits it can write, and
// tools/ci_wf_harness_check.py fails the script that does.
const H_CRITIC = { agentType: 'valoria-critic' }
function hCritic(opts) { return Object.assign({}, opts || {}, H_CRITIC) }
// ==== END VALORIA WF HARNESS v1 ====

const run = hRun('social-contest-deliberation-critique')

const CORPUS = [
  'VALORIA SOCIAL CONTEST CORPUS. All paths below are REPO-RELATIVE to the checkout root; resolve them there, not against any absolute machine path. Read what your lens needs:',
  '  PRIMARY (the system under critique):',
  '  systems/social_contest/social_contest_v30.md          - main spec, sections 1-12 (setup, exchange, resolution, asymmetric, BG, hybrid, obligations, succession, heresy).',
  '  systems/social_contest/social_contest_v30_infill.md   - prose/rationale infill.',
  '  engine/params/contest.md                            - formulas, tables, patch log.',
  '  engine/params/contest_extensions.md                 - Resonant Style targeting, Evidence Findings, temporal-axis, etc.',
  '  systems/social_contest/sim/contest/          - Python sim of the contest pipeline, now a PACKAGE — the single-file sim/personal/contest.py older notes cite no longer exists: resolver.py, rhetoric.py, appraise.py, armature.py, modes.py, policy.py, primitives.py, contract.py, faction.py, narrative.py, dictionaries.py, wrapper.py, agon_harness.py.',
  '  ADJACENT (the systems the contest plugs into - GREP THESE before claiming a gap is unfilled):',
  '  systems/npcs/npc_behavior_v30.md             - Stance Triangle, Conviction, Resonant Style taxonomy (S1.3), Conviction Scars (S3.3/3.4), arcs.',
  '  systems/characters/conviction_taxonomy_v30.md  - the 13-Conviction / 4-axis matrix (the interpretation primitive).',
  '  systems/fieldwork/knots_v30.md                - Knot/Disposition (-5..+5) relational substrate.',
  '  systems/_architecture/*                        - key_substrate, scale_transitions, complete_systems_reference (the Key bus, armature dot-product).',
  '  references/module_contracts.yaml             - module boundaries, resolver classes.',
  '  audit/2026-06-28-distillation-coherence/distillation_coherence_report.md - recent engine audit: "two primitives" (sigma resolver + armature dot-product), the contest IS the sigma kernel.',
].join('\n')

const PHILOSOPHY = [
  'DESIGN PHILOSOPHY (the standard to judge against - this is what "well-configured" means here):',
  '  - GRANULAR, BOTTOM-UP EMERGENT with TOP-DOWN VALIDATION. Macro outcomes (who wins, who governs,',
  '    what becomes binding) should EMERGE from granular per-move substrate, validated by a top-down constraint',
  '    (the adjudicator / persuasion track / obligation). Hard-coded macro outcomes are a smell.',
  '  - WORLD/PLAYER CHURN AXIOM: every decision must generate churn that seeds emergent narrative. SUSPECT any',
  '    inert or unreachable mechanic. A procedure whose FAILURE MODES generate story (capture, holdout, the',
  '    antechamber maneuver) is high-value churn, not a bug.',
  '  - ENGINE DISCIPLINE: there are two universal primitives - the SIGMA RESOLVER (will+advantage -> outcome) and',
  '    the ARMATURE DOT-PRODUCT (event -> meaning-for-an-observer, over a 13-Conviction x 4-axis matrix). A good',
  '    improvement REUSES these primitives and the Key bus; it does not bolt on a parallel subsystem.',
  '  Judge the contest as a DELIBERATIVE GAME in the rigorous sense, not just for internal consistency.',
].join('\n')

const METHOD = [
  'METHOD:',
  '  For your lens, do THREE things, honestly:',
  '   (1) CREDIT what the system already gets right against the research (cite it - strengths keep the critique honest).',
  '   (2) Find UNDER-CONFIGURATION (the research shows a richer design space the system has collapsed or omitted).',
  '   (3) Find MIS-CONFIGURATION (the system is configured in a way that FIGHTS the philosophy above - e.g. hard-codes',
  '       what should emerge, or suppresses churn the research says is the point).',
  '  EVIDENCE RULE: every claim about the system MUST carry a SHORT VERBATIM QUOTE you actually read from a named file.',
  '  Before asserting "X is missing", GREP THE ADJACENT FILES - the corpus is large and a mechanic may live in',
  '  npc_behavior / conviction_taxonomy / knots / faction docs. If it exists elsewhere, say so and downgrade to a',
  '  seam/integration finding rather than an absence.',
  '  Every improvement must be CONCRETE and reuse the engine primitives (sigma resolver, armature dot-product, Key bus,',
  '  the existing track/clock/pool buckets) where possible. No "add a whole new subsystem" hand-waving.',
].join('\n')

const LENSES = [
  {
    key: 'four-games',
    title: 'One track for four different games',
    brief: [
      'RESEARCH: The deliberation synthesis (Part 0) shows "game" is FOUR non-coextensive senses: Wittgensteinian',
      '(rule-constituted), Suitsian (voluntary inefficient obstacles), AGONISTIC (zero-sum contest with a victor),',
      'and GAME-THEORETIC (strategic interdependence, often MIXED-MOTIVE / positive-sum). Its deepest finding (Part VI.2-3,',
      'pragma-dialectics): the healthiest deliberation is resolution-ON-THE-MERITS, and "trying to win at all costs" is the',
      'very disposition that PRODUCES fallacies; eristic (pure contest) is the DEGENERATE type. The politics companion (Part D.4)',
      'sharpens it: the one word "game" quietly holds together FOUR different things a procedure can do - PRODUCE A WINNER,',
      'STRIKE A BARGAIN (positive-sum), DISCERN A TRUTH, or ENACT A UNITY - and the interesting questions live in the gaps.',
      '',
      'CRITIQUE TASK: The Valoria contest resolves almost everything on ONE bidirectional zero-sum Persuasion Track (0-10,',
      'Side A wins >=7 / Side B wins <=3, strain-as-damage, Composure-as-hit-points). Examine whether this collapses the four',
      'games into one agonistic bar. Look hard at: the Compromise zone (4-6) - is it a genuine positive-sum BARGAIN or just a',
      '"nobody won" default? (note S12 explicitly DEFERS "Negotiation compromise resolution (ZOPA-style)... structurally',
      'different from Persuasion Track, not designed"). Does anything reward resolution-on-the-merits vs win-at-all-costs?',
      'Is "discern a truth" (inquiry) modeled at all, or only persuasion/victory? Assess whether the single-track design is the',
      'right unification or a flattening that destroys churn the four-way distinction would generate.',
    ].join('\n'),
  },
  {
    key: 'commitment-store',
    title: 'No commitment store - hit-points, not concessions',
    brief: [
      'RESEARCH: The deepest, least-disputable correspondence (deliberation Part II.B-D, Part V.5): real argument is a',
      'MOVE-AND-COMMITMENT structure with a COMMITMENT STORE (Hamblin) - a running ledger of the propositions each party has',
      'conceded, which legal moves (assert, question, challenge, concede, justify) ALTER. Walton-Krabbe build six dialogue types',
      'on it; Dutilh Novaes shows even solitary deduction is an internalized Prover-Skeptic exchange. Validity/truth are DEFINED',
      'as having a winning STRATEGY over this structure. The commitment store is the granular substrate from which argumentative',
      'macro-structure emerges - i.e. it is the BOTTOM-UP substrate this project says it wants.',
      '',
      'CRITIQUE TASK: Does the Valoria contest have any commitment store? Examine what actually persists across exchanges: the',
      'Persuasion Track (a scalar), Doubt Markers (one transient -2), Recall "+2D when citing a specific named verifiable claim"',
      '(binary, per-exchange/per-source), Concentration, strain. Argument CONTENT (genre/orientation/style) buys dice bonuses but',
      'is there any persistent LEDGER of what each side has conceded or committed to, that constrains later moves? Is a contest a',
      'sequence of dice-margin attacks on a hit-point bar, or a structured exchange of commitments? Assess this as the single',
      'biggest bottom-up-substrate question. If a partial ledger exists (Obligations are post-contest; Beliefs/Convictions are',
      'NPC-side), say precisely how far it falls short of an IN-CONTEST commitment store. Propose how a commitment store could be',
      'a track/clock substrate the sigma resolver reads (reusing the engine), not a bolt-on.',
    ].join('\n'),
  },
  {
    key: 'caillois-families',
    title: 'One Caillois family (pure agon) - no alea / mimicry / ilinx',
    brief: [
      'RESEARCH: The politics companion classifies decision-procedures by Caillois\'s four families - AGON (regulated merit',
      'contest), ALEA (chance/lot), MIMICRY (performed legitimacy - acclamation, quasi-inspiration, sovereignty-as-performance),',
      'ILINX (the crowd-roar, charismatic/sacral charge). Pre-1600 polities mixed them: sortition (alea) to KILL FACTION by',
      'removing the prize; acclamation/quasi-inspiration (mimicry) as a real resolution mode (canonical Church election had THREE',
      'modes: scrutiny=agon, compromise=delegated agon, quasi-inspiration=mimicry); the Venetian doge = engineered ALEA+AGON',
      'hybrid to defeat capture. Succession was alea (primogeniture), agon (tanistry/kurultai), OR mimicry (acclamation).',
      '',
      'CRITIQUE TASK: The Valoria contest appears to be PURE AGON (dice-pool merit contest -> victor). Verify across the corpus',
      '(GREP for sortition/lot/acclamation/random) whether ANY non-agon resolution family exists. In particular: the Succession',
      'Contest (S7.2) uses Grand Contest infrastructure = pure agon, where history/theory show succession is often alea or mimicry.',
      'Is there any lot/sortition mechanic anywhere (an anti-capture, anti-faction device)? Any acclamation/quasi-inspiration',
      'resolution? Is ilinx (crowd affect) present beyond Charisma-as-pool? Assess whether having ONE resolution family where the',
      'research shows at least four - each generating DIFFERENT churn - is an under-configuration. Propose concrete additions that',
      'reuse the engine (e.g. an alea-hybrid succession; acclamation as a mimicry resolution mode).',
    ].join('\n'),
  },
  {
    key: 'contest-locus-and-type3',
    title: 'Where the contest sits + missing Type-3 pathology churn',
    brief: [
      'RESEARCH: The politics companion (Part D.1) - the load-bearing distinction is WHERE THE COMPETITION SITS relative to the',
      'decision: TYPE 1 (the contest IS the deciding: council/assembly/combat/adjudication), TYPE 2 (selects WHO decides:',
      'election, succession, degenerate-fiat), TYPE 3 (REMOVES competition by design: sortition, consensus). The crucial finding:',
      'Type-3 procedures generate their characteristic PATHOLOGY - the abolished competition RE-EMERGES (the consensus holdout/veto;',
      'the captured lottery pool; the liberum veto paralyzing the state). That re-emergence IS emergent narrative. Constitutions',
      'build "anti-gaming" antibodies (the Iroquois anti-frivolous-objection rule; Venetian anti-bribery oaths) precisely because',
      'they know the procedure can be gamed.',
      '',
      'CRITIQUE TASK: Map Valoria\'s contest types onto Type 1/2/3. It clearly has Type 1 (Formal/Grand Contest) and a Type 2',
      '(Succession Contest, election-by-electors-style). Does it have ANY Type 3 (consensus/unanimity, or sortition)? More important',
      'for the churn axiom: does the system model PROCEDURAL PATHOLOGY as a story engine - the holdout, the deadlock-gamed-for-leverage,',
      'the captured pool? It has Deadlock/Chain rules (S6.3) and Stays - assess whether these EXHAUST the design (they look like',
      'TERMINATORS that resolve stalls, the opposite of treating the pathology as generative churn). Connect directly to the churn',
      'axiom: the richest churn is a procedure whose failure mode seeds the next arc, and Valoria may be configured to suppress',
      'exactly that. Propose Type-3 procedures and pathology-as-churn hooks.',
    ].join('\n'),
  },
  {
    key: 'meta-game-capture',
    title: 'The meta-game: procedure capture, robust action, the broglio, the antechamber',
    brief: [
      'RESEARCH (the richest churn lens): The machination + testing companions show the CENTRAL empirical finding of the whole',
      'corpus - the SAME procedural materials produce wildly different outcomes by MECHANISM DESIGN and by CAPTURE. The Medici did',
      'NOT abolish Florence\'s lottery; they CAPTURED it (loaded the pool via accoppiatori/Borsellino, bypassed the draw "a mano").',
      'Cosimo won by ROBUST ACTION + MULTIVOCALITY (noncommittal moves preserving his options while narrowing opponents\'; one',
      'action legible from many angles). Venice did not eliminate maneuver; it CHANNELED it - the broglio: electioneering on the',
      'stairways, "big fish eat the smaller", the Signoria "helpless to stop the lobbying". Fiat DISPLACES contest to the',
      'ANTECHAMBER ("the most absolutist polities generate the most baroque court politics"). And politics Part D.4 + Hart\'s rule',
      'of recognition: the deepest political act is CHOOSING WHICH GAME legitimates power - a META-GAME.',
      '',
      'CRITIQUE TASK: Valoria\'s contest treats THE RULES AS FIXED AND FAIR - the GM sets adjudicator type, exchange count,',
      'resistance, faction boost at setup (S2), and play happens inside fixed rules. Examine: (a) Can a faction CAPTURE the',
      'procedure itself - load the pool, capture the adjudicator, choose the venue/adjudicator-type to its advantage? (BG Lobbying',
      'and the Lobby Cap S10/PP-256 are the closest - assess whether they model capture or just a +/-2 nudge.) (b) Is there any',
      'ROBUST-ACTION / multivocality lever (committing-legibly vs staying-ambiguous as a strategic choice)? (c) Is there an',
      'ANTECHAMBER / broglio layer - off-table maneuver, vote-soliciting, the channeled-not-eliminated game - or does all social',
      'conflict route through the formal contest? (d) Is the CHOICE OF PROCEDURE a player-facing, contestable, churn-generating',
      'lever, or hard-coded at GM setup? This is likely the highest-leverage region for improvement given the churn axiom. Propose',
      'concrete capture/robust-action/antechamber mechanics that reuse faction state, Disposition, and the Key bus.',
    ].join('\n'),
  },
  {
    key: 'adjudicator-armature',
    title: 'Adjudicator as a resistance scalar, not an armature/agent',
    brief: [
      'RESEARCH: The adjudicator is the firmest cross-domain correspondence (deliberation Part III.D, V.8): an impartial',
      'rule-applier who DECLARES the outcome - and Aristotle (Part I.G) grounds the three oratory genera in three KINDS of judge',
      '(juror of the past, juror of the future, spectator who judges the speaker). Competitive debate\'s tabula-rasa paradigm: judge',
      'decides solely on arguments made in the round. Politics model 9: the count was construed as DISCERNING the sanior et maior',
      'pars ("sounder and greater part"), and the LOSER could claim to BE the sounder part - discernment-language weaponized inside',
      'the dispute. I.e. the adjudicator is an AGENT with a standard the arguments must satisfy, not a number.',
      '',
      'CRITIQUE TASK: Valoria\'s adjudicator types (Expert Judge/Crowd/No-adjudicator/Panel, S2-S3) cleverly select the PRIMARY',
      'ATTRIBUTE (Cognition/Charisma/Attunement) - CREDIT this, it maps Aristotle\'s three judges well. BUT examine: beyond picking',
      'the attribute and contributing a "resistance" number (avg faction Stability -1) and a single faction "boost", does the',
      'adjudicator DELIBERATE? Does it have its own armature/convictions the argument must satisfy (the engine HAS a 13-Conviction',
      'x 4-axis armature dot-product - is the adjudicator one)? Is "Panel" still undesigned (ED-137)? Is there any sanior-pars',
      'dynamic (a losing side contesting the legitimacy of the verdict)? Assess whether the adjudicator is under-configured as a',
      'flat resistance scalar when the engine already has the primitive to make adjudication EMERGENT (argument symbolic-dimensions',
      'dot-producted against the adjudicator armature). Propose reusing the armature dot-product for adjudication.',
    ].join('\n'),
  },
  {
    key: 'fallacies-as-fouls',
    title: 'No fallacies-as-fouls, no dialectical shift, no good-faith/eristic distinction',
    brief: [
      'RESEARCH: Pragma-dialectics (deliberation Part II.C, V.10) defines a fallacy AS the violation of a discussion rule - a FOUL,',
      'an illegitimate move penalized within the game; the ten rules function as constitutive rules. Walton-Krabbe: a DIALECTICAL',
      'SHIFT (the exchange changing type mid-stream - a negotiation move smuggled into an inquiry) is productive when noticed and a',
      'source of fallacy/bad-faith when not. And the cooperative/competitive fault line (Part VI.2): the activity is healthiest when',
      'participants treat it LEAST as a contest to win; eristic is the degenerate type.',
      '',
      'CRITIQUE TASK: Valoria penalizes PHYSICAL fouls (S9.6 Chamber Violence = immediate forfeit) - CREDIT that. But examine',
      'whether there is any ARGUMENTATIVE foul system: a penalty for an illegitimate argumentative move, a bad-faith genre/style',
      'switch, an unmarked dialectical shift, eristic for its own sake. Is there any mechanic distinguishing good-faith',
      'resolution-seeking from win-at-all-costs? (Note the "Obscuring" orientation and "Suppression/Insinuation" styles - are these',
      'modeled as legitimate-but-shady tactics with consequences, or just neutral dice options?) The Adjudicator Thread Response',
      'table (S9.4b) penalizes one specific foul (illicit Thread use) - assess whether that is the ONLY foul concept and whether a',
      'general fouls-as-fouls layer is missing. Connect to churn: a foul caught/uncaught is a story. Propose a foul mechanic reusing',
      'the adjudicator and Doubt-Marker machinery.',
    ].join('\n'),
  },
  {
    key: 'mixed-motive-bargain',
    title: 'Mixed-motive bargaining, two-level games, and escalation between modes',
    brief: [
      'RESEARCH: Negotiation (deliberation Part IV) is the strictest game-theoretic game AND precisely NOT a zero-sum contest -',
      'it is MIXED-MOTIVE (parties cooperate to create the surplus, compete over its division: integrative vs distributive,',
      'Walton-McKersie; Nash bargain; ZOPA). Putnam\'s TWO-LEVEL game: a negotiator plays two boards at once (the table + domestic',
      'ratification), bound by a WIN-SET; a move strengthening one table can lose the other. Parliaments (politics model 8) are',
      'SUPPLY-FOR-REDRESS bargains, not pure contests. Litigation (deliberation III.E, Priest-Klein): cases SELECT for trial',
      'precisely when closest - i.e. a good system should route lopsided disputes AWAY from full contest.',
      '',
      'CRITIQUE TASK: Examine Valoria\'s treatment of bargaining. S12 explicitly DEFERS "Negotiation compromise resolution',
      '(ZOPA-style)" AND "Escalation between social modes (negotiation->debate->appeal)". The BG Parliamentary Vote (S10) and Hybrid',
      '(S11) and "Private Negotiation" proceeding type all still resolve on the same zero-sum Persuasion Track. Is parliament modeled',
      'as a supply-for-redress BARGAIN (each side can gain) or as a vote-contest (one side wins)? Is the Lead orator in a coalition',
      'mechanically ANSWERABLE to a faction win-set (Putnam two-level), or is the coalition just a shared dice/Concentration pool',
      '(S9.2)? Is there a "this dispute is too lopsided for a full contest" gate (Priest-Klein selection)? Note S1: "GMs should not',
      'call for a contest when one side has no plausible case" - is that the only selection mechanism? Assess the mixed-motive gap',
      'and propose a ZOPA/win-set treatment that reuses Disposition/faction-stat deltas as the bargaining payoffs.',
    ].join('\n'),
  },
]

const FINDINGS_SCHEMA = {
  type: 'object',
  properties: {
    lens: { type: 'string' },
    summary: { type: 'string', description: 'one-paragraph verdict for this lens: how well-configured is the system on this dimension?' },
    findings: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          id: { type: 'string', description: 'short stable id, e.g. FG-1' },
          type: { type: 'string', enum: ['strength', 'under-configured', 'mis-configured'] },
          title: { type: 'string' },
          research_basis: { type: 'string', description: 'the concept + source from the research corpus that grounds this' },
          system_state: { type: 'string', description: 'what the system currently does, in one or two sentences' },
          locations: {
            type: 'array',
            items: {
              type: 'object',
              properties: {
                file: { type: 'string' },
                section: { type: 'string' },
                quote: { type: 'string', description: 'verbatim text actually read from the file' },
              },
              required: ['file', 'quote'],
            },
          },
          critique: { type: 'string', description: 'the precise gap/misconfig, or for a strength, why it maps well' },
          churn_relevance: { type: 'string', description: 'how this bears on bottom-up-emergent + the churn axiom' },
          improvement: { type: 'string', description: 'concrete region for improvement, reusing engine primitives where possible. Empty for pure strengths.' },
          leverage: { type: 'string', enum: ['high', 'medium', 'low'] },
          effort: { type: 'string', enum: ['low', 'medium', 'high'] },
        },
        required: ['id', 'type', 'title', 'research_basis', 'system_state', 'locations', 'critique', 'churn_relevance', 'leverage'],
      },
    },
  },
  required: ['lens', 'summary', 'findings'],
}

const VERDICT_SCHEMA = {
  type: 'object',
  properties: {
    finding_id: { type: 'string' },
    verdict: { type: 'string', enum: ['sound', 'already-handled', 'overstated', 'refuted', 'uncertain'] },
    reasoning: { type: 'string', description: 'why. If already-handled, name WHERE in the corpus the mechanic actually lives, with a quote.' },
    evidence_quote: { type: 'string', description: 'a key verbatim quote you independently located (esp. checking whether a claimed gap is filled elsewhere)' },
    corrected_leverage: { type: 'string', enum: ['high', 'medium', 'low'] },
    refined_improvement: { type: 'string', description: 'tighten or correct the proposed improvement if needed' },
  },
  required: ['finding_id', 'verdict', 'reasoning'],
}

phase('Critique')
const results = await pipeline(
  LENSES,
  (l) => agent(
    [
      'You are a senior game-systems designer and philosopher of deliberation, critiquing the Valoria TTRPG social contest system.',
      'You have deep command of the research corpus (deliberation-as-game; politics-as-deliberative-game; Renaissance machination & mechanism design).',
      'Your lens: ' + l.title + '.',
      '',
      CORPUS, '', PHILOSOPHY, '', METHOD,
      '',
      'YOUR LENS BRIEF:', l.brief,
      '',
      'Return findings in the schema. lens="' + l.key + '". Aim for the 3-6 SHARPEST findings (mix of strengths and gaps), each grounded in a verbatim quote. Quality over quantity. Do not invent gaps without grepping the adjacent files first.',
    ].join('\n'),
    { label: 'critique:' + l.key, phase: 'Critique', schema: FINDINGS_SCHEMA, effort: 'high' },
  ),
  (review, l) => {
    // P7a: route the lens's yield through the run so a zero-finding lens raises the alarm rather
    // than blending into a healthy-looking total. Eight lenses over one system: if one comes back
    // empty, that is either a genuinely clean dimension or an agent that never opened the files,
    // and those two look identical in an aggregate count.
    const findings = run.lens(l.key, (review && review.findings) ? review.findings : [])
    return parallel(findings.map((f) => () =>
      agent(
        [
          'ADVERSARIAL VERIFICATION of a design-critique finding about the Valoria social contest system.',
          'Your job: pressure-test it. Open the cited files AND grep the adjacent corpus yourself.',
          CORPUS,
          '',
          'FINDING (JSON):', JSON.stringify(f, null, 2),
          '',
          'Decide a verdict:',
          ' - "sound": the critique holds; the gap/strength is real as described.',
          ' - "already-handled": the claimed gap is actually addressed somewhere in the corpus (npc_behavior, conviction_taxonomy, knots, faction docs, etc.). NAME WHERE with a quote. This is the most important check - the corpus is large.',
          ' - "overstated": partly true but the severity/leverage is too high, or the system handles more of it than claimed.',
          ' - "refuted": a cited quote cannot be located, or is out of context such that the critique does not hold.',
          ' - "uncertain": cannot resolve from the files.',
          'Independently locate at least one evidence_quote. Assess corrected_leverage honestly. Tighten the improvement if the original is vague or would violate engine discipline (no bolt-on subsystems; reuse sigma resolver / armature dot-product / Key bus).',
          'Return the verdict schema. finding_id = "' + f.id + '".',
        ].join('\n'),
        hCritic({ label: 'verify:' + l.key + ':' + f.id, phase: 'Verify', schema: VERDICT_SCHEMA, effort: 'high' }),
      ).then((v) => Object.assign({}, f, { lens: l.key, verdict: v })).catch(() => null),
    ))
  },
)

const all = results.flat().filter(Boolean)
const sound = all.filter((f) => f.verdict && (f.verdict.verdict === 'sound' || f.verdict.verdict === 'overstated' || f.verdict.verdict === 'already-handled'))
const refuted = all.filter((f) => f.verdict && f.verdict.verdict === 'refuted')
const strengths = all.filter((f) => f.type === 'strength' && f.verdict && f.verdict.verdict !== 'refuted')
const gaps = all.filter((f) => f.type !== 'strength' && f.verdict && (f.verdict.verdict === 'sound' || f.verdict.verdict === 'overstated' || f.verdict.verdict === 'already-handled'))

// Every raised finding should have met a critic; anything that did not is a draft, not a result.
run.critiqued('Verify', all.length, all.filter((f) => f.verdict).length)

// P8 · a verdict other than "sound" IS the critic disagreeing with the analyst. That was previously
// collapsed into a bucket count and lost. Record it as a dispute, classified by WHAT is disputed and
// WHY, so the shape of the disagreement survives to the adjudication stage.
const ROOT_BY_VERDICT = {
  'already-handled': 'different-sources-read',   // the critic opened the adjacent file the lens did not
  'overstated': 'severity-calibration',          // same facts, different weight
  'refuted': 'measurement-vs-assertion',         // the citation does not say what the claim says
  'uncertain': 'ambiguous-spec',                 // the corpus genuinely admits both readings
}
const LAYER_BY_VERDICT = { 'already-handled': 'scope', 'overstated': 'severity', 'refuted': 'evidence', 'uncertain': 'interpretation' }
const disputed = all.filter((f) => f.verdict && f.verdict.verdict !== 'sound')
for (const f of disputed) {
  run.dispute({
    finding_id: f.lens + ':' + f.id,
    layer_disputed: LAYER_BY_VERDICT[f.verdict.verdict],
    root_cause: ROOT_BY_VERDICT[f.verdict.verdict],
    positions: [
      { by: 'lens:' + f.lens, holds: String(f.critique || f.title || '').slice(0, 400) },
      { by: 'critic', holds: String(f.verdict.reasoning || '').slice(0, 400), verdict: f.verdict.verdict },
    ],
    resolution_model: 'adjudicated-by-synthesis',
  })
}

// P7b · rank by INDEPENDENT REDISCOVERY. Eight lenses read one system from eight unrelated
// theoretical traditions; when three of them land on the same file saying the same thing, that
// corroboration is the strongest signal a read-only audit produces — and this workflow used to
// throw it away. A lens cannot corroborate itself: the key counts DISTINCT lenses.
const ranked = hRediscover(all, (f) => f.lens)
const corroborated = ranked.filter((g) => g.rediscovery > 1)
log('critique complete: ' + all.length + ' findings raised; ' + gaps.length + ' gaps survive, '
  + strengths.length + ' strengths, ' + refuted.length + ' refuted; ' + corroborated.length
  + ' finding(s) independently rediscovered by 2+ lenses')

// P8 · ADJUDICATION IS REQUIRED, and no-silent-disappearance means the run says so if it is missing.
// This workflow had no synthesis stage, so a disputed finding simply vanished into a bucket. One
// adjudicator now rules on the disputes only — cheap, and it is the stage that GATES the result.
// Deliberately opus, not fable: §10 makes fable an upgrade trigger, never a default, and nothing
// here is evidence that opus failed this node. (Fable would in any case be legal shape for this
// stage — it writes nothing and rules on the run — but legal shape is not a reason to spend.)
if (disputed.length) {
  const rulings = await agent(
    [
      'ADJUDICATION. You are ruling on disagreements between per-lens analysts and the adversarial critics who checked them.',
      'You are READ-ONLY and you write no files. Open the cited files yourself before ruling — do not take either side on trust.',
      CORPUS,
      '',
      'For each dispute below, rule for ONE side and say which, in two sentences, citing what you read.',
      'Where the critic says "already-handled", the decisive question is whether the named alternative location genuinely does the job the lens said was missing, or merely mentions the topic.',
      'Where it says "overstated", rule on the leverage, not on whether the finding exists at all.',
      'A dispute you cannot resolve from the files is ruled "unresolved" WITH the specific reading that would settle it — that is a real outcome, not a failure.',
      '',
      'DISPUTES (JSON):', JSON.stringify(run.disagreements, null, 2),
    ].join('\n'),
    hCritic({
      label: 'adjudicate:disputes', phase: 'Verify', model: 'opus', effort: 'high',
      schema: {
        type: 'object',
        properties: {
          rulings: {
            type: 'array',
            items: {
              type: 'object',
              properties: {
                finding_id: { type: 'string' },
                ruling: { type: 'string', enum: ['lens-holds', 'critic-holds', 'split', 'unresolved'] },
                reasoning: { type: 'string' },
              },
              required: ['finding_id', 'ruling', 'reasoning'],
            },
          },
        },
        required: ['rulings'],
      },
    }),
  )
  for (const r of ((rulings && rulings.rulings) || [])) {
    run.adjudicate(r.finding_id, r.ruling + ': ' + r.reasoning, 'adjudicate:disputes')
  }
}

const summary = run.summary()
if (summary.degraded) log('[harness] run degraded — stop_reason=' + summary.stop_reason + '; results below are still complete, read the signals before banking them')

return {
  run: summary,
  totals: { raised: all.length, gaps: gaps.length, strengths: strengths.length, refuted: refuted.length, disputed: disputed.length },
  rediscovery: ranked.map((g) => ({ key: g.key, rediscovery: g.rediscovery, lenses: g.lenses })),
  corroborated,
  gaps,
  strengths,
  refuted,
  uncertain: all.filter((f) => f.verdict && f.verdict.verdict === 'uncertain'),
}
