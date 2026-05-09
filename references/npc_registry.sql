-- Valoria NPC Registry (SQLite)
-- Generated: 2026-05-08
-- Source: references/npc_registry.yaml migrated per PP-685
-- Usage: sqlite3 npc_registry.db < npc_registry.sql

BEGIN TRANSACTION;
CREATE TABLE convictions (
    npc_id TEXT NOT NULL,
    conviction TEXT NOT NULL,
    weight REAL NOT NULL,
    rank INTEGER,  -- 1=primary, 2=secondary, etc
    migration_notes TEXT,
    FOREIGN KEY (npc_id) REFERENCES npcs(id)
);
INSERT INTO "convictions" VALUES('NPC-001','Warden',0.4,1,'Legacy ''Continuity'' → Warden (stewardship duty: ''the work must continue'') + Precedent (ancestral practice). Per PP-685 §4 defaults.');
INSERT INTO "convictions" VALUES('NPC-001','Precedent',0.2,2,'Legacy ''Continuity'' → Warden (stewardship duty: ''the work must continue'') + Precedent (ancestral practice). Per PP-685 §4 defaults.');
INSERT INTO "convictions" VALUES('NPC-002','Honor',0.3,1,'Per PP-685 §2.2. Prior labels ''Reason'' + ''Military Honor''. NPC registry previously had ''Rawlsian'' (from infill) — PP-685 roster is authoritative; discrepancy noted.');
INSERT INTO "convictions" VALUES('NPC-002','Authority',0.3,2,'Per PP-685 §2.2. Prior labels ''Reason'' + ''Military Honor''. NPC registry previously had ''Rawlsian'' (from infill) — PP-685 roster is authoritative; discrepancy noted.');
INSERT INTO "convictions" VALUES('NPC-002','Identity',0.2,3,'Per PP-685 §2.2. Prior labels ''Reason'' + ''Military Honor''. NPC registry previously had ''Rawlsian'' (from infill) — PP-685 roster is authoritative; discrepancy noted.');
INSERT INTO "convictions" VALUES('NPC-003','Honor',0.35,1,'Per PP-685 §2.2. Prior labels in roster ''Continuity'' + ''Military Honor''; npc_roster_v30 says ''Rawlsian social contract''. PP-685 mapping used as authoritative. Discrepancy flagged.');
INSERT INTO "convictions" VALUES('NPC-003','Warden',0.25,2,'Per PP-685 §2.2. Prior labels in roster ''Continuity'' + ''Military Honor''; npc_roster_v30 says ''Rawlsian social contract''. PP-685 mapping used as authoritative. Discrepancy flagged.');
INSERT INTO "convictions" VALUES('NPC-003','Community',0.2,3,'Per PP-685 §2.2. Prior labels in roster ''Continuity'' + ''Military Honor''; npc_roster_v30 says ''Rawlsian social contract''. PP-685 mapping used as authoritative. Discrepancy flagged.');
INSERT INTO "convictions" VALUES('NPC-004','Faith',0.4,1,'No prior legacy label. Inferred from role: Church Inquisitor = Faith primary + Authority. Per PP-685 §4 defaults.');
INSERT INTO "convictions" VALUES('NPC-004','Authority',0.2,2,'No prior legacy label. Inferred from role: Church Inquisitor = Faith primary + Authority. Per PP-685 §4 defaults.');
INSERT INTO "convictions" VALUES('NPC-005','Utility',0.4,1,'Legacy ''Consequentialist'' → Utility. Honor added via lowenritter_military cultural template. Per PP-685 §4 defaults.');
INSERT INTO "convictions" VALUES('NPC-005','Honor',0.2,2,'Legacy ''Consequentialist'' → Utility. Honor added via lowenritter_military cultural template. Per PP-685 §4 defaults.');
INSERT INTO "convictions" VALUES('NPC-006','Honor',0.35,1,'No prior legacy label. Inferred from role: military officer = Honor + Authority. Per PP-685 §4 defaults.');
INSERT INTO "convictions" VALUES('NPC-006','Authority',0.25,2,'No prior legacy label. Inferred from role: military officer = Honor + Authority. Per PP-685 §4 defaults.');
INSERT INTO "convictions" VALUES('NPC-007','Utility',0.5,1,'Legacy ''Utilitarian'' → Utility. npc_roster_v30: ''Utilitarian — greatest good for greatest number of guild members''. Self-Other mildly self-interested (PROFIT-MAXIMISING flaw). Per PP-685 §4.');
INSERT INTO "convictions" VALUES('NPC-007','Community',0.1,2,'Legacy ''Utilitarian'' → Utility. npc_roster_v30: ''Utilitarian — greatest good for greatest number of guild members''. Self-Other mildly self-interested (PROFIT-MAXIMISING flaw). Per PP-685 §4.');
INSERT INTO "convictions" VALUES('NPC-008','Order',0.4,1,'No prior legacy label. Inferred from role: bureaucrat / CONSERVATIVE behavioral AI = Order + Precedent. Per PP-685 §4.');
INSERT INTO "convictions" VALUES('NPC-008','Precedent',0.2,2,'No prior legacy label. Inferred from role: bureaucrat / CONSERVATIVE behavioral AI = Order + Precedent. Per PP-685 §4.');
INSERT INTO "convictions" VALUES('NPC-009','Authority',0.3,1,'No prior legacy label. Inferred from role: competent administrator, OVERPERFORMER flaw, flattery vulnerability. Authority + Utility. Per PP-685 §4.');
INSERT INTO "convictions" VALUES('NPC-009','Utility',0.3,2,'No prior legacy label. Inferred from role: competent administrator, OVERPERFORMER flaw, flattery vulnerability. Authority + Utility. Per PP-685 §4.');
INSERT INTO "convictions" VALUES('NPC-010','Utility',0.3,1,'No prior legacy label. npc_roster_v30: ''Honour among operators — your word is your network.'' Utility (effectiveness) + Honor (personal trust, word-as-bond). Per PP-685 §4.');
INSERT INTO "convictions" VALUES('NPC-010','Honor',0.3,2,'No prior legacy label. npc_roster_v30: ''Honour among operators — your word is your network.'' Utility (effectiveness) + Honor (personal trust, word-as-bond). Per PP-685 §4.');
INSERT INTO "convictions" VALUES('NPC-011','Authority',0.3,1,'No prior legacy label. Inferred from role: PROTECTIVE behavioral AI, shields Elske = Warden. Imperial authority = Authority. Per PP-685 §4.');
INSERT INTO "convictions" VALUES('NPC-011','Warden',0.3,2,'No prior legacy label. Inferred from role: PROTECTIVE behavioral AI, shields Elske = Warden. Imperial authority = Authority. Per PP-685 §4.');
INSERT INTO "convictions" VALUES('NPC-012','Utility',0.3,1,'No prior legacy label. Inferred from role: STABILITY-SEEKING trade factor. Utility (trade pragmatism) + Order (stability). Per PP-685 §4.');
INSERT INTO "convictions" VALUES('NPC-012','Order',0.3,2,'No prior legacy label. Inferred from role: STABILITY-SEEKING trade factor. Utility (trade pragmatism) + Order (stability). Per PP-685 §4.');
INSERT INTO "convictions" VALUES('NPC-013','Faith',0.3,1,'No prior legacy label. Inferred from role: OPTIMISER (maximises Church Wealth throughput), aggressive tithe = Faith + Order + Utility. Per PP-685 §4.');
INSERT INTO "convictions" VALUES('NPC-013','Order',0.25,2,'No prior legacy label. Inferred from role: OPTIMISER (maximises Church Wealth throughput), aggressive tithe = Faith + Order + Utility. Per PP-685 §4.');
INSERT INTO "convictions" VALUES('NPC-013','Utility',0.2,3,'No prior legacy label. Inferred from role: OPTIMISER (maximises Church Wealth throughput), aggressive tithe = Faith + Order + Utility. Per PP-685 §4.');
INSERT INTO "convictions" VALUES('NPC-020','Virtue',0.45,1,'Per PP-685 §2.1. Prior labels ''Virtue Ethics'' + ''Reason''. Public-spirited Captain archetype.');
INSERT INTO "convictions" VALUES('NPC-020','Authority',0.3,2,'Per PP-685 §2.1. Prior labels ''Virtue Ethics'' + ''Reason''. Public-spirited Captain archetype.');
INSERT INTO "convictions" VALUES('NPC-021','Faith',0.5,1,'No prior legacy label. Inferred from role: Church leader / Confessor. Per PP-685 §4 defaults.');
INSERT INTO "convictions" VALUES('NPC-021','Authority',0.2,2,'No prior legacy label. Inferred from role: Church leader / Confessor. Per PP-685 §4 defaults.');
INSERT INTO "convictions" VALUES('NPC-033','Liberty',0.3,1,'faction_canon: ''Autonomy / Consequence MS / Certainty 3''. Autonomy → Liberty; Consequence → Utility. Per PP-685 §4.');
INSERT INTO "convictions" VALUES('NPC-033','Utility',0.3,2,'faction_canon: ''Autonomy / Consequence MS / Certainty 3''. Autonomy → Liberty; Consequence → Utility. Per PP-685 §4.');
INSERT INTO "convictions" VALUES('NPC-034','Faith',0.4,1,'faction_canon: ''Faith / Authority MS / Certainty 5''. Direct mapping. Per PP-685 §4.');
INSERT INTO "convictions" VALUES('NPC-034','Authority',0.2,2,'faction_canon: ''Faith / Authority MS / Certainty 5''. Direct mapping. Per PP-685 §4.');
INSERT INTO "convictions" VALUES('NPC-035','Order',0.35,1,'faction_canon: ''Order / Authority MS / Certainty 4''. Direct mapping. Per PP-685 §4.');
INSERT INTO "convictions" VALUES('NPC-035','Authority',0.25,2,'faction_canon: ''Order / Authority MS / Certainty 4''. Direct mapping. Per PP-685 §4.');
INSERT INTO "convictions" VALUES('NPC-036','Order',0.35,1,'faction_canon: ''Order / Authority MS / Certainty 4''. Direct mapping. Per PP-685 §4.');
INSERT INTO "convictions" VALUES('NPC-036','Authority',0.25,2,'faction_canon: ''Order / Authority MS / Certainty 4''. Direct mapping. Per PP-685 §4.');
INSERT INTO "convictions" VALUES('NPC-037','Precedent',0.35,1,'faction_canon: ''Precedent / Evidence MS / Certainty 5''. Direct mapping on Precedent; Evidence is Resonant Style. Per PP-685 §4.');
INSERT INTO "convictions" VALUES('NPC-037','Authority',0.25,2,'faction_canon: ''Precedent / Evidence MS / Certainty 5''. Direct mapping on Precedent; Evidence is Resonant Style. Per PP-685 §4.');
INSERT INTO "convictions" VALUES('NPC-038','Faith',0.4,1,'No prior legacy label. Only Faith inferred from Cardinal role. Per PP-685 §4 defaults.');
INSERT INTO "convictions" VALUES('NPC-039','Scholastic',0.35,1,'No prior legacy label. faction_canon: ''canonical scholar''. Scholastic + Faith inferred. Per PP-685 §4.');
INSERT INTO "convictions" VALUES('NPC-039','Faith',0.25,2,'No prior legacy label. faction_canon: ''canonical scholar''. Scholastic + Faith inferred. Per PP-685 §4.');
INSERT INTO "convictions" VALUES('NPC-040','Honor',0.35,1,'No prior legacy label. faction_canon: ''Templar arm'' for Fortitude cardinal → Honor (military-religious code) + Faith + Authority. Per PP-685 §4.');
INSERT INTO "convictions" VALUES('NPC-040','Faith',0.25,2,'No prior legacy label. faction_canon: ''Templar arm'' for Fortitude cardinal → Honor (military-religious code) + Faith + Authority. Per PP-685 §4.');
INSERT INTO "convictions" VALUES('NPC-040','Authority',0.15,3,'No prior legacy label. faction_canon: ''Templar arm'' for Fortitude cardinal → Honor (military-religious code) + Faith + Authority. Per PP-685 §4.');
INSERT INTO "convictions" VALUES('NPC-050','Faith',0.5,1,'Per PP-685 §2.3. Prior labels ''Divine Command'' + ''Virtue Ethics''. Selfless devotional archetype.');
INSERT INTO "convictions" VALUES('NPC-050','Virtue',0.2,2,'Per PP-685 §2.3. Prior labels ''Divine Command'' + ''Virtue Ethics''. Selfless devotional archetype.');
INSERT INTO "convictions" VALUES('NPC-050','Warden',0.1,3,'Per PP-685 §2.3. Prior labels ''Divine Command'' + ''Virtue Ethics''. Selfless devotional archetype.');
INSERT INTO "convictions" VALUES('NPC-052','Authority',0.4,1,'PP-685 §3 edge case: ''Authority + Honor + Identity, lowenritter_military background; orientation +0.20 (pragmatic militarist)''. PP-650 STRUCK status noted but Conviction profile provided as placeholder.');
INSERT INTO "convictions" VALUES('NPC-052','Honor',0.2,2,'PP-685 §3 edge case: ''Authority + Honor + Identity, lowenritter_military background; orientation +0.20 (pragmatic militarist)''. PP-650 STRUCK status noted but Conviction profile provided as placeholder.');
INSERT INTO "convictions" VALUES('NPC-052','Identity',0.2,3,'PP-685 §3 edge case: ''Authority + Honor + Identity, lowenritter_military background; orientation +0.20 (pragmatic militarist)''. PP-650 STRUCK status noted but Conviction profile provided as placeholder.');
CREATE TABLE goals (
    npc_id TEXT NOT NULL,
    goal TEXT NOT NULL,
    FOREIGN KEY (npc_id) REFERENCES npcs(id)
);
INSERT INTO "goals" VALUES('NPC-001','Maintain substrate stability');
INSERT INTO "goals" VALUES('NPC-001','Protect Southernmost practitioners');
INSERT INTO "goals" VALUES('NPC-001','Continue the work regardless of interference');
INSERT INTO "goals" VALUES('NPC-002','Serve Varfell intelligence');
INSERT INTO "goals" VALUES('NPC-002','Privately sympathize with Restoration Movement');
INSERT INTO "goals" VALUES('NPC-003','Cultural restoration');
INSERT INTO "goals" VALUES('NPC-003','Equity and social contract');
INSERT INTO "goals" VALUES('NPC-004','Investigate heresy');
INSERT INTO "goals" VALUES('NPC-004','Enforce Church orthodoxy');
INSERT INTO "goals" VALUES('NPC-005','Mission success');
INSERT INTO "goals" VALUES('NPC-005','Minimize Thread collateral');
INSERT INTO "goals" VALUES('NPC-006','Counter Altonian threat');
INSERT INTO "goals" VALUES('NPC-006','Strengthen peninsular defenses');
INSERT INTO "goals" VALUES('NPC-007','Maximize Guilds Wealth');
INSERT INTO "goals" VALUES('NPC-007','Protect artisan livelihoods');
INSERT INTO "goals" VALUES('NPC-008','Maintain procedural correctness');
INSERT INTO "goals" VALUES('NPC-008','Block radical action through procedure');
INSERT INTO "goals" VALUES('NPC-009','Efficient Crown administration');
INSERT INTO "goals" VALUES('NPC-009','Maintain personal indispensability');
INSERT INTO "goals" VALUES('NPC-010','Maintain Virke trade network');
INSERT INTO "goals" VALUES('NPC-010','Protect personal trust relationships');
INSERT INTO "goals" VALUES('NPC-011','Protect Elske''s safety');
INSERT INTO "goals" VALUES('NPC-011','Maintain province stability');
INSERT INTO "goals" VALUES('NPC-011','Sandbag imperial directives');
INSERT INTO "goals" VALUES('NPC-012','Maintain stable trade');
INSERT INTO "goals" VALUES('NPC-012','Avoid escalation');
INSERT INTO "goals" VALUES('NPC-012','Return home eventually');
INSERT INTO "goals" VALUES('NPC-013','Maximize Church Wealth throughput');
INSERT INTO "goals" VALUES('NPC-013','Aggressive tithe collection');
INSERT INTO "goals" VALUES('NPC-052','Varfell military expansion');
INSERT INTO "goals" VALUES('NPC-052','Intelligence-first approach to RM');
CREATE TABLE npcs (
    id TEXT PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT,
    faction TEXT,
    role TEXT,
    status TEXT DEFAULT 'canonical',
    title TEXT,
    age TEXT,
    birthplace TEXT,
    territory TEXT,
    ts TEXT,
    coherence TEXT,
    resonant_style TEXT,
    self_other_initial REAL,
    cultural_label TEXT,
    arc_trajectory TEXT,
    source TEXT,
    notes TEXT
);
INSERT INTO "npcs" VALUES('NPC-001','Edeyja',NULL,'Independent (Southernmost Wardens)','Warden-Chief','canonical',NULL,NULL,'Southernmost','T15 (Southernmost)','75–80','9','Evidence',-0.3,'solmund_alpine','Warden-Chief navigating Church pressure and Thread instability','designs/npcs/edeyja_npc.md, npc_roster_v30 §1','Highest TS of any living practitioner. Survived proximity to a major Gap/tear.');
INSERT INTO "npcs" VALUES('NPC-002','Maret','Uln','Varfell','Practitioner / Succession Fallback','canonical',NULL,NULL,'Western fjords (near southern Einhir communities in Varfell territory)',NULL,'~50',NULL,NULL,0.1,'lowenritter_military','Dual loyalty — personal sympathy vs professional duty. If Vaynard eliminated, takes Varfell leadership (PP-486).','npc_roster_v30 §2','Vaynard''s intelligence operative. Thread-sensitive. RM-adjacent targets consistently 1 season behind. Southern Einhir solidarity.');
INSERT INTO "npcs" VALUES('NPC-003','Yrsa','Vossen','Restoration Movement','RM Leader','canonical',NULL,NULL,NULL,NULL,'25',NULL,NULL,-0.3,'solmund_alpine','Visibility as vulnerability — permanent Heresy Investigation target','npc_roster_v30 §3','TS 25 — above practitioner threshold but below Forgetting resistance gate (29). PP-665 rename from Maret Vossen.');
INSERT INTO "npcs" VALUES('NPC-004','Sæmund','Haelgrund','Church','Inquisitor (Cardinal Justice)','canonical',NULL,NULL,NULL,NULL,'12',NULL,NULL,0.0,'ecclesiastical','Latent TS — doesn''t know he''s Thread Sensitive. PC diagnosis possible (Cognition vs Ob 2).','npc_roster_v30 §4','TS 12 — barely above practitioner threshold. Attributes hunches to investigative instinct. PROCEDURALIST behavioral AI.');
INSERT INTO "npcs" VALUES('NPC-005','Sigrid','Torsvald','Löwenritter','TS Riskbreaker (Covert)','canonical',NULL,NULL,NULL,NULL,NULL,NULL,NULL,0.0,'lowenritter_military','Risk-averse on Thread collateral despite Riskbreaker doctrine — TS lets her perceive damage colleagues can''t.','npc_roster_v30 §5',NULL);
INSERT INTO "npcs" VALUES('NPC-006','Halvar','Brandt','Löwenritter','Officer (Lions'' Table)','canonical',NULL,NULL,'Halvardshelm',NULL,NULL,NULL,NULL,-0.1,'lowenritter_military','External threat fixated — evaluates every action against Altonian metric. Brandt succession if Ehrenwall falls.','npc_roster_v30 §6','Named after birthplace Halvardshelm — confirmed intentional.');
INSERT INTO "npcs" VALUES('NPC-007','Annika','Feldhaus','Guilds','Guilds Representative','canonical',NULL,NULL,NULL,NULL,NULL,NULL,NULL,0.1,'hafenmark_procedural','Profit-maximizing — sacrifices Guilds Mandate for Wealth. Thread-touched supply chain discoverable.','npc_roster_v30 §7',NULL);
INSERT INTO "npcs" VALUES('NPC-008','Peder','Almstedt','Crown (Ministry)','Ministry Bureaucrat (Chief Parliamentary Clerk)','canonical',NULL,NULL,NULL,NULL,NULL,NULL,NULL,0.0,'valorian_court','CONSERVATIVE — blocks radical action through procedure, not force. Cognition-heavy social contest target.','npc_roster_v30 §8',NULL);
INSERT INTO "npcs" VALUES('NPC-009','Gerik','Strand','Crown','Crown Minister (Lord Steward)','canonical',NULL,NULL,NULL,NULL,NULL,NULL,NULL,-0.1,'valorian_court','OVERPERFORMER — runs every important task. Flattery vulnerability (−1 Ob on social actions acknowledging competence).','npc_roster_v30 §9',NULL);
INSERT INTO "npcs" VALUES('NPC-010','Dalla','Virke','Niflhel (Virke syndicate)','Syndicate Broker','canonical',NULL,NULL,NULL,NULL,NULL,NULL,NULL,0.1,'hafenmark_procedural','Personal loyalty to partners vs family directives. Third conflict with family triggers enforcement.','npc_roster_v30 §10',NULL);
INSERT INTO "npcs" VALUES('NPC-011','Alexios','Laskaris','Altonia','Doux (Altonian Prince)','canonical','Doux',NULL,'Altonia',NULL,NULL,NULL,NULL,-0.2,'altonian','PROTECTIVE — priority is Elske''s safety. Flips if Elske Loyalty ≤ 2 (IP +3 immediately).','npc_roster_v30 §11',NULL);
INSERT INTO "npcs" VALUES('NPC-012','Rikard','Solberg','Independent (Schoenland)','Schoenland Factor','canonical',NULL,NULL,'Schoenland','T16 (Schoenland)',NULL,NULL,NULL,0.0,'hafenmark_procedural','STABILITY-SEEKING — natural ally for peace, obstacle for escalation. Motivated by homesickness (discoverable via Read Ob 2).','npc_roster_v30 §12',NULL);
INSERT INTO "npcs" VALUES('NPC-013','Aldric','Tormann','Church','Fourth Cardinal (Prudence)','canonical',NULL,NULL,NULL,NULL,NULL,NULL,NULL,0.1,'ecclesiastical','Parish Revolt arc or PC intervention path. Inadvertently funds Church charitable mission while undermining cultural authority.','npc_roster_v30 §13, npc_character_analyses_v30_infill',NULL);
INSERT INTO "npcs" VALUES('NPC-020','Almud','Almqvist','Crown','King','canonical','King',NULL,NULL,'T1 (Valorsplatz)','28',NULL,NULL,-0.1,'valorian_court','Canonical Crown Captain per sim continuity §1.2. Royal Assassination Fuse target (Arc F Eliminated → Lenneth Widow Regent).','faction_canon_v30 §Crown','TS 28 per character_canon — no threshold crossing. Honor enters via valorian_court cultural template.');
INSERT INTO "npcs" VALUES('NPC-021','Arne','Himlensendt','Church','Confessor (Church Leader)','canonical','Confessor',NULL,NULL,'T9 (Himmelenger)',NULL,NULL,NULL,0.0,'ecclesiastical',NULL,'faction_canon_v30 §Church','Canonical per params/bg/core.md L233. Agent in Crown Inner Circle via Father Gustav Linder.');
INSERT INTO "npcs" VALUES('NPC-030','Elske','Almqvist','Crown (Royal Family)','Princess (married to Doux Alexios Laskaris)','canonical',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'Off-board diplomatic asset. Elske Loyalty stat drives Laskaris PROTECTIVE behavior. Return arc possible.','faction_canon_v30 §Crown','Royal Assassination Fuse — not a direct target but her safety drives Alexios''s behavior.');
INSERT INTO "npcs" VALUES('NPC-031','Torben','Almqvist','Crown (Royal Family)','Prince (Heir Apparent)','canonical','Prince',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'Arc E Bereaved Father (Royal Assassination Fuse target). Conviction emergence window Seasons 1–8 (ED-618).','faction_canon_v30 §Crown','Heir apparent. Convictions intentionally undefined at game start — emerge during play.');
INSERT INTO "npcs" VALUES('NPC-032','Lenneth','Almqvist','Crown (Royal Family)','Queen (Widow Regent if Almud eliminated)','canonical',NULL,NULL,NULL,'T1 (Valorsplatz)',NULL,NULL,NULL,NULL,NULL,'Arc D The Avenger. If Almud eliminated (Arc F): becomes Widow Regent. Pro-Restoration — allied with Yrsa Vossen.','faction_canon_v30 §Crown','Queen Lenneth Almqvist. Pro-Restoration alignment confirmed per Jordan 2026-05-08. PP-685 §2.3 ecclesiastical profile is a misattribution — needs correction in PP-685.');
INSERT INTO "npcs" VALUES('NPC-033','Kolbrun','Thale','Crown (Inner Circle)','Spymaster','canonical',NULL,NULL,NULL,NULL,NULL,NULL,NULL,0.0,'valorian_court','Sole inner-circle contact to settlement-layer intelligence brokers. Certainty 3 (lowest in Inner Circle).','faction_canon_v30 §Crown sub-Organizations',NULL);
INSERT INTO "npcs" VALUES('NPC-034','Gustav','Linder','Church (dual-loyalty: Crown Inner Circle agent for Himlensendt)','Archbishop''s Representative / Father','canonical','Father',NULL,NULL,NULL,NULL,NULL,NULL,0.0,'ecclesiastical','Dual-loyalty NPC — Himlensendt''s agent inside Crown Inner Circle. Certainty 5 (highest).','faction_canon_v30 §Crown sub-Organizations',NULL);
INSERT INTO "npcs" VALUES('NPC-035','Theodor','Kreutz','Crown (Inner Circle) / Löwenritter Liaison','Royal Guard Captain','canonical',NULL,NULL,NULL,NULL,NULL,NULL,NULL,-0.1,'lowenritter_military','Pre-designated allegiance to Almud personally. His removal triggers Löwenritter Autonomy escalation toward Split.','faction_canon_v30 §Crown sub-Organizations',NULL);
INSERT INTO "npcs" VALUES('NPC-036','Wilhelm','Voss','Crown (Inner Circle)','Royal Marshal','canonical',NULL,NULL,NULL,NULL,NULL,NULL,NULL,0.0,'valorian_court',NULL,'faction_canon_v30 §Crown sub-Organizations',NULL);
INSERT INTO "npcs" VALUES('NPC-037','Annalie','Reichard','Crown (Inner Circle)','Lord Treasurer','canonical',NULL,NULL,NULL,NULL,NULL,NULL,NULL,0.0,'valorian_court',NULL,'faction_canon_v30 §Crown sub-Organizations','CORRECTED: previously listed as ''Church / Cardinal Reichard''. Per faction_canon, Annalie Reichard is Crown Inner Circle Lord Treasurer, NOT a Cardinal. The ''Cardinal Reichard'' in PP-685 §2.3 may be a separate entity (artifact 15 sample) or a naming confusion. [OPEN: verify if there is a distinct Cardinal Reichard in Church hierarchy].');
INSERT INTO "npcs" VALUES('NPC-038','Arnlod','Olafsson','Church','Cardinal (virtue assignment unconfirmed)','canonical',NULL,NULL,NULL,NULL,NULL,NULL,NULL,0.0,'ecclesiastical',NULL,'faction_canon_v30 §Church','Cardinal virtue assignment not found in faction_canon (Justice = Haelgrund, Temperance = Klapp candidate, Fortitude = Jarnstal candidate, Prudence = Tormann). [OPEN: which virtue does Arnlod hold, or is he a 5th cardinal without virtue assignment?]');
INSERT INTO "npcs" VALUES('NPC-039','Magnus','Klapp','Church','Cardinal (Temperance candidate)','canonical',NULL,NULL,NULL,NULL,NULL,NULL,NULL,-0.1,'ecclesiastical','Scholar''s Dilemma — TS exposure via archive work.','faction_canon_v30 §Church','NPC-051 (''Klapp'') references in arcs (Klapp Combat, Klapp Thread, etc.) refer to this character''s surname, not a separate NPC.');
INSERT INTO "npcs" VALUES('NPC-040','Osten','Jarnstal','Church','Cardinal (Fortitude candidate)','canonical',NULL,NULL,NULL,NULL,NULL,NULL,NULL,0.0,'ecclesiastical',NULL,'faction_canon_v30 §Church',NULL);
INSERT INTO "npcs" VALUES('NPC-041','Aldric','Hann','Restoration Movement','RM Visible Leadership (alongside Yrsa Vossen)','canonical',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'faction_canon_v30 §11 (caste/organization hierarchy)','RESOLVED: distinct character from NPC-013 Aldric Tormann (Church Cardinal Prudence). Aldric Hann is RM visible leadership. Two different factions, different surnames.');
INSERT INTO "npcs" VALUES('NPC-050','Baralta',NULL,'Crown (claimant per foil dynamics)','Claimant (Custodian/Claimant foil with Almud)','canonical',NULL,NULL,NULL,NULL,NULL,NULL,NULL,-0.4,'ecclesiastical','Six foil pairings per npc_foils_v30: Almud ↔ Baralta (Custodian/Claimant); Lenneth ↔ Baralta (campaign-defining); Baralta ↔ Vaynard (total opposition).','arcs_31_35.md, faction_canon_v30, PP-685 §2.3',NULL);
INSERT INTO "npcs" VALUES('NPC-052','Vaynard',NULL,'Varfell','Varfell Leader','canonical',NULL,NULL,NULL,NULL,NULL,NULL,NULL,0.2,'lowenritter_military','Von Lohengramm programme — revolutionary expulsion. If eliminated, Maret Uln succession (PP-486).','faction_canon_v30, npc_roster_v30 (referenced as Maret''s superior)','PP-650 STRUCK status applies to Cultural Reformation + VTM associations; character remains active. ''Cunning + pride'' doctrine (faction_layer §1.5).');
CREATE TABLE open_issues (
    issue_id INTEGER PRIMARY KEY,
    status TEXT NOT NULL,
    summary TEXT NOT NULL,
    detail TEXT
);
INSERT INTO "open_issues" VALUES(1,'RESOLVED','Legacy ethical labels migrated to 13-Conviction taxonomy per PP-685',NULL);
INSERT INTO "open_issues" VALUES(2,'RESOLVED','Edeyja name confirmed final (mononym) per Jordan 2026-05-08',NULL);
INSERT INTO "open_issues" VALUES(3,'RESOLVED','Halvar birthplace Halvardshelm — intentional naming, per Jordan 2026-05-08',NULL);
INSERT INTO "open_issues" VALUES(4,'RESOLVED','Two Aldrics are distinct: Tormann=Church Prudence, Hann=RM leadership',NULL);
INSERT INTO "open_issues" VALUES(5,'PARTIAL','Unlisted NPCs: Crown Inner Circle + Cardinals verified. character_canon entries still pending.',NULL);
INSERT INTO "open_issues" VALUES(6,'RESOLVED','Vaynard confirmed as Varfell faction leader',NULL);
INSERT INTO "open_issues" VALUES(7,'OPEN','Stat gaps: explicitly deferred per npc_roster_v30 ("Deferred to next session")',NULL);
INSERT INTO "open_issues" VALUES(8,'RESOLVED','Conviction migration complete',NULL);
INSERT INTO "open_issues" VALUES(9,'OPEN','Cardinal Reichard collision: PP-685 refs Cardinal Reichard (Church), NPC-037 Annalie Reichard is Crown Lord Treasurer',NULL);
INSERT INTO "open_issues" VALUES(10,'RESOLVED','Lenneth is Queen, pro-Restoration aligned with Yrsa. PP-685 ecclesiastical profile is misattribution.',NULL);
INSERT INTO "open_issues" VALUES(11,'OPEN','Cardinal Arnlod virtue assignment: 4 virtues, 4+ cardinals, Arnlod unassigned',NULL);
INSERT INTO "open_issues" VALUES(12,'PARTIAL','Conviction discrepancies: Yrsa confirmed. Maret Uln prior-label discrepancy still open.',NULL);
CREATE TABLE stats (
    npc_id TEXT NOT NULL,
    stat_name TEXT NOT NULL,
    stat_value TEXT NOT NULL,
    FOREIGN KEY (npc_id) REFERENCES npcs(id)
);
INSERT INTO "stats" VALUES('NPC-001','cognition','5');
INSERT INTO "stats" VALUES('NPC-001','focus','5');
INSERT INTO "stats" VALUES('NPC-001','endurance','4');
INSERT INTO "stats" VALUES('NPC-001','social','3–4');
COMMIT;
