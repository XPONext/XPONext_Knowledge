---
name: seo-geo-audit
description: Use this skill whenever a user wants to analyze, audit, or check a website for SEO and GEO (Generative Engine Optimization) performance. Triggers on phrases like "SEO prüfen", "Website analysieren", "SEO Audit", "GEO Optimierung", "wie gut ist die Webseite", "Webseite checken", "SEO Check", or any request to evaluate a website's search engine visibility. Always use this skill before running any audit — it defines the complete analysis framework and output format.
---

# SEO & GEO Audit Skill

Dieses Skill führt eine vollständige SEO- und GEO-Analyse einer beliebigen Webseite durch und gibt das Ergebnis als strukturierte Markdown-Tabelle aus — mit klarer Trennung zwischen positiven Aspekten und Verbesserungspotenzialen.

**Quellen:** XPONext SEO & GEO Optimierungsleitfaden 2026, Google Search Central, Schema.org, Core Web Vitals Dokumentation, GEO-Forschung (Superlines, Onely, DebugBear 2026).

---

## Workflow — IMMER in dieser Reihenfolge ausführen

### Schritt 1: URL erfragen (falls nicht angegeben)

> „Welche Webseite soll analysiert werden? Bitte URL eingeben."

### Schritt 2: Webseite abrufen

Rufe die URL mit dem `WebFetch`-Tool ab. Verwende diesen Prompt:

> „Extract the complete raw HTML source and all visible text content of this page. Include: page title, meta description, all heading tags (H1-H4) with their text, all image alt attributes, any JSON-LD or schema.org markup, any robots meta tags, links (internal and external count), presence of key takeaway boxes or FAQ sections, content structure (use of tables and lists), loading indicators or JavaScript dependencies visible in the HTML, Open Graph tags, canonical tag, hreflang tags, and any visible contact/address information."

### Schritt 3: robots.txt prüfen

Rufe `[domain]/robots.txt` ab mit diesem Prompt:

> „List all User-agent rules and their Disallow/Allow directives. Specifically check if GPTBot, ClaudeBot, PerplexityBot, Google-Extended, Bingbot, Googlebot are mentioned and whether they are blocked or allowed."

### Schritt 4: Analyse durchführen

Analysiere alle gesammelten Daten anhand der Prüfkriterienliste unten. Ordne jeden Punkt entweder ✅ (erfüllt/positiv) oder ⚠️ (verbesserungswürdig) zu. Bewerte nur Punkte, die du aus den abgerufenen Daten tatsächlich beurteilen kannst — markiere nicht überprüfbare Punkte mit ℹ️.

### Schritt 5: Ergebnistabelle ausgeben

Gib eine formatierte Markdown-Tabelle mit folgender Struktur aus:

```
## SEO & GEO Audit: [Domain]
Analysiert am: [Datum]

### Zusammenfassung
[3–5 Sätze: Gesamteindruck, kritischste Probleme, größtes Verbesserungspotenzial]

---

### Ergebnistabelle
```

Danach folgen die Kategorietabellen (siehe Format unten).

Abschließend:

```
### Top 5 Sofortmaßnahmen
[Nummerierte Liste der 5 wichtigsten Handlungsempfehlungen, priorisiert nach Impact]
```

---

## Prüfkatalog & Bewertungskriterien

### KATEGORIE A — Technische SEO-Grundlagen

| # | Prüfpunkt | Wie prüfen | Bewertungsmaßstab |
|---|---|---|---|
| A1 | HTTPS aktiv | URL-Protokoll | ✅ = https://, ⚠️ = http:// |
| A2 | Title-Tag vorhanden & optimiert | `<title>` im HTML | ✅ = vorhanden, 30–60 Zeichen; ⚠️ = fehlt, zu kurz/lang oder generisch |
| A3 | Meta-Description | `<meta name="description">` | ✅ = vorhanden, 120–160 Zeichen; ⚠️ = fehlt oder zu kurz/lang |
| A4 | H1-Tag | `<h1>` | ✅ = genau ein H1, keyword-relevant; ⚠️ = fehlt, mehrere H1s oder generisch |
| A5 | Heading-Hierarchie (H2–H4) | Alle Heading-Tags | ✅ = logische Struktur; ⚠️ = Sprünge (z.B. H1→H4), keine H2s |
| A6 | Canonical-Tag | `<link rel="canonical">` | ✅ = vorhanden, korrekt; ⚠️ = fehlt |
| A7 | Open Graph / Social Meta Tags | `<meta property="og:...">` | ✅ = og:title, og:description, og:image vorhanden; ⚠️ = fehlen |
| A8 | Hreflang (mehrsprachig) | `<link rel="hreflang">` | ✅ = vorhanden wenn mehrsprachig; ℹ️ = nicht prüfbar (einsprachig unklar) |
| A9 | Bilder mit Alt-Text | `<img alt="...">` | ✅ = alle/meiste Bilder haben aussagekräftigen Alt-Text; ⚠️ = leer oder fehlt bei mehreren |
| A10 | Interne Verlinkung | Anzahl interner Links | ✅ = mehrere sinnvolle interne Links; ⚠️ = kaum oder keine internen Links |

