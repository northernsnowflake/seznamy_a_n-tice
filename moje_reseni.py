"""Napiš funkci vytvor_balicek, která vrátí nový zamíchaný seznam hracích karet pro hru Prší. Každá položka seznamu bude (na rozdíl od balíčku ze setkání) dvojice hodnota-barva.

Hodnoty karet jsou 2-10, 'J', 'Q', 'K', 'A'. Barvy jsou '♥' '♦' '♠' '♣'. (Symboly si můžeš zkopírovat jako text. Nezobrazují-li se ti v příkazové řádce správně, použij místo nich S, K, P, +.)

Například:

>>> from moje_reseni import vytvor_balicek
>>> vytvor_balicek()
[(2, '♥'), (10, '♠'), ('A', '♣'), ...

"""



import random


def vytvor_balicek():
    hodnoty = []
    symboly = '♥', '♦', '♠', '♣'
    for cislo in range(2,11):
        hodnoty.append(str(cislo))
    hodnoty = hodnoty + ['J', 'Q', 'K', 'A']

    karty = []
    for symbol in symboly:
        for hodnota in hodnoty:
            karty.append((hodnota, symbol))

    #print(hodnoty)
    #print(symboly)

    random.shuffle(karty)
    return karty

#print(vytvor_balicek())

#print(cisla)
