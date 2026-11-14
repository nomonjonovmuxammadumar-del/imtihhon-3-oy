import csv
from pathlib import Path

mahsulotlar = [
    ["Olma", 8000, 12],
    ["Non", 4000, 20],
    ["Sut", 14000, 5]
]

fayl_yoli = Path(__file__).resolve().parent / "products.csv"

with open(fayl_yoli, "w", newline="", encoding="utf-8") as fayl:
    yozuvchi = csv.writer(fayl)
    yozuvchi.writerow(["nom", "narx", "soni"])
    yozuvchi.writerows(mahsulotlar)

print("products.csv fayliga yozildi.")
