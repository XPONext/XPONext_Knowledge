---
name: xponext-design
description: Use this skill whenever creating ANY output for XPONext — websites, landing pages, HTML pages, presentations (PPTX or HTML), proposals, documents, or any other visual material. Also triggers when the user says "in unserem Stil", "in unserem Design", "XPONext-Design", or "wie bei uns". This skill defines the complete XPONext brand identity and must be applied consistently across all media. Always read this skill fully before producing any output.
---

# XPONext Brand & Design System

## 1. Brand Identity

XPONext is a modern online-marketing agency for local businesses in Germany. The brand is clean, bold, and professional — with a strong personality. The visual language communicates expertise and trust without being corporate or cold.

**Core brand values:** Klar. Direkt. Verlässlich.

**Tone of voice:** Du-Form, no jargon, results-focused. Never salesy. Always specific.

---

## 2. Logo

### Format
The XPONext logo is always rendered as two-tone bold text — no image file required.

```
XPO        →  color: #0D0D0D  (schwarz)
Next       →  color: #3F5137  (Akzentgrün)
font-weight: 800
```

### HTML
```html
<span style="font-weight:800;color:#0D0D0D;font-family:'Inter',sans-serif;">XPO<span style="color:#3F5137;">Next</span></span>
```

### Placement Rules
| Kontext | Position | Größe |
|---|---|---|
| Website Navigation | Oben links | font-size: 1.2rem |
| Website Footer | Unten links | font-size: 1rem |
| Präsentation Titelfolie | Oben links, Abstand: 2.5cm vom Rand | font-size: 28–32pt |
| Präsentation alle weiteren Folien | Oben links, kleiner | font-size: 16–18pt |
| Dokumente / Angebote | Oben links auf jeder Seite | font-size: 14–16pt |

### Logo Don'ts
- ❌ Niemals das Logo zentrieren (außer explizit gewünscht auf Titelfolien)
- ❌ Niemals andere Farben für XPO oder Next verwenden
- ❌ Niemals font-weight unter 700
- ❌ Niemals auf farbigem Hintergrund ohne Anpassung (auf dunklem Hintergrund: XPO weiß, Next grün)

### Logo auf dunklem Hintergrund
```html
<span style="font-weight:800;color:#FFFFFF;font-family:'Inter',sans-serif;">XPO<span style="color:#3F5137;">Next</span></span>
```

---

## 3. Farben

```css
/* Primärfarben */
--accent:        #3F5137;   /* Hauptgrün — Buttons, Highlights, Akzente in Headlines */
--accent-dark:   #2E3D28;   /* Hover-Zustände, dunklere Variante */
--accent-light:  #E8EDE6;   /* Badge-Hintergründe, dezente Highlights */

/* Text */
--text-primary:  #0D0D0D;   /* Headlines, Logo "XPO" */
--text-body:     #4B5563;   /* Fließtext, Untertitel */
--text-muted:    #9CA3AF;   /* Hinweise, Captions, Footer-Links */

/* Hintergründe */
--bg:            #FFFFFF;   /* Standard-Seitenhintergrund */
--bg-subtle:     #F9FAFB;   /* Abwechselnde Sections, Tabellen */
--bg-dark:       #0D0D0D;   /* CTA-Blöcke, dunkle Abschnitte */

/* UI */
--border:        #E5E7EB;   /* Trennlinien, Card-Rahmen */
--btn-outline-border: #D1D5DB;
```

### Farbeinsatz-Regeln
- Akzentgrün sparsam einsetzen — maximal 1–2 Elemente pro Sichtbereich
- Nie ganze Headlines grün — nur einzelne Schlüsselwörter oder -phrasen
- Hintergründe bleiben weiß oder hellgrau (`#F9FAFB`) — keine bunten Flächen
- Einzige Ausnahme: der dunkle CTA-Block (`#0D0D0D`) am Seitenende

---

## 4. Typografie

**Schriftart:** Inter (Google Fonts)

```html
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;700;800;900&display=swap" rel="stylesheet">
```

### Skala

