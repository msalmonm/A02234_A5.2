#!/usr/bin/env python3

import json
import sys
import time
from pathlib import Path


def read_json(path_value):
    try:
        with open(path_value, "r", encoding="utf-8") as file_obj:
            return json.load(file_obj)
    except Exception as err:
        print(f"Error loading {path_value}: {err}")
        sys.exit(1)


def create_price_map(source_list):
    container_map = {}

    for entry in source_list:
        container_map[entry["title"]] = float(entry["price"])

    return container_map


def calculate_amount(price_map, sales_list):
    accumulator = 0.0
    notes = []

    for record in sales_list:
        product_id = record["Product"]
        quantity_val = float(record["Quantity"])

        if quantity_val < 0:
            notes.append(f"Negative quantity: {product_id}")
            continue

        if product_id not in price_map:
            notes.append(f"Not found: {product_id}")
            continue

        accumulator += price_map[product_id] * quantity_val

    return accumulator, notes


def main():
    if len(sys.argv) != 3:
        print("Usage: python computeSales.py catalog.json sales.json")
        sys.exit(1)

    catalog_path = Path(sys.argv[1])
    sales_path = Path(sys.argv[2])

    start_mark = time.perf_counter()

    catalog_data = read_json(catalog_path)
    sales_data = read_json(sales_path)

    price_map = create_price_map(catalog_data)
    total_amount, warnings_list = calculate_amount(price_map, sales_data)

    end_mark = time.perf_counter()

    final_text = "=== SALES SUMMARY ===\n"
    final_text += f"Total: ${total_amount:,.2f}\n\n"

    if warnings_list:
        final_text += "Warnings:\n"
        final_text += "\n".join(warnings_list) + "\n\n"

    final_text += f"Execution time: {end_mark - start_mark:.6f} seconds\n"

    print(final_text)

    with open("SalesResults.txt", "w", encoding="utf-8") as out_file:
        out_file.write(final_text)


if __name__ == "__main__":
    main()
