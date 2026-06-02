---
name: architect-website
description: Use this skill whenever a user wants to modernize, rebuild, or improve an architect's or architecture firm's website. Triggers on phrases like "Architekt Webseite", "architect website", "modernize architect site", "Architektur Büro Website aufbessern", or any request to improve/rebuild a website for an architect, architecture firm, or design studio. Always use this skill before writing any HTML — it defines the complete design system and workflow for architect websites.
---

# Architect Website Design System

Dieses Skill basiert auf der Analyse der Webseiten von BIG, Zaha Hadid Architects, Herzog & de Meuron, Snøhetta, OMA, David Chipperfield, Kengo Kuma & Associates und Renzo Piano Building Workshop — allesamt Büros der Weltspitze.

## Workflow — IMMER in dieser Reihenfolge ausführen

### Schritt 1: URL erfragen

Frage den Nutzer nach der URL der zu verbessernden Webseite:

> „Welche Webseite soll aufgebessert werden? Bitte gib mir die URL des bestehenden Auftritts."

Falls keine URL vorhanden ist (neues Büro, noch keine Seite), weiter zu Schritt 3.

### Schritt 2: Bestehende Seite analysieren

Sobald die URL vorliegt, rufe sie mit WebFetch ab und extrahiere:

- **Büroname** (exakte Schreibweise)
- **Tagline oder Selbstbeschreibung** (falls vorhanden)
- **Projekte** (Titel, Ort, Typ — so viele wie erkennbar)
- **Team / Personen** (Namen, Rollen)
- **Leistungen / Disziplinen**
- **Kontaktdaten** (E-Mail, Telefon, Adresse)
- **Social-Media-Links**
- **Sprache(n)** der Seite

Prompt für den WebFetch-Aufruf:
> „Extract all textual content from this architecture firm website: firm name, tagline, project names and locations, team members and roles, services/disciplines, contact info, and any social media links. List everything you find."

### Schritt 3: Fehlende Infos nachfragen

Wenn Informationen fehlen oder die Seite nicht abrufbar ist, frage gezielt:

1. „Wie lautet der genaue Name des Büros?"
2. „Welche Projekte (mit Titel und Ort) sollen dargestellt werden?"
3. „Wer gehört zum Team? (Namen + Rollen)"
4. „Was sind die angebotenen Leistungen / Disziplinen?"
5. „Welche Kontaktdaten sollen erscheinen?"
6. „Gibt es ein Logo, oder soll nur Text verwendet werden?"
7. „Welche Sprache(n) soll die Seite haben?"

### Schritt 4: Neue Webseite bauen

Baue eine vollständige, moderne `index.html` nach dem unten definierten Design-System. Alle gesammelten Inhalte werden direkt eingesetzt — keine Platzhalter außer für fehlende Infos, die nicht erfragt werden konnten.

---

## Design-System

### Kernprinzip

Das Wichtigste, was alle Top-Architekturbüros gemeinsam haben: **maximale Zurückhaltung erzeugt maximalen Eindruck.** Die Webseite tritt in den Hintergrund — die Projekte stehen im Mittelpunkt. Kein dekoratives Design. Kein Overload. Das Interface ist nahezu unsichtbar.

### Farbpalette

```css
--bg:          #ffffff;   /* Primärer Hintergrund — immer weiß */
--bg-subtle:   #F7F7F7;   /* Sektionswechsel, Cards */
--text-primary:#0D0D0D;   /* Headlines */
--text-body:   #4B4B4B;   /* Fließtext */
--text-muted:  #9CA3AF;   /* Metadaten, Captions, Labels */
--border:      #E5E5E5;   /* Trennlinien, Card-Borders */
--accent:      #0D0D0D;   /* Primärer Akzent = Schwarz */
```

**Regel:** Farbe kommt ausschließlich aus den Projektfotos. Kein Brand-Grün, kein Brand-Blau — die Architektur selbst liefert die Farbe.

### Typografie

```css
/* Google Fonts laden */
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&family=DM+Sans:ital,wght@0,300;0,400;0,500;1,300&display=swap" rel="stylesheet">

/* Headings */
font-family: 'DM Sans', sans-serif;
font-weight: 300 oder 400;   /* Leicht — niemals fett */
letter-spacing: -0.02em;     /* Eng, modern */

/* Body */
font-family: 'Inter', sans-serif;
font-weight: 400;
line-height: 1.7;
```

**Regel:** Keine fetten Headlines (font-weight max 500). Größe statt Gewicht erzeugt Hierarchie. Dezente letter-spacing-Werte. Alles wirkt elegant durch Leichtigkeit, nicht durch Masse.

