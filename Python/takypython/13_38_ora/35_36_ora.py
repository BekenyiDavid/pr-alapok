"""
napi_ertekesitesek = [3, 12, 3, 4, 7, 15, 1]

osszesen = 0
for ertekesites in napi_ertekesitesek:
      osszesen = osszesen + ertekesites

print("A héten ennyi értékesítés történt: ", osszesen)

# --------------------------------------------------------------------------

print('Ez a program kiszámolja az átlagodat.')
print('Ha már nem akarsz több jegyet megadni, írj 0-át!')
print('--------------------------------------------')

darab = 0
osszeg = 0

erdemjegy = int(input('Add meg az első érdemjegyet: '))
while erdemjegy != 0:
      darab = darab + 1
      osszeg = osszeg + erdemjegy
      erdemjegy = int(input('Add meg az következő érdemjegyet: '))

if darab != 0:
      print('A jegyeid átlaga: ', osszeg / darab)
else:
      print('Nem adtál meg egy jegyet sem!')






'''
A SZÉLSŐÉRTÉK MEGHATÁROZÁSA esetében azt vizsgáljuk, hogy melyik a legkisebb, 
illetve a legnagyobb érték az adatsorban (itt a listában).
'''
lista = [12, 5, 4, 8, 9, 11, 10, 12, 6]

min = lista[0]
max = lista[0]
for szam in lista:
      if szam < min:
            min = szam
      if szam > max:
            max = szam

print('A legkisebb szám a listában: ', min)
print('A legnagyobb szám a listában: ', max)  

# -----------------------------------------------------------------------------------

'''
A SZÉLSŐÉRTÉK MEGHATÁROZÁSA esetében azt vizsgáljuk, hogy melyik a legkisebb, illetve a legnagyobb érték az adatsorban (itt a listában).
'''
lista = [12, 5, 4, 8, 9, 11, 10, 12, 6]

min = lista[0]
max = lista[0]
for szam in lista:
	if szam < min:
		min = szam
	if szam > max:
		max = szam

print('A legkisebb szám a listában: ', min)
print('A legnagyobb szám a listában: ', max)
"""

###########################&##########

r_lista = (6,5,3,1,8,7,9)
print(r_lista)
def buborekrend()