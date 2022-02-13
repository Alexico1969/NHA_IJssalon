from helper import header

menu = ["home", "prijzen", "recepten"]

header("IJssalon Whizzo")
header("Hoofdmenu")

print("[0] - Stop")

for item in menu:
    number = menu.index(item) + 1
    print(f"[{number}] - {item}")


print("----------------")

correcte_keuze = False

while not correcte_keuze:
    keuze = input("maak uw keuze: ")
    max = len(menu) + 1
    k = int(keuze)
    if k <= max and k >= 0:
        correcte_keuze = True

print(f"U koos: {keuze}")
