---
name: konzept
description: Use this skill whenever the user wants to create a client concept or proposal document (Konzept, Angebot, Pitch-Deck) for a potential XPONext customer. Triggers on phrases like "erstell ein Konzept für", "mach ein Konzept für", "schreib ein Angebot für", "Konzept für [Name/Firma]", or any request to prepare a proposal for a client. Always run this skill before writing any HTML — it defines the full analysis and generation workflow.
---

# XPONext Konzept-Generator

Erstellt ein personalisiertes, interaktives HTML-Pitch-Deck für einen potenziellen Kunden.
Das Konzept wird analysiert auf Basis der echten Website des Kunden und beinhaltet einen Google-Ranking-Check.

**Ausgabe:** `konzepte/{Firmenname}_XPONext_Konzept.html`
**Versand:** HTML-Datei direkt als E-Mail-Anhang schicken. Öffnet sich im Browser, ist vollständig interaktiv, hat klickbare CTAs – wirkt wie ein Dokument, ohne verdächtiger Link zu sein.

**Modulare Leistungen:** Das Konzept passt sich an die gewünschten Leistungen an. Nicht gewünschte Leistungen werden komplett aus Slide 3 und den Intro-Tags entfernt.

---

## Schritt 1: Infos sammeln

Frage den Nutzer nach folgenden Infos, falls noch nicht angegeben:

1. **Name des Ansprechpartners** (z.B. „Herr Breuer")
2. **Firmenname** (z.B. „Ralf Breuer Architekt")
3. **Website-URL** der aktuellen Website
4. **Stadt** (für den Ranking-Check)
5. **Branche** (z.B. Architekt, Gebäudereinigung, Physiotherapeut …)
6. **Welche Leistungen sollen rein?** (Standard: alle vier. Nur anpassen wenn explizit genannt.)
   - Website neu bauen
   - SEO & GEO
   - Google Ads
   - Laufende Pflege
7. **Preise mit rein?** (Standard: Nein → „auf Anfrage". Nur Ja, wenn der Nutzer das explizit sagt.)

Wenn der Nutzer Leistungen ausschließt (z.B. „keine neue Website"), passe Slide 3 und den Intro-Tag-Block entsprechend an:
- Headline Slide 3 nur mit den gewählten Leistungen (z.B. „SEO. GEO. Google Ads.")
- Intro-Tags nur mit den gewählten Leistungen
- Nicht gewählte Leistungskarten werden komplett weggelassen

---

## Schritt 2: Website analysieren

Rufe die Website mit WebFetch ab. Prompt:

> „Analysiere diese Website vollständig. Extrahiere: 1) Ist ein Viewport-Meta-Tag vorhanden (mobiloptimiert)? 2) Was ist der Page-Title und die Meta-Description? 3) Welche Technologie/CMS wird verwendet (erkennbar an Generator-Meta-Tags, Footer-Texten, URL-Strukturen)? 4) Gibt es ein Copyright-Jahr – welches? 5) Wie viele Bilder haben Alt-Texte? 6) Gibt es HTTPS? 7) Wie strukturiert ist die Seite (Menü-Punkte, Sektionen)? 8) Was fällt negativ auf (veraltete Elemente, fehlende CTAs, defekte Elemente, kein Blog/News, kein Google Maps, etc.)? Liste alle Mängel konkret auf."

Notiere die gefundenen Mängel – sie kommen in Slide 2.

Falls die Website nicht abrufbar ist: Notiere „Website nicht abrufbar" und verwende Standard-Mängel für die Branche.

---

## Schritt 3: Ranking-Check

Führe zwei WebSearch-Anfragen durch:

1. `"{Branche} {Stadt}"` – Suche nach dem Unternehmen in den Ergebnissen
2. `"{Firmenname}"` – Direkte Suche

Stelle fest:
- Auf welcher Position / Seite erscheint das Unternehmen bei Suche 1?
- Gibt es einen Google Business-Eintrag?
- Erscheinen Wettbewerber prominent?