### Abstände & Grid

```css
/* Section padding */
padding: 7rem 6%;   /* Desktop */
padding: 4rem 5%;   /* Mobile */

/* Max-Width */
max-width: 1280px;
margin: 0 auto;

/* Grid für Projekte */
grid-template-columns: repeat(auto-fill, minmax(380px, 1fr));
gap: 2px;   /* Fast kein Gap — Projekte stoßen aneinander */

/* Oder klassisches 2-Spalten Grid */
grid-template-columns: 1fr 1fr;
gap: 1.5rem;
```

**Regel:** Viel Whitespace innerhalb von Sektionen. Aber bei Projekt-Grids: enger zusammenstellen für maximale Bildwirkung.

---

## Seitenstruktur & Komponenten

### Navigation

```html
<nav style="
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 1.5rem 6%;
  position: sticky;
  top: 0;
  background: rgba(255,255,255,0.95);
  backdrop-filter: blur(8px);
  -webkit-backdrop-filter: blur(8px);
  border-bottom: 1px solid #E5E5E5;
  z-index: 100;
">
  <!-- Logo: nur Text, leichtes Gewicht -->
  <div style="font-family:'DM Sans',sans-serif;font-size:1rem;font-weight:400;letter-spacing:0.08em;text-transform:uppercase;color:#0D0D0D;">
    [BÜRONAME]
  </div>
  <!-- Links: max 4-5, alle gleich gestylt -->
  <div style="display:flex;gap:2.5rem;align-items:center;">
    <a href="#projekte" style="font-size:0.82rem;font-weight:400;color:#4B4B4B;letter-spacing:0.04em;text-decoration:none;text-transform:uppercase;">Projekte</a>
    <a href="#buero" style="font-size:0.82rem;font-weight:400;color:#4B4B4B;letter-spacing:0.04em;text-decoration:none;text-transform:uppercase;">Büro</a>
    <a href="#kontakt" style="font-size:0.82rem;font-weight:400;color:#4B4B4B;letter-spacing:0.04em;text-decoration:none;text-transform:uppercase;">Kontakt</a>
  </div>
</nav>
```

### Hero-Sektion

Kein klassischer Hero-Banner. Stattdessen: riesiges Bild eines Leitprojekts + minimaler Textblock.

```html
<section style="position:relative;width:100%;aspect-ratio:16/7;overflow:hidden;background:#F0EEE9;">
  <!-- Bild: img-Tag wenn vorhanden, sonst subtiler Gradient als Platzhalter -->
  <div style="
    position:absolute;inset:0;
    background: linear-gradient(135deg, #E8E4DE 0%, #D5D0C8 100%);
    display:flex;align-items:flex-end;
  ">
    <div style="padding:3rem 6%;max-width:700px;">
      <p style="font-size:0.75rem;font-weight:400;letter-spacing:0.1em;text-transform:uppercase;color:#9CA3AF;margin-bottom:0.6rem;">[Projektname], [Ort] — [Jahr]</p>
      <h1 style="font-family:'DM Sans',sans-serif;font-size:clamp(2rem,4vw,3.2rem);font-weight:300;line-height:1.15;letter-spacing:-0.02em;color:#0D0D0D;margin:0;">[Tagline oder Büroname vollständig]</h1>
    </div>
  </div>
</section>
```

### Intro-Text (unter Hero)

```html
<section style="padding:5rem 6%;max-width:800px;">
  <p style="font-family:'DM Sans',sans-serif;font-size:clamp(1.1rem,2vw,1.4rem);font-weight:300;line-height:1.65;color:#0D0D0D;letter-spacing:-0.01em;">
    [Selbstbeschreibung des Büros in 2-3 Sätzen. Keine Marketing-Floskeln. Sachlich, präzise, selbstbewusst.]
  </p>
</section>
```

### Projekt-Grid

