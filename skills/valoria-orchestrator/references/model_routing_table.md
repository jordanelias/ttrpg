# Model Routing Table
# Task type → model tier → rationale

| Task | Model | Rationale |
|------|-------|-----------|
| Chunking, section maps, indexing | Haiku 4.5 | Deterministic extraction; no reasoning needed |
| Find-and-replace, formatting | Haiku 4.5 | Scripted; model only for wrapping |
| Dice math, probability calculation | Haiku 4.5 | Arithmetic; script-driven |
| Mechanic audit (Modes A–E) | Sonnet 4.6 | Pattern recognition across large text |
| Simulation (Tier 1: combat, thread, social, mass battle) | Sonnet 4.6 | State machine reasoning |
| Simulation (Tier 2: TTRPG, BG, hybrid scenes) | Sonnet 4.6 | Multi-system orchestration |
| Canon compliance check | Sonnet 4.6 | Philosophical reasoning against P-01–P-14 |
| Compilation + assembly | Sonnet 4.6 | Judgment on section ordering and gate checks |
| Editorial decision tracking + propagation | Sonnet 4.6 | Affects-list verification requires reasoning |
| Ambiguous design intent | Opus 4.6 | Philosophical + creative synthesis |
| Setting/lore authorship | Opus 4.6 | Creative; requires editorial gate |
| Multi-step reasoning across dispersed docs | Opus 4.6 | Large-context synthesis |

## Downgrade Triggers
Before executing, assess:
- Is this purely deterministic? → Haiku
- Does it require reading one document and extracting fields? → Haiku
- Is it a yes/no compliance check with clear criteria? → Sonnet
- Does it require weighing competing philosophical considerations? → Opus

Flag downgrade opportunity before executing if current context model exceeds task needs.