| Rolle | Größe | Gewicht | Farbe |
|---|---|---|---|
| Headline XL (H1) | clamp(2.4rem, 5vw, 3.8rem) | 900 | #0D0D0D |
| Headline L (H2) | clamp(1.8rem, 3vw, 2.6rem) | 800 | #0D0D0D |
| Headline M (H3) | 1.4rem | 700 | #0D0D0D |
| Body | 1.05rem | 400 | #4B5563 |
| Small / Caption | 0.9rem | 400–600 | #9CA3AF |

### Für Präsentationen (pt-Werte)
| Rolle | Größe | Gewicht |
|---|---|---|
| Titelfolie Headline | 44–54pt | 900 |
| Abschnitts-Headline | 32–38pt | 800 |
| Inhalts-Headline | 22–26pt | 700 |
| Body / Bulletpoints | 16–18pt | 400 |
| Fußzeile / Quelle | 10–11pt | 400 |

### Typografie-Regeln
- Schlüsselwörter in Headlines immer mit Akzentfarbe hervorheben — nie die gesamte Headline
- Kein Italic für Headlines — nur für Zitate oder Hervorhebungen in Fließtext
- Zeilenabstand Body: 1.7 (Web) / 1.4 (Präsentation)

```html
<!-- Richtig: -->
<h1>Mehr Kunden für deinen Betrieb. <span style="color:#3F5137">Garantiert.</span></h1>

<!-- Falsch: -->
<h1 style="color:#3F5137">Mehr Kunden für deinen Betrieb.</h1>
```

---

## 5. Abstände & Spacing

Konsistentes Spacing ist entscheidend für das saubere, professionelle Erscheinungsbild.

### Web
```
Section vertikal:     padding 4rem–5rem oben/unten
Container max-width:  1200px, zentriert, padding 0 5%
Card-padding:         1.75rem
Gap zwischen Cards:   1.5rem
Gap Hero-Spalten:     3rem
Abstand Badge→H1:     1.2rem
Abstand H1→Subtext:   1.2rem
Abstand Subtext→CTA:  2rem
```

### Präsentationen
```
Folienrand:           2cm rundum (Mindestabstand aller Elemente vom Rand)
Logo oben links:      2cm vom linken Rand, 1.5cm von oben
Abschnitte:           mind. 0.8cm Abstand zwischen Inhaltselementen
Fußzeile:             0.8cm vom unteren Rand
```

### Dokumente (Angebote, Berichte)
```
Seitenränder:         2.5cm oben/unten, 2.5cm links/rechts
Logo oben links:      im Kopfbereich, Abstand 1.5cm vom Rand
Abschnitte:           16pt Abstand vor berschriften
```

---

## 6. Anwendung: Webseiten & Landing Pages

### Seitenstruktur (Reihenfolge)
1. Navigation (sticky)
2. Hero (2-spaltig: Text + Visual)
3. Social Proof Bar
4. Features / Leistungen (3er-Grid mit Cards)
5. Stats Row
6. Testimonials
7. CTA-Block (dunkel)
8. Footer

### Navigation
```html
<nav style="display:flex;align-items:center;justify-content:space-between;padding:1.2rem 5%;border-bottom:1px solid #E5E7EB;background:#fff;position:sticky;top:0;z-index:100;">
  <div style="font-size:1.2rem;font-weight:800;color:#0D0D0D;font-family:'Inter',sans-serif;">XPO<span style="color:#3F5137;">Next</span></div>
  <div style="display:flex;gap:2rem;align-items:center;">
    <a href="#" style="color:#4B5563;text-decoration:none;font-size:0.95rem;">Leistungen</a>
    <a href="#" style="color:#4B5563;text-decoration:none;font-size:0.95rem;">Ergebnisse</a>
    <a href="#" style="color:#4B5563;text-decoration:none;font-size:0.95rem;">Über uns</a>
    <a href="#" style="background:#3F5137;color:#fff;padding:0.55rem 1.3rem;border-radius:8px;text-decoration:none;font-weight:600;font-size:0.95rem;">Termin buchen</a>
  </div>
</nav>
```

### Badge
```html
<div style="display:inline-flex;align-items:center;gap:6px;background:#E8EDE6;color:#2E3D28;padding:0.35rem 0.9rem;border-radius:99px;font-size:0.85rem;font-weight:600;margin-bottom:1.2rem;">
  ⚡ Kurze Kategorie-Beschreibung
</div>
```

