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
- Ersetze alle `[PLATZHALTER]` mit echten Werten
- Slide 2 (Status Quo): Verwende die 3–4 stärksten Mängel aus der Analyse + die Ranking-Position
- Halte den Text knapp und direkt – keine langen Absätze
- Behalte die Slide-Struktur exakt bei (5 Slides)
- Wenn Preise gewünscht: Ergänze in Slide 4 die Preis-Box (siehe Ende dieses Dokuments)

---

## Das HTML-Template

```html
<!DOCTYPE html>
<html lang="de">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>[FIRMENNAME] × XPONext</title>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
  <style>
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    :root {
      --accent: #3F5137; --accent-dark: #2E3D28; --accent-light: #E8EDE6;
      --text-primary: #0D0D0D; --text-body: #4B5563; --text-muted: #9CA3AF;
      --bg: #FFFFFF; --bg-subtle: #F9FAFB; --bg-dark: #0D0D0D; --border: #E5E7EB;
    }
    html { scroll-behavior: smooth; }
    body { font-family: 'Inter', sans-serif; background: var(--bg); color: var(--text-primary); -webkit-font-smoothing: antialiased; overflow-x: hidden; }
    nav { position: fixed; top: 0; left: 0; right: 0; z-index: 100; background: rgba(255,255,255,0.96); backdrop-filter: blur(10px); border-bottom: 1px solid var(--border); display: flex; align-items: center; justify-content: space-between; padding: 0 2.5rem; height: 58px; }
    .nav-logo { font-size: 1.15rem; font-weight: 800; color: var(--text-primary); }
    .nav-logo span { color: var(--accent); }
    .nav-center { display: flex; gap: 6px; align-items: center; }
    .nav-dot { width: 8px; height: 8px; border-radius: 50%; background: var(--border); border: none; cursor: pointer; transition: background 0.2s, transform 0.2s; }
    .nav-dot.active { background: var(--accent); transform: scale(1.3); }
    .nav-label { font-size: 0.76rem; font-weight: 600; color: var(--text-muted); letter-spacing: 0.04em; white-space: nowrap; }
    .progress-bar { position: fixed; bottom: 0; left: 0; height: 3px; background: var(--accent); transition: width 0.3s ease; z-index: 200; }
    .slide-counter { position: fixed; bottom: 14px; right: 20px; font-size: 0.72rem; font-weight: 600; color: var(--text-muted); z-index: 200; }
    .slide { min-height: 100vh; display: flex; flex-direction: column; justify-content: center; padding: 90px 5% 60px; max-width: 1100px; margin: 0 auto; opacity: 0; transform: translateY(24px); transition: opacity 0.55s ease, transform 0.55s ease; }
    .slide.visible { opacity: 1; transform: translateY(0); }
    .slide-center { align-items: center; text-align: center; }
    .slide-dark { background: var(--bg-dark); max-width: none; padding-left: 10%; padding-right: 10%; }
    .slide-dark .inner { max-width: 1100px; margin: 0 auto; display: flex; flex-direction: column; align-items: center; text-align: center; }
    .badge { display: inline-flex; align-items: center; gap: 8px; background: var(--accent-light); color: var(--accent-dark); padding: 0.55rem 1.3rem; border-radius: 99px; font-size: 1rem; font-weight: 700; margin-bottom: 1.4rem; letter-spacing: -0.01em; }
    .badge-dark { background: rgba(63,81,55,0.3); color: #a8c0a0; }
    h1 { font-size: clamp(2.4rem, 5vw, 3.8rem); font-weight: 900; line-height: 1.08; letter-spacing: -0.03em; color: var(--text-primary); margin-bottom: 1.2rem; }
    h1 em, h2 em { color: var(--accent); font-style: normal; }
    h2 { font-size: clamp(2.2rem, 4.5vw, 3.4rem); font-weight: 900; line-height: 1.08; letter-spacing: -0.03em; color: var(--text-primary); margin-bottom: 0.9rem; }
    h2.light { color: #fff; } h2.light em { color: #7faa74; }
    h3 { font-size: 1.05rem; font-weight: 700; color: var(--text-primary); margin-bottom: 0.4rem; }
    p.body { font-size: 1.02rem; line-height: 1.72; color: var(--text-body); max-width: 640px; }
    p.hero-sub { font-size: clamp(1rem, 1.8vw, 1.18rem); color: var(--text-body); max-width: 560px; text-align: center; line-height: 1.65; }
    .divider { width: 44px; height: 3px; background: var(--accent); border-radius: 2px; margin: 1.1rem 0; }
    .divider-center { margin: 1.1rem auto; }
    .cards { display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 1rem; margin-top: 2rem; }
    .card { background: var(--bg); border: 1px solid var(--border); border-radius: 12px; padding: 1.4rem; transition: border-color 0.2s, transform 0.2s; }
    .card:hover { border-color: var(--accent); transform: translateY(-3px); }
    .card-icon { width: 40px; height: 40px; background: var(--accent-light); border-radius: 10px; display: flex; align-items: center; justify-content: center; font-size: 1.2rem; margin-bottom: 0.8rem; }
    .highlight { background: var(--accent-light); border: 1px solid rgba(63,81,55,0.28); border-radius: 12px; padding: 1.5rem; margin-top: 1.5rem; }
    .highlight h3 { color: var(--accent-dark); margin-bottom: 0.4rem; }
    .highlight p { color: var(--text-body); font-size: 0.96rem; max-width: none; line-height: 1.65; }
    .alert { background: #FEF2F2; border: 1px solid #FCA5A5; border-radius: 12px; padding: 1.5rem; margin-top: 1rem; }
    .alert h3 { color: #991B1B; margin-bottom: 0.35rem; }
    .alert p { color: #7F1D1D; font-size: 0.93rem; max-width: none; line-height: 1.6; }
    .stat-row { display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 1rem; margin-top: 1.75rem; }
    .stat-box { background: var(--bg-subtle); border: 1px solid var(--border); border-radius: 12px; padding: 1.2rem 1.4rem; }
    .stat-num { font-size: 2rem; font-weight: 900; color: var(--accent); letter-spacing: -0.04em; line-height: 1; }
    .stat-label { font-size: 0.82rem; color: var(--text-body); margin-top: 0.35rem; line-height: 1.45; }
    .steps { display: flex; flex-direction: column; gap: 0.85rem; margin-top: 1.6rem; }
    .step { display: flex; gap: 1.2rem; align-items: flex-start; background: var(--bg-subtle); border: 1px solid var(--border); border-radius: 12px; padding: 1rem 1.3rem; }
    .step-num { flex-shrink: 0; width: 32px; height: 32px; border-radius: 50%; background: var(--accent); color: #fff; font-weight: 900; font-size: 0.85rem; display: flex; align-items: center; justify-content: center; }
    .tag-row { display: flex; gap: 0.6rem; flex-wrap: wrap; }
    .tag { background: var(--bg-subtle); border: 1px solid var(--border); padding: 5px 14px; border-radius: 99px; font-size: 0.8rem; color: var(--text-body); }
    .tag.green { background: var(--accent-light); border-color: rgba(63,81,55,0.3); color: var(--accent-dark); }
    .cta-btn { display: inline-block; background: var(--accent); color: #fff; font-size: 1rem; font-weight: 700; padding: 0.9rem 2rem; border-radius: 8px; text-decoration: none; transition: opacity 0.2s, transform 0.2s; }
    .cta-btn:hover { opacity: 0.88; transform: translateY(-2px); }
    .cta-btn-outline { display: inline-block; background: transparent; color: #fff; font-size: 1rem; font-weight: 600; padding: 0.9rem 2rem; border-radius: 8px; text-decoration: none; border: 1.5px solid rgba(255,255,255,0.25); }
    .btn-row { display: flex; gap: 1rem; flex-wrap: wrap; }
    .two-col { display: grid; grid-template-columns: 1fr 1fr; gap: 1.75rem; align-items: start; }
    @media (max-width: 680px) { .two-col { grid-template-columns: 1fr; } nav .nav-label { display: none; } }
  </style>
</head>
<body>
<nav>
  <div class="nav-logo">XPO<span>Next</span></div>
  <div class="nav-center" id="navDots"></div>
  <div class="nav-label" id="navLabel"></div>
</nav>
<div class="progress-bar" id="progressBar"></div>
<div class="slide-counter" id="slideCounter"></div>

<!-- ======== SLIDE 1: INTRO ======== -->
<div class="slide slide-center" data-slide="1" data-label="Intro">
  <div class="badge">🎯 Für [FIRMENNAME]</div>
  <h1>[HEADLINE_SLIDE1]<br><em>[HEADLINE_SLIDE1_EM]</em></h1>
  <p class="hero-sub" style="margin-top:0.5rem;">[SUBLINE_SLIDE1]</p>
  <div class="tag-row" style="justify-content:center; margin-top:1.75rem;">
    <span class="tag">[TAG1]</span>
    <span class="tag">[TAG2]</span>
    <span class="tag">[TAG3]</span>
  </div>
  <div class="tag-row" style="justify-content:center; margin-top:0.75rem;">
    <span class="tag green">🌐 Neue Website</span>
    <span class="tag green">📈 SEO & GEO</span>
    <span class="tag green">🎯 Google Ads</span>
  </div>
</div>

<!-- ======== SLIDE 2: STATUS QUO ======== -->
<div class="slide" data-slide="2" data-label="Status Quo">
  <div class="badge">🔍 Was wir gesehen haben</div>
  <h2>[HEADLINE_SLIDE2]<br><em>[HEADLINE_SLIDE2_EM]</em></h2>
  <div class="divider"></div>
  <p class="body">[EINLEITUNG_SLIDE2]</p>

  <div class="stat-row">
    <div class="stat-box">
      <div class="stat-num">90%</div>
      <div class="stat-label">aller Klicks gehen an Ergebnisse auf Seite 1. Seite 2 existiert für Kunden kaum.</div>
    </div>
    <div class="stat-box">
      <div class="stat-num">60%</div>
      <div class="stat-label">der Nutzer surfen heute vom Smartphone. Nicht mobiloptimierte Seiten verlieren sie sofort.</div>
    </div>
    <div class="stat-box">
      <div class="stat-num">[RANKING_POSITION]</div>
      <div class="stat-label">Ihr aktuelles Google-Ranking für „[SUCHBEGRIFF]" – so finden Kunden Sie heute.</div>
    </div>
  </div>

  <div class="cards" style="margin-top:1.5rem;">
    <div class="card"><div class="card-icon">[ICON1]</div><h3>[MANGEL1_TITEL]</h3><p style="font-size:0.91rem;max-width:none;color:var(--text-body);">[MANGEL1_TEXT]</p></div>
    <div class="card"><div class="card-icon">[ICON2]</div><h3>[MANGEL2_TITEL]</h3><p style="font-size:0.91rem;max-width:none;color:var(--text-body);">[MANGEL2_TEXT]</p></div>
    <div class="card"><div class="card-icon">[ICON3]</div><h3>[MANGEL3_TITEL]</h3><p style="font-size:0.91rem;max-width:none;color:var(--text-body);">[MANGEL3_TEXT]</p></div>
  </div>

  <div class="highlight" style="margin-top:1.5rem;">
    <h3>Das ändern wir – und zwar von Grund auf.</h3>
    <p>XPONext analysiert, plant und setzt um. Von der ersten Zeile Code bis zum ersten Anruf über Google Ads – komplett aus einer Hand.</p>
  </div>
</div>

<!-- ======== SLIDE 3: WAS WIR TUN ======== -->
<div class="slide" data-slide="3" data-label="Unser Angebot">
  <div class="badge">💡 Was XPONext macht</div>
  <h2>Alles aus<br><em>einer Hand.</em></h2>
  <div class="divider"></div>
  <p class="body">Wir bauen nicht einfach eine Website – wir sorgen dafür, dass Sie gefunden werden und Anfragen bekommen.</p>

  <div class="cards">
    <div class="card">
      <div class="card-icon">🌐</div>
      <h3>Neue Website</h3>
      <p style="font-size:0.91rem;max-width:none;color:var(--text-body);">Mobil, schnell, modern. Ihre Inhalte – professionell präsentiert. Kein Aufwand für Sie.</p>
    </div>
    <div class="card">
      <div class="card-icon">📈</div>
      <h3>SEO & GEO</h3>
      <p style="font-size:0.91rem;max-width:none;color:var(--text-body);">Gefunden werden bei Google – und bei KI-Suchen wie ChatGPT. Neue Entwicklungen bauen wir direkt ein.</p>
    </div>
    <div class="card">
      <div class="card-icon">🎯</div>
      <h3>Google Ads</h3>
      <p style="font-size:0.91rem;max-width:none;color:var(--text-body);">Wir übernehmen Kampagnenerstellung und -pflege. Sie zahlen nur, was wirkt.</p>
    </div>
    <div class="card">
      <div class="card-icon">🔄</div>
      <h3>Laufende Pflege</h3>
      <p style="font-size:0.91rem;max-width:none;color:var(--text-body);">Neue Projekte, Texte, Bilder – wir aktualisieren, wenn Sie es brauchen. Immer erreichbar.</p>
    </div>
  </div>
</div>

<!-- ======== SLIDE 4: WIE WIR ARBEITEN ======== -->
<div class="slide" data-slide="4" data-label="Zusammenarbeit">
  <div class="badge">🤝 Wie wir zusammenarbeiten</div>
  <h2>Kein Auftrag.<br><em>Eine Partnerschaft.</em></h2>
  <div class="divider"></div>
  <p class="body">Wir verkaufen Ihnen nichts und verschwinden dann. Wir arbeiten über Monate gemeinsam – und alles, was wir lernen, kommt direkt Ihnen zugute.</p>

  <div class="steps">
    <div class="step">
      <div class="step-num">1</div>
      <div><h3>Kurzes Erstgespräch – ca. 30 Minuten</h3><p style="font-size:0.91rem;max-width:none;color:var(--text-body);margin-top:0.2rem;">Wir hören zu, verstehen Ihr Geschäft und erklären, was wir konkret tun würden. Ohne Druck.</p></div>
    </div>
    <div class="step">
      <div class="step-num">2</div>
      <div><h3>Wir bauen – Sie warten nicht lang</h3><p style="font-size:0.91rem;max-width:none;color:var(--text-body);margin-top:0.2rem;">Neue Website, SEO-Setup, Ads-Kampagne. Von der ersten Absprache bis Go-live in der Regel 1–3 Wochen.</p></div>
    </div>
    <div class="step">
      <div class="step-num">3</div>
      <div><h3>Immer erreichbar, immer aktuell</h3><p style="font-size:0.91rem;max-width:none;color:var(--text-body);margin-top:0.2rem;">Neue Projekte einstellen, Texte anpassen, neue Google-Entwicklungen einbauen – das erledigen wir laufend.</p></div>
    </div>
    <div class="step">
      <div class="step-num">4</div>
      <div><h3>Unser Wissen ist Ihr Wissen</h3><p style="font-size:0.91rem;max-width:none;color:var(--text-body);margin-top:0.2rem;">GEO, KI-Suchen, neue SEO-Signale – was wir lernen, bauen wir direkt für Sie ein. Automatisch.</p></div>
    </div>
  </div>
</div>

<!-- ======== SLIDE 5: CTA ======== -->
<div class="slide slide-dark slide-center" data-slide="5" data-label="Nächster Schritt">
  <div class="inner">
    <div class="badge badge-dark">XPONext × [FIRMENNAME]</div>
    <h2 class="light">Bereit für mehr<br>Anfragen aus <em>dem Internet?</em></h2>
    <div class="divider divider-center"></div>
    <p style="color:var(--text-muted); max-width:480px; line-height:1.7; font-size:1rem;">Kein Risiko, kein langer Vertrag. Einfach ein kurzes Gespräch – und wir legen los.</p>
    <div class="btn-row" style="justify-content:center; margin-top:1.75rem;">
      <a class="cta-btn" href="https://www.xponext.de" target="_blank">Gespräch vereinbaren →</a>
      <a class="cta-btn-outline" href="https://www.xponext.de" target="_blank">www.xponext.de</a>
    </div>
    <p style="margin-top:2.5rem; font-size:0.76rem; color:#444;">© 2026 XPONext GbR · Erstellt für [FIRMENNAME]</p>
  </div>
</div>

<script>
  const slides = document.querySelectorAll('.slide');
  const total = slides.length;
  const navDots = document.getElementById('navDots');
  const navLabel = document.getElementById('navLabel');
  const progressBar = document.getElementById('progressBar');
  const slideCounter = document.getElementById('slideCounter');
  slides.forEach((_, i) => {
    const dot = document.createElement('button');
    dot.className = 'nav-dot';
    dot.setAttribute('aria-label', `Folie ${i + 1}`);
    dot.addEventListener('click', () => slides[i].scrollIntoView({ behavior: 'smooth' }));
    navDots.appendChild(dot);
  });
  const dots = document.querySelectorAll('.nav-dot');
  function updateUI() {
    let current = 0, maxV = 0;
    slides.forEach((s, i) => {
      const r = s.getBoundingClientRect();
      const v = Math.max(0, Math.min(r.bottom, window.innerHeight) - Math.max(r.top, 0)) / window.innerHeight;
      if (v > maxV) { maxV = v; current = i; }
      if (r.top < window.innerHeight * 0.78) s.classList.add('visible');
    });
    dots.forEach((d, i) => d.classList.toggle('active', i === current));
    navLabel.textContent = slides[current]?.dataset.label || '';
    const pct = window.scrollY / (document.body.scrollHeight - window.innerHeight);
    progressBar.style.width = (pct * 100) + '%';
    slideCounter.textContent = `${current + 1} / ${total}`;
  }
  document.addEventListener('keydown', e => {
    const cur = [...slides].findIndex(s => { const r = s.getBoundingClientRect(); return r.top <= window.innerHeight / 2 && r.bottom >= window.innerHeight / 2; });
    if ((e.key === 'ArrowDown' || e.key === 'ArrowRight') && cur < total - 1) slides[cur + 1].scrollIntoView({ behavior: 'smooth' });
    if ((e.key === 'ArrowUp' || e.key === 'ArrowLeft') && cur > 0) slides[cur - 1].scrollIntoView({ behavior: 'smooth' });
  });
  window.addEventListener('scroll', updateUI, { passive: true });
  updateUI();
</script>
</body>
</html>
```

