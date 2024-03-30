"""Úkol na procvičení a vzpomenutí. Už jsi ho jednou vyřešila.

Pomocí cyklů for a parametru end pro print napiš program, který postupně z jednotlivých 'X' vypíše:

X X X X X
X X X X X
X X X X X
X X X X X
X X X X X
„Z jednotlivých 'X'“ znamená, že každý print vypíše jen jedno X. Nepoužívej tedy např. print('X X X X X') ani print('X ' * 5).
"""
for r in range(5):
     for s in range(5):
         print('X', end=' ') #end za sebe
     print('') # vytiskne nový řádek po každém průběhu vnitřní funkce

"""
Úkol na procvičení a vzpomenutí. Už jsi ho jednou vyřešila.

Napiš program, který vypíše „tabulku“ s násobilkou.
0 0 0 0 0
0 1 2 3 4
0 2 4 6 8
0 3 6 9 12
0 4 8 12 16

"""
for r in range(5):
     for s in range(5):
         print(r*s, end=' ') #end za sebe
     print('') # vytiskne nový řádek po každém průběhu vnitřní funkce

