# DESIGN NOTE: COMPANION APP

## Date: 2026-04-04
## Source: Systematic critique + cognitive load analysis

The reference architecture (META-3 in cogload_moderate_target.md) is a low-tech prototype of what should be a digital companion app. The game's tracking layer is computational; its experience layer is human. These should be separated.

## What the App Handles
- RS, Coherence, Certainty tracking (auto-updated on every Thread operation)
- Three-dimensional co-movement auto-effects (P-01 compliance automatic — no missed effects)
- Damage simultaneity in mass combat (Phase 6 Step 1 resolution)
- Seasonal accounting cascades (clock updates, threshold checks, NPC trigger evaluation)
- Conviction Track + Composure + Concentration tracking during social contests
- Strain computation (margin + Charisma modifier − Focus defence → lookup eliminated)
- Unit state tracking in mass combat (Size/Discipline/Morale checkboxes become app state)
- Cross-mode state transfer (Zoom In/Out variable inventory per state_transfer_spec.md)
- ×3 RS multiplier in mass battle Thread (applied automatically)

## What the Humans Handle
- All decisions (pool split, operation selection, argument style, battle plan, faction action)
- All narration (GM describes Leap phenomenology, Thread contact, Rendering Crisis, NPC behaviour)
- All roleplay (Beliefs, Knot relationships, faction politics, moral choices)
- All interpretation (what does Coherence 3 mean for THIS character? What does RS 22 feel like in THIS world?)

## Effect on Cognitive Load
With the app handling tracking, all systems drop to approximately:
- Decisions only (no lookups, no variable tracking, no arithmetic)
- Personal Combat: ~4.0 (Light-Moderate)
- Thread Operations: ~5.5 (Light-Moderate)
- Social Contest: ~4.5 (Light-Moderate)
- Mass Combat: ~5.0 (Light-Moderate)
- BG Turn: ~5.0 (Light-Moderate)
- Thread in Mass Combat: ~6.0 (Light-Moderate to Moderate)

The game becomes playable by narrative-first players. The complexity exists in the software, not in working memory.

## Implementation Priority
1. Faction stat + clock tracker (BG mode — highest immediate value)
2. Thread operation resolver (co-movement auto-effects + RS/Coherence updates)
3. Combat state tracker (damage simultaneity, unit cards, wound/Stamina)
4. Social contest tracker (Conviction Track + strain + Composure/Concentration)
5. Cross-mode state transfer (Zoom In/Out handoff)

## Note
This does not change any mechanic. Every formula, every constraint, every canon requirement remains identical. The app is an interface to the existing system, not a simplification of it.
