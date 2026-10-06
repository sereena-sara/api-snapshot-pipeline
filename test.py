import json
import ssl
import urllib.request
from datetime import datetime

url = "https://dummyjson.com/quotes/random"

headers = {"User-Agent": "Mozilla/5.0"}
context = ssl._create_unverified_context()
req = urllib.request.Request(url, headers=headers)

with urllib.request.urlopen(req, context=context) as response:
    raw_data = response.read().decode("utf-8")

parsed_data = json.loads(raw_data)

quote_text = parsed_data["quote"]
author_name = parsed_data["author"]
saved_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Bundle what we want to keep into a neat dictionary
clean_record = {
    "saved_at": saved_at,
    "quote": quote_text,
    "author": author_name,
}

# Write it directly into a file called "quote.json"
with open("quote.json", "w") as f:
    json.dump(clean_record, f, indent=4)

print(f"Saved to quote.json at {saved_at}!")