---

### KATEGORIE B — Performance & Core Web Vitals

| # | Prüfpunkt | Wie prüfen | Bewertungsmaßstab |
|---|---|---|---|
| B1 | LCP (Largest Contentful Paint) | PageSpeed-Hinweise im HTML / bekannte Richtwerte | ✅ = < 2,5s (schnell); ⚠️ = > 4s (langsam) — ℹ️ wenn nicht messbar |
| B2 | INP (Interaction to Next Paint) | JS-Menge / Rendering-Komplexität | ✅ = < 200ms angenommen bei wenig JS; ⚠️ = schwere JS-Last erkennbar |
| B3 | CLS (Cumulative Layout Shift) | Bilder ohne Dimensionen, keine fixed sizes | ✅ = Bilder mit width/height; ⚠️ = Bilder ohne Dimensionen erkennbar |
| B4 | Bild-Optimierung | Bildformate (webp, avif vs. jpg/png) | ✅ = WebP/AVIF sichtbar; ⚠️ = nur JPEG/PNG, keine modernen Formate erkennbar |
| B5 | JS-/CSS-Minifizierung | Dateinamen im HTML (`.min.js`) | ✅ = minifizierte Ressourcen; ⚠️ = unminifizierte Dateien erkennbar |

---

### KATEGORIE C — Crawling & Indexierung

| # | Prüfpunkt | Wie prüfen | Bewertungsmaßstab |
|---|---|---|---|
| C1 | robots.txt vorhanden | Abruf `[domain]/robots.txt` | ✅ = vorhanden & korrekt; ⚠️ = fehlt oder Kernseiten geblockt |
| C2 | Googlebot erlaubt | robots.txt | ✅ = nicht geblockt; ⚠️ = geblockt oder unklar |
| C3 | Sitemap deklariert | `Sitemap:` in robots.txt | ✅ = Sitemap-URL eingetragen; ⚠️ = fehlt |
| C4 | Robots-Meta-Tag | `<meta name="robots">` | ✅ = index, follow (oder nicht gesetzt = Standard); ⚠️ = noindex oder nofollow auf wichtigen Seiten |
| C5 | Keine JS-only Kerninhalte | HTML-Quelltext prüfen | ✅ = Hauptcontent im rohen HTML sichtbar; ⚠️ = leerer Body, Inhalte nur via JS geladen |
| C6 | Server-Side Rendering erkennbar | Inhalt im HTML-Quelltext vorhanden | ✅ = Text/Headings direkt im HTML; ⚠️ = nur `<div id="app"></div>` oder ähnlich |

---

### KATEGORIE D — GEO: KI-Crawler-Zugang

| # | Prüfpunkt | Wie prüfen | Bewertungsmaßstab |
|---|---|---|---|
| D1 | GPTBot (OpenAI) erlaubt | robots.txt | ✅ = nicht geblockt; ⚠️ = `Disallow: /` für GPTBot |
| D2 | ClaudeBot (Anthropic) erlaubt | robots.txt | ✅ = nicht geblockt; ⚠️ = geblockt |
| D3 | PerplexityBot erlaubt | robots.txt | ✅ = nicht geblockt; ⚠️ = geblockt |
| D4 | Google-Extended erlaubt | robots.txt | ✅ = nicht geblockt; ⚠️ = geblockt (verhindert AI Overviews) |
| D5 | Kein JS-Wall für Kerncontent | HTML-Quelltext | ✅ = Textinhalte im Raw-HTML sichtbar; ⚠️ = Inhalte hinter JS-Rendering verborgen |
| D6 | Server-Side Rendering | Seitenstruktur im HTML | ✅ = vollständiger Content im HTML; ⚠️ = SPA ohne SSR erkennbar |

---

### KATEGORIE E — GEO: Strukturierte Daten (Schema.org)

