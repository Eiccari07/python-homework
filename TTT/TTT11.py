hawaji = ['Kinkku', 'Ananas', 'Paprika', 'Aura', 'Pepperooni']
margareta = ['Mozzarella', 'Tomaatti',]
mika = input('Mikä pizza teille saisi olla? Vaihtoehdot omn hawaji tai maragreta: ')

if mika == 'margareta':
    mika = margareta.copy()
else:
    mika = hawaji.copy()

for i in mika:
    if i == 'Ananas':
        print('Hyi ananasta!')