---

## Platzhalter-Referenz

| Platzhalter | Beispiel |
|---|---|
| `[FIRMENNAME]` | `Ralf Breuer Architekt` |
| `[HEADLINE_SLIDE1]` | `Ihr Lebenswerk.` |
| `[HEADLINE_SLIDE1_EM]` | `Würdig präsentiert.` |
| `[SUBLINE_SLIDE1]` | `Ein Konzept für Ihre neue Website – modern, gefunden, wirkungsvoll.` |
| `[TAG1–3]` | Branchenspezifische Begriffe (z.B. `Wohnungsbau`, `Bauen im Bestand`) |
| `[HEADLINE_SLIDE2]` | `Starke Arbeit –` |
| `[HEADLINE_SLIDE2_EM]` | `veraltete Bühne.` |
| `[EINLEITUNG_SLIDE2]` | 1–2 Sätze über die aktuelle Situation, spezifisch für den Kunden |
| `[RANKING_POSITION]` | `Seite 2` oder `#14` oder `Nicht gefunden` |
| `[SUCHBEGRIFF]` | `Architekt Düsseldorf` |
| `[ICON1–3]` | Passende Emojis (📱 🕰️ 🔗 📊 🖼️ etc.) |
| `[MANGEL1–3_TITEL]` | Konkreter Mangelname aus der Analyse |
| `[MANGEL1–3_TEXT]` | 1–2 Sätze Erklärung, warum das Kunden kostet |

---

## Wenn Preise gewünscht sind

Füge diesen Block am Ende von Slide 4 (vor `</div>`) ein:

```html
<div class="highlight" style="margin-top:1.5rem;">
  <h3>💰 Investition</h3>
  <p>Monatliche Pauschale – alles inklusive: Website, SEO, GEO, Google Ads, laufende Pflege. Einmalige Einrichtungsgebühr für den Start. Genaues Angebot nach dem Erstgespräch – individuell auf Ihr Geschäft zugeschnitten.</p>
</div>
```

---

## Ausgabe-Dateiname

`konzepte/[Firmenname_bereinigt]_XPONext_Konzept.html`

Beispiel: `konzepte/Breuer_Architekt_XPONext_Konzept.html`

Bereinigung: Leerzeichen → `_`, Umlaute → `ae/oe/ue/ss`, Sonderzeichen entfernen.
