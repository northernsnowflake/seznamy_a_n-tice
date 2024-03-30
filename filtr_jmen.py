"""
Napiš funkci filtruj_kratka_jmena, která dostane seznam řetězců a vrátí seznam těch, které jsou kratší než 5 písmen.

Například:

>>> from moje_reseni import vytvor_seznam_zvirat, filtruj_kratka_jmena
>>> zvirata = vytvor_seznam_zvirat()
>>> filtruj_kratka_jmena(zvirata)
['pes', 'had']
Vzpomeň si, jak se vytváří seznam: začni s prázdným seznamem a postupně přidávej prvek po prvku.

Funkce by měla opět vracet nový seznam a svůj argument nechat nezměněný. Vyzkoušej si to následujícím „dialogem“:

>>> from moje_reseni import vytvor_seznam_zvirat, filtruj_kratka_jmena
>>> zvirata = vytvor_seznam_zvirat()
>>> filtruj_kratka_jmena(zvirata)
['pes', 'had']
>>> zvirata
['pes', 'kočka', 'králík', 'had']
"""
def filtruj_kratka_jmena(seznam):
    seznam_kratsich = []
    for zvire in seznam:
        if len(zvire) < 5:
            seznam_kratsich.append(zvire)
    return seznam_kratsich