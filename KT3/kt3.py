print("Vertaile onko bensiinimoottorisella autolla vai dieselmoottorisella autolla halvempi ajaa")

print("Autolla ajettava vuotuinen kilometrimäärä?")
vuotuinen = float(input("Vuotuinen: "))

print("Bensiinin litrahinta euroina?")
bh = float(input("Hinta: "))

print("Dieselöljyn litrahinta euroina?")
dh = float(input("Hinta: "))

print("Bensiinimoottorisen auton kulutus (litraa / 100 km)?")
bak = float(input("Kulutus: "))

print("Dieselmoottorisen auton kulutus (litraa / 100 km)?")
dak = float(input("Kulutus: "))

print("Dieselin käyttövoimaveron määrä")
dkv = float(input("Vero: "))

bsum = vuotuinen / 100 * bak * bh
dsum = vuotuinen / 100 * dak * dh + dkv

if bsum < dsum:
    print("Bensiinimoottorisen auton ajaminen on halvempaa")
    print("Bensiinimoottorisen auton ajamisen kustannus on: " + str(bsum) + "€")
    print("Dieselmoottorisen auton ajamisen kustannus on: " + str(dsum) + "€")
else:
    print("Dieselmoottorisen auton ajaminen on halvempaa")
    print("Bensiinimoottorisen auton ajamisen kustannus on: " + str(bsum) + "€")
    print("Dieselmoottorisen auton ajamisen kustannus on: " + str(dsum) + "€")