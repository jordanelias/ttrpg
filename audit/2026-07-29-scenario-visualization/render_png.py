"""render_png.py — rasterise scenarios.html to PNG with the pre-installed headless Chromium.

Separate from render_scenarios.py on purpose: SVG generation is pure and testable, rasterisation
needs a browser. Same split the existing research/diagrams/mass_battle_formations/ generator uses.

Emits one PNG per scenario (so each can be read on its own at full resolution by machine vision)
plus a full-page contact sheet. Machine-vision review is the POINT of the PNGs — an SVG in a repo
nobody opens is not a comparison against history.

    python3 audit/2026-07-29-scenario-visualization/render_png.py
"""
import json
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    from playwright.sync_api import sync_playwright
    scale = os.environ.get('VIZ_SCALE','historical')
    html = os.path.join(_HERE, f'scenarios_{scale}.html')
    if not os.path.exists(html):
        print(f"missing {html} — run render_scenarios.py first", file=sys.stderr)
        return 2
    manifest = json.load(open(os.path.join(_HERE, f'manifest_{scale}.json'), encoding='utf-8'))
    png_dir = os.path.join(_HERE, f'png_{scale}')
    os.makedirs(png_dir, exist_ok=True)

    exe = os.environ.get('CHROMIUM_PATH', '/opt/pw-browsers/chromium')
    with sync_playwright() as pw:
        launch = {'args': ['--no-sandbox', '--disable-dev-shm-usage']}
        if os.path.exists(exe):
            launch['executable_path'] = exe
        browser = pw.chromium.launch(**launch)
        page = browser.new_page(viewport={'width': 1700, 'height': 1200},
                                device_scale_factor=2)
        page.goto('file://' + html)
        page.wait_for_timeout(400)
        sheet = os.path.join(_HERE, f'contact_sheet_{scale}.png')
        page.screenshot(path=sheet, full_page=True)
        print('wrote', sheet)
        for rid in manifest['scenarios']:
            el = page.query_selector(f'#{rid}')
            if el is None:
                print('  [warn] no element for', rid, file=sys.stderr)
                continue
            p = os.path.join(png_dir, f'{rid}.png')
            el.screenshot(path=p)
            print('  wrote', p)
        browser.close()
    return 0


if __name__ == '__main__':
    sys.exit(main())