| # | Prüfpunkt | Wie prüfen | Bewertungsmaßstab |
|---|---|---|---|
| E1 | JSON-LD Schema vorhanden | `<script type="application/ld+json">` | ✅ = mindestens 1 Schema vorhanden; ⚠️ = kein Schema-Markup |
| E2 | Organization-Schema | JSON-LD Inhalt | ✅ = Organization mit Name, URL, Logo, Kontakt; ⚠️ = fehlt |
| E3 | FAQPage-Schema | JSON-LD Inhalt | ✅ = vorhanden (stark für GEO); ⚠️ = fehlt trotz FAQ-Abschnitt auf der Seite |
| E4 | Article/BlogPosting-Schema | JSON-LD Inhalt | ✅ = vorhanden bei Artikelseiten; ⚠️ = fehlt bei Blog/Newsseiten |
| E5 | LocalBusiness-Schema | JSON-LD Inhalt | ✅ = vorhanden mit Adresse, Öffnungszeiten; ⚠️ = fehlt bei lokalen Unternehmen |
| E6 | BreadcrumbList-Schema | JSON-LD Inhalt | ✅ = vorhanden; ⚠️ = fehlt trotz Breadcrumbs im Layout |

---

### KATEGORIE F — GEO: Content-Struktur & Extrahierbarkeit

| # | Prüfpunkt | Wie prüfen | Bewertungsmaßstab |
|---|---|---|---|
| F1 | Frage-basierte Überschriften (Q&A-Format) | H2/H3-Texte | ✅ = Headings als Fragen oder direkte Antworten formuliert; ⚠️ = nur generische Überschriften |
| F2 | Front-Loading (Inverted Pyramid) | Erster Absatz nach H1/H2 | ✅ = Kernaussage direkt im ersten Satz; ⚠️ = lange Einleitung ohne Kerninformation |
| F3 | Key Takeaways / TL;DR Box | Seiteninhalt | ✅ = Summary-Box am Seitenanfang erkennbar; ⚠️ = fehlt bei langen Inhaltsseiten |
| F4 | HTML-Tabellen für Vergleiche/Daten | `<table>` im HTML | ✅ = Tabellen vorhanden wo sinnvoll; ⚠️ = Vergleichsdaten nur als Fließtext |
| F5 | Bullet-Point-Listen für Fakten | `<ul>`, `<ol>` | ✅ = Listen für Aufzählungen genutzt; ⚠️ = Fakten in langen Fließtext-Absätzen |
| F6 | Direkte Definitionen | Erster Satz nach Heading | ✅ = „X ist …" Muster erkennbar; ⚠️ = keine klaren Definitionen für Schlüsselbegriffe |
| F7 | Textlänge & Informationsdichte | Geschätzter Textumfang | ✅ = ausführliche Inhalte mit konkreten Fakten; ⚠️ = sehr dünner Content (< 300 Wörter) |

---

### KATEGORIE G — GEO: Autorität & Off-Page Signale

| # | Prüfpunkt | Wie prüfen | Bewertungsmaßstab |
|---|---|---|---|
| G1 | Autorenangabe / E-E-A-T Signale | Seiteninhalt | ✅ = Autor, Qualifikation, Datum sichtbar; ⚠️ = kein Autor erkennbar |
| G2 | Quellen & externe Links | `<a href="...">` zu externen Domains | ✅ = Verlinkung zu autoritativen Quellen; ⚠️ = keine externen Quellen |
| G3 | Kontaktdaten / Impressum sichtbar | Adresse, Telefon, E-Mail im HTML | ✅ = NAP-Daten (Name, Adresse, Telefon) vorhanden; ⚠️ = fehlen oder nicht auffindbar |
| G4 | Statistiken & konkrete Daten | Inhalt auf Zahlen prüfen | ✅ = spezifische Zahlen, Studien, Daten vorhanden; ⚠️ = nur allgemeine Aussagen |
| G5 | Einzigartiger Informationsgewinn | Inhaltsbewertung | ✅ = spezifische, einzigartige Inhalte erkennbar; ⚠️ = generisch, austauschbar, standardisiert |
| G6 | Bewertungsplattformen erwähnt | Links zu Google Business, Trustpilot etc. | ✅ = Verlinkung/Erwähnung externer Reviews; ⚠️ = keine externen Bewertungsplattformen referenziert |

---

## Ausgabeformat (Beispiel)

