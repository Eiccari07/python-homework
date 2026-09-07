kuukausi = int(input("Anna kuukausi: "))
if kuukausi == 1 or kuukausi == 3 or kuukausi == 5 or kuukausi == 7 or kuukausi == 8 or kuukausi == 10 or kuukausi == 12:
    print("31 Päivää")
elif kuukausi == 2:
    print("28 päivää (29 karkausvuonna)")
elif kuukausi == 4 or kuukausi == 6 or kuukausi == 9 or kuukausi == 11:
    print("30 päivää")
else:
    print("Ei ole kuukausi")