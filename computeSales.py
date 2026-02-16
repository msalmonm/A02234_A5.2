import json
import sys

if len(sys.argv) < 3:
    print("Usage: python computeSales.py catalog.json sales.json")
    sys.exit()

file_a = sys.argv[1]
file_b = sys.argv[2]

def read_json(path_value):
    try:
        with open(path_value) as file_obj:
            return json.load(file_obj)
    except Exception as err:
        print("Load error:", err)
        sys.exit()


data_a = read_json(file_a)
data_b = read_json(file_b)


lookup_table = {}

for element in data_a:
    lookup_table[element["title"]] = element["price"]

sum_value = 0

for sale_entry in data_b:
    key_name = sale_entry["Product"]
    qty_number = sale_entry["Quantity"]

    if qty_number < 0:
        print("Invalid quantity:", key_name)
        continue

    if key_name in lookup_table:
        sum_value += lookup_table[key_name] * qty_number
    else:
        print("Missing product:", key_name)
