"""
Složitější, nepovinný úkol!

Had byl pyšný na to, že je v abecedě první. Dokud nepřiletěla "andulka".

Abys hada uklidnila, vytvoř funkci serad_od_druheho, která zvířata seřadí podle abecedy, ale bude ignorovat první písmeno. Například:

>>> from moje_reseni import vytvor_seznam_zvirat, serad_od_druheho
>>> zvirata = vytvor_seznam_zvirat()
>>> serad_od_druheho(zvirata)
["had", "pes", "andulka", "kočka", "králík"]
>>> # (barvy jsou tu jen pro přehlednost, váš program vypisuje bez barev)
Máš tady seznam hodnot, které chceš seřadit podle nějakého klíče. Klíč se dá z každé hodnoty vypočítat – v našem případě je to hodnota kromě prvního písmenka (tedy od druhého písmenka dál).

Postup:

Vytvoř seznam dvojic (klíč, hodnota).
Seřaď tento seznam dvojic – dvojice se řadí nejdřív podle prvního prvku, pak druhého atd.
Nakonec vytvoř ze seznamu dvojic výsledný seznam hodnot.
Vytvoření seznamu se dělá tak, že začneš s prázdným seznamem a postupně do něj přidáváš hodnoty jednu po druhé."""

from seznam_zvirat import vytvor_seznam_zvirat


def serad_od_druheho(seznam):
    dvojice = []
    klice = []
    hodnoty = []
    obracene = []
    reseni = []
    spojene = []
    vysledek = []

    for prvni in seznam:
        hodnoty.append(prvni[1:])
        klice.append(prvni[0])
    dvojice = zip(hodnoty,klice)
    obracene = sorted(list(dvojice))
    klice = []
    hodnoty = []
    for prvni in list(obracene):
        hodnoty.append(prvni[0])
        klice.append(prvni[1])
    reseni = zip(klice,hodnoty)  
    reseni = (list(reseni))
    for cast in reseni:
        spojene = cast[0] + cast[1]
        vysledek.append(spojene)
    return print(vysledek)
    

zvirata = vytvor_seznam_zvirat()
serad_od_druheho(zvirata)
