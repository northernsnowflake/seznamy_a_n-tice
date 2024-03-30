"""
Napiš funkci, která dostane seznam souřadnic (párů čísel menších než 10, která určují sloupec a řádek), a vypíše je jako mapu: mřížku 10×10, kde na políčka která jsou v seznamu napíše X, jinde tečku. Například:

nakresli_mapu([(0, 0), (1, 0), (2, 2), (4, 3), (8, 9), (8, 9)])

X . . . . . . . . .
X . . . . . . . . .
. . X . . . . . . .
. . . . . . . . . .
. . . X . . . . . .
. . . . . . . . . .
. . . . . . . . . .
. . . . . . . . . .
. . . . . . . . . X
. . . . . . . . . .
Jak na to?

Vzpomeň si, jak se vypisuje tabulka: pomocí dvou cyklů for zanořených do sebe.
Pro každou buňku tabulky (tedy vevnitř v cyklu) si vytvoř dvojici radek_a_sloupec = (cislo_radku, cislo_sloupce).
Napiš X, pokud je dvojice radek_a_sloupec v seznamu. Jinak napiš ..
Slova jako „souřadice“ a „pozice“ bohužel vypadají v jednotném i množném čísle stejně. Aby ses nezamotala, doporučuju proměnnou s jednou dvojicí pojmenovat radek_a_sloupec a seznam několika takových dvojic seznam_souradnic.

"""
"""Napiš funkci pohyb, která dostane seznam souřadnic a světovou stranu ("s", "j", "v" nebo "z"), a přidá k seznamu poslední bod „posunutý“ v daném směru. Např.:

seznam_souradnic = [(0, 0)]
pohyb(seznam_souradnic, 'j')
print(seznam_souradnic)         # → [(0, 0), (1, 0)]
pohyb(seznam_souradnic, 'j')
print(seznam_souradnic)         # → [(0, 0), (1, 0), (2, 0)]
pohyb(seznam_souradnic, 'v')
print(seznam_souradnic)         # → [(0, 0), (1, 0), (2, 0), (2, 1)]
pohyb(seznam_souradnic, 'z')
print(seznam_souradnic)         # → [(0, 0), (1, 0), (2, 0), (2, 1), (2, 0)]
Funkce by neměla nic vracet. Jen mění už existující seznam.
"""

"""
Doplň funkci pohyb tak, aby při pohybu umazala první bod ze seznamu souřadnic. Výsledný seznam tak bude mít stejnou délku jako před voláním.

Jestli hraješ počítačové hry a víte co je WASD, můžeš změnit ovládání na tyto klávesy místo SZJV.
"""

"""
Teď máš hotový základ hry "Had"! Zkus si s ní chvíli hrát.
Pak přidej do hry hadí potravu.
Seznam jídla obsahuje na začátku dvě jídla na políčkách, na kterých není had (například: jidlo = [(2, 3), (4, 5)] znamená jedno jídlo na pozici (2, 3) a druhé na (4, 5)). Když had sežere jídlo, vyroste 
(„nesmaže“ se mu ocas, tedy neprovede se to, co jsi přidali v předminulém úkolu) a na náhodném místě (kde není had) se přidá jídlo nové.
Na mapě se jídlo zobrazuje třeba jako otazník (?).
"""

"""Napiš cyklus, který se bude ptát uživatele na světovou stranu, 
podle ní zavolá pohyb, a následně vykreslí seznam jako mapu. Pak se opět se zeptá na stranu atd.

Začínej se seznamem [(0, 0), (0, 1), (0, 2)].
"""
import random
VELIKOST = 10


def nakresli_mapu(seznam_souradnic, jidlo):
    dvojice = []
    for x in range(VELIKOST):
        for y in range(VELIKOST):
            dvojice = x,y
            if dvojice in jidlo:
                print('?',end=' ')
            elif dvojice in seznam_souradnic:
                print('X',end=' ')
            else:
                print('.',end=' ')
        print('')
    return()

def pohyb(seznam_souradnic,svetova_strana,jidlo):
    seznam = ["w", "s", "d", "a"]
    pozice = []
    dvojice = []
    n = seznam_souradnic[-1][0] #takes first element of last tuple in list 
    m = seznam_souradnic[-1][1] #takes second element of last tuple in list 
    if svetova_strana == 's':
        seznam_souradnic.append((n+1,m))
    elif svetova_strana == 'd':
        seznam_souradnic.append((n,m+1))
    elif svetova_strana == 'a':
        seznam_souradnic.append((n,m-1))
    elif svetova_strana == 'w':
        seznam_souradnic.append((n-1,m))
    else:
        print('Vyber jiné písmeno - w,s,a,d')
        return

    vpravo = seznam_souradnic[-1][1] >= VELIKOST
    vlevo = seznam_souradnic[-1][1] < 0
    nahoru = seznam_souradnic[-1][0] < 0
    dolu = seznam_souradnic[-1][0] >= VELIKOST

    if dolu or vpravo or nahoru or vlevo:
         raise ValueError('Game Over')

    
    #had narazí sám do sebe
    if seznam_souradnic[-1] in seznam_souradnic[:-1]:
         raise ValueError('Game Over')
    #jídlo
    if seznam_souradnic[-1] in jidlo:
        pocitadlo = 0
        for prvek in jidlo:
            if prvek == seznam_souradnic[-1]:
                del jidlo[pocitadlo]
                pridej_jidlo(jidlo)
            pocitadlo += 1
    else:
        del seznam_souradnic[0]
    return

def pridej_jidlo(jidlo):
    x = random.randrange(VELIKOST)
    y = random.randrange(VELIKOST)
    while (y,x) in jidlo or (y,x) in seznam_souradnic:
        x = random.randrange(VELIKOST)
        y = random.randrange(VELIKOST)
    jidlo.append((y,x))


seznam_souradnic = [(0,0),(1,0),(2,0),(2,1)]
jidlo = [(2,3), (1,3)]
while True:
     svetova_strana = str(input('Na jakou světovou stranu půjdeme? '))
     pohyb(seznam_souradnic, svetova_strana, jidlo)
     nakresli_mapu(seznam_souradnic,jidlo)