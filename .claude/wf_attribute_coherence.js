export const meta = {
  name: 'attribute-value-coherence',
  description: 'Cross-silo census + all-directions pipeline trace + schema audit of every attribute/score/stat/value, bound into the Key & Echo Armature (quantity layer)',
  phases: [
    { title: 'Sweep', detail: 'seven finder families inventory every named quantity per surface family', model: 'haiku/sonnet' },
    { title: 'Census', detail: 'barrier merge: dedup, alias-collapse, key-binding join -> quantity-contract rows', model: 'sonnet' },
    { title: 'Validate', detail: 'spot-check 10 random census rows against cited file:line', model: 'haiku' },
    { title: 'Trace', detail: 'per-cluster all-directions branching pipeline trace + dossier', model: 'sonnet' },
    { title: 'Critic', detail: 'read-only adversarial critic per dossier (agonist->antagonist relay)', model: 'sonnet' },
    { title: 'Synthesis', detail: 'verdict report + docket + armature extension + finding_status', model: 'opus (effort max)' },
    { title: 'Guardrail', detail: 'read-only conformance ruling over the run summary — writes nothing', model: 'opus' },
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

  // A CRITIC THAT DIED IS NOT A CRITIC THAT FOUND NOTHING, and the scripts could not tell them
  // apart. The pipeline pattern is `.then(v => ({...f, verdict: v})).catch(() => null)` followed by
  // `.filter(Boolean)` — so a critic that errors drops the WHOLE FINDING, and the obvious coverage
  // check (`produced = survivors.length`) then compares a set to itself and can never fire. The
  // finding vanishes and the run reports `completed`.
  //
  // That hole sits exactly where P4 could open one: switching critics to a tools-restricted
  // agentType is the change most likely to make a critic stage fail, and the harness would have
  // hidden it. Wrap the critic call in this instead of a bare .catch so the loss is counted.
  //   parallel(findings.map(f => () => run.attempt('Verify', agent(...).then(v => ({...f, verdict: v})))))
  run.attempted = 0
  run.lost = 0
  run.attempt = function (stage, promise) {
    run.attempted += 1
    return Promise.resolve(promise).then(
      v => {
        if (v === null || v === undefined) {
          run.lost += 1
          run.signal('critic_starved', stage + ': a critic returned null — the finding it was '
            + 'checking is dropped from the results, NOT cleared. Check the agentType resolves and '
            + 'that a tools-restricted critic can still emit structured output.')
        }
        return v
      },
      err => {
        run.lost += 1
        run.signal('critic_starved', stage + ': a critic threw (' + String(err && err.message || err)
          + ') — the finding it was checking is dropped from the results, NOT cleared.')
        return null
      })
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

  // IDEMPOTENT, AND A COPY. Both properties were missing and both bit immediately.
  //  · summary() SIGNALS on unadjudicated disputes, and wf_attribute_coherence.js calls it twice —
  //    once to hand the run to the guardrail stage, once to return it. Every open dispute was
  //    therefore reported twice, and the guardrail was judging a run whose signal list the final
  //    return then contradicted. The `_summarised` latch fires the signal once, on the first call.
  //  · it returned the LIVE arrays. A caller holding an earlier summary saw it mutate underneath
  //    them, which is the opposite of a snapshot. Now copied.
  // Neither is cosmetic: a report-only harness whose report changes after you read it is worse
  // than no report, because it reads as authoritative.
  run.summary = function () {
    const unadj = run.disagreements.filter(d => d.status === 'open')
    if (unadj.length && !run._summarised) {
      run.signal('disagreement_unadjudicated', unadj.length + ' dispute(s) reached the return with no '
        + 'ruling: ' + unadj.map(d => d.finding_id).join(', '))
    }
    run._summarised = true
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
      signals: run.signals.map(s => Object.assign({}, s)),
      disagreements: run.disagreements.map(d => Object.assign({}, d)),
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

// P8b · build a dispute record FROM a critic verdict, instead of by hand.
//
// WHY THIS EXISTS, and it is not a convenience. Five wave scripts hand-rolled the record as
// `{ layer, target, detail, severity }`. Not one of those four keys is a key run.dispute() reads,
// so every field silently took its default: finding_id became '?', layer_disputed 'interpretation',
// root_cause 'ambiguous-spec', positions []. The record carried ZERO information from its call
// site, and because run.adjudicate() binds on finding_id, no ruling could ever attach to one. That
// shipped and ran live (the W4 run: 8 disputes, all keyed '?'). The three critique scripts wrote it
// correctly, so this was a copy-paste lineage defect — wave0 got it wrong and waves 1-4 inherited.
//
// A record that is error-prone to build by hand gets built by the owner. The correct call is now
// the SHORT one. Hand-rolled records stay legal (the critique scripts have richer positions), so
// the guard that fails on recurrence is static and lives in tools/ci_wf_harness_check.py: it
// derives the legal key set from THIS FILE and rejects a literal run.dispute({...}) that uses a
// key the owner never reads, or that omits finding_id.
//
// The verdict enum below is the uphold/overturn/soften/sharpen funnel every critic stage in this
// repo already emits; the two maps are lifted verbatim from wf_attribute_coherence.js, which had
// them right. `uphold` is not a dispute and callers are expected to filter it out; if one arrives
// anyway it maps to the same conservative defaults as an unrecognised verdict.
const H_LAYER_BY_VERDICT = { overturn: 'evidence', soften: 'severity', sharpen: 'severity' }
const H_ROOT_BY_VERDICT = {
  overturn: 'measurement-vs-assertion',
  soften: 'severity-calibration',
  sharpen: 'severity-calibration',
}
function hVerdictDispute(v, criticLabel, producerHolds) {
  const verdict = v && v.verdict
  return {
    finding_id: String((v && (v.target || v.target_id)) || ''),
    layer_disputed: H_LAYER_BY_VERDICT[verdict] || 'interpretation',
    root_cause: H_ROOT_BY_VERDICT[verdict] || 'ambiguous-spec',
    positions: [
      { by: 'producer', holds: String(producerHolds || '').slice(0, 400) },
      {
        by: String(criticLabel || 'critic'),
        holds: String((v && v.evidence) || '').slice(0, 400),
        verdict: String(verdict || ''),
        severity: String((v && v.severity) || ''),
      },
    ],
    resolution_model: 'adjudicated-by-synthesis',
  }
}

// P4 · the read-only critic. Independence is STRUCTURAL, not a sentence in a prompt: the
// agentType below is defined in .claude/agents/valoria-critic.md with a tools list that has no
// Write/Edit. Passing it is the whole mechanism — a critic stage that omits it can write, and
// tools/ci_wf_harness_check.py fails the script that does.
const H_CRITIC = { agentType: 'valoria-critic' }
function hCritic(opts) { return Object.assign({}, opts || {}, H_CRITIC) }
// ==== END VALORIA WF HARNESS v1 ====

const run = hRun('attribute-value-coherence')
const ROOT = '/home/user/ttrpg'
const AUD = `${ROOT}/audit/2026-07-08-attribute-value-coherence-audit`

const SHARED = `
You are one agent in the ATTRIBUTE/VALUE COHERENCE AUDIT of the Valoria design repo at ${ROOT}
(lane IN, anchor ED-IN-0029, READ-ONLY audit unless your stage explicitly instructs a Write into
${AUD}/). The WORKING TREE is the source of truth — read actual files; never trust memory, summaries,
or values_master.yaml over disk. Cite file:line for every claim.

WHY THIS AUDIT EXISTS (Jordan): "We desperately lack unity, consistency and coherence with our
explosion of attributes and derived scores across all our different systems and subsystems developed
in silos."

ARMATURE FRAMING (binding): this audit is the QUANTITY-LAYER extension of the Key & Echo Armature
(systems/_architecture/key_echo_armature_v1.md, RATIFIED ED-IN-0018 — Jordan's mandate: "a
harness/armature that properly shapes the subsystems so they fit into the systems together
properly"). The armature unified the Key/seam layer; this audit covers the quantities those seams
read and write — the stats named in Key payloads (stat_deltas, impact_vector,
required_payload_fields), module_contracts state:/derivations:, params prose tables, sim/engine
constants, and Godot exports. The armature guardrail (§1, holonic doctrine ED-1083 §2) names the
failure class: "never grow a scale-local interface dialect (shape divergence)". Silo-grown attribute
vocabularies ARE shape divergence at the stat layer — the same disease as the C-INJ-12
causes[]/cause_keys/origin_keys split the armature §2.4 unified for provenance naming.

QUANTITY = any named attribute, aggregate, derived value, track, clock, pool, faction/settlement
stat, practitioner stat, unit stat, or load-bearing tunable constant. The registry taxonomy
(references/descriptor_registry.yaml) is the KIND vocabulary: attribute_scalar, attribute_aggregate,
faction_stat, settlement_stat, plus its not_descriptors classes derived_value / track / clock / pool,
plus code_constant for engine coefficients.

VERIFIED BASELINE FACTS (confirm, extend, find MORE — do not merely restate):
- descriptor_registry.yaml: 9 personal attributes (3 body/mind/social) IN FLUX with legacy aliases;
  agg.body/mind/social are status:placeholder, NOT wired (legacy Stat-x-3 multipliers remain live);
  not_descriptors block lists 9 derived_values, 5 tracks, 4 clocks, 7 pools OUTSIDE the registry.
  ALL attr/agg/fac/set keys in names_index.yaml are enforce:warn — nothing blocks legacy names.
- Combat Pool is still triple-carried: struck (Agility x 2)+History+3 form at values_master.yaml:212
  (filed under NONEXISTENT params/combat.md) and values_master.yaml:1150, AND in params/core.md:4's
  stale PP-247 header comment — while params/core.md:161 (live table), module_contracts.yaml:810 and
  combat_config.gd agree on canonical max(5, History+6) (ED-901/900/904).
- values_master.yaml is QUARANTINED-STALE (ED-1084); generator tools/extract_values.py is dead;
  8 entries leak from engine/params/threadwork_superseded.md; its 5 conflicts: blocks are live-vs-superseded
  mixing artifacts.
- engine/params/board_game.md and engine/params/factions.md are BROKEN auto-generated indexes (links to
  nonexistent references/params_bg_*.md / params_factions_*.md; real content in params/bg/*.md and
  engine/params/factions/* + engine/params/factions_personal.md).
- engine/params/mass_combat.md header carries superseded (PP-233 pool) and superseding (ED-899 2xCommand)
  formulas side by side.
- tests/registry/test_descriptor_registry.py is DEAD: imports a module moved to deprecated/, and
  defines no test_* function so pytest collects zero tests — the registry has NO running validator.
- The one typed export is engine/engine_params/combat_engine_v1.json (from config.py via
  tools/export_engine_params.py --check, blocking CI). No tool parses params/*.md prose — prose
  formula drift has NO automated detector.
- Mandate = round(0.5*Legitimacy + 0.5*Popular_Support) (engine/params/factions_personal.md), also derived
  size-weighted in module_contracts faction_state — check for divergence.

KNOWN-TRACKED OPEN ITEMS (cite, do NOT re-litigate; the value-add is the cross-silo interlock view):
ED-IN-0008 (glossary vs descriptor_registry/names_index naming-authority conflict, 7-vs-9 roster),
workplan v6 T1 queue-13 (attribute-roster ratification — Jordan's call; we only assemble its
decision surface), ED-1051 (module_contracts doc:null gaps), ED-1052 (typed engine-params scope),
ED-PC-0003 (sigma band-discipline unification, armature §5.12 direction ruled), ED-FA-0003 (BG
victory-params re-export), ED-SC-0008 (social_contest contract refresh), values_master
regenerate-vs-retire (2026-07-01 decision queue item 17), ED-IN-0025 (resonance_style retirement
correction, NEEDS-JORDAN).

CARDINAL RULES:
(a) file:line evidence for every claim;
(b) build-state (stub/unwired/unported) is routing metadata, NEVER verdict evidence;
(c) KNOWN-TRACKED overlaps are cited with their ED id, never re-argued;
(d) BIND, DON'T INVENT — criteria come from the armature guardrails (shape divergence / scripting
    drift), the holonic doctrine, and descriptor_registry's own KIND discipline; no new criteria;
(e) rule no forks — genuine design calls (roster picks, values_master disposition, tier promotion)
    are DOCKET items for Jordan, options stated with a recommended default;
(f) lane scoping — SC/SE/PC-owned questions are recorded as feeds to their owning lanes
    (armature §5.8/5.9 precedent), not ruled from this IN pass.

SEVERITY: P1 = an engine/Godot consumer would ingest a wrong or ambiguous value (undecidable
canonical definition, live formula divergence); P2 = materially misleads (stale carrier surfaces,
synonym splits, unregistered load-bearing quantities, enforcement gaps); P3 = friction/debt.
CALIBRATION: KNOWN-TRACKED (open ED exists — name it) / KNOWN-UNTRACKED (documented somewhere but
no ED owns it) / NEW.
FINDING KINDS: collision (same name, different formula/definition) · synonym (different names, one
concept) · orphan (defined, never consumed) · dead (consumed surface is dead/unreachable) ·
unregistered (load-bearing quantity with no registry key) · enforcement-gap (warn-tier or
unvalidated where it should block) · stale (superseded value still carried live) · export-drift
(prose vs oracle vs port disagree) · key-binding-gap (a Key payload needs this quantity but no
registry key covers it) · other.
STYLE: curious in extension, adversarial in review, judicious in reconciliation. Your final output
IS structured data returned via the schema — no prose wrapper.
`

const FINDING = {
  type: 'object', additionalProperties: false,
  required: ['id', 'severity', 'kind', 'calibration', 'claim', 'evidence'],
  properties: {
    id: { type: 'string' },
    severity: { type: 'string', enum: ['P1', 'P2', 'P3'] },
    kind: { type: 'string', enum: ['collision', 'synonym', 'orphan', 'dead', 'unregistered', 'enforcement-gap', 'stale', 'export-drift', 'key-binding-gap', 'other'] },
    calibration: { type: 'string', enum: ['KNOWN-TRACKED', 'KNOWN-UNTRACKED', 'NEW'] },
    known_ref: { type: 'string', description: 'ED/PP id or doc that already tracks this, if calibration != NEW' },
    claim: { type: 'string' },
    evidence: { type: 'string', description: 'file:line citations' },
  },
}

const INVENTORY_ITEM = {
  type: 'object', additionalProperties: false,
  required: ['name', 'kind_guess', 'surface', 'detail'],
  properties: {
    name: { type: 'string' },
    kind_guess: { type: 'string', enum: ['attribute_scalar', 'attribute_aggregate', 'faction_stat', 'settlement_stat', 'derived_value', 'track', 'clock', 'pool', 'unit_stat', 'practitioner_stat', 'code_constant', 'other'] },
    surface: { type: 'string', description: 'file:line where defined/carried' },
    detail: { type: 'string', description: 'formula / value / range / scale exactly as written, with any PP/ED provenance tag present' },
    aliases_or_variants: { type: 'array', items: { type: 'string' } },
    consumers_seen: { type: 'array', items: { type: 'string' }, description: 'file:line of consumption sites noticed while sweeping' },
    key_bindings_seen: { type: 'array', items: { type: 'string' }, description: 'Key types / payload fields (stat_deltas, impact_vector, required_payload_fields) that touch this quantity' },
    notes: { type: 'string' },
  },
}

const FINDER_SCHEMA = {
  type: 'object', additionalProperties: false,
  required: ['family', 'items', 'findings', 'coverage_notes'],
  properties: {
    family: { type: 'string' },
    items: { type: 'array', items: INVENTORY_ITEM },
    findings: { type: 'array', items: FINDING },
    coverage_notes: { type: 'string', description: 'what was swept, what was skipped and why — no silent caps' },
  },
}

const CENSUS_ROW = {
  type: 'object', additionalProperties: false,
  required: ['canonical_name', 'kind', 'cluster', 'defining_surface', 'formulas', 'registered', 'status'],
  properties: {
    canonical_name: { type: 'string' },
    kind: { type: 'string' },
    cluster: { type: 'string', enum: ['C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7'] },
    defining_surface: { type: 'string', description: 'THE canonical definition site file:line per CURRENT.md resolution; AMBIGUOUS:<candidates> if undecidable' },
    aliases: { type: 'array', items: { type: 'string' } },
    formulas: { type: 'array', items: { type: 'object', additionalProperties: false, required: ['formula', 'surface'], properties: { formula: { type: 'string' }, surface: { type: 'string' }, provenance: { type: 'string' } } } },
    consumers: { type: 'array', items: { type: 'string' } },
    scale_bounds: { type: 'string' },
    registered: { type: 'string', enum: ['block', 'warn', 'by_reference', 'not_descriptors', 'unregistered'] },
    key_bindings: { type: 'array', items: { type: 'string' } },
    divergences: { type: 'array', items: { type: 'string' } },
    finding_basis: { type: 'string' },
    status: { type: 'string', enum: ['COHERENT', 'DRIFTED', 'AMBIGUOUS', 'ORPHANED', 'DEAD', 'UNREGISTERED-LOAD-BEARING'] },
  },
}

const CENSUS_SCHEMA = {
  type: 'object', additionalProperties: false,
  required: ['rows', 'merge_notes'],
  properties: {
    rows: { type: 'array', items: CENSUS_ROW },
    merge_notes: { type: 'string', description: 'dedup/alias-collapse decisions + anything dropped and why — no silent caps' },
  },
}

const VALIDATE_SCHEMA = {
  type: 'object', additionalProperties: false,
  required: ['checked', 'pass_count', 'fail_count'],
  properties: {
    checked: { type: 'array', items: { type: 'object', additionalProperties: false, required: ['canonical_name', 'verdict', 'note'], properties: { canonical_name: { type: 'string' }, verdict: { type: 'string', enum: ['pass', 'fail'] }, note: { type: 'string' } } } },
    pass_count: { type: 'number' },
    fail_count: { type: 'number' },
  },
}

const DOSSIER_SCHEMA = {
  type: 'object', additionalProperties: false,
  required: ['cluster', 'headline', 'findings', 'unification_options', 'dossier_written'],
  properties: {
    cluster: { type: 'string' },
    headline: { type: 'string' },
    findings: { type: 'array', items: FINDING },
    unification_options: { type: 'array', items: { type: 'object', additionalProperties: false, required: ['id', 'what', 'recommended_default'], properties: { id: { type: 'string' }, what: { type: 'string' }, recommended_default: { type: 'string' }, feeds: { type: 'string', description: 'ED/queue item or lane this feeds' } } } },
    registry_delta_candidates: { type: 'array', items: { type: 'string' }, description: 'quantities this cluster says should gain descriptor_registry keys (armature §3 analog)' },
    dossier_written: { type: 'string', description: 'absolute path of the dossier md you wrote' },
  },
}

const CRITIC_SCHEMA = {
  type: 'object', additionalProperties: false,
  required: ['cluster', 'verdicts', 'missed', 'conformance_note'],
  properties: {
    cluster: { type: 'string' },
    verdicts: { type: 'array', items: { type: 'object', additionalProperties: false, required: ['target_id', 'verdict', 'reason'], properties: { target_id: { type: 'string' }, verdict: { type: 'string', enum: ['uphold', 'overturn', 'soften', 'sharpen'] }, reason: { type: 'string' } } } },
    missed: { type: 'array', items: FINDING, description: 'real defects the dossier failed to find' },
    conformance_note: { type: 'string', description: 'did the dossier invent criteria, rule a fork, or violate lane scoping? name instances or state clean' },
  },
}

const SYNTH_SCHEMA = {
  type: 'object', additionalProperties: false,
  required: ['headline', 'files_written', 'confirmed_p1', 'confirmed_p2', 'confirmed_p3', 'docket_items', 'adjudications'],
  properties: {
    headline: { type: 'string' },
    files_written: { type: 'array', items: { type: 'string' } },
    confirmed_p1: { type: 'number' },
    confirmed_p2: { type: 'number' },
    confirmed_p3: { type: 'number' },
    docket_items: { type: 'number' },
    // P8: required, so a dispute cannot vanish between the critic funnel and the report. An
    // out-of-lane record (status "observation") is NOT ruled on — it is carried, not adjudicated.
    adjudications: {
      type: 'array',
      items: {
        type: 'object', additionalProperties: false,
        required: ['finding_id', 'ruling', 'reasoning'],
        properties: {
          finding_id: { type: 'string' },
          ruling: { type: 'string', enum: ['dossier-holds', 'critic-holds', 'split', 'unresolved'] },
          reasoning: { type: 'string' },
        },
      },
    },
  },
}

const FAMILIES = [
  { key: 'REG', model: 'haiku', title: 'Registries', focus: `references/descriptor_registry.yaml (FULL — every section incl. by_reference, deprecated, not_descriptors), references/names_index.yaml (enforcement tiers for attr./agg./fac./set. keys), references/values_master.yaml (header banner + schema + BOTH Combat Pool entries + the 5 conflicts: blocks + which source files it indexes), references/glossary.md (its self-declared naming authority + attribute roster — the ED-IN-0008 conflict side), registers/mechanics_index.yaml (quantity-bearing entries).` },
  { key: 'PARAMS', model: 'sonnet', title: 'Params prose', focus: `Every file in params/ incl. params/bg/*.md and engine/params/factions/* and engine/params/factions_personal.md and engine/params/threadwork_superseded.md. Extract every derived-score/pool/track/clock/stat table row with its formula EXACTLY as written + PP/ED tags. Verify the broken indexes (board_game.md, factions.md link targets). Capture internal header-vs-body drift (core.md:4 vs :161; mass_combat.md header). Note which params file each not_descriptors quantity actually lives in.` },
  { key: 'DESIGN', model: 'sonnet', title: 'Design heads', focus: `Resolve heads via CURRENT.md first. Sweep for quantity definitions/consumption: the derived-stats doc (find it — 'derived_stats §14' is cited by descriptor_registry as authoritative for Stat-x-3 multipliers), systems/social_contest/social_contest_v30.md (+contest pools, Composure), systems/combat/combat_v30.md vs systems/combat/combat_engine_v1/ (two combat surfaces), systems/mass_battle/mass_battle_v30.md (unit stats), faction_*.md heads, systems/settlements/settlement_layer_v30.md §1.8, systems/threadwork/threadwork_v30.md (TS/TPS/Coherence), systems/npcs/npc_behavior_v30.md (tracks, Resonant Style), conviction_track_v30 if present, systems/fieldwork/fieldwork_v30.md.` },
  { key: 'CONTRACT', model: 'haiku', title: 'Contracts + armature', focus: `references/module_contracts.yaml — EVERY state:/derivations:/gates: entry naming a quantity (name, bucket, writable, formula) across all 27 modules. systems/_architecture/key_echo_armature_v1.md §1 (payload obligations: stat_deltas/impact_vector/targets[]), §2 tables (which faction/settlement stats echoes move), §3 registry deltas. systems/_architecture/key_type_registry_v30.md required_payload_fields that name stats. systems/_architecture/key_substrate_v30.md stat-bearing fields.` },
  { key: 'SIM', model: 'haiku', title: 'Sim + engine code', focus: `engine/substrate/keys.py (Key fields, stat_deltas validation — what vocabulary does it accept?), engine/autoload/sigma_leverage.py + game_state.py + dice_engine.py (constants + provenance tags), systems/combat/combat_engine_v1/config.py (ALL CFG coefficients with their [SIM-CALIBRATE]/[FIAT]/[ASSERTED]/ED tags) + combatant.py (derived-stat formulas in code), tests/sim/v32-combat-balance/{m1_dice_sigma_core,r1_sigma_resolution,r8_parity_harness}.py (canonical constants), and the per-subsystem sims — systems/characters/sim/ + systems/social_contest/sim/ + systems/fieldwork/sim/ + systems/overview/sim/ + systems/factions/sim/ + systems/mass_battle/sim/ — for quantity constants (grep for stat names + = numbers with tags). NOTE the flat sim/personal/ and sim/provincial/ trees named by older notes no longer exist; they were split across those subsystem packages and the whole sim/ tree was retired 2026-07-21.` },
  { key: 'GODOT', model: 'haiku', title: 'Godot port + typed export', focus: `godot/skeleton/engines/combat/resources/{combat_config.gd,weapon_resource.gd} (every exported field + its cited canon), any .tres files naming stats, engine/engine_params/combat_engine_v1.json (the typed export — every key), tools/export_engine_params.py (what it covers and does NOT cover). Flag every value that exists in the port but has no prose head, and vice versa.` },
  { key: 'INDEX', model: 'haiku', title: 'Secondary indices + validators', focus: `references/mechanical_terms_index.md, references/numeric_bounds_report.yaml, references/propagation_map.md, references/silo_overlap_matrix.yaml, references/name_collision_database.yaml, references/collision_registry.yaml — which quantities each indexes and where they disagree with each other. tests/registry/test_descriptor_registry.py (confirm dead: import path + zero pytest collection). tools/ci_names_check.py / ci_names_consistency.py / ci_naming_check.py (what tier actually enforces what).` },
]

const CLUSTERS = [
  { key: 'C1', title: 'Personal attributes, aliases & aggregates', focus: `The 9-attribute roster + every legacy alias (Vitality, Dexterity, Cognition/Reasoning, Spirit, Perception, Influence/Presence, Sincerity/Affability) + agg.* placeholders. Trace every surface still using a LEGACY name live (not as alias documentation). The 7-vs-9 glossary conflict (ED-IN-0008 decision surface). Where does Spirit still act as a standalone attribute in formulas (Stamina 3*End+2*Spirit, Concentration, threadwork (Spirit x 2)) vs its fold into Will? Is any aggregate consumed anywhere despite placeholder status?` },
  { key: 'C2', title: 'Derived values', focus: `Health, Stamina, Composure, Concentration, Thread Fatigue, Resolve, Garrison Strength, Local Economy, Mandate. For each: every formula occurrence across params prose, module_contracts derivations, engine code, Godot port — do they agree? Composure has at least two forms (Charisma+6 in engine/params/contest.md vs Charisma x 3 legacy multiplier per descriptor_registry note). Mandate has two derivations (0.5L+0.5PS vs size-weighted). Health has a monster formula in module_contracts:810ff — matched where?` },
  { key: 'C3', title: 'Pools', focus: `Combat, Argue, Thread, Fieldwork, Knot, MassCombat, FactionDomain pools. Combat Pool triple-carriage is the FLAGSHIP (fully documented in SHARED — extend to: which of the 7 pools have the same disease?). Thread pool (Spirit x 2)+History+TPS vs fieldwork (Primary x 2)+History vs combat max(5,History+6) — three construction idioms; is divergence ruled (fieldwork.md says its x2 is 'fieldwork-native') or drift? MassCombat pool PP-233 vs ED-899. Contest/Argue pool (ED-SC-0004 P0 fork — decision surface only). Knot pool definition site?` },
  { key: 'C4', title: 'Tracks & clocks', focus: `Tracks: Piety, Disposition, Renown, Standing, Persuasion (+ knots gauge -5..+5 ED-912). Clocks: Evidence, CI, MS, IP. Ranges/caps/thresholds across surfaces: CI milestones 40/55/65/80/100 vs 75 (armature §5.11 — carried as data, cite only), Disposition/Knot ±5 (ED-912), IP milestones. Which tracks are registered nowhere but consumed by Key payloads or gates (module_contracts gates like Bonds >= 5 — is Bonds a track here and an attribute in C1? name collision!).` },
  { key: 'C5', title: 'Faction & settlement stats + Mandate seam', focus: `Faction: Influence, Wealth, Military, Intel, Stability (1-7) + Treasury (x100). Settlement: Legitimacy, Popular Support, Prosperity, Defense, Order (+Accord? scale_transitions §5.5 — is Accord a stat, a delta, or neither?). These are what Domain Echo stat_deltas actually MOVE (armature §2.1) — for each stat: is the name the substrate/Key payloads would carry canonical + collision-free (the C-FA-3 'PS' collision precedent)? Prosperity x 50 = Local Economy etc. derivations consistent? Where do BG-mode (params/bg/) stats diverge from faction_stats registry?` },
  { key: 'C6', title: 'Code constants & the export pipeline', focus: `prose -> config.py oracle -> combat_engine_v1.json -> combat_config.gd chain: for each coefficient, is provenance intact and value identical end-to-end? config.py [FIAT]/[ASSERTED]/[SIM-CALIBRATE] tags — how many constants have NO canon backing (that is fine per Class-C, but count them + flag any that params prose ALSO states differently). sigma constants (PER_DIE, LEVEL_SIGMA, M_MAX, SIGMA_N_COEFF) across m1_dice_sigma_core.py / sigma_leverage.py / engine — verbatim? The dead DAMAGE_SCALE=4.0 precedent — more like it? What quantities does engine/substrate/keys.py validate stat_deltas against (anything? nothing = key-binding-gap).` },
  { key: 'C7', title: 'Cross-index consistency, enforcement tiers & check backlogs', focus: `The 6 secondary indices vs descriptor_registry vs glossary: for a sample of 10 quantities, how many indices carry each and how many disagree? Enforcement audit: everything at warn, registry test dead, values_master quarantined, no prose-drift detector — measure the would-be backlog of the two PROPOSED checks: A17 stat-vocabulary closure (every stat named in module_contracts state:/derivations:/gates: + substrate stat_deltas resolves to a registry key or explicit not_descriptors row — count violations) and A18 formula single-source (every derived-value formula has exactly ONE defining surface, others cite it — count multi-definition quantities). These backlog counts are the audit's headline numbers.` },
]

// retry wrapper (wf_combat_critique.js precedent): agent() returns null on skip/terminal error
async function A(p, o) {
  for (let i = 0; i < 3; i++) {
    const r = await agent(p, o)
    if (r) return r
    log(`retry ${(o && o.label) || 'agent'} (attempt ${i + 1} returned null)`)
  }
  return await agent(p, o)
}

phase('Sweep')
const finders = await parallel(FAMILIES.map(f => () => agent(
  `${SHARED}\n\n=== YOUR FINDER FAMILY: F-${f.key} (${f.title}) ===\nSweep ONLY this surface family. Read the cited files (resolve heads via ${ROOT}/CURRENT.md where told).\nFOCUS: ${f.focus}\n\nProduce the COMPLETE quantity inventory for this family (one item per named quantity occurrence-site with formula/value verbatim + provenance tags), plus findings you can already prove from within this family alone, plus honest coverage notes (state explicitly anything skipped). Deterministic extraction — quote, cite, do not editorialize.`,
  { schema: FINDER_SCHEMA, label: `find:${f.key}`, phase: 'Sweep', model: f.model }
)))
const finderResults = finders.filter(Boolean)
// P7a · a finder family that swept a surface and found nothing is either a clean surface or an
// agent that never opened it, and those are indistinguishable in the totals below. Route each
// through the run so the second case raises an alarm the reader can take to the coverage notes.
for (const f of finderResults) run.lens(`find:${f.family}`, f.findings || [])
run.critiqued('Sweep', FAMILIES.length, finderResults.length)
log(`Sweep complete: ${finderResults.length}/${FAMILIES.length} families, ${finderResults.reduce((n, r) => n + r.items.length, 0)} inventory items, ${finderResults.reduce((n, r) => n + r.findings.length, 0)} early findings`)

phase('Census')
const census = await A(
  `${SHARED}\n\n=== CENSUS MERGE (you are the single merge node — barrier stage) ===\nBelow are ${finderResults.length} finder-family inventories (JSON). Merge them into ONE quantity census:\n1. Collapse aliases/synonyms onto one row per CONCEPT (Vitality->Endurance etc. per descriptor_registry aliases; where two names might be one concept but no registry alias says so, keep separate rows and cross-link in divergences — that IS a synonym finding).\n2. Assign each row its cluster: C1 attributes/aliases/aggregates · C2 derived values · C3 pools · C4 tracks+clocks · C5 faction/settlement stats · C6 code constants/export-pipeline · C7 = none (C7 is a meta-cluster; give rows their substantive cluster).\n3. defining_surface = the canonical site per CURRENT.md resolution rules; if genuinely undecidable write AMBIGUOUS:<candidates> and set status AMBIGUOUS.\n4. Join key_bindings across families (CONTRACT/SIM finders saw Key payload touches).\n5. Record every formula variant with its surface — do NOT pick a winner silently.\n6. status per row: COHERENT / DRIFTED / AMBIGUOUS / ORPHANED / DEAD / UNREGISTERED-LOAD-BEARING.\nTHEN write these files (your ONLY permitted writes, into the audit folder):\n- ${AUD}/01_workings/finder_F-<FAMILY-KEY>.json — one per finder family below, its JSON verbatim (pretty-printed), preserving the raw sweep evidence.\n- ${AUD}/02_census/quantity_census.yaml — machine-readable: header comment (generated-by, date 2026-07-08, anchor ED-IN-0029, QUARANTINE-note: evidence artifact, not a registry) then rows: as a YAML list matching your schema.\n- ${AUD}/02_census/quantity_census.md — human view: one table per cluster (Name | Kind | Defining surface | Formula(s) | Registered | Key bindings | Status), a divergence-highlights section, and totals.\nReturn the full rows JSON + merge_notes.\n\nFINDER INVENTORIES:\n${JSON.stringify(finderResults)}`,
  { schema: CENSUS_SCHEMA, label: 'census-merge', phase: 'Census', model: 'sonnet', effort: 'high' }
)
log(`Census: ${census.rows.length} rows (${census.rows.filter(r => r.status !== 'COHERENT').length} non-coherent)`)

phase('Validate')
const validation = await A(
  `${SHARED}\n\n=== CENSUS SPOT-CHECK ===\nRead ${AUD}/02_census/quantity_census.yaml. Pick 10 rows spread across clusters and statuses (deterministic pick: sort rows by canonical_name, take every Nth so you cover 10). For each, open the cited defining_surface and one cited formula surface and verify the census row states them accurately (formula verbatim, line number correct within +/-3, status defensible). verdict fail on ANY inaccuracy, with the correction in note. READ-ONLY — write nothing.`,
  hCritic({ schema: VALIDATE_SCHEMA, label: 'census-validate', phase: 'Validate', model: 'haiku' })
)
log(`Census spot-check: ${validation.pass_count} pass / ${validation.fail_count} fail`)

// Trace+dossier then critic per cluster — pipeline, no barrier between the two stages
phase('Trace')
const clusterResults = await pipeline(
  CLUSTERS,
  (c) => A(
    `${SHARED}\n\n=== CLUSTER DOSSIER: ${c.key} — ${c.title} (agonist) ===\nYour census rows (JSON below) are the starting map — verify against disk, then TRACE ALL DIRECTIONS for each quantity: definition -> params prose -> design heads -> module_contracts state/derivations -> Key payload bindings (armature §1-§3, key_type_registry required_payload_fields, engine/substrate/keys.py) -> sim/engine code -> typed export -> Godot port. Branch on every discovered edge; follow consumers you find mid-trace.\nFOCUS: ${c.focus}\n\nProduce findings (severity/kind/calibration per SHARED), unification_options (Jordan-rulable, each with a recommended default + what open ED/queue item it feeds), and registry_delta_candidates (quantities that should gain descriptor_registry keys — armature §3 analog).\nTHEN write ${AUD}/01_workings/dossier_${c.key}.md (your ONLY permitted write): title + one-paragraph headline, the trace narrative per quantity (with file:line), findings table, unification options table. Set dossier_written to that path.\nBe adversarial with the census: if a row is wrong, say so (that is also a finding against the census).\n\nCENSUS ROWS FOR THIS CLUSTER (plus cross-cluster rows you may need):\n${JSON.stringify(census.rows.filter(r => r.cluster === c.key))}\n\nCENSUS TOTALS FOR CONTEXT: ${census.rows.length} rows; validation spot-check ${validation.pass_count}p/${validation.fail_count}f.`,
    { schema: DOSSIER_SCHEMA, label: `dossier:${c.key}`, phase: 'Trace', model: 'sonnet' }
  ),
  (dossier, c) => dossier && run.attempt('Critic', A(
    `${SHARED}\n\n=== ADVERSARIAL CRITIC: ${c.key} — ${c.title} (antagonist relay — you never saw the agonist's reasoning, only its output) ===\nYou are READ-ONLY. Do not create or modify ANY file.\nThe dossier output (JSON) is below. Attack it:\n1. Per finding: re-verify against disk. uphold / overturn (claim false or stale) / soften (severity inflated, or actually KNOWN-TRACKED — name the ED) / sharpen (worse than claimed — escalate).\n2. Per unification_option: is the recommended default actually neutral bookkeeping, or does it smuggle a design call that must stay an open fork? Does it violate lane scoping (SC/SE/PC-owned)?\n3. Conformance: did the dossier invent criteria beyond the armature/holonic/registry discipline? Rule a fork? Use build-state as verdict evidence (cardinal rule)?\n4. missed: hunt for at least the OBVIOUS defect class the dossier under-covered (read 2-3 of its cited surfaces yourself and one it did NOT cite).\nDefault to skepticism — an audit finding that survives you should be bankable.\n\nDOSSIER (JSON):\n${JSON.stringify(dossier)}`,
    hCritic({ schema: CRITIC_SCHEMA, label: `critic:${c.key}`, phase: 'Critic', model: 'sonnet' })
  )).then(critic => ({ cluster: c.key, title: c.title, dossier, critic }))
)
const clusters = clusterResults.filter(Boolean).filter(r => r.dossier)
log(`Clusters complete: ${clusters.length}/7 dossiers, ${clusters.filter(r => r.critic).length} critic passes`)
run.critiqued('Trace', clusters.length, clusters.filter(r => r.critic).length)

// P8 · the uphold/overturn/soften/sharpen funnel IS a disagreement record — it just had no shape,
// so the Synthesis stage was free to fold a dispute in silently, or to drop it. Anything other than
// `uphold` is now a record the synthesis MUST rule on. A critic's `missed` finding is not a dispute:
// nobody contradicted it, so it enters as an ordinary finding.
const LAYER_BY_CRITIC = { overturn: 'evidence', soften: 'severity', sharpen: 'severity' }
const ROOT_BY_CRITIC = { overturn: 'measurement-vs-assertion', soften: 'severity-calibration', sharpen: 'severity-calibration' }
for (const r of clusters) {
  for (const v of ((r.critic && r.critic.verdicts) || [])) {
    if (v.verdict === 'uphold') continue
    const src = ((r.dossier && r.dossier.findings) || []).find(f => f.id === v.target_id || `${r.cluster}:${f.id}` === v.target_id)
    run.dispute({
      finding_id: `${r.cluster}:${v.target_id}`,
      layer_disputed: LAYER_BY_CRITIC[v.verdict] || 'interpretation',
      root_cause: ROOT_BY_CRITIC[v.verdict] || 'ambiguous-spec',
      positions: [
        { by: `dossier:${r.cluster}`, holds: String((src && src.claim) || '').slice(0, 400), severity: src && src.severity },
        { by: `critic:${r.cluster}`, holds: String(v.reason || '').slice(0, 400), verdict: v.verdict },
      ],
      resolution_model: 'adjudicated-by-synthesis',
    })
  }
  // Lane scoping is the repo's own cross-domain boundary (CLAUDE.md §4): an IN-lane critic noting a
  // conformance problem that belongs to SC/SE/PC may REPORT it and may not rule on it. The harness
  // marks it `observation`, which is a terminal state no later adjudication can overwrite.
  const note = String((r.critic && r.critic.conformance_note) || '')
  if (/lane|SC-|SE-|PC-|MB-|FA-|out of scope/i.test(note)) {
    run.dispute({
      finding_id: `${r.cluster}:conformance`,
      layer_disputed: 'scope',
      root_cause: 'scope-boundary',
      positions: [{ by: `critic:${r.cluster}`, holds: note.slice(0, 600) }],
      cross_domain: true,
    })
  }
}

// P7b · rank by independent rediscovery across the seven clusters. These clusters trace the same
// quantities through different surfaces — prose, contracts, Key payloads, code, the typed export —
// so a defect that shows up in three of those traces is a pipeline-wide problem, not a local one.
// That is precisely the distinction this audit exists to draw, and it was being computed and thrown
// away every run.
const allFindings = [].concat(
  ...clusters.map(r => ((r.dossier && r.dossier.findings) || []).map(f => Object.assign({ lens: r.cluster }, f))),
  ...clusters.map(r => ((r.critic && r.critic.missed) || []).map(f => Object.assign({ lens: `critic:${r.cluster}` }, f))),
)
const ranked = hRediscover(allFindings, f => f.lens)
const corroborated = ranked.filter(g => g.rediscovery > 1)
log(`Rediscovery: ${corroborated.length}/${ranked.length} distinct finding(s) surfaced independently by 2+ clusters`)

phase('Synthesis')
const synthPrompt = `${SHARED}

=== SYNTHESIS — the armature-extension authorship node (final stage) ===
You have the full audit: census (+spot-check), 7 dossiers, 7 critic passes (JSON below). Apply the
critic funnel FIRST: drop overturned findings, adjust softened/sharpened severities, fold critic
"missed" findings in (marked critic-sourced). Then WRITE these files (your permitted writes — all
inside ${AUD}/):

1. ${AUD}/attribute_value_coherence_v1.md — the verdict-first corpus report. Status header:
   "## Status: PROPOSED (read-only audit, 2026-07-08) · Lane: IN · Anchor: ED-IN-0029". Sections:
   headline stats · the coherence picture per cluster (verdict-first, evidence-cited) · the
   collision/synonym/stale/export-drift registers as tables · the A17/A18 measured backlogs (C7) ·
   what this feeds (the KNOWN-TRACKED open items, each with what the audit adds to its decision
   surface).
2. ${AUD}/ed_options.md — the Jordan-rulable docket. One row per option: id (OPT-AV-1..N), what,
   recommended default, severity, feeds (ED/queue/lane), owning lane if not IN. Include at minimum:
   the roster decision surface (queue-13/ED-IN-0008), values_master retire-vs-regenerate
   (decision-queue 17), the descriptor_registry quantity-extension adoption, A17/A18 adoption +
   report-only sequencing, warn->block tier promotion, the hygiene batch (core.md:4 stale header,
   broken board_game/factions indexes, dead registry test), and the shaping-wave slot. Mark
   lane-owned items "feeds <LANE>, not ruled here" (armature §5.8/5.9 precedent).
3. ${AUD}/proposed_quantity_armature_extension.md — PROPOSED companion to
   systems/_architecture/key_echo_armature_v1.md (quantity layer). Status: PROPOSED, held back from
   merge-ratification (ED-1094). Mirror the armature's anatomy: §1 the quantity-contract row (bind
   the census row format as the per-quantity analog of the seam-contract row) · §2 registry deltas
   (armature §3 analog): the registry_delta_candidates consolidated, each with key, KIND, aliases,
   defining-surface citation, Class-B vetting note per PP-674 · §3 conformance checks (armature §4
   analog, same lifecycle report-only -> flip-on-zero-backlog): A17 stat-vocabulary closure and A18
   formula single-source, each with mechanical predicate, input surface, missing artifact, and the
   MEASURED backlog from C7 (A18's input tooling = the prose-drift detector, specified here, not
   built) · §4 the shaping-wave slot (armature §6.3 analog): "Quantity/descriptor unification wave
   (IN)" with its worklist (the hygiene batch + registry filing + tier promotion), sequenced against
   waves 1-5.
4. ${AUD}/finding_status.md — tallies: findings by severity/kind/calibration BEFORE and AFTER the
   critic funnel (uphold/overturn/soften/sharpen/missed counts per cluster), census stats
   (rows/statuses/spot-check), coverage notes from finders (including anything skipped).
5. ${AUD}/README.md — reading order + headline, modeled on
   audit/2026-07-08-pessimist-action-audit/README.md (status line: ED-IN-0029 · Lane IN ·
   READ-ONLY · PROPOSED, docket UNRULED). State loudly: nothing ratifies on merge; the docket and
   the extension are held back (ED-1094).
6. For each cluster, write ${AUD}/01_workings/critic_<CK>.md from the critic JSON (verdicts table +
   missed findings + conformance note). The dossier files already exist.

Severity discipline: keep P1 for "an engine/Godot consumer would ingest a wrong or ambiguous value".
Every claim in every file carries its file:line. Every docket option has a recommended default.

ADJUDICATION IS REQUIRED, NOT OPTIONAL. DISAGREEMENTS below is every place a critic contradicted a
dossier, with what is disputed and why. Return one \`adjudications\` entry per record, ruling for one
side from your OWN reading of the cited surface — "the critic said so" is not a ruling. A record you
cannot settle from the files is ruled "unresolved" WITH the specific check that would settle it;
that is a real outcome and it belongs in finding_status.md. A record you simply do not mention is
the failure this field exists to prevent: it disappears while looking resolved.
Records with status "observation" are OUT-OF-LANE and are NOT yours to rule on. Carry them into
finding_status.md verbatim as observations routed to the owning lane. Do not adjudicate them.

WEIGHT BY CORROBORATION. REDISCOVERY below counts how many INDEPENDENT clusters surfaced each
finding while tracing different surfaces of the same pipeline. Treat a defect three clusters hit as
structural and lead the report with it; treat a solitary one as one cluster's reading until you have
checked the surface yourself. Say which is which — a reader cannot tell corroborated from singular
in a flat findings table, and that difference is most of the audit's value.

Return the summary JSON (headline, files_written, confirmed counts, docket_items, adjudications).

CENSUS: ${JSON.stringify({ rows: census.rows, merge_notes: census.merge_notes, validation })}

CLUSTER RESULTS (dossier + critic per cluster):
${JSON.stringify(clusters)}

DISAGREEMENTS (JSON): ${JSON.stringify(run.disagreements)}

REDISCOVERY (JSON): ${JSON.stringify(ranked.map(g => ({ key: g.key, rediscovery: g.rediscovery, lenses: g.lenses })))}`

// This node was `model: 'fable'` with an opus fallback. Jordan ruled 2026-07-28 that fable is a
// READ-ONLY audit / planner / orchestrator / guardrail tier and NOT a synthesis or artifact-
// authorship tier (CLAUDE.md §10) — and this node writes six files, so it is the clearest possible
// case of what the ruling excludes. Opus at max effort was already the declared fallback; it is now
// simply the node, and the two-attempt fable dance and its opus retry collapse into A()'s existing
// retry. tools/ci_wf_harness_check.py fails any workflow that puts fable back on a writing stage.
const synth = await A(synthPrompt, { schema: SYNTH_SCHEMA, label: 'synthesis', phase: 'Synthesis', model: 'opus', effort: 'max' })
for (const a of ((synth && synth.adjudications) || [])) {
  run.adjudicate(a.finding_id, `${a.ruling}: ${a.reasoning}`, 'synthesis')
}

// The guardrail slot IS where fable belongs under the ruling: read-only, writes nothing, rules on
// the run rather than authoring it. It stays on opus here for the same reason as the social-contest
// adjudicator — §10 makes fable an upgrade trigger, never a default, and nothing yet shows opus
// failing this node. Promote it only on evidence, and record the evidence when you do.
phase('Guardrail')
const guardrail = await A(
  [
    'RUN GUARDRAIL. You are read-only and you write nothing. You are not re-auditing the subject —',
    'you are judging whether THIS RUN produced a bankable result, and your output goes to a human',
    'deciding how much to trust it.',
    '',
    'RUN SUMMARY (JSON):', JSON.stringify(run.summary()),
    '',
    'SYNTHESIS RETURN (JSON):', JSON.stringify(synth),
    '',
    'Rule on four things, each in one or two sentences with the evidence you used:',
    ' 1. COVERAGE. Did every finder family and cluster actually run, and does any null_result signal',
    '    line up with a coverage note that explains it? An unexplained silence is a hole, not a clean surface.',
    ' 2. ADJUDICATION. Is every non-observation disagreement ruled on? Name any that are not.',
    ' 3. CORROBORATION. Does the report lead with findings multiple clusters hit independently, or',
    '    with whichever finding was written most confidently?',
    ' 4. THE CAPS. Was anything truncated, sampled or skipped without being declared? (§0.1 point 5:',
    '    a silent cap reads as full coverage.)',
    'Then give an overall verdict: bankable / bankable-with-caveats / not-bankable, and say what a',
    'reader should re-check first.',
  ].join('\n'),
  hCritic({
    label: 'guardrail:run', phase: 'Guardrail', model: 'opus', effort: 'high',
    schema: {
      type: 'object', additionalProperties: false,
      required: ['coverage', 'adjudication', 'corroboration', 'undeclared_caps', 'verdict', 'recheck_first'],
      properties: {
        coverage: { type: 'string' },
        adjudication: { type: 'string' },
        corroboration: { type: 'string' },
        undeclared_caps: { type: 'string' },
        verdict: { type: 'string', enum: ['bankable', 'bankable-with-caveats', 'not-bankable'] },
        recheck_first: { type: 'string' },
      },
    },
  }),
)

const summary = run.summary()
if (summary.degraded) log(`[harness] run degraded — stop_reason=${summary.stop_reason}; the results below are complete, read the signals before banking them`)

return {
  run: summary,
  guardrail,
  headline: synth && synth.headline,
  files_written: synth && synth.files_written,
  confirmed: synth && { P1: synth.confirmed_p1, P2: synth.confirmed_p2, P3: synth.confirmed_p3 },
  docket_items: synth && synth.docket_items,
  rediscovery: ranked.map(g => ({ key: g.key, rediscovery: g.rediscovery, lenses: g.lenses })),
  corroborated,
  census_rows: census.rows.length,
  census_validation: { pass: validation.pass_count, fail: validation.fail_count },
  finder_families: finderResults.length,
  clusters_completed: clusters.length,
  finder_payloads: finderResults.map(f => ({ family: f.family, items: f.items.length, findings: f.findings.length, coverage: f.coverage_notes })),
}
