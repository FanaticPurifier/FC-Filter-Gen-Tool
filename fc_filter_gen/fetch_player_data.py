import requests
import csv
import time
import json

API_URL = "https://api.futdatabase.com/api/players"  # Base endpoint
API_TOKEN = "e2c7c465-2e10-1c4d-130e-7d5265a57308"  # Your API token
OUTPUT_CSV = "fc_filter_gen/player_id_mapping.csv"
OUTPUT_JSON = "fc_filter_gen/player_data.json"

FIELDS = [
    "id", "firstName", "lastName", "commonName", "name", "rating"
]

HEADERS = {
    "accept": "application/json",
    "X-AUTH-TOKEN": API_TOKEN
}

def fetch_all_players(api_url=API_URL, output_csv=OUTPUT_CSV, output_json=OUTPUT_JSON):
    all_players = []
    page = 1
    items_per_page = 20
    total_pages = None
    print("Fetching player data from API...")
    while True:
        url = f"{api_url}?page={page}&itemsPerPage={items_per_page}"
        resp = requests.get(url, headers=HEADERS)
        if resp.status_code != 200:
            print(f"Error fetching page {page}: {resp.status_code}")
            break
        data = resp.json()
        if total_pages is None:
            total_pages = data["pagination"]["pageTotal"]
        items = data.get("items", [])
        for item in items:
            player = {field: item.get(field, "") for field in FIELDS}
            all_players.append(player)
        print(f"Fetched page {page}/{total_pages} ({len(all_players)} players)")
        if page >= total_pages:
            break
        page += 1
        time.sleep(0.1)  # Be kind to the API
    # Write CSV
    with open(output_csv, "w", newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(all_players)
    # Write JSON
    with open(output_json, "w", encoding='utf-8') as f:
        json.dump(all_players, f, indent=2)
    print(f"Done! Saved {len(all_players)} players to {output_csv} and {output_json}")

if __name__ == "__main__":
    fetch_all_players()
