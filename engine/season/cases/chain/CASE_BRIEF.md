# CASE-EXTRACTION BRIEF — produce runnable case specs, not prose

You are extracting **case requirements** that will be executed against a tracer implementing a
proposed "idealized code shape". Your output is DATA, not analysis. Another process maps each
requirement onto the shape and records where the shape cannot carry it.

## THE RULE THAT MATTERS MOST
**Describe what the case REQUIRES in shape-neutral language.** Do not name the shape's types
(Person/Rung/Office/Site/Proposition/Tenure/Claim) and do not judge whether the shape can do it —
you have not read the shape and must not. Say what has to be *possible* for this character's season
or this arc's story to happen at all.

Good: `"a person with no office must be able to put a demand in front of someone who does"`
Bad:  `"needs a Petition -> carry -> DocketItem chain"`  (that is the shape's answer, not the need)

Good: `"the outcome of a private conversation must be able to change what a third party believes,
       later, without that third party having been present"`
Bad:  `"needs witness() to be called per person"`

## OUTPUT — YAML, exactly this shape, nothing else
```yaml
- id: <NPC-0xx or ARC-nn>
  name: <name / arc title>
  one_line: <what this case is, in one line>
  scale: <person | settlement | faction | realm | world>
  season_requires:          # 4-12 rows. The atomic things that must be possible.
    - need: <one sentence, shape-neutral, mechanically specific>
      why: <what is lost if it is impossible — the concrete play or story beat>
      hardness: <core | important | flavour>
  temporal:                 # how this case sits in time
    span_seasons: <int or "ongoing">
    needs_memory_of: <what must persist across seasons for this to work>
    needs_deadline: <yes/no — does something have to happen BY a date>
  who_acts:                 # every actor whose choice this case depends on
    - <name or role>
  knowledge:                # the epistemic requirements
    - <who must know / not know what, and how they come to know it>
  ends_when: <the condition under which this case concludes, or "never">
```

## DISCIPLINE
- **Every `need` must be falsifiable** — a thing that either can or cannot be done.
- **`hardness: core`** means: cut this and the case is not this case any more. Be strict; most
  needs are `important`, few are `core`.
- If a source is marked STRUCK / SUPERSEDED / RETIRED, still extract it but set
  `one_line` to begin `[STRUCK] ` — downstream needs to know not to treat it as live.
- Where the source is vague, write `need: "UNCLEAR: <what the source fails to say>"` rather than
  inventing a mechanism. An unclear source is itself data.
- No preamble, no commentary. Emit only the YAML list.
