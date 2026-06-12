"""
Holt Gebäudereinigungsbetriebe in NRW aus OpenStreetMap (Overpass API)
und prueft die Datenqualitaet (Telefon/Website-Abdeckung).
"""

import csv
import json
import urllib.parse
import urllib.request

OVERPASS_URL = "https://overpass-api.de/api/interpreter"

QUERY = """
[out:json][timeout:120];
area["name"="Nordrhein-Westfalen"]["admin_level"="4"]->.searchArea;
(
  nwr["craft"="cleaning"](area.searchArea);
);
out center tags;
"""

OUTPUT_CSV = "leadgen/gebaeudereinigung_nrw.csv"
FIELDNAMES = ["name", "strasse", "plz", "ort", "telefon", "website", "email"]


def fetch():
    data = urllib.parse.urlencode({"data": QUERY}).encode("utf-8")
    req = urllib.request.Request(
        OVERPASS_URL, data=data, headers={"User-Agent": "XPONext-Leadgen/1.0"}
    )
    with urllib.request.urlopen(req, timeout=150) as resp:
        return json.load(resp)


def extract(elements):
    rows = []
    for el in elements:
        tags = el.get("tags", {})
        name = tags.get("name", "")
        if not name:
            continue
        street = tags.get("addr:street", "")
        housenumber = tags.get("addr:housenumber", "")
        rows.append({
            "name": name,
            "strasse": f"{street} {housenumber}".strip(),
            "plz": tags.get("addr:postcode", ""),
            "ort": tags.get("addr:city", ""),
            "telefon": tags.get("phone", tags.get("contact:phone", "")),
            "website": tags.get("website", tags.get("contact:website", "")),
            "email": tags.get("email", tags.get("contact:email", "")),
        })
    return rows


def main():
    data = fetch()
    elements = data.get("elements", [])
    rows = extract(elements)

    total = len(rows)
    with_phone = sum(1 for r in rows if r["telefon"])
    with_website = sum(1 for r in rows if r["website"])
    with_address = sum(1 for r in rows if r["plz"])

    print(f"Rohdaten von Overpass: {len(elements)}")
    print(f"Davon mit Namen: {total}")
    if total:
        print(f"Mit Telefonnummer: {with_phone} ({with_phone/total*100:.0f}%)")
        print(f"Mit Website:      {with_website} ({with_website/total*100:.0f}%)")
        print(f"Mit Adresse/PLZ:  {with_address} ({with_address/total*100:.0f}%)")

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