```markdown
## SEO & GEO Audit: beispiel.de
Analysiert am: 17. Juni 2026

### Zusammenfassung
Die Webseite zeigt solide On-Page-Grundlagen mit korrekten Meta-Tags und HTTPS.
Die größten Schwächen liegen im Bereich GEO: Es fehlen sämtliche Schema.org-Markups,
KI-Crawler werden in der robots.txt nicht explizit erlaubt und der Content ist
kaum für KI-Extraktion strukturiert. Sofortmaßnahme: Schema-Markup + robots.txt anpassen.

---

### A — Technische SEO-Grundlagen

| Status | Prüfpunkt | Befund |
|--------|-----------|--------|
| ✅ | HTTPS aktiv | Seite läuft vollständig über https:// |
| ✅ | Title-Tag | „Muster GmbH – Webdesign München" (42 Zeichen) |
| ⚠️ | Meta-Description | Fehlt vollständig |
| ✅ | H1-Tag | Genau ein H1: „Professionelles Webdesign für München" |
| ⚠️ | Bilder mit Alt-Text | 6 von 9 Bilder ohne Alt-Attribut |

### B — Performance & Core Web Vitals

| Status | Prüfpunkt | Befund |
|--------|-----------|--------|
| ℹ️ | LCP | Nicht direkt messbar; hohe JS-Last erkennbar |
| ⚠️ | Bild-Optimierung | Alle Bilder als JPEG — kein WebP/AVIF erkennbar |

### C — Crawling & Indexierung

| Status | Prüfpunkt | Befund |
|--------|-----------|--------|
| ✅ | robots.txt | Vorhanden, Googlebot nicht geblockt |
| ⚠️ | Sitemap deklariert | Kein Sitemap-Eintrag in robots.txt |

### D — GEO: KI-Crawler-Zugang

| Status | Prüfpunkt | Befund |
|--------|-----------|--------|
| ⚠️ | GPTBot erlaubt | Nicht erwähnt in robots.txt — Status unklar |
| ⚠️ | ClaudeBot erlaubt | Nicht erwähnt — Standard-Blocking möglich |
| ✅ | Kein JS-Wall | Kerncontent im Raw-HTML vorhanden |

### E — GEO: Strukturierte Daten

| Status | Prüfpunkt | Befund |
|--------|-----------|--------|
| ⚠️ | JSON-LD Schema | Kein Schema-Markup vorhanden |
| ⚠️ | Organization-Schema | Fehlt |
| ⚠️ | FAQPage-Schema | Fehlt, obwohl FAQ-Sektion vorhanden |

### F — GEO: Content-Struktur

| Status | Prüfpunkt | Befund |
|--------|-----------|--------|
| ⚠️ | Frage-basierte Headings | Alle H2s als kurze Labels, nicht als Fragen |
| ⚠️ | Key Takeaways Box | Fehlt |
| ✅ | Bullet-Point-Listen | Listen für Leistungen verwendet |

### G — GEO: Autorität & Off-Page

| Status | Prüfpunkt | Befund |
|--------|-----------|--------|
| ⚠️ | Autorenangabe | Kein Autor, kein Datum erkennbar |
| ✅ | Kontaktdaten | Adresse, Telefon und E-Mail im Footer |
| ⚠️ | Statistiken & Daten | Nur allgemeine Aussagen, keine konkreten Zahlen |

---

### Top 5 Sofortmaßnahmen

1. **Schema.org JSON-LD einbauen** — Organization + FAQPage + LocalBusiness → stärkster GEO-Hebel
2. **robots.txt aktualisieren** — GPTBot, ClaudeBot, PerplexityBot und Google-Extended explizit erlauben
3. **Meta-Description ergänzen** — Fehlt komplett; direkte Auswirkung auf CTR
4. **Bilder optimieren** — Alt-Texte nachtragen + WebP-Format für alle Bilder einführen
5. **Sitemap in robots.txt eintragen** — Crawl-Effizienz verbessern
```

---

## Wichtige Hinweise für die Analyse

- Prüfe **immer** die robots.txt separat — sie ist das wichtigste Dokument für KI-Crawler-Zugang
- Bewerte nie Punkte als ✅, die du nicht im Quellcode/HTML verifiziert hast
- Nutze ℹ️ für Punkte wie Page Speed, die nur mit Dritttools (PageSpeed Insights) exakt messbar sind
- Weise den Nutzer am Ende immer auf Tools hin, mit denen er die ℹ️-Punkte selbst prüfen kann:
  - **Google PageSpeed Insights** → Core Web Vitals
  - **Google Rich Results Test** → Schema.org Validierung
  - **Google Search Console** → Indexierungsstatus, Crawl-Fehler
  - **Screaming Frog** → Technisches Full-Site-Audit
