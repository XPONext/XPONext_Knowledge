---
name: xponext-design
description: Use this skill whenever building any HTML page, landing page, website, or presentation for XPONext or in the XPONext brand style. Triggers when the user asks to create a website, landing page, HTML page, Präsentation, or any visual web content for XPONext or "in unserem Stil" / "in unserem Design". Always use this skill before writing any HTML — it defines the complete design system, components, and layout patterns that must be used consistently across all XPONext web output.
---

# XPONext Design System

## Brand Identity

XPONext is a modern online-marketing agency for local businesses. The visual style is clean, bold, and professional — inspired by top German digital agencies. White backgrounds, very large bold headlines, generous whitespace, and a strong green accent color.

## Color Palette

```css
--accent:        #3F5137;   /* Primary green RAL 6020 — headlines, buttons, badges */
--accent-dark:   #2E3D28;   /* Hover states */
--accent-light:  #E8EDE6;   /* Badge backgrounds, subtle highlights */
--text-primary:  #0D0D0D;   /* Headlines */
--text-body:     #4B5563;   /* Body text, subtitles */
--text-muted:    #9CA3AF;   /* Small hints, captions */
--bg:            #FFFFFF;   /* Page background */
--bg-subtle:     #F9FAFB;   /* Section alternates */
--border:        #E5E7EB;   /* Dividers, card borders */
--btn-outline-border: #D1D5DB;
```

## Typography

```css
font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;

/* Load Inter from Google Fonts */
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;700;800;900&display=swap" rel="stylesheet">

/* Scale */
.headline-xl  { font-size: clamp(2.4rem, 5vw, 3.8rem); font-weight: 900; line-height: 1.1; color: #0D0D0D; }
.headline-lg  { font-size: clamp(1.8rem, 3vw, 2.6rem); font-weight: 800; line-height: 1.2; color: #0D0D0D; }
.headline-md  { font-size: 1.4rem; font-weight: 700; color: #0D0D0D; }
.body         { font-size: 1.05rem; font-weight: 400; line-height: 1.7; color: #4B5563; }
.small        { font-size: 0.9rem; color: #9CA3AF; }
```

**Key rule:** Important words or phrases in headlines get the accent color — never the entire headline.

```html
<h1>Mehr Kunden für dein Unternehmen. <span style="color:#3F5137">Garantiert.</span></h1>
```

## Core Components

### Navigation

```html
<nav style="display:flex;align-items:center;justify-content:space-between;padding:1.2rem 5%;border-bottom:1px solid #E5E7EB;background:#fff;position:sticky;top:0;z-index:100;">
  <div style="font-size:1.2rem;font-weight:800;color:#0D0D0D;">XPO<span style="color:#3F5137">Next</span></div>
  <div style="display:flex;gap:2rem;align-items:center;">
    <a href="#" style="color:#4B5563;text-decoration:none;font-size:0.95rem;">Leistungen</a>
    <a href="#" style="color:#4B5563;text-decoration:none;font-size:0.95rem;">Ergebnisse</a>
    <a href="#" style="color:#4B5563;text-decoration:none;font-size:0.95rem;">Über uns</a>
    <a href="#" style="background:#3F5137;color:#fff;padding:0.55rem 1.3rem;border-radius:8px;text-decoration:none;font-weight:600;font-size:0.95rem;">Termin buchen</a>
  </div>
</nav>
```

### Badge (small label above headline)

```html
<div style="display:inline-flex;align-items:center;gap:6px;background:#E8EDE6;color:#2E3D28;padding:0.35rem 0.9rem;border-radius:99px;font-size:0.85rem;font-weight:600;margin-bottom:1.2rem;">
  ⚡ Online-Marketing für lokale Betriebe
</div>
```

### Hero Section (two-column)

```html
<section style="display:grid;grid-template-columns:1fr 1fr;gap:3rem;align-items:center;padding:5rem 5%;max-width:1200px;margin:0 auto;">
  <div>
    <!-- Badge -->
    <div style="display:inline-flex;align-items:center;gap:6px;background:#E8EDE6;color:#2E3D28;padding:0.35rem 0.9rem;border-radius:99px;font-size:0.85rem;font-weight:600;margin-bottom:1.2rem;">
      ⚡ Kurze Beschreibung
    </div>
    <!-- Headline -->
    <h1 style="font-size:clamp(2.4rem,5vw,3.8rem);font-weight:900;line-height:1.1;color:#0D0D0D;margin:0 0 1.2rem;">
      Headline hier.<br><span style="color:#3F5137">Akzent hier.</span>
    </h1>
    <!-- Subheadline -->
    <p style="font-size:1.1rem;color:#4B5563;line-height:1.7;margin:0 0 2rem;">
      Kurze überzeugende Beschreibung in 2-3 Sätzen.
    </p>
    <!-- CTA Buttons -->
    <div style="display:flex;gap:1rem;flex-wrap:wrap;">
      <a href="#" style="background:#3F5137;color:#fff;padding:0.85rem 1.8rem;border-radius:8px;text-decoration:none;font-weight:700;font-size:1rem;display:inline-flex;align-items:center;gap:8px;">Termin buchen →</a>
      <a href="#" style="background:#fff;color:#0D0D0D;padding:0.85rem 1.8rem;border-radius:8px;text-decoration:none;font-weight:600;font-size:1rem;border:1.5px solid #D1D5DB;display:inline-flex;align-items:center;gap:8px;">Mehr erfahren</a>
    </div>
  </div>
  <div>
    <!-- Image or visual element here -->
  </div>
</section>
```

