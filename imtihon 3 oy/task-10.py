import matplotlib.pyplot as plt
from pathlib import Path

kunlar = ["Du", "Se", "Cho", "Pay", "Ju", "Sha", "Yak"]
daromad = [120, 150, 100, 180, 200, 240, 210]

plt.figure(figsize=(8, 5))
plt.plot(kunlar, daromad, marker="o", color="royalblue", label="Daromad")

plt.title("Haftalik daromad")
plt.xlabel("Hafta kunlari")
plt.ylabel("Daromad")

plt.legend()
plt.grid(True)

rasm_yoli = Path(__file__).resolve().parent / "daromad.png"
plt.savefig(rasm_yoli, dpi=150, bbox_inches="tight")
print("daromad.png fayli yaratildi.")
plt.show()