### Buttons
```html
<!-- Primär -->
<a href="#" style="background:#3F5137;color:#fff;padding:0.85rem 1.8rem;border-radius:8px;text-decoration:none;font-weight:700;font-size:1rem;display:inline-flex;align-items:center;gap:8px;">Termin buchen →</a>

<!-- Sekundär -->
<a href="#" style="background:#fff;color:#0D0D0D;padding:0.85rem 1.8rem;border-radius:8px;text-decoration:none;font-weight:600;font-size:1rem;border:1.5px solid #D1D5DB;display:inline-flex;align-items:center;gap:8px;">Mehr erfahren</a>
```

### Cards
```html
<div style="background:#fff;border:1px solid #E5E7EB;border-radius:12px;padding:1.75rem;">
  <div style="width:44px;height:44px;background:#E8EDE6;border-radius:10px;display:flex;align-items:center;justify-content:center;margin-bottom:1rem;font-size:1.3rem;">🌐</div>
  <h3 style="font-size:1.15rem;font-weight:700;color:#0D0D0D;margin:0 0 0.5rem;">Titel</h3>
  <p style="color:#4B5563;font-size:0.95rem;line-height:1.6;margin:0;">Beschreibung in 1-2 Sätzen.</p>
</div>
```

### CTA-Block (dunkel)
```html
<section style="padding:5rem 5%;background:#0D0D0D;text-align:center;">
  <h2 style="font-size:clamp(1.8rem,3vw,2.4rem);font-weight:800;color:#fff;margin:0 0 1rem;">Bereit für mehr Sichtbarkeit?</h2>
  <p style="color:#9CA3AF;font-size:1.05rem;margin:0 0 2rem;">Kkin Yudget. Kostenloses Erstgespräch.</p>
  <a href="#" style="background:#3F5137;color:#fff;padding:1rem 2.2rem;border-radius:8px;text-decoration:none;font-weight:700;font-size:1.05rem;">Termin buchen →</a>
</section>
```

### Footer
```html
<footer style="padding:2rem 5%;border-top:1px solid #E5E7EB;display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:1rem;">
  <div style="font-size:1rem;font-weight:800;color:#0D0D0D;font-family:'Inter',sans-serif;">XPO<span style="color:#3F5137;">Next</span></div>
  <div style="display:flex;gap:1.5rem;">
    <a href="#" style="color:#9CA3AF;text-decoration:none;font-size:0.85rem;">Impressum</a>
    <a href="#" style="color:#9CA3AF;text-decoration:none;font-size:0.85rem;">Datenschutz</a>
    <a href="#" style="color:#9CA3AF;text-decoration:none;font-size:0.85rem;">Kontakt</a>
  </div>
  <p style="color:#9CA3AF;font-size:0.85rem;margin:0;">© 2026 XPONext GbR></p>
</footer>
```

### HTML-Basis-Template
```html
<!DOCTYPE html>
<html lang="de">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>XPONext — [Seitentitel]</title>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;700;800;900&display=swap" rel="stylesheet">
  <style>
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    body { font-family: 'Inter', -apple-system, sans-serif; background: #fff; color: #0D0D0D; -webkit-font-smoothing: antialiased; }
    a { transition: opacity 0.15s; }
    a:hover { opacity: 0.85; }
    section { width: 100%; }
    .container { max-width: 1200px; margin: 0 auto; padding: 0 5%; }
  </style>
</head>
<body>
  <!-- NAV -->
  <!-- HERO -->
  <!-- SOCIAL PROOF -->
  <!-- FEATURES -->
  <!-- STATS -->
  <!-- CTA -->
  <!-- FOOTER
 -->
</body>
</html>
```

---

## 7. Anwendung: Präsentationen

Gilt für PPTX (python-pptx) und HTML-Präsentationen gleichermaßen.

### Folien-Typen & Layout

#### Titelfolie
- Hintergrund: Weiß (`#FFFFFF`)
- Logo: oben links, font-size 28pt
- Headline (Präsentationstitel): links ausgerichtet, sehr groß (44–54pt, font-weight 900), Schlüsselwort in Grün
- Untertitel: 18pt, `#4B5563`
- Dünne grüne Linie (`#3F5137`, 3pt) als horizontaler Akzent unter dem Titel
- Datum / Empfänger: unten links, 11pt, `#9CA3AF`

