p1 = input("Anna päivämäärä yyyy-mm-dd muodossa:")
vuosi = p1[0:4]
kuukausi1 = p1[5]
kuukausi2 = p1[6]
paiva1 = p1[8]
paiva2 = p1[9]
if kuukausi1 == "0" and paiva1 == "0":
    print(f"Päivämäärä suomalaisessa muodossa: {paiva2}.{kuukausi2}.{vuosi}")
elif kuukausi1 == "0":
    print(f"Päivämäärä suomalaisessa muodossa: {paiva1}{paiva2}.{kuukausi2}.{vuosi}")
elif paiva1 == "0":
    print(f"Päivämäärä suomalaisessa muodossa: {paiva2}.{kuukausi1}{kuukausi2}.{vuosi}")