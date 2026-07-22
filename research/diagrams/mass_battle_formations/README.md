# Mass-battle formations — engine vs history (visual comparison)

Reviewable comparison of the mass-battle engine's deployment/pathing (after the **ED-MB-0017** fix)
against historical formation geometry. Sources for the historical side are in **`SOURCES.md`** (image
downloads are proxy-blocked, so the historical side is my schematic reconstruction from the cited
geometry + links to the canonical diagrams/animations for you to open).

## Files

| file | what it is |
|---|---|
| `comparison_engine_vs_history.html` | interactive: per-formation, historical schematic (left) vs engine sim tick-by-tick (right). Open in a browser. |
| `comparison_rendered.png` | a rendered screenshot of the above (for quick review without running anything). |
| `cannae_wrap_detail.png` | the double-envelopment at ticks 0/4/8/12/16/20 — the wrap needs until ~t16 to complete. |
| `generate_comparison.py` | the generator (reproducible: `python generate_comparison.py out.html`). |
| `SOURCES.md` | citations + links to the canonical historical diagrams/animations. |

## Method

- **Machine-vision comparison:** the sim output was rendered to PNG (headless Chromium) and inspected
  visually against the historical schematic, adversarially (looking for what's still wrong), not just
  asserted numerically. The geometry is also pinned by `tests/valoria/test_deployment_geometry.py`.
- Orientation (both sides): the enemy deploys at the **top**; our army (red) advances **upward**. Each
  dot is a cell, coloured by subunit.

## Findings (adversarial vision read)

**Fixed and confirmed:**
- **No subunit overlap (P-1)** — battle lines of 3, 7, and 11 subunits deploy as a clean, centred line;
  distinct subunits, no interpenetration. (Pre-fix: subunits deployed 4 cols apart, narrower than their
  ~6-col frontage, so they overlapped.)
- **Symmetric double envelopment (P-2)** — the centre sits on the anchor with wings straddling it on
  **both** flanks (left + right), which then wheel **opposite senses** around opposite flanks. In
  `cannae_wrap_detail.png` the wings reach the enemy's rear-left and rear-right corners by t16–t20 — a
  genuine envelopment. (Pre-fix: both wings deployed to one side of centre and wrapped the same flank —
  the "weird wheel" with no ring.)
- **Echeloned refused flank (P-3)** — the refused wing deploys clearly **rearward** of the strong wing
  (and laterally offset), out of the initial line of contact, as an oblique order should. (Pre-fix: the
  refused wing sat level with the strong wing and overlapped it.)

**Honest caveats (still imperfect):**
- **The wrap needs time.** The wings complete the encirclement only by ~t16–t20 (they have to march wide
  and around); at t15 it's mid-wrap. A faster/committed enveloping march would tighten it — a follow-on.
- **No cavalry ride-around.** History closes the Cannae ring with cavalry riding across the rear
  (a distinct transit phase); the sim's infantry wings reach the rear *corners* but nothing closes the
  rear-*centre*. The ring is a horseshoe, not a full circle. (`_envelop_goal` models the infantry wrap;
  the cavalry rear-transit is unmodelled.)
- **Single line, not a reserve/triplex system.** The battle-line sim deploys one lateral line; the Roman
  *triplex acies* schematic (3 depth-lines, quincunx, line-relief) is shown as the historical ideal but
  the engine does not model reserve lines / depth-line relief yet.
- **Envelopment still often loses** in raw outcome (a separate matter from geometry) — that is the DG-6
  over-decisiveness / envelopment-not-rewarded issue tracked under ED-MB-0016 (the grounded friction +
  the still-needed conjunctive envelopment gate), not a pathing bug. The structurally-correct wrap this
  fix delivers is the *precondition* for rewarding envelopment correctly.

See `../../../audit/2026-07-22-mass-battle-stress-test/pathing_deployment_diagnosis.md` for the full
diagnosis and the historical-geometry research synthesis it was built from.
