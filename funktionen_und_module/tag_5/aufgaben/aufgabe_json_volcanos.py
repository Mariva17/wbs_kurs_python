""" (MITTEL)
Lese die Datei active_volcanos.csv ein und filtere
die Einträge nach Land (zb. Italy).
Die gefilterten Einträge kommen in eine entsprechende
json-Datei (zb. data/volcanos_italy.json).
Es sollen nur Vulkane berücksichtigt werden, für die gilt:
risk != NULL

Die Json-Einträge sollen enthalten:
Name des Vulkans
Risiko
Latitude
Longitude
Country
Region

zb. als Array von Objekten

[
    {
        "name": "Farallon de Pajaros",
        "latitude": "20.538000000000000",
        "longitude": "144.895999999999000",
        "risk": "1",
        "country": "United States",
        "region": "Japan, Taiwan, Marianas"
    },
    {..},

]

Achte auf die Schreibweise der Json-Namen, zb. "name"
"""

import json
from pathlib import Path
import csv



# map column name CSV -> JSON
COLUMN_MAPPING = (
    ('V_Name', 'name'),
    ('Latitude', 'latitude'),
    ('Longitude', 'longitude'),
    ('risk', 'risk'),
    ('Country', 'country'),
    ('Region', 'region'),
)

SRC_DIR = Path(__file__).parent

NULL_RISK = "NULL"


def load_volcanos_from_csv(filename: str) -> list[dict]:
    """read CSV and get a list of volcanos."""
    with open(SRC_DIR / filename, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f, delimiter=",")
        volcanos = list(reader)
    return volcanos


def filter_volcanos_by_country_and_risk(
        volcanos: list[dict],
        country: str) -> list[dict]:
    """filter a list of volcanos."""
    risky_volcanos = []
    for volcano in volcanos:
        if volcano["Country"].lower() == country.lower() and volcano["risk"] != NULL_RISK:
            risky_volcano = {}
            for key_csv, key_json in COLUMN_MAPPING:
                risky_volcano[key_json] = volcano[key_csv]
            risky_volcanos.append(risky_volcano)
    return risky_volcanos


def save_volcanos_to_json(volcanos: list[dict], filename: str) -> None:
    """saves a list of dicts (volcanos) to a JSON file."""
    with open(SRC_DIR / filename, mode="w", encoding="utf_8") as f:
        json.dump(volcanos, f, ensure_ascii=False, indent=4)


def main():

    # country = input("Bitte gebe das Land ein:")
    country = "italy"
    input_filename = "active_volcanos.csv"
    output_filename = "{}_{}.json".format("volcanos", country)

    volcanos = load_volcanos_from_csv(input_filename)
    print("Vulkane gelesen von {}".format(input_filename))
    risky_volcanos = filter_volcanos_by_country_and_risk(volcanos, country)
    print(risky_volcanos)
    save_volcanos_to_json(risky_volcanos, output_filename)
    s = "{} aktive Vulkane mit Risikopotential in {} geschrieben auf {}"
    print(s.format(len(risky_volcanos), country, output_filename))


main()