def tietovisa (a , b):
    if (a == 'a'):
        return b['a']
    elif (a == 'b'):
        return b['b']
    elif (a == 'c'):
        return b['c']
    else:
        return False


kysymys1 = {'kysymys':'Kuinka monta albumia Metallica on julkaissut? A: 2 B: 7 C: 11', 'a': False, 'b': False, 'c': True}

print(kysymys1['kysymys'])
user = input()
if tietovisa(user, kysymys1) == True:
    print('Oikein meni!')

else:
    print('Väärin meni!')