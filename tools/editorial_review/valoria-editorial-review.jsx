import { useState } from "react";

// ── Data loading ──────────────────────────────────────────────────────────────
// DATA is empty by default. Paste JSON into the load box to populate.
const EMPTY = [];

const SYSTEM_MAP = [
  ["board_game","Board Game"],["debate","Debate"],["threadwork","Threadwork"],
  ["mass_combat","Mass Combat"],["hybrid","Hybrid"],["combat","Combat"],
  ["worldbuilding","Worldbuilding / NPCs"],["core","Core"],["thread","Thread Ops"],
];

const P_COLOR = {"P1-BLOCKER":"#e05050","P1":"#e08030","P2":"#c0a020","P3":"#4488cc"};
const S_STYLE = {
  open:{bg:"#131a2a",tx:"#6a9fdd",lb:"Open"},
  provisional:{bg:"#201800",tx:"#ddaa30",lb:"Provisional"},
};

function groupItems(items) {
  const groups = {};
  for (const item of items) {
    let found = false;
    for (const [key, label] of SYSTEM_MAP) {
      if (item.tags && item.tags.includes(key)) {
        if (!groups[label]) groups[label] = [];
        groups[label].push(item);
        found = true; break;
      }
    }
    if (!found) { if (!groups["Other"]) groups["Other"] = []; groups["Other"].push(item); }
  }
  return groups;
}

function cleanDecision(d) {
  if (!d || d === "null" || d === "~") return null;
  return d.replace(/\[PROVISIONAL\]/g,"").replace(/\[GAP:[^\]]+\]/g,"").trim() || null;
}

