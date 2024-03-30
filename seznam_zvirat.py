"""
Napiš funkci vytvor_seznam_zvirat(), která vytvoří nový seznam domácích zvířat a vrátí ho. Domácí zvířata známe tato: "pes", "kočka", "králík", "had".

Tuto funkci použiješ pro otestování dalších úloh. Nehledej v ní nic složitého.

Příklad:

>>> vytvor_seznam_zvirat()
['pes', 'kočka', 'králík', 'had']
Každé zavolání funkce by mělo vytvořit nový, nezávislý seznam. Vyzkoušej si to následujícím „dialogem“:

>>> from moje_reseni import vytvor_seznam_zvirat
>>> zvirata = vytvor_seznam_zvirat()
>>> zvirata.pop()
'had'
>>> vytvor_seznam_zvirat()
['pes', 'kočka', 'králík', 'had']
>>> zvirata
['pes', 'kočka', 'králík']
"""
def vytvor_seznam_zvirat():
    seznam = ["pes", "kočka", "králík", "had", "andulka"]
    #seznam = ["pes", "kočka", "králík", "had"]
    return seznam

"""
Napiš funkci filtruj_k, která dostane seznam řetězců a vrátí seznam těch, které začínají na k.

Například:

>>> from moje_reseni import vytvor_seznam_zvirat, filtruj_k
>>> zvirata = vytvor_seznam_zvirat()
>>> filtruj_k(zvirata)
['kočka', 'králík']
Funkce by měla opět vracet nový seznam a svůj argument nechat nezměněný.
"""
def filtruj_k(seznam):
    seznam_zacinajicich_k = []
    for zvire in seznam:
        if zvire[0] == 'k':
            seznam_zacinajicich_k.append(zvire)
    return seznam_zacinajicich_k