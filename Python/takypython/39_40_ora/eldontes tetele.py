# van egy N elemu lista sorozat, a sorozatban vagy egy T= tulajdonsag. Az algoritmusom megadja nekem hogy van e a sorozatba, a listaban ilyen t tulajdonsagu elem.(igen vagy nem)

from operator import index

"""
lista = [2, 5, 4, 8, 19, 11, 10, 13]

talalat = False
index = 0

while index < len(lista) and not talalat:
    if lista[index] % 3 == 0:
        talalat = True
    index = index + 1
    
if talalat:
    print('Van a listában hárommal osztható szám.')
else:
    print('Nincs a listában hárommal osztható szám.')
"""
"""
Az KERESÉS esetében azt vizsgáljuk, 
    hogy szerepel-e egy bizonyos tulajdonságú elem az adatsorban (itt a listában),
    és ha igen, hányadik helyen.

    A program azt vizsgálja, hogy szerepel-e a piros szín a listában, és ha igen, hányadik helyen.
"""
lista = ['kék', 'zöld', 'piros', 'fehér']

talalat = False
index = 0
while index < len(lista) and not talalat:
	if lista[index] == 'piros':
		talalat = True
	index = index + 1

if talalat:
	print('Van a listában piros szín, az indexe: ', index-1)
else:
	print('Nincs a listában piros szín.')
  