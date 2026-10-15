import json
import os
import ssl
import urllib.request
from datetime import datetime

DATASET_FILE = "dataset.json"

# 1. Fetch live data
url = "https://dummyjson.com/quotes/random"
headers = {"User-Agent": "Mozilla/5.0"}
context = ssl._create_unverified_context()
req = urllib.request.Request(url, headers=headers)

with urllib.request.urlopen(req, context=context) as response:
    raw_data = response.read().decode("utf-8")

parsed = json.loads(raw_data)

# 2. Structure new record
new_entry = {
    "quote_id": parsed["id"],
    "quote": parsed["quote"],
    "author": parsed["author"],
    "collected_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
}

# 3. Load existing dataset or create an empty list
if os.path.exists(DATASET_FILE):
    with open(DATASET_FILE, "r") as f:
        data_list = json.load(f)
else:
    data_list = []

# 4. Append and write back
data_list.append(new_entry)

with open(DATASET_FILE, "w") as f:
    json.dump(data_list, f, indent=4)

print(f"Logged quote #{new_entry['quote_id']}. Total records in dataset: {len(data_list)}")