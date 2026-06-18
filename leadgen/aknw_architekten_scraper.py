"""
AKNW Architekten-Scraper (NRW)
Scrapt Junior-Mitglieder + freischaffende regulaere Mitglieder
mit Name, PLZ, Ort, Buero, Fachrichtung, Telefon, E-Mail, Website.

Ausgabe: leadgen/aknw_architekten_nrw.csv
Laufzeit: ca. 12 Minuten
"""

import csv
import html as html_module
import json
import re
import sys
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed

BASE = "https://www.aknw.de"
OUTPUT = "leadgen/aknw_architekten_nrw.csv"
FIELDNAMES = ["typ", "name", "fachrichtung", "buero", "plz", "ort", "telefon", "email", "website"]

MAX_WORKERS = 8    # parallele Profil-Requests
LIST_DELAY = 0.3   # Sekunden zwischen Listen-API-Seiten

# Beide Quellen: Junior + freischaffende regulaere Mitglieder
SOURCES = [
    {
        "typ": "Junior",
        "list_path": "/berufspraxis/architektensuche/junior-architektenliste",
        "extra_filter": "",
    },
    {
        "typ": "freischaffend",
        "list_path": "/berufspraxis/architektensuche/online-architektenliste",
        "extra_filter": "member_type_of_activity=freischaffend",
    },
]


def get_html(url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=20) as resp:
        return resp.read().decode("utf-8", errors="replace")


def get_json(url):
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "Mozilla/5.0", "X-Requested-With": "XMLHttpRequest"},
    )
    with urllib.request.urlopen(req, timeout=20) as resp:
        return json.load(resp)


def get_endpoint(list_path):
    """Liest den aktuellen API-Endpoint (inkl. cHash) direkt von der Listenseite."""
    html = get_html(BASE + list_path)
    m = re.search(r'data-endpoint="([^"]+)"', html)
    if not m:
        raise ValueError(f"Kein data-endpoint auf {list_path} gefunden.")
    return html_module.unescape(m.group(1))


def get_all_items(endpoint, extra_filter=""):
    """Paginiert durch alle Seiten der Listen-API und gibt alle Items zurueck."""
    items = []
    page = 1
    while True:
        url = f"{BASE}{endpoint}&page={page}"
        if extra_filter:
            url += f"&{extra_filter}"
        try:
            data = get_json(url)
        except Exception as e:
            print(f"\n  Fehler auf Seite {page}: {e}")
            break

        batch = data.get("items", [])
        if not batch:
            break

        items.extend(batch)
        total_pages = data.get("pageAmount", 1)
        print(f"  Seite {page}/{total_pages} — {len(items)} Eintraege gesammelt  ", end="\r")

        if page >= total_pages:
            break
        page += 1
        time.sleep(LIST_DELAY)

    print()
    return items


def parse_profile(html):
    """Extrahiert Telefon, E-Mail und Website aus einer Profilseite."""
    # Telefon / Mobil: steht als Klartext in <li> nach dem Label
    phone_m = re.search(
        r"<strong>(?:Mobil|Telefon)</strong></li><li>([^<]+)", html
    )
    phone = phone_m.group(1).strip() if phone_m else ""

    # E-Mail: erstes mailto:-Link, das nicht aknw.de ist
    emails = re.findall(r"mailto:([^\"?\s&]+)", html)
    email = next((e for e in emails if "aknw.de" not in e), "")

    # Website: external-link href
    web_m = re.search(r'class="external-link"[^>]*href="(https?://[^"]+)"', html)
    if not web_m:
        web_m = re.search(r'href="(https?://[^"]+)"[^>]*class="external-link"', html)
    website = web_m.group(1) if web_m else ""

    return phone, email, website


def fetch_profile_row(item, typ):
    """Holt fuer ein Listen-Item die Kontaktdaten vom Profilseite."""
    f = item.get("fields", {})
    name = f.get("name", {}).get("value", "")
    plz = f.get("zip", {}).get("value", "")
    city = f.get("city", {}).get("value", "")
    company = f.get("company", {}).get("value", "")
    if company == "-":
        company = ""
    fachrichtung = ", ".join(f.get("field_of_study", {}).get("value", []))
    profile_url = BASE + item.get("src", "")

    try:
        html = get_html(profile_url)
        phone, email, website = parse_profile(html)
    except Exception:
        phone = email = website = ""

    return {
        "typ": typ,
        "name": name,
        "fachrichtung": fachrichtung,
        "buero": company,
        "plz": plz,
        "ort": city,
        "telefon": phone,
        "email": email,
        "website": website,
    }


def scrape_source(source):
    typ = source["typ"]
    list_path = source["list_path"]
    extra = source["extra_filter"]

    print(f"\n{'='*50}")
    print(f"Starte: {typ}  ({list_path})")
    print(f"{'='*50}")

    endpoint = get_endpoint(list_path)
    items = get_all_items(endpoint, extra)
    print(f"{len(items)} Eintraege in Listenabfrage gefunden.")

    print(f"Lade {len(items)} Profile ({MAX_WORKERS} parallele Workers)...")
    rows = []
    done = 0
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        futures = {executor.submit(fetch_profile_row, item, typ): item for item in items}
        for fut in as_completed(futures):
            done += 1
            if done % 100 == 0:
                print(f"  {done}/{len(items)} Profile fertig...  ", end="\r")
            try:
                rows.append(fut.result())
            except Exception:
                pass

    print(f"\n{len(rows)} Profile erfolgreich geladen.")
    return rows


def main():
    all_rows = []

    for source in SOURCES:
        rows = scrape_source(source)
        all_rows.extend(rows)

    with open(OUTPUT, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(all_rows)

    total = len(all_rows)
    with_phone = sum(1 for r in all_rows if r["telefon"])
    with_email = sum(1 for r in all_rows if r["email"])
    with_website = sum(1 for r in all_rows if r["website"])
    junior = sum(1 for r in all_rows if r["typ"] == "Junior")
    frei = sum(1 for r in all_rows if r["typ"] == "freischaffend")

    print(f"\n{'='*50}")
    print(f"FERTIG: {total} Eintraege → {OUTPUT}")
    print(f"  Junior:        {junior}")
    print(f"  freischaffend: {frei}")
    print(f"Mit Telefon:  {with_phone} ({with_phone/total*100:.0f}%)")
    print(f"Mit E-Mail:   {with_email} ({with_email/total*100:.0f}%)")
    print(f"Mit Website:  {with_website} ({with_website/total*100:.0f}%)")


if __name__ == "__main__":
    main()
