
kysymykset = []

try:
    tiedosto = open("kysymykset.txt", "r")
    sisalto = tiedosto.readlines()
    tiedosto.close()
    for rivi in sisalto:
        osat = rivi.strip().split("|")

        if len(osat) != 5:
            print("Error: Tiedostossa on liian vähän osia")
            exit()

        kysymys = {
            "kysymys": osat[0],
            "a": osat[1],
            "b": osat[2],
            "c": osat[3],
            "vastaus": osat[4]
        }
        kysymykset.append(kysymys)

except FileNotFoundError:
    print("Error: tiedostoa ei löydetty")
    exit()

pisteet = 0
i = 0
for kysymys in kysymykset:
    i += 1
    print(f"{i}. {kysymys['kysymys']}")
    print(f"a: {kysymys['a']}")
    print(f"b: {kysymys['b']}")
    print(f"c: {kysymys['c']}")

    while True:
        vastaus = input("Valitse a, b tai c: ")

        if vastaus != "a" and vastaus != "b" and vastaus != "c":
            print("Yritä uudelleen")
        else:
            break

    if vastaus == kysymys["vastaus"]:
        print("Oikein meni")
        pisteet += 1
    else:
        print("Väärin meni")

print("")
print(f"Pisteet: {pisteet}/{len(kysymykset)}")
