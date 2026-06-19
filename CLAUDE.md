# XPONext Knowledge — Claude Instructions

## Repo-Struktur

Die vollständige Struktur dieses Repos ist in [`INDEX.md`](INDEX.md) dokumentiert.

**Bei jeder Änderung am Repo `INDEX.md` aktualisieren:**
- Neue Datei oder Ordner hinzugefügt → Eintrag in INDEX.md ergänzen
- Datei umbenannt oder verschoben → INDEX.md anpassen
- Datei gelöscht → Eintrag aus INDEX.md entfernen
- Neuer Skill erstellt → In der Skills-Tabelle eintragen (Name, Trigger, Beschreibung)
- Neues Konzept generiert → In der Konzepte-Tabelle ergänzen

## Ordner-Übersicht

| Ordner | Zweck |
|---|---|
| `skills/` | Claude Code Skills — werden täglich mit Google Drive synchronisiert |
| `wissen/` | Fachdokumente als Referenz für Claude |
| `konzepte/` | Fertige Kundenpitches als HTML (generiert mit `konzept_generator`) |
| `leadgen/` | Scraper-Skripte und Lead-Datensätze |

## Konzepte

Kundenpitches werden mit dem `konzept_generator` Skill als HTML-Dateien generiert und unter `konzepte/` gespeichert. Namensschema: `[Kundenname]_XPONext_Konzept.html`

## Wissen

Fachdokumente unter `wissen/` dienen als Referenz. Neue Wissensdokumente als `.md` ablegen und in `INDEX.md` eintragen.

---

## Google Drive Sync (Skills)

Alle Skills in diesem Repository (im Ordner `skills/`) werden **einmal täglich mit Google Drive synchronisiert**.

### Regeln

- **Täglich prüfen:** Vergleiche alle lokalen Skills unter `skills/` mit den entsprechenden Dateien in Google Drive.
- **Neue Skills hochladen:** Wenn ein neuer Skill-Ordner oder eine neue Skill-Datei lokal entdeckt wird, die noch nicht in Drive existiert, wird sie automatisch in Drive erstellt/aktualisiert.
- **Änderungen synchronisieren:** Wenn sich eine bestehende Skill-Datei lokal geändert hat (anhand von git-Änderungen oder Zeitstempeln), wird die Drive-Version damit überschrieben.
- **Drive ist nicht die Quelle der Wahrheit** — das lokale Repository ist führend. Drive dient als Backup und zur Weitergabe.

### Skill-Verzeichnis

```
skills/
├── XPONext_HTML/           — XPONext HTML Design System Skill
├── architect_website_creation/ — Architekt-Website Skill
├── google_ads_knowledge/   — Google Ads Wissen
├── konzept_generator/      — Konzept-Generator Skill
└── seo_geo_audit/          — SEO & GEO Audit Skill
```

### Durchführung

Nutze das Google Drive MCP (`mcp__claude_ai_Google_Drive__*`) für die Synchronisation:
1. Lokale Skills mit `ls skills/` auflisten
2. Drive-Inhalte mit `search_files` oder `list_recent_files` prüfen
3. Fehlende oder veraltete Dateien mit `create_file` oder `copy_file` aktualisieren
