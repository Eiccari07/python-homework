pituus = float(input("Hypyn pituus: "))

yp = 0

for tuomari in range(1,6):

    tpisteet = float(input("Tuomarin "+ str(tuomari) +" pisteet: "))
    yp = yp + tpisteet
    tuomari = tuomari + 1

yp = yp + 0.9 * pituus

print("Yhteispisteet "+ str(yp))