"""
3.
Napiš funkci obsahuje, která dostane seznam a slovo a zjistí, jestli je to slovo v daném seznamu. Podle toho vrátí True nebo False.

Například:

>>> from moje_reseni import vytvor_seznam_zvirat, obsahuje
>>> zvirata = vytvor_seznam_zvirat()
>>> obsahuje(zvirata, 'pes')
True
>>> obsahuje(zvirata, 'vodováha')
False
"""
from seznam_zvirat import vytvor_seznam_zvirat

def obsahuje(seznam, slovo):
    if slovo in seznam:
        return slovo in seznam
    else:
        return False
    

zvirata = vytvor_seznam_zvirat()
print(obsahuje(zvirata, 'pes'))
print(obsahuje(zvirata, 'vodováha'))