```html
<section id="projekte" style="padding:0 6% 6rem;">
  <div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:2rem;">
    <h2 style="font-family:'DM Sans',sans-serif;font-size:0.75rem;font-weight:400;letter-spacing:0.1em;text-transform:uppercase;color:#9CA3AF;">Projekte</h2>
    <!-- Optional: Filter-Links -->
    <div style="display:flex;gap:1.5rem;">
      <a href="#" style="font-size:0.75rem;letter-spacing:0.06em;text-transform:uppercase;color:#0D0D0D;text-decoration:none;border-bottom:1px solid #0D0D0D;padding-bottom:1px;">Alle</a>
      <a href="#" style="font-size:0.75rem;letter-spacing:0.06em;text-transform:uppercase;color:#9CA3AF;text-decoration:none;">Wohnbau</a>
      <a href="#" style="font-size:0.75rem;letter-spacing:0.06em;text-transform:uppercase;color:#9CA3AF;text-decoration:none;">Kultur</a>
    </div>
  </div>
  <div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(380px,1fr));gap:2px;">
    <!-- Projekt-Card -->
    <div style="position:relative;aspect-ratio:4/3;overflow:hidden;background:#E8E4DE;cursor:pointer;group;">
      <!-- Bild hier -->
      <div style="
        position:absolute;inset:0;
        background:linear-gradient(to top, rgba(0,0,0,0.55) 0%, transparent 50%);
        opacity:0;
        transition:opacity 0.3s;
      " onmouseover="this.style.opacity='1'" onmouseout="this.style.opacity='0'">
        <div style="position:absolute;bottom:0;left:0;padding:1.5rem;">
          <p style="font-size:0.7rem;font-weight:400;letter-spacing:0.08em;text-transform:uppercase;color:rgba(255,255,255,0.7);margin-bottom:0.3rem;">[Ort] — [Jahr]</p>
          <p style="font-size:1rem;font-weight:400;color:#fff;font-family:'DM Sans',sans-serif;">[Projekttitel]</p>
        </div>
      </div>
    </div>
  </div>
</section>
```

### Büro / About-Sektion

```html
<section id="buero" style="padding:7rem 6%;background:#F7F7F7;">
  <div style="max-width:1280px;margin:0 auto;display:grid;grid-template-columns:1fr 2fr;gap:6rem;align-items:start;">
    <div>
      <p style="font-size:0.75rem;font-weight:400;letter-spacing:0.1em;text-transform:uppercase;color:#9CA3AF;margin-bottom:1.5rem;">Büro</p>
      <h2 style="font-family:'DM Sans',sans-serif;font-size:clamp(1.6rem,2.5vw,2.2rem);font-weight:300;line-height:1.2;letter-spacing:-0.02em;color:#0D0D0D;">[Büroname]<br>seit [Gründungsjahr]</h2>
    </div>
    <div>
      <p style="font-size:1rem;color:#4B4B4B;line-height:1.75;margin-bottom:2rem;">[Beschreibung des Büros — Philosophie, Ansatz, Spezialisierung. 3-4 Sätze.]</p>
      <!-- Disziplinen/Leistungen als schmale Liste -->
      <div style="display:flex;flex-wrap:wrap;gap:0.5rem;">
        <span style="font-size:0.75rem;letter-spacing:0.06em;text-transform:uppercase;border:1px solid #D1D1D1;padding:0.3rem 0.8rem;color:#4B4B4B;">[Leistung 1]</span>
        <span style="font-size:0.75rem;letter-spacing:0.06em;text-transform:uppercase;border:1px solid #D1D1D1;padding:0.3rem 0.8rem;color:#4B4B4B;">[Leistung 2]</span>
      </div>
    </div>
  </div>
</section>
```

### Team-Sektion

```html
<section style="padding:7rem 6%;">
  <div style="max-width:1280px;margin:0 auto;">
    <p style="font-size:0.75rem;font-weight:400;letter-spacing:0.1em;text-transform:uppercase;color:#9CA3AF;margin-bottom:3rem;">Team</p>
    <div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));gap:2.5rem;">
      <!-- Team-Member -->
      <div>
        <!-- Foto-Platzhalter -->
        <div style="aspect-ratio:3/4;background:#E8E4DE;margin-bottom:1rem;border-radius:2px;"></div>
        <p style="font-size:0.95rem;font-weight:500;color:#0D0D0D;margin-bottom:0.2rem;">[Name]</p>
        <p style="font-size:0.82rem;color:#9CA3AF;letter-spacing:0.03em;">[Rolle]</p>
      </div>
    </div>
  </div>
</section>
```

### Kontakt-Sektion