Notiere die Ranking-Position (z.B. „Seite 2, Position 4" oder „nicht auffindbar") – kommt in Slide 2.

---

## Schritt 4: HTML-Konzept generieren

Fülle das Template unten mit den gesammelten Daten und speichere die Datei unter:
`konzepte/{Firmenname ohne Sonderzeichen}_XPONext_Konzept.html`

**Befüllungsregeln:**
- Ersetze alle [PLATZHALTER] mit echten Werten
- Slide 2 (Status Quo): Verwende die 3–4 stärksten Mängel aus der Analyse + die Ranking-Position
- Halte den Text knapp und direkt – keine langen Absätze, keine Emojis, keine Bindestriche in Headlines
- Behalte die Slide-Struktur exakt bei (5 Slides)
- Wenn Preise gewünscht: Ergänze in Slide 4 die Preis-Box (siehe Ende dieses Dokuments)

**Stil-Regeln (immer einhalten):**
- Keine Emojis in Badges, Card-Icons oder Tags
- Keine Bindestriche (–) in Headlines → stattdessen Punkt + neue Zeile
- Sachlicher, professioneller Ton – kein „wir verkaufen Ihnen nichts", kein „kein Risiko"
- Eyebrow-Labels statt Badge-Bubbles
- Card-Icons: kleine grüne Linie (.card-bar) statt Emoji

---

## Das HTML-Template

Siehe aktuellste Version in konzepte/Bestattungshaus_Andriessen_XPONext_Konzept.html als Referenz für das finale Design (ohne Emojis, mit Eyebrow-Labels, kompaktes Spacing).

Struktur:
- Slide 1: Intro (Eyebrow, H1, Hero-Sub, Tags)
- Slide 2: Status Quo (Eyebrow, H2, Divider, Body, Stat-Row mit 3 Zahlen, 3 Cards mit card-bar, Highlight-Box)
- Slide 3: Leistungen (Eyebrow, H2, Divider, Body, Cards – nur gewählte Leistungen)
- Slide 4: Zusammenarbeit (Eyebrow, H2, Divider, Body, 4 Steps)
- Slide 5: CTA dark (Eyebrow-dark, H2 light, Divider, Body, Buttons)

---

## Platzhalter-Referenz

| Platzhalter | Beispiel |
|---|---|
| [FIRMENNAME] | Ralf Breuer Architekt |
| [HEADLINE_SLIDE1] | Da sein, wenn es darauf ankommt. |
| [HEADLINE_SLIDE1_EM] | Auch bei Google. |
| [SUBLINE_SLIDE1] | Ein Konzept für Ihre digitale Sichtbarkeit in [Stadt]. |
| [TAG1–3] | Branchenspezifische Begriffe |
| [HEADLINE_SLIDE2] | Gute Arbeit. |
| [HEADLINE_SLIDE2_EM] | Zu wenig Reichweite. |
| [EINLEITUNG_SLIDE2] | 1–2 Sätze über die aktuelle Situation, spezifisch für den Kunden |
| [RANKING_POSITION] | #1, Seite 2, Nicht gefunden |
| [SUCHBEGRIFF] | Architekt Düsseldorf |
| [MANGEL1–3_TITEL] | Konkreter Mangelname aus der Analyse |
| [MANGEL1–3_TEXT] | 1–2 Sätze Erklärung |

---

## Wenn Preise gewünscht sind

Füge am Ende von Slide 4 ein:

Einmalig (Website + SEO-Setup): €800–1.200
Monatlich Basis (Hosting, Pflege, SEO-Monitoring): €200/Monat
Monatlich mit Google Ads: €350/Monat

---

## Ausgabe-Dateiname

konzepte/[Firmenname_bereinigt]_XPONext_Konzept.html

Bereinigung: Leerzeichen → _, Umlaute → ae/oe/ue/ss, Sonderzeichen entfernen.
