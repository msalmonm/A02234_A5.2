import json
import sys

if len(sys.argv) < 3:
    print("Usage: python computeSales.py catalog.json sales.json")
    sys.exit()

file_a = sys.argv[1]
file_b = sys.argv[2]

data_a = json.load(open(file_a))
data_b = json.load(open(file_b))

lookup_table = {}

for element in data_a:
    lookup_table[element["title"]] = element["price"]

sum_value = 0

for sale_entry in data_b:
    key_name = sale_entry["Product"]

    if key_name in lookup_table:
        sum_value += lookup_table[key_name] * sale_entry["Quantity"]
    else:
        print("Missing product:", key_name)

print("Result:", sum_value)