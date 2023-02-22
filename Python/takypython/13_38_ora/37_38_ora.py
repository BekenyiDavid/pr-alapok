# szelsoertek meghazarozassa min max keresese (itt a listaban)
"""
lista = [12, 5, 4, 8, 9, 11, 10, 12, 6]

min = lista[0]
max = lista[0]

print(min(lista))
print(max(lista))

for szam in lista:
    if szam < min:
        min = szam
    if szam > max:
        max = szam

print(f"a legkisebb szam a listaban {min}")
print(f"a legnagybb szam a listaban {max}")
"""
"""
lista = [12, 5, 4, 8, 9, 11, 10, 12, 6]

def szelsoertek_10c():
    min = lista[0]
    max = lista[0]

    for szam in lista:
        if szam < min:
            min = szam
        if szam > max:
            max = szam

    print(f"a legkisebb szam a listaban {min}")
    print(f"a legnagybb szam a listaban {max}")

szelsoertek_10c()
"""

lista = [12, 5, 4, 8, 9, 11, 10, 12, 6]

def szelsoertek_10c(munkalista):

    min = munkalista[0]
    max = munkalista[0]

    for szam in munkalista:
        if szam < min:
            min = szam
        if szam > max:
            max = szam

    print(f"a legkisebb szam a listaban {min}")
    print(f"a legnagybb szam a listaban {max}")

szelsoertek_10c(lista)