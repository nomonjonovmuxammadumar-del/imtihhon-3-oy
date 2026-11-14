import json
from pathlib import Path

FAYL = Path(__file__).resolve().parent / "products.json"

try:
    with open(FAYL, "r", encoding="utf-8") as fayl:
        mahsulotlar = json.load(fayl)
except FileNotFoundError:
    print(f"{FAYL} fayli topilmadi.")
    raise SystemExit

nom = input("Mahsulot nomi: ").strip()
yangi_miqdor = int(input("Yangi miqdor: "))

topildi = False
for mahsulot in mahsulotlar:
    if mahsulot["nom"].lower() == nom.lower():
        mahsulot["miqdor"] = yangi_miqdor
        topildi = True
        break

if topildi:
    with open(FAYL, "w", encoding="utf-8") as fayl:
        json.dump(mahsulotlar, fayl, ensure_ascii=False, indent=4)
    print("Miqdor yangilandi.")
    print(json.dumps(mahsulotlar, ensure_ascii=False, indent=4))
else:
    print("Mahsulot topilmadi.")
