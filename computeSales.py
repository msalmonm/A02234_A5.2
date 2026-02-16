import json
import sys

if len(sys.argv) < 3:
    print("Usage: python computeSales.py catalog.json sales.json")
    sys.exit()

file_a = sys.argv[1]
file_b = sys.argv[2]

data_a = json.load(open(file_a))
data_b = json.load(open(file_b))

sum_value = 0

for item_b in data_b:
    match_found = False

    for item_a in data_a:
        if item_a["title"] == item_b["Product"]:
            sum_value += item_a["price"] * item_b["Quantity"]
            match_found = True

    if not match_found:
        print("Missing product:", item_b["Product"])

print("Result:", sum_value)