```html
<section id="kontakt" style="padding:7rem 6%;background:#0D0D0D;">
  <div style="max-width:1280px;margin:0 auto;display:grid;grid-template-columns:1fr 1fr;gap:6rem;align-items:end;">
    <div>
      <p style="font-size:0.75rem;font-weight:400;letter-spacing:0.1em;text-transform:uppercase;color:#6B7280;margin-bottom:1.5rem;">Kontakt</p>
      <h2 style="font-family:'DM Sans',sans-serif;font-size:clamp(2rem,3.5vw,3rem);font-weight:300;line-height:1.15;letter-spacing:-0.02em;color:#fff;margin-bottom:2.5rem;">Gemeinsam<br>etwas bauen.</h2>
      <a href="mailto:[EMAIL]" style="font-size:1rem;color:#fff;text-decoration:none;border-bottom:1px solid rgba(255,255,255,0.3);padding-bottom:2px;">[EMAIL]</a>
    </div>
    <div style="display:flex;flex-direction:column;gap:0.75rem;align-self:end;">
      <p style="font-size:0.82rem;color:#6B7280;line-height:1.7;">[Adresse, PLZ, Stadt]</p>
      <p style="font-size:0.82rem;color:#6B7280;">[Telefon]</p>
      <div style="display:flex;gap:1.5rem;margin-top:1rem;">
        <a href="#" style="font-size:0.75rem;letter-spacing:0.06em;text-transform:uppercase;color:#6B7280;text-decoration:none;">Instagram</a>
        <a href="#" style="font-size:0.75rem;letter-spacing:0.06em;text-transform:uppercase;color:#6B7280;text-decoration:none;">LinkedIn</a>
      </div>
    </div>
  </div>
</section>
```

### Footer

```html
<footer style="padding:1.5rem 6%;background:#0D0D0D;border-top:1px solid #1A1A1A;display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:1rem;">
  <p style="font-size:0.75rem;color:#4B5563;letter-spacing:0.04em;">© [JAHR] [BÜRONAME]. Alle Rechte vorbehalten.</p>
  <div style="display:flex;gap:1.5rem;">
    <a href="#" style="font-size:0.75rem;color:#4B5563;text-decoration:none;letter-spacing:0.04em;">Impressum</a>
    <a href="#" style="font-size:0.75rem;color:#4B5563;text-decoration:none;letter-spacing:0.04em;">Datenschutz</a>
  </div>
</footer>
```

---

## Vollständiges HTML-Template

```html
<!DOCTYPE html>
<html lang="de">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>[BÜRONAME] — Architektur</title>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500&family=DM+Sans:ital,wght@0,300;0,400;0,500;1,300&display=swap" rel="stylesheet">
  <style>
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    body { font-family: 'Inter', sans-serif; background: #fff; color: #0D0D0D; -webkit-font-smoothing: antialiased; }
    a { transition: opacity 0.2s, color 0.2s; }
    a:hover { opacity: 0.6; }
    img { display: block; width: 100%; height: 100%; object-fit: cover; }

    @media (max-width: 768px) {
      /* Grid → 1 Spalte */
      /* Nav: Logo + Hamburger oder nur Logo */
      /* Kontakt: 1 Spalte */
    }
  </style>
</head>
<body>
  <!-- NAV -->
  <!-- HERO (großes Projektfoto) -->
  <!-- INTRO TEXT -->
  <!-- PROJEKTE GRID -->
  <!-- BÜRO / ABOUT -->
  <!-- TEAM -->
  <!-- KONTAKT -->
  <!-- FOOTER -->
</body>
</html>
```

---

## Design-Regeln (niemals brechen)

1. **Kein Bold für Headlines** — font-weight 300 oder 400, nie 700+
2. **Uppercase nur für Labels** — Sektionsnamen, Metadaten, Nav-Links; niemals für Headlines
3. **Farbe kommt vom Foto** — kein Brand-Farbschema
4. **Bilder dominieren** — mindestens 60% der Viewport-Fläche sollten Projektbilder sein; wenn keine vorhanden, neutrale Platzhalter mit `#E8E4DE`
5. **Maximal 5 Nav-Punkte**
6. **Kein Carousel, kein Slider** — statisches Grid ist professioneller
7. **Hover-Effekte subtil** — Overlay mit Projekt-Info beim Hover auf Cards; opacity-Transition
8. **Viel Luft** — padding vertikal mindestens 5rem pro Sektion
9. **letter-spacing uppercase** — immer 0.06em–0.1em bei Uppercase-Text
10. **Kontakt-Sektion = einzige dunkle Sektion** — dark background (#0D0D0D) nur am Ende

---

## Bildstrategie bei fehlenden Fotos

Falls keine Projektfotos verfügbar sind:

```css
/* Neutrale Platzhalter — wirken hochwertig durch Farbabstufung */
.placeholder-1 { background: #E8E4DE; }  /* Warmgrau */
.placeholder-2 { background: #D5D0C8; }  /* Mittleres Warmgrau */
.placeholder-3 { background: #EAE8E4; }  /* Hellbeige */
.placeholder-4 { background: #DDDAD4; }  /* Graubeige */
```

Immer darauf hinweisen, dass echte Projektfotografie den größten Qualitätssprung bringt.