#### Inhaltsfolie (Standard)
- Hintergrund: Weiß
- Logo: oben links, klein (16pt)
- Seitennummer: unten rechts, 10pt, `#9CA3AF`
- Section-Label (optional): oben, Badge-Stil mit grünem Hintergrund
- Headline: 26–32pt, font-weight 800
- Body / Bullets: 16–18pt, `#4B5563`, Zeilenabstand 1.4

#### Abschnitts-Trennfolie
- Hintergrund: `#0D0D0D` (dunkel)
- Logo: oben links, weiß/grün
- Abschnittsname: zentriert, 38–44pt, font-weight 900, weiß
- Optional: grüne Linie als Dekorelement

#### Abschlussfolie
- Hintergrund: Weiß
- Headline: "Fragen?" oder CTA-Text, sehr groß, Akzent in Grün
- Kontakt: Name, E-Mail, Telefon — 16pt, `#4B5563`
- Logo: mittig oder unten links

### Präsentations-Regeln
- Maximal 6 Bulletpoints pro Folie — lieber mehr Folien
- Keine Bullet-Wände: Bullets sind kurz (max. 1 Zeile) + erklärende Notizen im Speaker-Bereich
- Bilder und Icons immer in grünem Badge-Stil (`#E8EDE6` Hintergrund, border-radius)
- Keine drop shadows, keine Verläufe, keine clipart-artigen Elemente
- Tabellen: Header-Zeile mit `#3F5137` Hintergrund + weißer Text, Zeilen alternieren `#fff` / `#F9FAFB`

---

## 8. Anwendung: Dokumente (Angebote, Berichte, E-Mails)

### Kopfzeile (jede Seite)
- Links: XPONext Logo (XPO schwarz, Next grün, font-weight 800)
- Rechts: Seitenzahl oder Dokumenttitel
- Trennlinie darunter: 1pt, `#E5E7EB`

### Angebots-Dokument Struktur
1. Deckblatt — Logo, Titel, Empfänger, Datum
2. Zusammenfassung — max. 1 Seite, das Wichtigste auf einen Blick
3. Leistungen — klare Abschnitte mit H2-Überschriften
4. Preise — Tabelle, sauber, kein Kleinstgedrucktes
5. Nächste Schritte — nummeriert, konkret
6. Kontakt & Impressum

### Schriften in Dokumenten
- Überschriften H1: 22pt, font-weight 800, `#0D0D0D`
- Überschriften H2: 16pt, font-weight 700, `#0D0D0D`
- Fließtext: 11pt, `#4B5563`, Zeilenabstand 1.5
- Tabellen-Header: 10pt, weiß auf `#3F5137`

### Hervorhebungen in Texten
- Wichtige Begriffe: **fett**, niemals unterstrichen
- Zahlen / Ergebnisse: Akzentgrün `#3F5137`, fett
- Niemals kursiv für ganze Sätze

---

## 9. Design Don'ts (gilt für alle Medien)

- ❌ Kein Dunkel-Modus — außer explizit als dunkler CTA-Block / Trennfolie
- ❌ Keine bunten Hintergründe (lila, blau, rot, etc.)
- ❌ Keine drop shadows oder Verläufe
- ❌ Kein Logo zentriert (außer spezifisch auf Titelfolie)
- ❌ Nicht die gesamte Headline in Grün
- ❌ Kein font-weight unter 700 für Headlines
- ❌ Keine anderen Schriften als Inter
- ❌ Keine Bilder mit weißem Hintergrund freigestellt (wirkt billig) — lieber auf `#F9FAFB`
- ❌ Kein Clipart, keine Stock-Icons mit Farbverläufen — von Emojis oder einfache Flat-Icons

---

## 10. Schnellreferenz

| Element | Wert |
|---|---|
| Primärfarbe | `#3F5137` |
| Hintergrund | `#FFFFFF` |
| Dunkel-Block | `#0D0D0D` |
| Schrift | Inter (Google Fonts) |
| Logo | `XPO` #0D0D0D + `Next` #3F5137, font-weight 800 |
| Logo-Position | Immer oben links |
| H1 Gewicht | 900 |
| H2 Gewicht | 800 |
| Border-radius Cards | 12px |
| Button border-radius | 8px |
| Max. Content-Breite | 1200px |
