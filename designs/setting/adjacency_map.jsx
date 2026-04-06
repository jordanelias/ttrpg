import { useState } from "react";

export default function App() {
  const territories = {
    // Crown (6)
    T1:  { id: 'T1',  name: 'Valorsplatz',  sub: 'Capital', control: 'Crown', color: '#3b82f6', x: 560, y: 245 },
    T2:  { id: 'T2',  name: 'Kronmark',     sub: 'Heartland', control: 'Crown', color: '#3b82f6', x: 475, y: 205 },
    T3:  { id: 'T3',  name: 'Lowenskyst',   sub: 'Border Fortress', control: 'Crown', color: '#3b82f6', x: 510, y: 58 },
    T5:  { id: 'T5',  name: 'Feldmark',     sub: 'Breadbasket', control: 'Crown', color: '#3b82f6', x: 500, y: 375 },
    T6:  { id: 'T6',  name: 'Stillhelm',    sub: 'S. Farmland', control: 'Crown', color: '#3b82f6', x: 410, y: 475 },
    T14: { id: 'T14', name: 'Ehrenfeld',    sub: 'Military Hinge', control: 'Crown', color: '#3b82f6', x: 373, y: 285 },

    // Hafenmark (4)
    T7:  { id: 'T7',  name: 'Rendstad',     sub: 'Highland Timber', control: 'Hafenmark', color: '#f59e0b', x: 230, y: 210 },
    T8:  { id: 'T8',  name: 'Gransol',      sub: 'Hafenmark Capital', control: 'Hafenmark', color: '#f59e0b', x: 250, y: 118 },
    T10: { id: 'T10', name: 'Spartfell',    sub: 'Border Castle', control: 'Hafenmark', color: '#f59e0b', x: 155, y: 130 },
    T17: { id: 'T17', name: 'Halvarshelm',  sub: 'Northern Mines', control: 'Hafenmark', color: '#f59e0b', x: 340, y: 60 },

    // Varfell (4)
    T4:  { id: 'T4',  name: 'Grauwald',     sub: 'Highland Timber', control: 'Varfell', color: '#22c55e', x: 230, y: 315 },
    T11: { id: 'T11', name: 'Halvardshelm', sub: 'Central Fjords', control: 'Varfell', color: '#22c55e', x: 125, y: 278 },
    T12: { id: 'T12', name: 'Sigurdshelm',  sub: 'Varfell Seat', control: 'Varfell', color: '#22c55e', x: 128, y: 400 },
    T13: { id: 'T13', name: 'Oastad',       sub: 'Southern Fjords', control: 'Varfell', color: '#22c55e', x: 252, y: 468 },

    // Church (1)
    T9:  { id: 'T9',  name: 'Himmelenger',  sub: 'Cathedral City', control: 'Church', color: '#a855f7', x: 390, y: 165 },

    // Other
    T15: { id: 'T15', name: 'Askeheim',     sub: 'Southernmost', control: 'Uncontrolled', color: '#6b7280', x: 340, y: 588 },
    T16: { id: 'T16', name: 'Schoenland',   sub: 'Island Republic', control: 'Schoenland', color: '#e5e7eb', x: 648, y: 168 },
  };

  const edges = [
    // === NORTHERN BELT ===
    ['T3', 'T2'],   // Lowenskyst (Crown) — Kronmark (Crown)
    ['T3', 'T17'],  // Lowenskyst (Crown) — Halvarshelm (Hafenmark)
    ['T3', 'T9'],   // Lowenskyst (Crown) — Himmelenger (Church)

    ['T17', 'T9'],  // Halvarshelm (Hafenmark) — Himmelenger (Church)
    ['T17', 'T8'],  // Halvarshelm (Hafenmark) — Gransol (Hafenmark)

    ['T9', 'T2'],   // Himmelenger (Church) — Kronmark (Crown)
    ['T9', 'T8'],   // Himmelenger (Church) — Gransol (Hafenmark)
    ['T9', 'T14'],  // Himmelenger (Church) — Ehrenfeld (Crown)

    ['T8', 'T10'],  // Gransol (Hafenmark) — Spartfell (Hafenmark)
    ['T8', 'T7'],   // Gransol (Hafenmark) — Rendstad (Hafenmark)

    ['T10', 'T11'], // Spartfell (Hafenmark) — Halvardshelm (Varfell)

    // === MIDDLE BAND ===
    ['T2', 'T1'],   // Kronmark (Crown) — Valorsplatz (Crown)
    ['T2', 'T14'],  // Kronmark (Crown) — Ehrenfeld (Crown)

    ['T1', 'T14'],  // Valorsplatz (Crown) — Ehrenfeld (Crown)
    ['T1', 'T16'],  // Valorsplatz (Crown) — Schoenland (sea)
    ['T1', 'T5'],   // Valorsplatz (Crown) — Feldmark (Crown)

    ['T14', 'T4'],  // Ehrenfeld (Crown) — Grauwald (Varfell)
    ['T14', 'T5'],  // Ehrenfeld (Crown) — Feldmark (Crown)

    ['T7', 'T4'],   // Rendstad (Hafenmark) — Grauwald (Varfell)

    // === WESTERN-CENTRAL ===
    ['T4', 'T12'],  // Grauwald (Varfell) — Sigurdshelm (Varfell)

    ['T11', 'T12'], // Halvardshelm (Varfell) — Sigurdshelm (Varfell)

    // === SOUTHERN ZONE ===
    ['T5', 'T6'],   // Feldmark (Crown) — Stillhelm (Crown)

    ['T12', 'T13'], // Sigurdshelm (Varfell) — Oastad (Varfell)

    ['T13', 'T15'], // Oastad (Varfell) — Askeheim (GATE 1)
    ['T13', 'T6'],  // Oastad (Varfell) — Stillhelm (Crown)

    ['T6', 'T15'],  // Stillhelm (Crown) — Askeheim (GATE 2)
  ];

  const [hovered, setHovered] = useState(null);

  const getAdjacent = (id) => {
    const adj = new Set();
    edges.forEach(([a, b]) => {
      if (a === id) adj.add(b);
      if (b === id) adj.add(a);
    });
    return adj;
  };

  const highlightSet = hovered ? getAdjacent(hovered) : new Set();

  const getEdgeStyle = (a, b) => {
    const isGate = (a === 'T15' || b === 'T15');
    const isSea = (a === 'T16' || b === 'T16');
    const isHighlighted = hovered && (a === hovered || b === hovered);
    if (hovered && !isHighlighted) return { stroke: '#1f2937', strokeWidth: 1, opacity: 0.12, dash: 'none' };
    return {
      stroke: isGate ? '#ef4444' : isSea ? '#06b6d4' : '#6b7280',
      strokeWidth: isGate ? 2.5 : isSea ? 2 : isHighlighted ? 2.5 : 1.2,
      opacity: isHighlighted ? 1 : 0.4,
      dash: isSea ? '8,4' : 'none',
    };
  };

  const R = 30;

  return (
    <div style={{ background: '#111827', minHeight: '100vh', display: 'flex', flexDirection: 'column', alignItems: 'center', padding: '14px 8px' }}>
      <h1 style={{ color: '#f9fafb', fontSize: '18px', fontWeight: 700, margin: '0 0 2px', fontFamily: 'system-ui' }}>VALORIA — Territory Adjacency Map</h1>
      <p style={{ color: '#9ca3af', fontSize: '11px', margin: '0 0 10px', fontFamily: 'system-ui', textAlign: 'center' }}>Tap territory to highlight connections. Red = Southernmost gate. Dashed cyan = sea route.</p>

      <div style={{ display: 'flex', gap: '12px', marginBottom: '10px', flexWrap: 'wrap', justifyContent: 'center' }}>
        {[
          { label: 'Crown (6)', color: '#3b82f6' },
          { label: 'Varfell (4)', color: '#22c55e' },
          { label: 'Hafenmark (4)', color: '#f59e0b' },
          { label: 'Church (1)', color: '#a855f7' },
          { label: 'Uncontrolled', color: '#6b7280' },
          { label: 'Schoenland', color: '#e5e7eb' },
        ].map(({ label, color }) => (
          <div key={label} style={{ display: 'flex', alignItems: 'center', gap: '5px' }}>
            <div style={{ width: 12, height: 12, borderRadius: '50%', background: color, border: '1.5px solid #374151' }} />
            <span style={{ color: '#d1d5db', fontSize: '10px', fontFamily: 'system-ui' }}>{label}</span>
          </div>
        ))}
      </div>

      <svg viewBox="0 0 720 660" style={{ width: '100%', maxWidth: '720px', height: 'auto' }}>
        <path d="M 50 32 L 120 12 L 190 28 L 270 8 L 350 22 L 430 10 L 510 24 L 570 14 L 630 30"
              fill="none" stroke="#78716c" strokeWidth="2.5" strokeDasharray="6,3" opacity="0.5" />
        <text x="340" y="6" textAnchor="middle" fill="#a8a29e" fontSize="9" fontFamily="system-ui" fontStyle="italic">— ALTONIA (beyond mountains) —</text>

        <ellipse cx="360" cy="625" rx="240" ry="55" fill="#ef4444" opacity="0.06" />
        <ellipse cx="360" cy="618" rx="160" ry="35" fill="#ef4444" opacity="0.1" />
        <ellipse cx="360" cy="612" rx="80" ry="18" fill="#ef4444" opacity="0.16" />
        <text x="360" y="652" textAnchor="middle" fill="#ef4444" fontSize="9" fontFamily="system-ui" opacity="0.6">CALAMITY EPICENTER / FORGETTING ZONE</text>

        <path d="M 215 45 C 225 140, 210 240, 230 340 C 240 390, 248 420, 255 445"
              fill="none" stroke="#78716c" strokeWidth="1.2" strokeDasharray="4,4" opacity="0.3" />
        <text x="198" y="225" fill="#a8a29e" fontSize="8" fontFamily="system-ui" transform="rotate(-82, 198, 225)" opacity="0.4">western ridges</text>

        <text x="680" y="360" fill="#164e63" fontSize="10" fontFamily="system-ui" fontStyle="italic" opacity="0.4">EASTERN</text>
        <text x="680" y="373" fill="#164e63" fontSize="10" fontFamily="system-ui" fontStyle="italic" opacity="0.4">SEA</text>
        <text x="38" y="345" fill="#164e63" fontSize="10" fontFamily="system-ui" fontStyle="italic" opacity="0.4">WESTERN</text>
        <text x="38" y="358" fill="#164e63" fontSize="10" fontFamily="system-ui" fontStyle="italic" opacity="0.4">OCEAN</text>

        <text x="155" y="95" fill="#f59e0b" fontSize="7" fontFamily="system-ui" opacity="0.6">NW Pass ↑</text>
        <text x="498" y="38" fill="#3b82f6" fontSize="7" fontFamily="system-ui" opacity="0.6">NE Pass ↑</text>

        {/* Central Lake - between Ehrenfeld, Feldmark, Korntal, Sudwald */}
        <ellipse cx="330" cy="405" rx="75" ry="50" fill="#0e4a6e" opacity="0.35" />
        <ellipse cx="330" cy="405" rx="55" ry="35" fill="#0c5a82" opacity="0.3" />
        <text x="330" y="410" textAnchor="middle" fill="#38bdf8" fontSize="8" fontFamily="system-ui" fontStyle="italic" opacity="0.5">Eidursjo</text>

        {edges.map(([a, b], i) => {
          const ta = territories[a];
          const tb = territories[b];
          const s = getEdgeStyle(a, b);
          return <line key={i} x1={ta.x} y1={ta.y} x2={tb.x} y2={tb.y}
            stroke={s.stroke} strokeWidth={s.strokeWidth} opacity={s.opacity} strokeDasharray={s.dash} />;
        })}

        <text x={(territories.T13.x + territories.T15.x) / 2 - 32} y={(territories.T13.y + territories.T15.y) / 2 - 2}
          fill="#ef4444" fontSize="8" fontWeight="700" fontFamily="system-ui">GATE 1</text>
        <text x={(territories.T6.x + territories.T15.x) / 2 + 12} y={(territories.T6.y + territories.T15.y) / 2 + 2}
          fill="#ef4444" fontSize="8" fontWeight="700" fontFamily="system-ui">GATE 2</text>

        {Object.values(territories).map((t) => {
          const isH = hovered === t.id;
          const isAdj = highlightSet.has(t.id);
          const dim = hovered && !isH && !isAdj;
          const cnt = getAdjacent(t.id).size;
          return (
            <g key={t.id}
              onMouseEnter={() => setHovered(t.id)}
              onMouseLeave={() => setHovered(null)}
              onClick={() => setHovered(hovered === t.id ? null : t.id)}
              style={{ cursor: 'pointer' }}
              opacity={dim ? 0.2 : 1}>
              {isH && <circle cx={t.x} cy={t.y} r={R + 5} fill={t.color} opacity={0.2} />}
              <circle cx={t.x} cy={t.y} r={R}
                fill={isH ? t.color : '#1f2937'}
                stroke={t.color}
                strokeWidth={isH ? 3 : isAdj ? 2.5 : 1.8} />
              <text x={t.x} y={t.y - 8} textAnchor="middle" fill={isH ? '#111827' : t.color}
                fontSize="10" fontWeight="700" fontFamily="system-ui">{t.id.replace('T','')}</text>
              <text x={t.x} y={t.y + 4} textAnchor="middle" fill={isH ? '#111827' : '#f9fafb'}
                fontSize="7.5" fontWeight="600" fontFamily="system-ui">{t.name}</text>
              <text x={t.x} y={t.y + 14} textAnchor="middle" fill={isH ? '#374151' : '#9ca3af'}
                fontSize="6.5" fontFamily="system-ui">{t.sub}</text>
              {isH && <text x={t.x} y={t.y + 45} textAnchor="middle" fill="#d1d5db"
                fontSize="8" fontFamily="system-ui">{cnt} connections</text>}
            </g>
          );
        })}
      </svg>

      {hovered && (
        <div style={{ background: '#1f2937', border: '1px solid #374151', borderRadius: '8px', padding: '10px 14px', marginTop: '6px', maxWidth: '380px', width: '100%' }}>
          <div style={{ color: territories[hovered].color, fontSize: '13px', fontWeight: 700, fontFamily: 'system-ui' }}>
            {territories[hovered].name} ({hovered})
          </div>
          <div style={{ color: '#9ca3af', fontSize: '10px', fontFamily: 'system-ui', marginTop: '2px' }}>
            {territories[hovered].control} · {territories[hovered].sub}
          </div>
          <div style={{ color: '#d1d5db', fontSize: '10px', fontFamily: 'system-ui', marginTop: '5px' }}>
            Adjacent: {[...getAdjacent(hovered)].map(id => `${territories[id].name} (${id})`).join(', ')}
          </div>
        </div>
      )}
    </div>
  );
}
