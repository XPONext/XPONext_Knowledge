"""
Holt Gebaeudereinigungsbetriebe in NRW ueber die Google Places API (New) -
Text Search, inkl. Telefonnummer und Website (Contact Data).

WICHTIG (Stand 2026):
- Das frueher beworbene "$200 Gratis-Guthaben/Monat" existiert nicht mehr.
  Google hat es durch kostenlose monatliche Anfrage-Kontingente PRO SKU ersetzt:
    * Text Search Pro:        5.000 kostenlose Anfragen/Monat
    * Text Search Enterprise:  1.000 kostenlose Anfragen/Monat
  Felder wie nationalPhoneNumber / websiteUri koennen die Anfrage in die
  "Enterprise"-Kategorie heben -> sicherheitshalber wird hier mit dem
  strengeren Limit (1.000/Monat) gerechnet.

- Dieses Skript hat einen HARTEN Sicherheits-Limit (MAX_REQUESTS), das weit
  unter 1.000 liegt. Es bricht ab, sobald das Limit erreicht ist, damit auf
  keinen Fall versehentlich Kosten entstehen.

Voraussetzungen:
1. Google Cloud Projekt anlegen, "Places API (New)" aktivieren.
2. API-Key erstellen (Abrechnungskonto ist Pflicht, wird aber innerhalb des
   Gratis-Kontingents NICHT belastet).
3. Key als Umgebungsvariable setzen:
       export GOOGLE_PLACES_API_KEY="dein-key"
"""

import csv
import json
import os
import time
import urllib.error
import urllib.request

API_KEY = os.environ.get("GOOGLE_PLACES_API_KEY")
SEARCH_URL = "https://places.googleapis.com/v1/places:searchText"

# Sicherheits-Limit: deutlich unter dem strengsten Gratis-Kontingent (1.000/Monat)
MAX_REQUESTS = 60

FIELD_MASK = (
    "places.id,places.displayName,places.formattedAddress,"
    "places.nationalPhoneNumber,places.websiteUri"
)

# Kreisfreie Staedte + Landkreise in NRW (53 Regionen)
NRW_REGIONEN = [
    "Bielefeld", "Bochum", "Bonn", "Bottrop", "Dortmund", "Duisburg",
    "Duesseldorf", "Essen", "Gelsenkirchen", "Hagen", "Hamm", "Herne",
    "Koeln", "Krefeld", "Leverkusen", "Moenchengladbach",
    "Muelheim an der Ruhr", "Muenster", "Oberhausen", "Remscheid",
    "Solingen", "Wuppertal",
    "Kreis Aachen", "Kreis Borken", "Kreis Coesfeld", "Kreis Dueren",
    "Ennepe-Ruhr-Kreis", "Kreis Euskirchen", "Kreis Guetersloh",
    "Kreis Heinsberg", "Kreis Herford", "Hochsauerlandkreis",
    "Kreis Hoexter", "Kreis Kleve", "Kreis Lippe", "Maerkischer Kreis",
    "Kreis Mettmann", "Kreis Minden-Luebbecke", "Oberbergischer Kreis",
    "Kreis Olpe", "Kreis Paderborn", "Kreis Recklinghausen",
    "Rhein-Erft-Kreis", "Rhein-Kreis Neuss", "Rheinisch-Bergischer Kreis",
    "Rhein-Sieg-Kreis", "Kreis Siegen-Wittgenstein", "Kreis Soest",
    "Kreis Steinfurt", "Kreis Unna", "Kreis Viersen", "Kreis Warendorf",
    "Kreis Wesel",
]

OUTPUT_CSV = "leadgen/gebaeudereinigung_nrw_places.csv"
FIELDNAMES = ["name", "adresse", "telefon", "website", "place_id"]


def search_text(query):
    body = json.dumps({
        "textQuery": query,
        "languageCode": "de",
        "regionCode": "DE",
    }).encode("utf-8")

    req = urllib.request.Request(
        SEARCH_URL,
        data=body,
        method="POST",
        headers={
            "Content-Type": "application/json",
            "X-Goog-Api-Key": API_KEY,
            "X-Goog-FieldMask": FIELD_MASK,
        },
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.load(resp)


def main():
    if not API_KEY:
        raise SystemExit(
            "Fehler: Umgebungsvariable GOOGLE_PLACES_API_KEY ist nicht gesetzt."
        )

    rows = []
    seen_ids = set()
    request_count = 0

    for region in NRW_REGIONEN:
        if request_count >= MAX_REQUESTS:
            print(f"Sicherheits-Limit ({MAX_REQUESTS} Anfragen) erreicht - Abbruch.")
            break

        query = f"Gebaeudereinigung in {region}"
        request_count += 1
        try:
            data = search_text(query)
        except urllib.error.HTTPError as e:
            print(f"Fehler bei '{region}': HTTP {e.code} - {e.read().decode()}")
            continue

        for place in data.get("places", []):
            pid = place.get("id")
            if not pid or pid in seen_ids:
                continue
            seen_ids.add(pid)
            rows.append({
                "name": place.get("displayName", {}).get("text", ""),
                "adresse": place.get("formattedAddress", ""),
                "telefon": place.get("nationalPhoneNumber", ""),
                "website": place.get("websiteUri", ""),
                "place_id": pid,
            })

        time.sleep(0.1)  # kleine Pause, freundlich zur API

    total = len(rows)
    with_phone = sum(1 for r in rows if r["telefon"])
    with_website = sum(1 for r in rows if r["website"])

    print(f"\nAPI-Anfragen verbraucht: {request_count} (Limit: {MAX_REQUESTS})")
    print(f"Gefundene Betriebe (dedupliziert): {total}")
    if total:
        print(f"Mit Telefonnummer: {with_phone} ({with_phone/total*100:.0f}%)")
        print(f"Mit Website:      {with_website} ({with_website/total*100:.0f}%)")

    with open(OUTPUT_CSV, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(rows)
    print(f"\nGespeichert: {OUTPUT_CSV}")

    print("\nErste 20 Eintraege:")
    for r in rows[:20]:
        print(r)


if __name__ == "__main__":
    main()
