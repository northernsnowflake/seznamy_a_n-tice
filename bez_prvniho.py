"""
Napiš funkci bez_prvniho, která dostane seznam jmen a vrátí seznam se všemi jeho prvky kromě prvního.

>>> from moje_reseni import vytvor_seznam_zvirat, bez_prvniho
>>> zvirata = vytvor_seznam_zvirat()
>>> zvirata
['pes', 'kočka', 'králík', 'had']
>>> bez_prvniho(zvirata)
['kočka', 'králík', 'had']
Funkce by opět neměla změnit původní seznam:

>>> zvirata
['pes', 'kočka', 'králík', 'had']
A měla by fungovat i pro prázdný seznam:

>>> bez_prvniho([])
[]
"""
from seznam_zvirat import vytvor_seznam_zvirat

def bez_prvniho(seznam):
    seznam_bez_prvniho = list(seznam) #vytvoří se kopie seznamu
    if seznam != []:
        seznam_bez_prvniho.pop(0) #vrátí první prvek
    return seznam_bez_prvniho

zvirata = vytvor_seznam_zvirat()
print(zvirata)
print(bez_prvniho(zvirata))