def palidrom(lause):
    save = []
    i = 0
    for kirjain in lause:
        if kirjain.isalpha():
            save.insert(i, kirjain.lower())
        else:
            continue
        i += 1

    rsave = save.copy()
    rsave.reverse()

    if rsave == save:
        return True
    else:
        return False

ehdokkaat = [
    'A man, a plan, a canal: Panama.',
    'Iso rikas sika sökösakissa kirosi.',
    '"Aa, viinaa sitruksilla", kallis kurtisaani ivaa.',
    'Joku satunnainen lause',
    'Madam, Im Adam.',
    'Never odd or even.',
    'Was it a car or a cat I saw?',
    'Mr. Owl ate my metal worm.',
    'No lemon, no melon.',
    'Evil rats on no star live.'
]

for e in ehdokkaat:
    tulos = 'EI OLE'
    if palidrom(e):
        tulos = 'ON'
    print(f'"{e}": {tulos} palindromi')