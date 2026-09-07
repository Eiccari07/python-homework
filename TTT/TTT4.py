print("Anna ensin hissille painoraja ja tämän jälkeen anna neljän henkilön paino jotka ovat hissiin menossa.")
p = int(input("Anna hissin painoraja: "))
raja = int(p)
henk1 = input("Anna ensimmäisen henkilön paino: ")
num1 = int(henk1)
henk2 = input("Anna toisen henkilön paino: ")
num2 = int(henk2)
henk3 = input("Anna kolmannen henkilön paino: ")
num3 = int(henk3)
henk4 = input("Anna neljännen henkilön paino: ")
num4= int(henk4)

yhteispaino = num1 + num2 + num3 + num4
if yhteispaino > raja:
    print("Painorajoitus ylitetty, hissiä ei saa käyttää! VITUN LÄSKI NEEKERIHOMO!!!!")
elif yhteispaino < raja:
    print("Kiitos, hissi on käytettävissänne!")