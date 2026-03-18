import re
import json

f = open("raw.txt", "r", encoding="utf-8")
text = f.read()
f.close()

prices = re.findall(r"\d{1,3}(?: \d{3})*,\d{2}", text)
prices = [float(p.replace(" ", "").replace(",", ".")) for p in prices]

products = re.findall(r"\d+\.\n(.+?)\n\d", text)
products = [p.strip() for p in products]

total_match = re.search(r"ИТОГО:\n([\d ]+,\d{2})", text)
total = float(total_match.group(1).replace(" ", "").replace(",", ".")) if total_match else None

datetime_match = re.search(r"(\d{2}\.\d{2}\.\d{4}) (\d{2}:\d{2}:\d{2})", text)
date = datetime_match.group(1) if datetime_match else None
time = datetime_match.group(2) if datetime_match else None

payment_match = re.search(r"(Банковская карта|Наличные)", text)
payment = payment_match.group(1) if payment_match else None

result = {
    "products": products,
    "prices": prices,
    "total": total,
    "date": date,
    "time": time,
    "payment": payment
}

print(json.dumps(result, indent=4, ensure_ascii=False))