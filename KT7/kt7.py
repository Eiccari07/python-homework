pizzat = {
    1: {'nimi': 'Bolognese',
        'taytteet': ['jauheliha'],
        'hinta': 9.50},
    2: {'nimi': 'Frutti di Mare',
        'taytteet': ['ananas', 'katkarapu', 'tonnikala'],
        'hinta': 10.50},
    3: {'nimi': 'Americano',
        'taytteet': ['ananas', 'aurajuusto', 'kinkku'],
        'hinta': 9.00},
    4: {'nimi': 'Opera Special',
        'taytteet': ['kinkku', 'salami', 'tonnikala'],
        'hinta': 11.00},
    5: {'nimi': 'Mexicana',
        'taytteet': ['ananas', 'pepperoni', 'chili',
                     'tacokastike'],
        'hinta': 12.00},
    6: {'nimi': 'Julia',
        'taytteet': ['ananas', 'aurajuusto', 'katkarapu',
                     'kinkku'],
        'hinta': 10.00},
    7: {'nimi': 'Empire Special',
        'taytteet': ['katkarapu', 'kinkku', 'mustapippuri',
                     'salami', 'sipuli', 'tuplajuusto',
                     'valkosipuli'],
        'hinta': 11.00},
    8: {'nimi': 'Kummisetä',
        'taytteet': ['herkkusieni', 'katkarapu', 'kinkku',
                     'valkosipuli'],
        'hinta': 10.00},
    10: {'nimi': 'Hawaii',
         'taytteet': ['ananas', 'kana', 'aurajuusto'],
         'hinta': 11.50},
    9: {'nimi': 'Chicken Hawaii',
        'taytteet': ['ananas', 'aurajuusto', 'kana'],
        'hinta': 11.00},
    11: {'nimi': 'Romeo',
         'taytteet': ['ananas', 'aurajuusto', 'katkarapu',
                      'salami'],
        'hinta': 10.50},
    12: {'nimi': 'Vegetariana',
         'taytteet': ['herkkusieni', 'oliivi', 'paprika',
                      'sipuli', 'tomaatti'],
        'hinta': 9.50},
    13: {'nimi': 'Dillinger',
         'taytteet': ['jauheliha', 'kinkku', 'salami',
                      'sipuli'],
        'hinta': 10.00},
    14: {'nimi': 'Papa''s Special',
         'taytteet': ['aurajuusto', 'mustapippuri', 'oliivi',
                      'paprika', 'salami', 'sipuli'],
        'hinta': 11.00},
    15: {'nimi': 'Quattro Stagioni',
         'taytteet': ['herkkusieni', 'katkarapu', 'kinkku',
                      'paprika'],
        'hinta': 10.50},
    16: {'nimi': 'Cambretti',
         'taytteet': ['tuplajuusto', 'katkarapu',
                      'valkosipuli'],
        'hinta': 10.00},
    17: {'nimi': 'Pepperoni',
         'taytteet': ['paprika', 'pepperoni', 'tonnikala'],
        'hinta': 10.50},
    19: {'nimi': 'Spicy Hot Crispy',
         'taytteet': ['mausteinen naudanliha', 'sipuli',
                      'tomaatti', 'chili'],
        'hinta': 11.00},
    21: {'nimi': 'Finlandia',
         'taytteet': ['kana', 'katkarapu', 'kinkku',
                      'salami', 'tonnikala'],
        'hinta': 10.50},
    23: {'nimi': 'Driver''s Special',
         'taytteet': ['pekoni', 'pepperoni', 'kinkku',
                      'salami', 'aurajuusto'],
        'hinta': 11.00},
    26: {'nimi': 'Fantasia',
         'taytteet': [None, None, None, None],
        'hinta': 10.00}
}

def tilaus():
    print('Tervetuloa Guidos Pizza Palaceen, mitä haluaisitte?')
    save = 0
    while True:
        numero = int(input('Anna pizzan numero (0 = lopetus): '))
        if numero == 0:
           print(f'Kiitos tilauksestanne! Kokonaishintanne on {save} euroa.')
           break
        elif (numero not in pizzat):
            print(f'Virheellinen pizzan numero!')
        else:
            hm = int(input(f'Pizzan numero {numero} kappalemäärä: '))
            if hm > 50 or hm <= 0:
                print(f'Kappalemäärän pitää olla enemmän kuin nolla tai vähemmän kun 50')
            else:
                save += pizzat[numero]['hinta'] * hm
                print(f'Välisumma: {hm} x {pizzat[numero]['hinta']} = {pizzat[numero]['hinta'] * hm} euroa')


tilaus()
