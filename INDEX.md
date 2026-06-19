# XPONext Knowledge — Index

Zentrale Wissensdatenbank der XPONext GbR. Enthält Skills, Wissen, Konzepte und Leadgen-Tools.

---

## Skills (`skills/`)

Claude Code Skills, die täglich mit Google Drive synchronisiert werden.

| Skill | Trigger | Beschreibung |
|---|---|---|
| [`XPONext_HTML`](skills/XPONext_HTML/SKILL.md) | „in unserem Stil", „XPONext-Design", jede HTML-Ausgabe für XPONext | Komplettes XPONext Brand & Design System — Farben, Typografie, Komponenten |
| [`architect_website_creation`](skills/architect_website_creation/SKILL.md) | „Architekt Webseite", „Architektur Büro Website" | Design-System und Workflow für Architekten-Websites |
| [`google_ads_knowledge`](skills/google_ads_knowledge/SKILL.md) | „Google Ads Kampagne", „Keywords", „Anzeigen optimieren" | Google Ads Wissen aus der Zertifizierung (Tim) |
| [`konzept_generator`](skills/konzept_generator/SKILL.md) | „erstell ein Konzept für", „Angebot für [Firma]" | Analyse- und Generierungs-Workflow für Kundenpitches als HTML |
| [`seo_geo_audit`](skills/seo_geo_audit/SKILL.md) | „SEO prüfen", „Website analysieren", „SEO Audit" | Vollständiges SEO & GEO Audit-Framework |

---

## Wissen (`wissen/`)

Dokumentiertes Fachwissen als Referenz für Claude.

| Datei | Inhalt |
|---|---|
| [`geo_seo.md`](wissen/geo_seo.md) | GEO (Generative Engine Optimization) & SEO Grundlagen |
| [`google_ads_zertifizierung.md`](wissen/google_ads_zertifizierung.md) | Inhalte der Google Ads Zertifizierung |

---

## Konzepte (`konzepte/`)

Fertige Kundenpitches als HTML-Dateien (generiert mit dem `konzept_generator` Skill).

| Branche | Konzepte |
|---|---|
| Architektur | Acconci Architekten, Atmo Architektur, Dielen Innenarchitekten, ER Architekten, Edoo Architects |
| Bestattungen | Beerdigungsinstitut Werner, Berger, Orlob, Weller, Andriessen, Erwin Pfeil, Happe, Waigand |
| Sonstiges | Buschkuehle |

---

## Leadgen (`leadgen/`)

Scraper und Datensätze zur Lead-Generierung.

| Datei | Beschreibung |
|---|---|
| [`aknw_architekten_scraper.py`](leadgen/aknw_architekten_scraper.py) | Scraper für die AKNW Architektenliste NRW |
| [`aknw_architekten_nrw.csv`](leadgen/aknw_architekten_nrw.csv) | Ergebnis-Datensatz Architekten NRW |
| [`gebaeudereinigung_nrw_overpass.py`](leadgen/gebaeudereinigung_nrw_overpass.py) | Scraper via Overpass API (OpenStreetMap) |
| [`gebaeudereinigung_nrw_places.py`](leadgen/gebaeudereinigung_nrw_places.py) | Scraper via Google Places API |
| [`gebaeudereinigung_nrw.csv`](leadgen/gebaeudereinigung_nrw.csv) | Ergebnis-Datensatz Gebäudereinigung NRW |

---

## Automatisierung

| Cron | Zeit | Richtung |
|---|---|---|
| Skills → Google Drive | täglich 09:00 Berlin | Repo ist Quelle der Wahrheit |
| Google Drive → Skills | täglich 08:00 Berlin | Drive-Änderungen ins Repo committen |
| post-merge Hook (lokal) | nach jedem `git pull` | `skills/` → `~/.claude/skills/` |
