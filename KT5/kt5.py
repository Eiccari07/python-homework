
def muunna(asteet, mista, mihin):
    if mista == "c":
        if mihin == "f":
            return 9 / 5 * asteet + 32
        elif mihin == "k":
            return asteet + 273
    elif mista == "f":
        if mihin == "c":
            return 5 / 9 * (asteet - 32)
        elif mihin == "k":
            return 5 / 9 * (asteet - 32) + 273
    elif mista == "k":
        if mihin == "c":
            return asteet - 273
        elif mihin == "f":
            return 9 / 5 * (asteet - 273) + 32

asteet = float(input("Mikä lämpötila?: "))
mista = input("Mikä on lämpötilan muoto? (c, f, k): ")
mihin = input("Mihin muotoon lämpötila muutetaan? (c, f, k): ")
tulos = muunna(asteet, mista, mihin)

print(f'{asteet} astetta {mista} on {round(tulos)} astetta {mihin}.')