function Item({ item, dec, onDec }) {
  const [showNote, setShowNote] = useState(false);
  const [note, setNote] = useState(dec?.note || "");
  const chosen = dec?.choice;
  const ss = S_STYLE[item.status] || S_STYLE.open;
  const cleanDec = cleanDecision(item.decision);

  const choose = (c) => onDec(item.id, { choice: chosen === c ? null : c, note });
  const saveNote = () => { onDec(item.id, { choice: chosen || null, note }); setShowNote(false); };

  const borderColor = chosen === "approve" ? "#2a5a2a" : chosen === "reject" ? "#5a2020" : "#1e2230";
  const bgColor = chosen === "approve" ? "#0b1a0b" : chosen === "reject" ? "#1a0b0b" : "#111420";

  return (
    <div style={{ background: bgColor, border: `1px solid ${borderColor}`, borderRadius: 6,
      padding: "12px 14px", marginBottom: 7, transition: "all 0.15s" }}>
      <div style={{ display:"flex", flexWrap:"wrap", gap:6, alignItems:"center", marginBottom:7 }}>
        <span style={{ fontFamily:"monospace", fontSize:13, fontWeight:700, color:"#ddd" }}>{item.id}</span>
        <span style={{ fontSize:10, fontWeight:700, letterSpacing:0.8, padding:"1px 6px",
          border:`1px solid ${P_COLOR[item.priority]||"#666"}`, color:P_COLOR[item.priority]||"#666",
          borderRadius:3, fontFamily:"monospace" }}>{item.priority}</span>
        <span style={{ fontSize:10, fontWeight:600, padding:"1px 7px", borderRadius:10,
          background: ss.bg, color: ss.tx }}>{ss.lb}</span>
        {(item.tags||[]).slice(0,2).map(t => (
          <span key={t} style={{ fontSize:9, color:"#556", background:"#181a24",
            padding:"1px 5px", borderRadius:3, fontFamily:"monospace" }}>{t}</span>
        ))}
      </div>
      <p style={{ margin:"0 0 6px", fontSize:13, color:"#bdb5a5", lineHeight:1.55 }}>{item.description}</p>
      {item.full_flag_text && item.full_flag_text !== item.description && (
        <p style={{ margin:"0 0 6px", fontSize:11, color:"#777", fontStyle:"italic", lineHeight:1.4 }}>
          {item.full_flag_text}
        </p>
      )}
      {cleanDec && (
        <div style={{ margin:"8px 0", padding:"7px 10px", background:"#141e14",
          borderLeft:"3px solid #3a6a3a", borderRadius:"0 4px 4px 0",
          fontSize:12, color:"#8fcc8f", lineHeight:1.5 }}>
          <span style={{ color:"#4a7a4a", fontWeight:700, fontSize:10, letterSpacing:0.8 }}>PROVISIONAL · </span>
          {cleanDec}
        </div>
      )}
      {item.source_file && (
        <div style={{ fontSize:10, color:"#445", fontFamily:"monospace", marginTop:4 }}>{item.source_file}</div>
      )}
      {showNote && (
        <div style={{ marginTop:8 }}>
          <textarea value={note} onChange={e => setNote(e.target.value)}
            placeholder="Your comment or decision…"
            style={{ width:"100%", minHeight:64, background:"#0c0e14", border:"1px solid #2a2d3a",
              borderRadius:4, color:"#c8c0b0", fontSize:12, padding:"7px 9px",
              resize:"vertical", fontFamily:"inherit", boxSizing:"border-box" }} />
          <button onClick={saveNote} style={{ marginTop:5, padding:"4px 14px",
            background:"#1a2040", border:"1px solid #334", borderRadius:4,
            color:"#8899cc", fontSize:11, cursor:"pointer" }}>Save</button>
        </div>
      )}
      {!showNote && dec?.note && (
        <div style={{ marginTop:7, padding:"5px 9px", background:"#141820",
          borderLeft:"3px solid #334", borderRadius:"0 4px 4px 0",
          fontSize:12, color:"#8899bb", lineHeight:1.4 }}>
          <span style={{ color:"#445", fontSize:10, fontWeight:700 }}>NOTE · </span>{dec.note}
        </div>
      )}
      <div style={{ marginTop:9, display:"flex", gap:7, flexWrap:"wrap" }}>
        {[["approve","✓ Approve","#2a5a2a","#1a3a1a","#6fcc6f"],
          ["reject","✕ Reject","#5a2020","#3a1010","#cc6f6f"]].map(([c,label,border,bg,color]) => (
          <button key={c} onClick={() => choose(c)} style={{
            padding:"5px 14px", borderRadius:4,
            border:`1px solid ${chosen===c ? border : border+"55"}`,
            background: chosen===c ? bg : "transparent",
            color: chosen===c ? color : color+"66",
            fontSize:12, fontWeight:600, cursor:"pointer", transition:"all 0.12s"
          }}>{label}</button>
        ))}
        <button onClick={() => setShowNote(!showNote)} style={{
          padding:"5px 12px", borderRadius:4, border:"1px solid #252840",
          background:"transparent", color: dec?.note ? "#7f99cc" : "#3a4a6a",
          fontSize:12, cursor:"pointer"
        }}>{dec?.note ? "✏ Edit note" : "✏ Note"}</button>
      </div>
    </div>
  );
}

function NavBar({ groups, decisions }) {
  return (
    <div style={{ position:"sticky", top:0, zIndex:10, background:"#090b12",
      borderBottom:"1px solid #181a26", padding:"7px 14px",
      display:"flex", gap:5, flexWrap:"wrap", overflowX:"auto" }}>
      {Object.entries(groups).map(([label, items]) => {
        const done = items.filter(i => decisions[i.id]?.choice).length;
        return (
          <a key={label} href={`#sec-${label.replace(/\s+/g,"-").replace(/[^a-zA-Z0-9-]/g,"")}`}
            style={{ fontSize:10, padding:"3px 9px", borderRadius:10,
              background: done===items.length ? "#0d1f0d" : "#14162a",
              border:`1px solid ${done===items.length ? "#2a5a2a" : "#232540"}`,
              color: done===items.length ? "#6acc6a" : "#5a6a8a",
              textDecoration:"none", flexShrink:0, fontWeight:600 }}>
            {label} {done}/{items.length}
          </a>
        );
      })}
    </div>
  );
}

// ── Main App ──────────────────────────────────────────────────────────────────