### Social Proof Bar

```html
<div style="text-align:center;padding:1.5rem 5%;border-top:1px solid #E5E7EB;border-bottom:1px solid #E5E7EB;background:#F9FAFB;">
  <p style="font-size:0.9rem;font-weight:600;color:#9CA3AF;letter-spacing:0.05em;">BEREITS ÜBER 50 LOKALE UNTERNEHMEN BETREUT</p>
</div>
```

### Feature Cards (3-column grid)

```html
<section style="padding:5rem 5%;max-width:1200px;margin:0 auto;">
  <div style="text-align:center;margin-bottom:3rem;">
    <h2 style="font-size:clamp(1.8rem,3vw,2.4rem);font-weight:800;color:#0D0D0D;">Was wir für euch tun</h2>
    <p style="color:#4B5563;font-size:1.05rem;margin-top:0.75rem;">Alles aus einer Hand.</p>
  </div>
  <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:1.5rem;">
    <!-- Card -->
    <div style="background:#fff;border:1px solid #E5E7EB;border-radius:12px;padding:1.75rem;">
      <div style="width:44px;height:44px;background:#E8EDE6;border-radius:10px;display:flex;align-items:center;justify-content:center;margin-bottom:1rem;font-size:1.3rem;">🌐</div>
      <h3 style="font-size:1.15rem;font-weight:700;color:#0D0D0D;margin:0 0 0.5rem;">Webseite</h3>
      <p style="color:#4B5563;font-size:0.95rem;line-height:1.6;margin:0;">Professionelle, mobiloptimierte Webseite die auf Google gefunden wird.</p>
    </div>
  </div>
</section>
```

### Stats Row

```html
<section style="padding:4rem 5%;background:#F9FAFB;">
  <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(160px,1fr));gap:2rem;max-width:900px;margin:0 auto;text-align:center;">
    <div>
      <p style="font-size:2.6rem;font-weight:900;color:#3F5137;margin:0;">50+</p>
      <p style="font-size:0.9rem;color:#4B5563;margin:0.3rem 0 0;">Kunden betreut</p>
    </div>
  </div>
</section>
```

### CTA Section (full-width)

```html
<section style="padding:5rem 5%;background:#0D0D0D;text-align:center;">
  <h2 style="font-size:clamp(1.8rem,3vw,2.4rem);font-weight:800;color:#fff;margin:0 0 1rem;">Bereit für mehr Sichtbarkeit?</h2>
  <p style="color:#9CA3AF;font-size:1.05rem;margin:0 0 2rem;">Kostenloses Erstgespräch — kein Risiko.</p>
  <a href="#" style="background:#3F5137;color:#fff;padding:1rem 2.2rem;border-radius:8px;text-decoration:none;font-weight:700;font-size:1.05rem;">Termin buchen →</a>
</section>
```

### Footer

```html
<footer style="padding:2rem 5%;border-top:1px solid #E5E7EB;display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:1rem;">
  <div style="font-size:1rem;font-weight:800;color:#0D0D0D;">XPO<span style="color:#3F5137">Next</span></div>
  <div style="display:flex;gap:1.5rem;">
    <a href="#" style="color:#9CA3AF;text-decoration:none;font-size:0.85rem;">Impressum</a>
    <a href="#" style="color:#9CA3AF;text-decoration:none;font-size:0.85rem;">Datenschutz</a>
    <a href="#" style="color:#9CA3AF;text-decoration:none;font-size:0.85rem;">Kontakt</a>
  </div>
  <p style="color:#9CA3AF;font-size:0.85rem;margin:0;">© 2026 XPONext GbR</p>
</footer>
```

## Full Page Template

Every HTML page starts with this base:

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
  <!-- FOOTER -->
</body>
</html>
```

## Design Rules (always follow)

1. **Weißer Hintergrund** — kein Dunkel-Modus, keine bunten Hintergründe außer dem dunklen CTA-Block
2. **Sehr fette Headlines** — font-weight 800 oder 900 immer für h1/h2
3. **Akzentfarbe sparsam** — nur für einzelne Wörter in Headlines, Buttons, Icons, Badges
4. **Viel Whitespace** — padding mindestens 4rem–5rem vertikal für Sections
5. **Sticky Navigation** — immer oben fixiert mit weißem Hintergrund
6. **Zwei CTA-Stile** — primär (grün ausgefüllt) + sekundär (weiß mit Border)
7. **Karten** — weißer Hintergrund, 1px Border `#E5E7EB`, border-radius 12px
8. **Responsive** — immer `grid-template-columns: repeat(auto-fit, minmax(Xpx, 1fr))` für Grids
9. **Inter Font** — immer von Google Fonts laden
10. **Logo-Format** — `XPO` in schwarz + `Next` in Akzentgrün, font-weight 800

## Accent Color Variants

Standard:   #3F5137
Dark hover: #2E3D28
Light fill: #E8EDE6
Text on light fill: #2E3D28
```
