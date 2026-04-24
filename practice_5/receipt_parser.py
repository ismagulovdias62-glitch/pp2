import re
import json

# read file
with open("raw.txt", "r", encoding="utf-8") as file:
    text = file.read()

# 1. Extract prices (e.g. 12.50, 100, 5.99)
prices = re.findall(r"\d+\.\d+|\d+", text)
prices = [float(p) for p in prices]

# 2. Find product names (assume words before price)
products = re.findall(r"([A-Za-z ]+)\s+\d+\.\d+", text)

# 3. Calculate total
total = sum(prices)

# 4. Extract date (example: 2024-10-12 or 12/10/2024)
date = re.findall(r"\d{2,4}[-/]\d{1,2}[-/]\d{1,4}", text)

# 5. Extract time (e.g. 14:35)
time = re.findall(r"\d{1,2}:\d{2}", text)

# 6. Payment method (card / cash / visa etc.)
payment = re.findall(r"(card|cash|visa|mastercard|apple pay)", text, re.IGNORECASE)

# structured output
result = {
    "products": products,
    "prices": prices,
    "total": total,
    "date": date,
    "time": time,
    "payment_method": payment
}

print(json.dumps(result, indent=4))