export default function App() {
  const [data, setData] = useState(EMPTY);
  const [rawInput, setRawInput] = useState("");
  const [loadError, setLoadError] = useState(null);
  const [loaded, setLoaded] = useState(false);

  const [decisions, setDecisions] = useState({});
  const [filter, setFilter] = useState("all");
  const [priFilter, setPriFilter] = useState("all");
  const [submitted, setSubmitted] = useState(false);
  const [copyLabel, setCopyLabel] = useState("Copy for Claude");

  const onDec = (id, d) => setDecisions(prev => ({ ...prev, [id]: d }));

  const handleLoad = () => {
    setLoadError(null);
    try {
      const parsed = JSON.parse(rawInput.trim());
      if (!Array.isArray(parsed)) throw new Error("Expected a JSON array.");
      setData(parsed);
      setDecisions({});
      setSubmitted(false);
      setLoaded(true);
    } catch(e) {
      setLoadError(e.message);
    }
  };

  const handleSubmit = () => setSubmitted(true);

  const handleCopy = () => {
    const batch = Object.entries(decisions)
      .filter(([,d]) => d.choice)
      .map(([id,d]) => {
        const item = data.find(i => i.id === id);
        return {
          id,
          choice: d.choice,
          note: d.note || null,
          description: item?.description || null,
          current_decision: item?.decision || null,
          priority: item?.priority || null,
          tags: item?.tags || [],
        };
      });
    const payload = JSON.stringify(batch, null, 2);
    navigator.clipboard.writeText(payload).then(() => {
      setCopyLabel("Copied ✓");
      setTimeout(() => setCopyLabel("Copy for Claude"), 2000);
    });
  };

  const allGroups = groupItems(data);
  const totalItems = data.length;
  const totalDone = data.filter(i => decisions[i.id]?.choice).length;

  const visibleGroups = {};
  for (const [label, items] of Object.entries(allGroups)) {
    let f = items;
    if (priFilter !== "all") f = f.filter(i => i.priority === priFilter);
    if (filter === "undecided") f = f.filter(i => !decisions[i.id]?.choice);
    if (filter === "decided") f = f.filter(i => decisions[i.id]?.choice);
    if (f.length) visibleGroups[label] = f;
  }

  // ── Load screen ──
  if (!loaded) {
    return (
      <div style={{ minHeight:"100vh", background:"#090b12", fontFamily:"Georgia,serif",
        display:"flex", alignItems:"center", justifyContent:"center", padding:24 }}>
        <div style={{ maxWidth:480, width:"100%" }}>
          <div style={{ fontFamily:"monospace", fontSize:8, letterSpacing:3, color:"#334", marginBottom:4 }}>
            VALORIA PROJECT
          </div>
          <h1 style={{ fontSize:20, color:"#cec6b6", fontWeight:400, margin:"0 0 6px", letterSpacing:-0.3 }}>
            Editorial Review
          </h1>
          <p style={{ fontSize:12, color:"#556", margin:"0 0 16px", lineHeight:1.5 }}>
            Paste the JSON data array from Claude to load items.
          </p>
          <textarea
            value={rawInput}
            onChange={e => setRawInput(e.target.value)}
            placeholder='[{"id":"ED-001",...}]' 
            style={{ width:"100%", minHeight:120, background:"#0c0e14", border:"1px solid #252838",
              borderRadius:6, color:"#c8c0b0", fontSize:11, padding:"10px 12px",
              fontFamily:"monospace", boxSizing:"border-box", resize:"vertical", marginBottom:10 }}
          />
          {loadError && <div style={{ fontSize:11, color:"#cc5555", marginBottom:8 }}>Error: {loadError}</div>}
          <button onClick={handleLoad} disabled={!rawInput.trim()}
            style={{ width:"100%", padding:"10px", background: rawInput.trim() ? "#1e2a4a" : "#111420",
              border:`1px solid ${rawInput.trim() ? "#2a3a6a" : "#1e2030"}`,
              borderRadius:6, color: rawInput.trim() ? "#8aacdf" : "#334",
              fontSize:13, fontWeight:600, cursor: rawInput.trim() ? "pointer" : "default" }}>
            Load Items →
          </button>
        </div>
      </div>
    );
  }

  // ── Review screen ──
  return (
    <div style={{ minHeight:"100vh", background:"#090b12", fontFamily:"Georgia,serif", color:"#c0b8a8" }}>
      {/* Header */}
      <div style={{ background:"#0b0d18", borderBottom:"1px solid #181a28",
        padding:"10px 14px", display:"flex", alignItems:"center",
        justifyContent:"space-between", flexWrap:"wrap", gap:10 }}>
        <div>
          <div style={{ fontFamily:"monospace", fontSize:8, letterSpacing:3, color:"#334" }}>VALORIA PROJECT</div>
          <div style={{ fontSize:15, fontWeight:600, color:"#cec6b6", letterSpacing:-0.3 }}>
            Editorial Review · {totalItems} items
          </div>
        </div>
        <div style={{ display:"flex", alignItems:"center", gap:8, flexWrap:"wrap" }}>
          <span style={{ fontSize:11, color:"#556" }}>{totalDone}/{totalItems}</span>
          <select value={filter} onChange={e => setFilter(e.target.value)}
            style={{ background:"#111420", border:"1px solid #222438", borderRadius:4,
              color:"#8890a8", fontSize:10, padding:"3px 7px" }}>
            <option value="all">All</option>
            <option value="undecided">Undecided</option>
            <option value="decided">Decided</option>
          </select>
          <select value={priFilter} onChange={e => setPriFilter(e.target.value)}
            style={{ background:"#111420", border:"1px solid #222438", borderRadius:4,
              color:"#8890a8", fontSize:10, padding:"3px 7px" }}>
            {["all","P1-BLOCKER","P1","P2","P3"].map(p =>
              <option key={p} value={p}>{p==="all"?"All priorities":p}</option>)}
          </select>
          {!submitted ? (
            <button onClick={handleSubmit} disabled={totalDone===0}
              style={{ padding:"5px 16px", background: totalDone>0 ? "#12301a" : "#111420",
                border:`1px solid ${totalDone>0 ? "#2a6a3a" : "#222438"}`,
                borderRadius:4, color: totalDone>0 ? "#6acc8a" : "#334",
                fontSize:11, fontWeight:700, cursor: totalDone>0 ? "pointer":"default" }}>
              Submit {totalDone}
            </button>
          ) : (
            <button onClick={handleCopy}
              style={{ padding:"5px 16px", background:"#1a2a4a",
                border:"1px solid #2a4a8a", borderRadius:4,
                color:"#8aacdf", fontSize:11, fontWeight:700, cursor:"pointer" }}>
              {copyLabel}
            </button>
          )}
          <button onClick={() => { setLoaded(false); setData(EMPTY); setDecisions({}); setSubmitted(false); }}
            style={{ padding:"5px 10px", background:"transparent", border:"1px solid #222",
              borderRadius:4, color:"#445", fontSize:10, cursor:"pointer" }}>
            ↺ Reset
          </button>
        </div>
      </div>

      <NavBar groups={visibleGroups} decisions={decisions} />

      {submitted && (
        <div style={{ margin:"10px 14px", padding:"10px 14px", background:"#0b180b",
          border:"1px solid #1f4a1f", borderRadius:6, fontSize:12, color:"#8fcc8f" }}>
          <strong style={{ color:"#6acc6a", fontSize:11, letterSpacing:1 }}>READY · </strong>
          {totalDone} decision{totalDone!==1?"s":""} packaged. Hit <em>Copy for Claude</em> then paste into chat.
        </div>
      )}

      <div style={{ padding:"10px 14px", maxWidth:740, margin:"0 auto" }}>
        {Object.entries(visibleGroups).map(([label, items]) => (
          <div key={label}
            id={`sec-${label.replace(/\s+/g,"-").replace(/[^a-zA-Z0-9-]/g,"")}`}
            style={{ marginBottom:24 }}>
            <div style={{ fontFamily:"monospace", fontSize:10, letterSpacing:2, color:"#3a4a6a",
              fontWeight:700, textTransform:"uppercase", marginBottom:8,
              paddingBottom:5, borderBottom:"1px solid #181a26",
              display:"flex", justifyContent:"space-between" }}>
              <span>{label}</span>
              <span style={{ color:"#2a3a4a" }}>
                {items.filter(i=>decisions[i.id]?.choice).length}/{items.length}
              </span>
            </div>
            {items.map(item => (
              <Item key={item.id} item={item} dec={decisions[item.id]} onDec={onDec} />
            ))}
          </div>
        ))}
        {Object.keys(visibleGroups).length===0 && (
          <div style={{ textAlign:"center", padding:48, color:"#334", fontSize:13 }}>
            No items match filter.
          </div>
        )}
        <div style={{ height:50 }} />
      </div>
    </div>
  );
}
