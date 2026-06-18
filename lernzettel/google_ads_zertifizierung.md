# Google Ads Zertifizierung — Lernzettel

> Erstellt von Tim, zusammengeführt und strukturiert mit Claude.  
> Für Simon und Tim zur gemeinsamen Prüfungsvorbereitung.

---

## Inhaltsverzeichnis

1. [AI-powered Search Ads](#1-ai-powered-search-ads)
   - [Die 3 KI-Tools im Suchnetzwerk](#die-3-ki-tools-im-suchnetzwerk)
   - [Search-Kampagne erstellen](#search-kampagne-erstellen)
   - [Broad Match auf bestehende Kampagnen ausweiten](#broad-match-auf-bestehende-kampagnen-ausweiten)
2. [Google Ads Auction & Ad Rank](#2-google-ads-auction--ad-rank)
3. [Keyword-Strategie](#3-keyword-strategie)
4. [Reach your users with Responsive Search Ads](#4-reach-your-users-with-responsive-search-ads)
   - [KI-powered Creative](#ki-powered-creative)
   - [Ad Assets](#ad-assets)
   - [Ad Customizers](#ad-customizers)
5. [AI-powered Search Ads Bid Strategies](#5-ai-powered-search-ads-bid-strategies)
   - [Bid Strategies im Überblick](#bid-strategies-im-überblick)
   - [Performance mit Smart Bidding aktivieren](#performance-mit-smart-bidding-aktivieren)
   - [Search Ad Bid Strategies erstellen](#search-ad-bid-strategies-erstellen)
   - [Conversion-basierte Strategien optimieren](#conversion-basierte-strategien-optimieren)
   - [Conversion-Wert mit Value-based Bidding steigern](#conversion-wert-mit-value-based-bidding-steigern)
6. [Budget mit dem Performance Planner optimieren](#6-budget-mit-dem-performance-planner-optimieren)

---

## 1. AI-powered Search Ads

Google KI ist seit Jahren in der Suche integriert und wird laufend besser — in den letzten 5 Jahren um 50% genauer beim Verstehen menschlicher Sprache.

### Die 3 KI-Tools im Suchnetzwerk

#### Broad Match
Statt fixer Keywords versteht Google die **Absicht** hinter einer Suchanfrage. Man muss keine langen Keyword-Listen pflegen — die KI erkennt relevante Varianten automatisch.

#### Smart Bidding
Google bietet automatisch auf Suchanfragen, bei denen ein Abschluss wahrscheinlich ist. Grundlage sind Nutzersignale wie Uhrzeit, Gerät, Standort und Verhalten:

| Signal | Beispiel | Gebot |
|---|---|---|
| Hohes Potenzial | Montag 9 Uhr, PC, München | Hoch |
| Niedriges Potenzial | Sonntag 2 Uhr nachts, Handy | Niedrig |

Ziel: Budget dort einsetzen, wo Conversions am wahrscheinlichsten sind (optimiert auf ROAS oder CPA).

#### Responsive Search Ads (RSAs)
Man gibt bis zu **15 Headlines** und **4 Descriptions** vor — Google testet automatisch verschiedene Kombinationen und zeigt die beste Variante für den jeweiligen Nutzer.

> **Merksatz:** Broad Match + Smart Bidding + RSAs zusammen → durchschnittlich **20% mehr Conversions** bei gleichem CPA.

### Search-Kampagne erstellen

#### Kontostruktur — 4 Ebenen

```
Manager Account  →  mehrere Konten verwalten (z.B. für Agentur)
  └── Account        Sammlung aller Kampagnen eines Kunden
        └── Kampagne    Eigenes Budget + eigene Einstellungen
              └── Ad Group  Zusammengehörige Anzeigen + Keywords (1 Thema)
```

**Merksatz:** Je enger eine Ad Group thematisch ist, desto relevanter sind Keywords und Anzeigen — und desto besser die Performance.

#### Kampagnenziel festlegen
Search-Kampagnen eignen sich für:
- **Sales** — direkte Käufe / Anfragen
- **Leads** — Formulare, Anrufe, Kontaktaufnahmen
- **Web Traffic** — Besucher auf die Website lenken

#### Die 3 Kernkomponenten einer Kampagne

| Komponente | Was es ist |
|---|---|
| **Targeting** | Keywords + Zielgruppen — wer die Anzeige sieht |
| **Ad Formats** | RSAs — Headlines, Descriptions, Assets |
| **Bid Strategy** | Smart Bidding: Fokus auf CPA (Volumen) oder ROAS (Wert) |

#### Budget
Tagesbudget selbst festlegen. Google kann täglich bis zu 2× davon abweichen, gleicht es aber über den Monat aus — nie mehr als Tagesbudget × 30,4.

#### Netzwerke
- **Search Network** — Anzeigen auf Google Suche + Search Partners (z.B. CNN)
- **Display Network** — Banner auf Websites im Google Netzwerk

> Tipp: Display Network für fokussierte Search-Kampagnen **deaktivieren**.

#### Standort & Sprache
Kampagne auf Region und Sprache der Zielkunden einschränken — besonders wichtig für lokale Betriebe.

#### Ad Groups & Keywords
- Pro Ad Group: **ein Thema** (z.B. "Dachdecker" vs. "Fassade")
- Keywords: ein Keyword pro Zeile, Broad Match ohne Sonderzeichen
- Google bietet Keyword-Vorschläge per URL-Scan oder Produktbeschreibung

#### Keywordlose Alternativen
- **DSAs** — Google scannt die Website und erstellt automatisch passende Anzeigen
- **Performance Max** — KI bespielt alle Google-Kanäle gleichzeitig

### Broad Match auf bestehende Kampagnen ausweiten

Broad Match deckt denselben Traffic ab wie Exact und Phrase Match — plus zusätzliche relevante Anfragen, die man selbst nicht vorhersehen würde.

**Warum wechseln? — Zahlen aus Google-Studien:**

| Upgrade | Ergebnis |
|---|---|
| Exact Match → Broad Match (mit Ziel-CPA) | **+35% mehr Conversions** |
| Phrase Match → Broad Match (mit Ziel-CPA) | **+25% mehr Conversions** |
| Phrase Match → Broad Match (mit Ziel-ROAS) | **+12% mehr Conversion-Wert** |

> Broad Match funktioniert nur gut **zusammen mit Smart Bidding** — Smart Bidding braucht dafür wiederum ausreichend Conversion-Daten im Konto.

**So testet man Broad Match (One-Click-Experiment):**
1. Recommendations-Seite → Empfehlung "Broad Match Keywords hinzufügen" suchen
2. Drei-Punkte-Menü der Kampagne → "Experiment anwenden"
3. Speichern — Google erstellt automatisch Kontroll- vs. Testgruppe
4. Experiment **mindestens 4 Wochen** laufen lassen, erste Woche (Anlaufphase) bei Auswertung ignorieren
5. Während des Tests: **keine Änderungen** an der Kampagne vornehmen
6. Ergebnisse auswerten → bei Erfolg auf weitere Kampagnen ausrollen

**Nach dem Test:** Search Terms Report nutzen, um zu sehen welche neuen Suchanfragen Broad Match ausgelöst hat.

---

## 2. Google Ads Auction & Ad Rank

Bei jeder Suchanfrage führt Google eine **Auktion** durch — nicht der höchste Preis gewinnt, sondern der höchste **Ad Rank**. Das bedeutet: gute Anzeigenqualität schlägt oft ein hohes Gebot.

### Die 6 Faktoren des Ad Rank

| Faktor | Erklärung |
|---|---|
| **Gebot** | Maximalbetrag pro Klick (oft zahlt man weniger) |
| **Ad Rank Threshold** | Mindest-Qualitätsschwelle — wird diese nicht erreicht, erscheint die Anzeige gar nicht |
| **Suchkontext** | Suchbegriff, Standort, Gerät, Uhrzeit, andere Anzeigen auf der Seite |
| **Asset-Einfluss** | Zusatzinfos wie Sitelinks und Bilder verbessern den Ad Rank |
| **Anzeigenqualität** | Zusammengefasst im **Quality Score** (im Konto einsehbar) |
| **Wettbewerb** | Je kleiner der Ad-Rank-Abstand zweier Anzeigen, desto offener der Ausgang |

### Quality Score — die 3 Teilfaktoren

| Faktor | Was bewertet wird |
|---|---|
| **Expected CTR** | Wie wahrscheinlich ist ein Klick auf die Anzeige? |
| **Landing Page Experience** | Ist die Zielseite relevant, transparent und gut navigierbar? |
| **Ad Relevance** | Passt die Anzeige zum Suchbegriff des Nutzers? |

### Das Wichtigste in einem Satz
> Höherer Quality Score = bessere Position **und** günstigerer CPC. Qualität wird also doppelt belohnt.

### Praktische Konsequenz
- Gute Anzeigentexte + passende Landing Page senken die Kosten pro Klick
- Quality Score regelmäßig im Konto prüfen und schwache Keywords oder Anzeigen verbessern
- Assets (Sitelinks, Bilder, Standort) immer hinzufügen — sie verbessern den Ad Rank ohne Mehrkosten

---

## 3. Keyword-Strategie

### Die 3 Match Types im Vergleich

| Match Type | Syntax | Reichweite | Wann nutzen? |
|---|---|---|---|
| **Exact Match** | `[tennis shoes]` | Schmal | Wenn nur sehr spezifische Suchanfragen relevant sind |
| **Phrase Match** | `"tennis shoes"` | Mittel | Kern-Konzept muss enthalten sein, aber mehr Volumen als Exact |
| **Broad Match** | `tennis shoes` | Breit | Standard — KI findet relevante Suchanfragen automatisch |

> **Wichtig:** Kein Keyword in allen drei Match Types gleichzeitig in eine Ad Group — Broad Match deckt die anderen ohnehin ab.

### Broad Match testen — 2 Wege

**Standard (schnell):** Über die Recommendations-Seite ein One-Click-Experiment starten. Google erstellt automatisch eine Kontrollgruppe (bisherige Keywords) vs. Testgruppe (Broad Match). Experiment mindestens **3–4 Wochen** laufen lassen, erste 7 Tage (Anlaufphase) bei der Auswertung ignorieren. Ziel: **30 Conversions** für statistische Aussagekraft.

**Customized (mehr Kontrolle):** Kampagne manuell per Custom Experiments auf Broad Match umstellen. Budget dabei **nicht deckeln** — sonst kann Broad Match sein Potenzial nicht zeigen. Performance-Ziel (CPA/ROAS) während des Tests nicht anpassen.

### Ad Groups nach Thema organisieren
- Jede Ad Group = ein Thema → Google KI versteht die Keyword-Intention besser
- Keywords einer Ad Group müssen zur Landing Page der Kampagne passen
- Keywords thematisch bündeln, nicht wild mischen

### Keyword-Optimierung — 4 Werkzeuge

| Tool | Wozu |
|---|---|
| **Keyword Planner** | Suchvolumen, neue Keywords, Wettbewerb einsehen |
| **Search Terms Report** | Sehen, welche echten Suchanfragen die Anzeigen ausgelöst haben |
| **Optimization Score** | Empfehlungen: neue Keywords hinzufügen, Duplikate entfernen, Konflikte lösen |
| **Negative Keywords** | Irrelevante Suchanfragen ausschließen (z.B. "cleats" wenn man keine Stollen verkauft) |

> **Vorsicht bei Negative Keywords:** Zu viele schränken die Reichweite ein und blockieren ggf. relevante Suchanfragen, die man nicht bedacht hat.

### Broad Match skalieren
Wenn das Experiment erfolgreich war: Empfehlungen aus dem Konto anwenden oder automatisch angewendete Empfehlungen aktivieren, um Broad Match auf weitere Kampagnen auszurollen.

---

## 4. Reach your users with Responsive Search Ads

### KI-powered Creative

**Warum RSAs?** 15% aller täglichen Suchanfragen bei Google sind völlig neu — sie wurden so noch nie gestellt. RSAs ermöglichen es, auch diese unbekannten Anfragen mit der richtigen Anzeige zu treffen.

Google testet automatisch verschiedene Kombinationen aus Headlines und Descriptions und lernt, welche für welchen Nutzer am besten funktioniert. Je mehr Assets man bereitstellt, desto mehr Kombinationen kann Google testen.

### 3 Wege zur RSA-Optimierung

| Tool | Wofür |
|---|---|
| **Optimization Score** (0–100%) | Empfehlungen für neue RSAs, fehlende Assets, Verbesserungen. 100% = volles Potenzial ausgeschöpft |
| **Ad Builder** (Search Ads 360) | Assets in Tausenden von Ad Groups auf einmal hinzufügen oder aktualisieren |
| **Google Ads Editor** | RSAs offline erstellen, Headlines anpinnen, Ad Strength prüfen, Empfehlungen umsetzen |

### Ad Strength vs. Asset Performance

| Kennzahl | Wann relevant | Was gemessen wird |
|---|---|---|
| **Ad Strength** | Bei der Erstellung | Relevanz, Menge und Vielfalt der Assets — noch bevor die Anzeige ausgespielt wird |
| **Asset Performance** | Nach der Ausspielung | Wie gut ein einzelnes Asset im Vergleich zu anderen Assets in der Anzeige performt |

> Ziel: mindestens **1 RSA pro Ad Group** mit Ad Strength "Gut" oder "Ausgezeichnet". Maximum: 3 RSAs pro Ad Group.

### Best Practices für RSAs

- **Mind. 10 Headlines** und **mind. 3 Descriptions** bereitstellen
- Mind. 3 relevante Keywords in den Headlines einbauen
- Headlines müssen einzeln und in Kombination Sinn ergeben (beliebige Reihenfolge möglich)
- Headlines nicht wiederholen oder ähnliche Formulierungen doppeln
- Call-to-Action-Wörter verwenden ("Jetzt anfragen", "Kostenlos testen")
- Descriptions für Zusatzinfos nutzen, die in Headlines keinen Platz haben
- **Nicht pinnen** wenn möglich — gepinnte Assets schränken die Kombinationsmöglichkeiten ein
- Wenn ein Text in jeder Anzeige erscheinen muss: an **Headline-Position 1 oder 2** oder **Description-Position 1** pinnen

> **Merksatz:** RSA + Broad Match + Smart Bidding = die drei KI-Hebel greifen ineinander und optimieren gemeinsam Reichweite, Gebot und Anzeigeninhalt in Echtzeit.

### Ad Assets

Assets sind Zusatzinformationen, die eine Anzeige erweitern. Sie kosten nichts extra, verbessern aber den Ad Rank und steigern CTR und Conversions.

**Warum Assets wichtig sind:**
- Anzeige sticht heraus → höhere CTR
- Mehr Klicks kommen oft zu niedrigerem CPC
- Mehr Conversions durch gezieltere Nutzerführung

#### Asset-Typen im Überblick

| Asset | Was es ist | Best Practice |
|---|---|---|
| **Business Name & Logo** | Name + Logo erscheinen in der Anzeige | Immer aktivieren — bringt **+8% mehr Conversions** |
| **Bilder** | Fotos ergänzen Textanzeigen visuell | Mind. 4 einzigartige Bilder pro Ad Group; beide Formate: **1:1** und **1,91:1**; wichtige Inhalte in der **mittleren 80%** der Bildfläche halten; zuerst Ad Groups mit hohem Impressionsvolumen priorisieren |
| **Dynamic Image Assets** | Google wählt automatisch passende Bilder von der Website | Auf Konto- oder Kampagnenebene aktivieren für mehr Reichweite |
| **Sitelinks** | Deep-Links zu einzelnen Unterseiten | 8–10 Sitelinks sind ideal; mind. 2 Unterseiten nötig damit Sitelinks ausgespielt werden; auf Konto-, Kampagnen- oder Ad-Group-Ebene einstellbar |
| **Structured Snippets** | Nicht klickbarer Zusatztext im Format "Header: Wert1, Wert2" — z.B. "Leistungen: SEO, Google Ads, Webdesign" | Nützliche und attraktive Header wählen; Ad-Group-Ebene hat Vorrang vor Kampagnen- und Kontoebene |
| **Callouts** | Kurze Stichpunkte zu USPs (nicht klickbar) | Mind. **6 Callouts** pro Kampagne; so kurz und spezifisch wie möglich |
| **Automatically Created Assets** | Google KI generiert Headlines und Descriptions automatisch aus der Landing Page und bestehenden Anzeigen | Auf Kampagnenebene aktivieren — reduziert manuellen Pflegeaufwand, hält Anzeigen aktuell |

> **Merksatz:** Je mehr hochwertige Assets, desto mehr Kombinationsmöglichkeiten hat Google — und desto besser passt die Anzeige zur jeweiligen Suchanfrage.

### Ad Customizers

Ad Customizers fügen Echtzeit-Informationen in Anzeigentexte ein — so können Anzeigen personalisiert wirken, ohne jede Variante manuell zu erstellen.

#### Die 3 RSA-Customizer-Typen

| Customizer | Was er macht | Beispiel |
|---|---|---|
| **Location Insertion** | Passt den Anzeigentext an den Standort des Nutzers an (Stadt, Bundesland, Land) | "Dachdecker in **München**" |
| **Countdown** | Zeigt einen Live-Countdown bis zu einem Sale oder Event | "Angebot endet in **2 Tagen 4 Std.**" |
| **Keyword Insertion** | Ersetzt einen Platzhalter automatisch mit dem Keyword, das die Anzeige ausgelöst hat | Nutzer sucht "Klempner" → Anzeige zeigt "Ihr **Klempner** in der Region" |

#### Implementierung in 4 Schritten

1. **Business Data öffnen** — Datenbasis im Google Ads Konto aufrufen
2. **Ad Customizer erstellen** — Attribute definieren (Kategorisierung des dynamischen Textes)
3. **Attributwerte eingeben** — den tatsächlichen Text zuweisen (auf Konto-, Kampagnen- oder Ad-Group-Ebene)
   > ⚠️ Ohne eingetragene Werte kann die Anzeige nicht überprüft und nicht ausgespielt werden
4. **Anzeigentext anpassen** — den Customizer-Code in die RSA-Headline oder Description einfügen

---

## 5. AI-powered Search Ads Bid Strategies

### Bid Strategies im Überblick

#### Manuell vs. Automatisiert

| Typ | Wie es funktioniert |
|---|---|
| **Manuelles Bidding** | Eigener Max-CPC pro Ad Group (Standardgebot); zusätzlich individuelle Gebote pro Keyword oder Placement möglich |
| **Automatisiertes Bidding** | Google KI setzt Gebote anhand der Wahrscheinlichkeit, dass eine Anzeige zum Klick und zur Conversion führt |
| **Smart Bidding** | Teilbereich des automatisierten Biddings — fokussiert auf zwei Ziele: **Conversions** und **Conversion Value** |

#### Die richtige Strategie je nach Ziel

| Ziel | Strategie | Funktionsweise |
|---|---|---|
| **Mehr Website-Besuche** | Maximize Clicks | Automatische Optimierung auf möglichst viele Klicks |
| **Mehr Sichtbarkeit** | Target Impression Share | Anzeige soll oben auf der Seite erscheinen |
| **Mehr Conversions** | Maximize Conversions (Smart Bidding) | Mit Ziel-CPA: so viele Conversions wie möglich zum gesetzten CPA. Ohne Ziel-CPA: Budget so einsetzen, dass möglichst viele Conversions entstehen |
| **Mehr Conversion-Wert** | Maximize Conversion Value | Maximiert den Wert der Conversions, hält sich dabei an das gesetzte Budget |

### Best Practices

- **Targets & Budget:** Beim Opt-in empfohlene Ziele oder historische Performance als Ausgangswert nutzen. Budgets bei Target ROAS/CPA **nicht deckeln**, um das volle Potenzial auszuschöpfen
- **Conversion-Volumen:** Performance über längere Zeiträume bewerten — mind. **1 Monat** oder **50 Conversions**
- **Conversion Delay:** Bei Offline-Conversion-Uploads = Zeit bis zur Conversion + Zeit bis zum Hochladen der Daten
- **Lernphase:** Erste **4–7 Tage** bei der Auswertung ausschließen — das System kalibriert sich noch
- **Bid Strategy Report:** Zeigt strategiespezifische Kennzahlen — Status, Target-/Budget-Simulatoren, durchschnittlicher Ziel-CPA/ROAS, Conversion Delay, wichtigste Signale

### Performance mit Smart Bidding aktivieren

**Zwei Spielarten von Smart Bidding:**

| Typ | Funktionsweise | Leitfrage |
|---|---|---|
| **Value-based Bidding** | KI passt das Gebot an den **vorhergesagten Wert** der Conversion an — nicht jede Conversion ist gleich wertvoll fürs Geschäft | "Wie viel ist diese Person wert?" |
| **Conversion-based Bidding** | KI nutzt historische Daten + Echtzeit-Auktionssignale (Standort, Uhrzeit, Gerät), um die Nutzer zu finden, die am ehesten konvertieren | "Wird diese Person konvertieren?" |

**Die 4 Strategien im Quadranten:**

| | Fokus: Conversions | Fokus: Conversion-Wert |
|---|---|---|
| **Mit Ziel** | Target CPA — maximiert Conversions zum gesetzten Ziel-CPA | Target ROAS — maximiert Conversion-Wert zum gesetzten Ziel-ROAS |
| **Ohne Ziel / Budget-gesteuert** | Maximize Conversions — höchstmögliche Conversion-Zahl im Tagesbudget | Maximize Conversion Value — höchstmöglicher Gesamtwert im Tagesbudget |

> **Target ROAS — wichtig für Kunden mit klaren Margen:** "Für jeden investierten Euro brauche ich X Euro zurück, um profitabel zu sein." Risiko: Ziel zu hoch angesetzt → System bietet in vielen Auktionen nicht mehr mit, obwohl diese noch profitabel gewesen wären → Volumen bricht ein.

> **Maximize Conversion Value (ohne Ziel) — passend für:** Betriebe mit unterschiedlich wertvollen Conversion-Arten (z.B. ein Produkt für 20€, eines für 100€), die eher Marktanteil/Umsatzwachstum wollen als einen festen ROI pro Euro. Budget ist hier die eigentliche Stellschraube für die Performance.

**Conversion-Tracking richtig aufsetzen:**

1. **Primary vs. Secondary Actions:**
   - **Primary Actions** = Ziele, auf die die Kampagne optimiert. Erscheinen in der Spalte "Conversions" und werden direkt von Smart Bidding für Gebotsanpassungen genutzt
   - **Secondary Actions** = nur zur Beobachtung, erscheinen in "Alle Conversions", fließen aber **nicht** ins Bidding ein
   - ⚠️ Bei jeder Kontoprüfung die Conversion-Aktionen kontrollieren: Nur Aktionen, die echte "Business Truth" abbilden (z.B. Käufe, qualifizierte Leads), dürfen auf Primary stehen — sonst optimiert die KI auf das Falsche
2. **Account Default vs. Campaign Specific:** Performance-Strategie und Ziele sollten kontoweit konsistent sein (Account Default = die wichtigsten Ziele, z.B. Umsatz, gelten überall — maximiert das KI-Lernen). Campaign Specific (Override) nur sparsam einsetzen, wenn eine einzelne Kampagne ein wirklich anderes Ziel verfolgt
3. **Goal Classification:** Jeder Aktion eine korrekte Kategorie zuweisen (Kauf, Lead-Formular, Terminbuchung). Wichtig, damit Google KI weiß, welche Art Ereignis sie bewerten soll — bei Lead-Generierung gibt es zudem Schutzmechanismen gegen ungültigen Traffic je nach Kategorie
4. **Custom Goals:** Gruppieren mehrere Conversion-Aktionen für individuelle Bidding-/Reporting-Zwecke — eine Secondary Action wird dadurch biddingfähig. Trotzdem: wo möglich Standard-Kategorien bevorzugen, da die KI diese besser versteht als individuelle Gruppierungen → effizienteres Lernen

**Bevor man die Strategie wechselt oder neu bewertet:**
- **Genug Conversion-Daten sammeln:** Search-Kampagnen sollten mind. **15 Conversions in 30 Tagen** haben, bevor eine Target-ROAS-Strategie aktiviert wird — sonst fehlt der KI die Datenbasis
- **Zeit zum Optimieren geben:** Smart-Bidding-Kampagnen brauchen eine Anlaufphase, bevor man ihre Performance bewertet
- **Ziel-CPA nicht zu niedrig ansetzen:** Ein zu niedriger Ziel-CPA bei "Maximize Conversions (mit CPA-Ziel)" begrenzt das erreichbare Conversion-Volumen

> **Merksatz:** Performance Max bespielt alle Google-Kanäle aus einer einzigen Kampagne — braucht dafür aber robuste Inputs (klare Ziele, gute Assets, eigene Signale/Zielgruppendaten), um Marketing wirklich auf das Geschäftsergebnis auszurichten.

### Search Ad Bid Strategies erstellen

**Welche Strategie passt zu welchem Geschäftsziel — Übersicht:**

| Geschäftsziel | Bid Strategy | Wofür einsetzen |
|---|---|---|
| Mehr Transaktionen/Leads (Volumen) | **Maximize Conversions** | So viele Conversions wie möglich innerhalb eines festen Budgets |
| Mehr Sales/Profit/qualifizierte Leads (mit Effizienzziel) | **Target CPA** | So viele Conversions wie möglich zu einem festgelegten Ziel-CPA |
| Mehr Website-Besucher | **Maximize Conversion Value** | So viel Conversion-Wert wie möglich innerhalb eines festen Budgets |
| Awareness erhöhen/stabilisieren | **Target ROAS** | So viel Conversion-Wert wie möglich zu einem festgelegten Ziel-ROAS |
| Klicks/Traffic | **Maximize Clicks** | So viele Klicks wie möglich aus dem Budget holen |
| Awareness/Sichtbarkeit | **Target Impression Share** | Anzeige an einer bestimmten Position der Suchergebnisse zeigen |

> ⚠️ Aus den Kursfolien: "Awareness/Visibility" wird mit Target Impression Share verknüpft, "Increase or stabilize awareness" aber mit Target ROAS — beide Karten stammen aus dem offiziellen Material. In der Praxis: Target ROAS für wertorientierte Skalierung nutzen, Target Impression Share gezielt für reine Sichtbarkeits-/Markenziele.

#### Value-based Strategien im Detail

- **Maximize Conversions (mit Ziel-CPA):** Smart Bidding versucht, so viele Conversions wie möglich **zum gesetzten Ziel-CPA** zu erreichen. Ohne Ziel-CPA: Budget wird so eingesetzt, dass möglichst viele Conversions entstehen (Effizienzziel entfällt)
- **Maximize Conversion Value (mit Ziel-ROAS):** Bietet weiterhin für jede Conversion, gewichtet aber nach **Wert** (z.B. kleiner vs. großer Auftrag) und hält sich dabei an Budget bzw. das gesetzte Ziel-ROAS

**Best Practices für Value-based Bidding:**
- Ausreichend Conversion-Daten sammeln, bevor man bewertet
- Wissen, wie viel man mit Maximize Conversion Value tatsächlich ausgibt (Budget im Blick behalten)
- Der Strategie Zeit zur Optimierung geben (Lernphase)
- Den Bid Strategy Report zur Auswertung nutzen

#### Awareness mit Target Impression Share stärken

Automatisierte Strategie, die Gebote so setzt, dass die Anzeige an einer **bestimmten Position** der Google-Suchergebnisse erscheint — ideal für Markenaufbau über einen längeren Zeitraum.

**3 Positionsoptionen:** ganz oben auf der Seite (absolute top), oben auf der Seite (top), irgendwo auf der Seite (anywhere). Google setzt die Gebote automatisch passend zur gewählten Position.

**Best Practices:**
- **Keine zu restriktiven CPC-Limits:** Ein Max-CPC-Limit verhindert, dass Google Ads zu viel pro Klick zahlt — aber zu niedrig angesetzt bremst es die Strategie aus und das Impression-Share-Ziel wird verfehlt
- **Realistischen Startwert wählen:** Das Ziel sollte sich an der durchschnittlichen 30-Tage-Impression-Share der Kampagne orientieren
- Der Strategie Zeit zur Optimierung geben
- Bid Strategy Report zur Auswertung nutzen

#### Traffic steigern mit Maximize Clicks

**Standardstrategie für neue Search-Kampagnen ohne Conversion-Tracking.** Holt so viele Klicks wie möglich aus dem Tagesbudget heraus, bei minimalem manuellem Pflegeaufwand — passt den Max-CPC pro Auktion automatisch an, um die Klickzahl im Rahmen des Budgets zu maximieren.

> Praxis-Tipp für Kunden: Maximize Clicks ist ein guter **Startpunkt ohne Conversion-Tracking** — sobald Tracking eingerichtet ist, auf eine conversion- oder wertorientierte Strategie (Maximize Conversions/Target CPA/Target ROAS) umstellen, um wirklich auf das Geschäftsergebnis zu optimieren.

### Conversion-basierte Strategien optimieren

**Strategien sind nicht in Stein gemeißelt:** Ändern sich die Marketingziele im Lauf der Kampagne, lässt sich die Bid Strategy in der bestehenden Kampagne jederzeit anpassen — z.B. der klassische Wechsel von **Maximize Conversions → Target CPA**, sobald genug Daten für ein Effizienzziel da sind.

#### Mit Target CPA auf das Kosten-Ziel optimieren

Mit Target CPA lässt sich eine Kampagne gezielt auf einen gewünschten **Cost-per-Conversion** hin optimieren.

**Best Practices:**
- Den Ziel-CPA zu Beginn **nah am aktuellen CPA** ansetzen, um das bisherige Volumen zu halten — keine Schockänderung für die Lernphase
- Die **Google-Ads-Empfehlung für den Ziel-CPA** prüfen — sie basiert auf den historischen Conversion-Daten des Kontos

#### "Reach who matters" — weitere Stellschrauben zur Optimierung

Neben der Bid Strategy selbst gibt es weitere Hebel, um eine Search-Kampagne performanter zu machen:

- **Keywords erweitern:** neue Keywords ergänzen, breitere Match Types nutzen (Richtung Broad Match), Dynamic Search Ads (DSAs) einsetzen, um automatisch neue Suchanfragen abzudecken
- **Audiences (Zielgruppenlisten):** Customer Match und Remarketing Lists for Search Ads (RLSA) erlauben es, Search-Kampagnen gezielt auf Personen auszurichten, die bereits mit dem Unternehmen interagiert haben:
  - **Past Visitors** — frühere Website-Besucher erneut ansprechen
  - **New customers** — neue potenzielle Kunden ähnlich zu bestehenden finden
  - **Existing customers** — bestehende Kunden zu weiteren Käufen/Anfragen bewegen
- **Creative Optimization:** das Anzeigentexting selbst verbessern —
  - **Ad Extensions** — zusätzliche Infos/Links, helfen Leads zu generieren oder Nutzer gezielt auf bestimmte Seiten zu lenken
  - **Ad Customizers** — Echtzeit-Infos wie Standort oder Countdown einbauen → dynamische Anzeigen in großem Maßstab, hyper-relevante Creatives
  - **Keyword Insertion** — Anzeigentext spiegelt automatisch das Suchwort des Nutzers (z.B. Suche nach "CRM Software" → Headline enthält "CRM Software") → höhere wahrgenommene Relevanz

> **Merksatz:** Performance-Optimierung in Search ist nie nur "an der Bid Strategy drehen" — Keywords, Zielgruppen UND Creative-Qualität wirken alle gemeinsam auf das Ergebnis ein.

### Conversion-Wert mit Value-based Bidding steigern

Value-based Bidding hilft dabei, die Auktionen zu priorisieren, die fürs Geschäft am wichtigsten sind — und so den größtmöglichen Conversion-Wert zu erzielen.

**Kernidee:** Conversion-Werte lassen sich mit beliebigen vorhandenen Geschäftsdaten anpassen/gewichten. Beispiel: Der Customer Lifetime Value unterscheidet sich zwischen Käufen auf Desktop vs. Mobile — beide Geräte sollten in **derselben Kampagne** bleiben, da Smart Bidding dann je nach Gerät unterschiedlich bietet, um das ROAS-Ziel zu erreichen. Kann man die ~2 Conversion-Zyklen zur Auswertung nicht abwarten, lohnt sich ggf. eine "flachere" Conversion-Aktion oder eine andere Strategie als Übergang.

**Fundament für eine Value-based-Strategie:**
1. Solide Grundlage beim Online-Conversion-Measurement schaffen — erst Conversion-Aktionen sauber tracken, **bevor** Attribution & Optimierung über Smart Bidding aufgesetzt werden
2. Best Practice: **Global Site Tag + Enhanced Conversions** implementieren, um Datenlücken zu minimieren, wenn Cookies nicht verfügbar sind

**Bei der Auswertung beachten:**
- Die ersten **2–3 Conversion-Zyklen** aus der Bewertung herausnehmen — das ist die Anlaufphase (Ramp-up)
- Wurden Conversion-Werte neu importiert, der Kampagne **ausreichend Zeit** geben, bevor man die Bid Strategy wechselt (Richtwerte siehe die Timelines der vorherigen Workflows)
- **Conversion Delay** einberechnen — die Zeit zwischen Klick und tatsächlicher Conversion. Mit dem Bid Strategy Report den eigenen Conversion Delay ermitteln und diesen Zeitraum aus der Analyse herausnehmen
- Den Erfolg eines Strategiewechsels idealerweise per **A/B-Test (Campaign Experiment)** belegen — anhand der wichtigsten Geschäftskennzahlen, nicht nur an Upstream-Metriken wie CPC, Conversion-Volumen oder CPA

**Erfolgsmetriken je Strategie (Key Metrics):**

| Strategie | Key Metric | "Erfolg sieht so aus" |
|---|---|---|
| **Maximize Conversion Value** | Total Conversion Value | Conversion-Wert steigt, während das Tagesbudget der Kampagne ausgegeben wird. Spend & Value-Volumen hängen direkt am Budget — mehr Volumen = Tagesbudget erhöhen |
| **Target ROAS** | Total Conversion Value **und** Average ROAS (Conv. Value / Cost) | Conversion-Wert steigt, während das gesetzte Ziel-ROAS erreicht wird. Spend & Value-Volumen hängen am ROAS-Ziel — bei vorhandener Werte-Historie die empfohlenen Werte als Ausgangspunkt nutzen |

> **Merksatz:** Vor jeder Bewertung zuerst eine klare Erfolgskennzahl festlegen, die wirklich die Geschäftswahrheit abbildet (z.B. Umsatz/Gewinn) — nicht an Zwischenmetriken wie CPC oder CPA hängenbleiben, die nur Symptome sind.

---

## 6. Budget mit dem Performance Planner optimieren

Der **Performance Planner** ist ein Forecasting-Tool, mit dem sich zukünftige Zeiträume von **bis zu 18 Monaten** planen lassen. Er zeigt, wie sich Anpassungen an Budgets und Targets (Ziel-CPA/ROAS) voraussichtlich auf wichtige Kennzahlen und den Gesamt-Return auswirken — bevor man die Änderung tatsächlich vornimmt.

**Einsatzmöglichkeiten:**
- **Forecasts für Kampagnen einsehen** — Prognose, wohin sich Performance bei unveränderten Einstellungen entwickelt
- **Szenarien durchspielen** — verschiedene Kampagneneinstellungen (Budget, Ziel-CPA/ROAS) anpassen und die simulierten Auswirkungen vergleichen
- **Saisonale Chancen verstehen** — z.B. Vorweihnachtsgeschäft, Sale-Phasen — und Budgets entsprechend vorausplanen
- **Budgets kontoübergreifend verwalten** — Mittel zwischen Kampagnen oder sogar Konten gezielt verschieben, basierend auf den prognostizierten Effekten
