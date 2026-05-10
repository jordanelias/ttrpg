-- Valoria NPC Registry v2 (SQLite)
-- Generated: 2026-05-08
-- Audit corrections applied: behavior_v30 authoritative

BEGIN TRANSACTION;
CREATE TABLE convictions (
    npc_id TEXT NOT NULL, conviction TEXT NOT NULL, weight REAL NOT NULL,
    rank INTEGER, conviction_notes TEXT,
    FOREIGN KEY (npc_id) REFERENCES npcs(id)
);
INSERT INTO "convictions" VALUES('NPC-001','Warden',0.4,1,NULL);
INSERT INTO "convictions" VALUES('NPC-001','Precedent',0.2,2,NULL);
INSERT INTO "convictions" VALUES('NPC-002','Honor',0.3,1,NULL);
INSERT INTO "convictions" VALUES('NPC-002','Authority',0.3,2,NULL);
INSERT INTO "convictions" VALUES('NPC-002','Identity',0.2,3,NULL);
INSERT INTO "convictions" VALUES('NPC-003','Equity',0.4,1,'Equity primary per behavior_v30 §RM: ''The community is the only legitimate political unit.'' Secondary: Continuity → Warden (cultural preservation fallback). PP-685 mapping (Honor/Warden/Community) superseded by behavior file. Rosa Luxemburg archetype — visibility as vulnerability.');
INSERT INTO "convictions" VALUES('NPC-003','Warden',0.25,2,'Equity primary per behavior_v30 §RM: ''The community is the only legitimate political unit.'' Secondary: Continuity → Warden (cultural preservation fallback). PP-685 mapping (Honor/Warden/Community) superseded by behavior file. Rosa Luxemburg archetype — visibility as vulnerability.');
INSERT INTO "convictions" VALUES('NPC-004','Faith',0.4,1,NULL);
INSERT INTO "convictions" VALUES('NPC-004','Authority',0.2,2,NULL);
INSERT INTO "convictions" VALUES('NPC-005','Utility',0.4,1,NULL);
INSERT INTO "convictions" VALUES('NPC-005','Honor',0.2,2,NULL);
INSERT INTO "convictions" VALUES('NPC-006','Honor',0.35,1,NULL);
INSERT INTO "convictions" VALUES('NPC-006','Authority',0.25,2,NULL);
INSERT INTO "convictions" VALUES('NPC-007','Utility',0.5,1,NULL);
INSERT INTO "convictions" VALUES('NPC-007','Community',0.1,2,NULL);
INSERT INTO "convictions" VALUES('NPC-008','Order',0.4,1,NULL);
INSERT INTO "convictions" VALUES('NPC-008','Precedent',0.2,2,NULL);
INSERT INTO "convictions" VALUES('NPC-009','Authority',0.3,1,NULL);
INSERT INTO "convictions" VALUES('NPC-009','Utility',0.3,2,NULL);
INSERT INTO "convictions" VALUES('NPC-010','Utility',0.3,1,NULL);
INSERT INTO "convictions" VALUES('NPC-010','Honor',0.3,2,NULL);
INSERT INTO "convictions" VALUES('NPC-011','Authority',0.3,1,NULL);
INSERT INTO "convictions" VALUES('NPC-011','Warden',0.3,2,NULL);
INSERT INTO "convictions" VALUES('NPC-012','Utility',0.3,1,NULL);
INSERT INTO "convictions" VALUES('NPC-012','Order',0.3,2,NULL);
INSERT INTO "convictions" VALUES('NPC-013','Faith',0.3,1,NULL);
INSERT INTO "convictions" VALUES('NPC-013','Order',0.25,2,NULL);
INSERT INTO "convictions" VALUES('NPC-013','Utility',0.2,3,NULL);
INSERT INTO "convictions" VALUES('NPC-020','Virtue',0.45,1,NULL);
INSERT INTO "convictions" VALUES('NPC-020','Authority',0.3,2,NULL);
INSERT INTO "convictions" VALUES('NPC-021','Faith',0.5,1,NULL);
INSERT INTO "convictions" VALUES('NPC-021','Authority',0.2,2,NULL);
INSERT INTO "convictions" VALUES('NPC-032','Equity',0.45,1,'character_analyses §2: ''Primary Conviction: Equity. She believes caste suppression is wrong and the Crown should be the instrument of reform.'' Archivist by training. Pro-Restoration — allied with Yrsa Vossen.');
INSERT INTO "convictions" VALUES('NPC-033','Liberty',0.3,1,NULL);
INSERT INTO "convictions" VALUES('NPC-033','Utility',0.3,2,NULL);
INSERT INTO "convictions" VALUES('NPC-034','Faith',0.4,1,NULL);
INSERT INTO "convictions" VALUES('NPC-034','Authority',0.2,2,NULL);
INSERT INTO "convictions" VALUES('NPC-035','Order',0.35,1,NULL);
INSERT INTO "convictions" VALUES('NPC-035','Authority',0.25,2,NULL);
INSERT INTO "convictions" VALUES('NPC-036','Order',0.35,1,NULL);
INSERT INTO "convictions" VALUES('NPC-036','Authority',0.25,2,NULL);
INSERT INTO "convictions" VALUES('NPC-037','Precedent',0.35,1,NULL);
INSERT INTO "convictions" VALUES('NPC-037','Authority',0.25,2,NULL);
INSERT INTO "convictions" VALUES('NPC-038','Faith',0.4,1,NULL);
INSERT INTO "convictions" VALUES('NPC-039','Scholastic',0.35,1,NULL);
INSERT INTO "convictions" VALUES('NPC-039','Faith',0.25,2,NULL);
INSERT INTO "convictions" VALUES('NPC-040','Honor',0.35,1,NULL);
INSERT INTO "convictions" VALUES('NPC-040','Faith',0.25,2,NULL);
INSERT INTO "convictions" VALUES('NPC-040','Authority',0.15,3,NULL);
INSERT INTO "convictions" VALUES('NPC-050','Precedent',0.45,1,'Precedent primary per behavior_v30 §2.3: ''Constitutional procedure IS justice.'' PP-685 §2.3 misattributed as Faith/ecclesiastical — character_canon D6 already flagged this. Catherine the Great archetype — unshakeable force of conviction, sovereign authority as constitutional principle.');
INSERT INTO "convictions" VALUES('NPC-050','Authority',0.25,2,'Precedent primary per behavior_v30 §2.3: ''Constitutional procedure IS justice.'' PP-685 §2.3 misattributed as Faith/ecclesiastical — character_canon D6 already flagged this. Catherine the Great archetype — unshakeable force of conviction, sovereign authority as constitutional principle.');
INSERT INTO "convictions" VALUES('NPC-050','Order',0.15,3,'Precedent primary per behavior_v30 §2.3: ''Constitutional procedure IS justice.'' PP-685 §2.3 misattributed as Faith/ecclesiastical — character_canon D6 already flagged this. Catherine the Great archetype — unshakeable force of conviction, sovereign authority as constitutional principle.');
INSERT INTO "convictions" VALUES('NPC-052','Equity',0.35,1,'Reinhardt von Lohengramm archetype — revolutionary aristocrat. Genuine Einhir revival idealism (Equity) fused with any-cost pragmatism (Utility). Self/Other −0.40: ego-driven, wants to be the one who tears down the order and replaces it. PP-685 §3 mapping (Authority/Honor/Identity) superseded per Jordan 2026-05-08.');
INSERT INTO "convictions" VALUES('NPC-052','Utility',0.3,2,'Reinhardt von Lohengramm archetype — revolutionary aristocrat. Genuine Einhir revival idealism (Equity) fused with any-cost pragmatism (Utility). Self/Other −0.40: ego-driven, wants to be the one who tears down the order and replaces it. PP-685 §3 mapping (Authority/Honor/Identity) superseded per Jordan 2026-05-08.');
INSERT INTO "convictions" VALUES('NPC-060','Warden',0.4,1,'behavior_v30 §2.14: Primary = Continuity (''The work continues regardless of who sits on the throne'') → Warden. Secondary = Precedent (procedural correctness fallback). Administrative Proceduralism ethical framework.');
INSERT INTO "convictions" VALUES('NPC-060','Precedent',0.25,2,'behavior_v30 §2.14: Primary = Continuity (''The work continues regardless of who sits on the throne'') → Warden. Secondary = Precedent (procedural correctness fallback). Administrative Proceduralism ethical framework.');
CREATE TABLE goals (
    npc_id TEXT NOT NULL, goal TEXT NOT NULL,
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
INSERT INTO "goals" VALUES('NPC-032','Einhir revival through Crown authority');
INSERT INTO "goals" VALUES('NPC-032','Caste dismantlement through royal decree');
INSERT INTO "goals" VALUES('NPC-050','Sovereign Authority Doctrine');
INSERT INTO "goals" VALUES('NPC-050','Constitutional framework supersedes Church jurisdiction');
INSERT INTO "goals" VALUES('NPC-050','Hafenmark parliamentary sovereignty');
INSERT INTO "goals" VALUES('NPC-052','Einhir cultural revival at any cost');
INSERT INTO "goals" VALUES('NPC-052','Varfell military expansion');
INSERT INTO "goals" VALUES('NPC-052','Dismantle post-war caste order');
INSERT INTO "goals" VALUES('NPC-052','Intelligence-first approach to RM');
INSERT INTO "goals" VALUES('NPC-060','Maintain institutional function');
INSERT INTO "goals" VALUES('NPC-060','Ministry neutrality');
CREATE TABLE npcs (
    id TEXT PRIMARY KEY, first_name TEXT NOT NULL, last_name TEXT,
    faction TEXT, role TEXT, status TEXT DEFAULT 'canonical', title TEXT,
    age TEXT, birthplace TEXT, territory TEXT, ts TEXT, coherence TEXT,
    certainty TEXT, resonant_style TEXT, self_other_initial REAL,
    cultural_label TEXT, arc_trajectory TEXT, source TEXT, notes TEXT
);
INSERT INTO "npcs" VALUES('NPC-001','Edeyja',NULL,'Independent (Southernmost Wardens)','Warden-Chief','canonical',NULL,NULL,'Southernmost','T15 (Southernmost)','75–80','9',NULL,'Evidence',-0.3,'varfell_alpine','Warden-Chief navigating Church pressure and Thread instability','designs/npcs/edeyja_npc.md, npc_roster_v30 §1','Highest TS of any living practitioner. Survived proximity to a major Gap/tear.');
INSERT INTO "npcs" VALUES('NPC-002','Maret','Uln','Varfell','Practitioner / Succession Fallback','canonical',NULL,NULL,'Western fjords (near southern Einhir communities in Varfell territory)',NULL,'~50',NULL,NULL,NULL,0.1,'lowenritter_military','Dual loyalty — personal sympathy vs professional duty. If Vaynard eliminated, takes Varfell leadership (PP-486).','npc_roster_v30 §2','Vaynard''s intelligence operative. Thread-sensitive. RM-adjacent targets consistently 1 season behind. Southern Einhir solidarity.');
INSERT INTO "npcs" VALUES('NPC-003','Yrsa','Vossen','Restoration Movement','RM Leader','canonical',NULL,NULL,NULL,NULL,'25',NULL,NULL,NULL,-0.3,'varfell_alpine','Visibility as vulnerability — permanent Heresy Investigation target','npc_roster_v30 §3','TS 25 — above practitioner threshold but below Forgetting resistance gate (29). PP-665 rename from Maret Vossen.');
INSERT INTO "npcs" VALUES('NPC-004','Sæmund','Haelgrund','Church','Inquisitor (Cardinal Justice)','canonical',NULL,NULL,NULL,NULL,'12',NULL,NULL,NULL,0.0,'ecclesiastical','Latent TS — doesn''t know he''s Thread Sensitive. PC diagnosis possible (Cognition vs Ob 2).','npc_roster_v30 §4','TS 12 — barely above practitioner threshold. Attributes hunches to investigative instinct. PROCEDURALIST behavioral AI.');
INSERT INTO "npcs" VALUES('NPC-005','Sigrid','Torsvald','Löwenritter','TS Riskbreaker (Covert)','canonical',NULL,NULL,NULL,NULL,'35',NULL,NULL,NULL,0.0,'lowenritter_military','Risk-averse on Thread collateral despite Riskbreaker doctrine — TS lets her perceive damage colleagues can''t.','npc_roster_v30 §5',NULL);
INSERT INTO "npcs" VALUES('NPC-006','Halvar','Brandt','Löwenritter','Officer (Lions'' Table)','canonical',NULL,NULL,'Halvardshelm',NULL,NULL,NULL,NULL,NULL,-0.1,'lowenritter_military','External threat fixated — evaluates every action against Altonian metric. Brandt succession if Ehrenwall falls.','npc_roster_v30 §6','Named after birthplace Halvardshelm — confirmed intentional.');
INSERT INTO "npcs" VALUES('NPC-007','Annika','Feldhaus','Guilds','Guilds Representative','canonical',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,0.1,'hafenmark_procedural','Profit-maximizing — sacrifices Guilds Mandate for Wealth. Thread-touched supply chain discoverable.','npc_roster_v30 §7',NULL);
INSERT INTO "npcs" VALUES('NPC-008','Peder','Almstedt','Crown (Ministry)','Ministry Bureaucrat (Chief Parliamentary Clerk)','canonical',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,0.0,'valorian_court','CONSERVATIVE — blocks radical action through procedure, not force. Cognition-heavy social contest target.','npc_roster_v30 §8',NULL);
INSERT INTO "npcs" VALUES('NPC-009','Gerik','Strand','Crown','Crown Minister (Lord Steward)','canonical',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,-0.1,'valorian_court','OVERPERFORMER — runs every important task. Flattery vulnerability (−1 Ob on social actions acknowledging competence).','npc_roster_v30 §9',NULL);
INSERT INTO "npcs" VALUES('NPC-010','Dalla','Virke','Niflhel (Virke syndicate)','Syndicate Broker','canonical',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,0.1,'hafenmark_procedural','Personal loyalty to partners vs family directives. Third conflict with family triggers enforcement.','npc_roster_v30 §10',NULL);
INSERT INTO "npcs" VALUES('NPC-011','Alexios','Laskaris','Altonia','Doux (Altonian Prince)','canonical','Doux',NULL,'Altonia',NULL,NULL,NULL,NULL,NULL,-0.2,'altonian','PROTECTIVE — priority is Elske''s safety. Flips if Elske Loyalty ≤ 2 (IP +3 immediately).','npc_roster_v30 §11',NULL);
INSERT INTO "npcs" VALUES('NPC-012','Rikard','Solberg','Independent (Schoenland)','Schoenland Factor','canonical',NULL,NULL,'Schoenland','T16 (Schoenland)',NULL,NULL,NULL,NULL,0.0,'hafenmark_procedural','STABILITY-SEEKING — natural ally for peace, obstacle for escalation. Motivated by homesickness (discoverable via Read Ob 2).','npc_roster_v30 §12',NULL);
INSERT INTO "npcs" VALUES('NPC-013','Aldric','Tormann','Church','Fourth Cardinal (Prudence)','canonical',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,0.1,'ecclesiastical','Parish Revolt arc or PC intervention path. Inadvertently funds Church charitable mission while undermining cultural authority.','npc_roster_v30 §13, npc_character_analyses_v30_infill',NULL);
INSERT INTO "npcs" VALUES('NPC-020','Almud','Almqvist','Crown','King','canonical','King',NULL,NULL,'T1 (Valorsplatz)','28',NULL,NULL,NULL,-0.1,'valorian_court','Canonical Crown Captain per sim continuity §1.2. Royal Assassination Fuse target (Arc F Eliminated → Lenneth Widow Regent).','faction_canon_v30 §Crown','TS 28 per character_canon — no threshold crossing. Honor enters via valorian_court cultural template.');
INSERT INTO "npcs" VALUES('NPC-021','Arne','Himlensendt','Church','Confessor (Church Leader)','canonical','Confessor',NULL,NULL,'T9 (Himmelenger)',NULL,NULL,NULL,NULL,0.0,'ecclesiastical',NULL,'faction_canon_v30 §Church','Canonical per params/bg/core.md L233. Agent in Crown Inner Circle via Father Gustav Linder.');
INSERT INTO "npcs" VALUES('NPC-030','Elske','Almqvist','Crown (Royal Family)','Princess (married to Doux Alexios Laskaris)','canonical',NULL,NULL,NULL,NULL,'0',NULL,'3',NULL,NULL,NULL,'Off-board diplomatic asset. Elske Loyalty stat drives Laskaris PROTECTIVE behavior. Return arc possible.','faction_canon_v30 §Crown','Royal Assassination Fuse — not a direct target but her safety drives Alexios''s behavior.');
INSERT INTO "npcs" VALUES('NPC-031','Torben','Almqvist','Crown (Royal Family)','Prince (Heir Apparent)','canonical','Prince',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'Arc E Bereaved Father (Royal Assassination Fuse target). Conviction emergence window Seasons 1–8 (ED-618).','faction_canon_v30 §Crown','Heir apparent. Convictions intentionally undefined at game start — emerge during play.');
INSERT INTO "npcs" VALUES('NPC-032','Lenneth','Almqvist','Crown (Royal Family)','Queen (Widow Regent if Almud eliminated)','canonical',NULL,NULL,NULL,'T1 (Valorsplatz)',NULL,NULL,NULL,NULL,-0.2,'valorian_court','Arc D The Avenger. If Almud eliminated (Arc F): becomes Widow Regent. Pro-Restoration — institutional revivalist, allied with Yrsa Vossen.','npc_character_analyses §2, faction_canon_v30 §Crown','Queen Lenneth Almqvist. Archivist by training. PP-685 §2.3 ecclesiastical profile was misattribution. Lenneth archive awakened Torsvald''s TS (character_analyses_infill §5).');
INSERT INTO "npcs" VALUES('NPC-033','Kolbrun','Thale','Crown (Inner Circle)','Spymaster','canonical',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,0.0,'valorian_court','Sole inner-circle contact to settlement-layer intelligence brokers. Certainty 3 (lowest in Inner Circle).','faction_canon_v30 §Crown sub-Organizations',NULL);
INSERT INTO "npcs" VALUES('NPC-034','Gustav','Linder','Church (dual-loyalty: Crown Inner Circle agent for Himlensendt)','Archbishop''s Representative / Father','canonical','Father',NULL,NULL,NULL,NULL,NULL,NULL,NULL,0.0,'ecclesiastical','Dual-loyalty NPC — Himlensendt''s agent inside Crown Inner Circle. Certainty 5 (highest).','faction_canon_v30 §Crown sub-Organizations',NULL);
INSERT INTO "npcs" VALUES('NPC-035','Theodor','Kreutz','Crown (Inner Circle) / Löwenritter Liaison','Royal Guard Captain','canonical',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,-0.1,'lowenritter_military','Pre-designated allegiance to Almud personally. His removal triggers Löwenritter Autonomy escalation toward Split.','faction_canon_v30 §Crown sub-Organizations',NULL);
INSERT INTO "npcs" VALUES('NPC-036','Wilhelm','Voss','Crown (Inner Circle)','Royal Marshal','canonical',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,0.0,'valorian_court',NULL,'faction_canon_v30 §Crown sub-Organizations',NULL);
INSERT INTO "npcs" VALUES('NPC-037','Annalie','Reichard','Crown (Inner Circle)','Lord Treasurer','canonical',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,0.0,'valorian_court',NULL,'faction_canon_v30 §Crown sub-Organizations','CORRECTED: previously listed as ''Church / Cardinal Reichard''. Per faction_canon, Annalie Reichard is Crown Inner Circle Lord Treasurer, NOT a Cardinal. The ''Cardinal Reichard'' in PP-685 §2.3 may be a separate entity (artifact 15 sample) or a naming confusion. [OPEN: verify if there is a distinct Cardinal Reichard in Church hierarchy].');
INSERT INTO "npcs" VALUES('NPC-038','Arnlod','Olafsson','Church','Cardinal (virtue assignment unconfirmed)','canonical',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,0.0,'ecclesiastical',NULL,'faction_canon_v30 §Church','Cardinal virtue assignment not found in faction_canon (Justice = Haelgrund, Temperance = Klapp candidate, Fortitude = Jarnstal candidate, Prudence = Tormann). [OPEN: which virtue does Arnlod hold, or is he a 5th cardinal without virtue assignment?]');
INSERT INTO "npcs" VALUES('NPC-039','Magnus','Klapp','Church','Cardinal (Temperance candidate)','canonical',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,-0.1,'ecclesiastical','Scholar''s Dilemma — TS exposure via archive work.','faction_canon_v30 §Church','NPC-051 (''Klapp'') references in arcs (Klapp Combat, Klapp Thread, etc.) refer to this character''s surname, not a separate NPC.');
INSERT INTO "npcs" VALUES('NPC-040','Osten','Jarnstal','Church','Cardinal (Fortitude candidate)','canonical',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,0.0,'ecclesiastical',NULL,'faction_canon_v30 §Church',NULL);
INSERT INTO "npcs" VALUES('NPC-041','Aldric','Hann','Restoration Movement','RM Visible Leadership (alongside Yrsa Vossen)','canonical',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'faction_canon_v30 §11 (caste/organization hierarchy)','RESOLVED: distinct character from NPC-013 Aldric Tormann (Church Cardinal Prudence). Aldric Hann is RM visible leadership. Two different factions, different surnames.');
INSERT INTO "npcs" VALUES('NPC-050','Inge','Baralta','Hafenmark','Duchess (Sovereign Authority claimant, Custodian/Claimant foil with Almud)','canonical','Duchess',NULL,NULL,NULL,NULL,NULL,NULL,NULL,-0.3,'hafenmark_procedural','Six foil pairings per npc_foils_v30: Almud ↔ Baralta (Custodian/Claimant); Lenneth ↔ Baralta (campaign-defining); Baralta ↔ Vaynard (total opposition).','npc_behavior_v30 §2.3, npc_character_analyses §6, faction_canon_v30',NULL);
INSERT INTO "npcs" VALUES('NPC-052','Magnus','Vaynard','Varfell','Duke (Varfell Leader)','canonical','Duke',NULL,NULL,NULL,NULL,NULL,NULL,NULL,-0.4,'lowenritter_military','Von Lohengramm programme — revolutionary expulsion. If eliminated, Maret Uln succession (PP-486).','npc_behavior_v30 §2.4, npc_character_analyses_infill §5, faction_canon_v30','PP-650 STRUCK on Cultural Reformation + VTM associations; character active. Reinhardt von Lohengramm archetype per Jordan.');
INSERT INTO "npcs" VALUES('NPC-060','Lennart','Haelgrund','Crown (Ministry)','Registrar (Ministry — Throughline T4)','canonical',NULL,NULL,NULL,NULL,'12 (Hidden)',NULL,NULL,'Consequence',0.0,'valorian_court','Arc A: The System''s Memory. Arc B: The Whistleblower (player shows Evidence that Ministry records have been altered).','npc_behavior_v30 §2.14','DISTINCT from NPC-004 Sæmund Haelgrund (Cardinal Justice, Church). Same surname — relationship unknown. Both TS 12. Ministry Registrar, not Church.');
CREATE TABLE open_issues (
    issue_id INTEGER PRIMARY KEY, status TEXT NOT NULL, summary TEXT NOT NULL
);
INSERT INTO "open_issues" VALUES(1,'RESOLVED','Legacy ethical labels migrated to 13-Conviction taxonomy');
INSERT INTO "open_issues" VALUES(2,'RESOLVED','Edeyja name confirmed final (mononym)');
INSERT INTO "open_issues" VALUES(3,'RESOLVED','Halvar birthplace Halvardshelm — intentional');
INSERT INTO "open_issues" VALUES(4,'RESOLVED','Two Aldrics are distinct (Tormann/Hann)');
INSERT INTO "open_issues" VALUES(5,'PARTIAL','Unlisted NPCs verified; character_canon entries pending');
INSERT INTO "open_issues" VALUES(6,'RESOLVED','Vaynard confirmed as Magnus Vaynard, Duke');
INSERT INTO "open_issues" VALUES(7,'OPEN','Stat gaps: deferred per npc_roster_v30');
INSERT INTO "open_issues" VALUES(8,'RESOLVED','Conviction migration complete — behavior_v30 authoritative');
INSERT INTO "open_issues" VALUES(9,'OPEN','Cardinal Reichard collision with Crown Lord Treasurer');
INSERT INTO "open_issues" VALUES(10,'RESOLVED','Lenneth is Queen, Equity primary, pro-Restoration');
INSERT INTO "open_issues" VALUES(11,'OPEN','Cardinal Arnlod virtue assignment unknown');
INSERT INTO "open_issues" VALUES(12,'RESOLVED','Conviction discrepancies resolved — behavior_v30 over PP-685');
INSERT INTO "open_issues" VALUES(13,'RESOLVED','Baralta = Inge, Duchess of Hafenmark, Precedent primary');
INSERT INTO "open_issues" VALUES(14,'RESOLVED','Vaynard = Magnus, Duke, Equity/Utility, Lohengramm archetype');
INSERT INTO "open_issues" VALUES(15,'RESOLVED','Lenneth Equity primary, archivist by training');
INSERT INTO "open_issues" VALUES(16,'NEW','Lennart Haelgrund added NPC-060 — Ministry Registrar, distinct from Cardinal');
INSERT INTO "open_issues" VALUES(17,'OPEN','Torsvald TS: roster=35, behavior=20+. Using 35.');
INSERT INTO "open_issues" VALUES(18,'OPEN','Maret Uln conviction discrepancy unresolved');
CREATE TABLE stats (
    npc_id TEXT NOT NULL, stat_name TEXT NOT NULL, stat_value TEXT NOT NULL,
    FOREIGN KEY (npc_id) REFERENCES npcs(id)
);
INSERT INTO "stats" VALUES('NPC-001','cognition','5');
INSERT INTO "stats" VALUES('NPC-001','focus','5');
INSERT INTO "stats" VALUES('NPC-001','endurance','4');
INSERT INTO "stats" VALUES('NPC-001','social','3–4');
COMMIT;
