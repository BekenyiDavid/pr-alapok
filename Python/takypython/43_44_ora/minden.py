def osszegzes():
    napi_ertekesitesek = [3, 12, 3, 4, 7, 15, 1]

    osszesen = 0
    for ertekesites in napi_ertekesitesek:
	      osszesen = osszesen + ertekesites

    print("A héten ennyi értékesítés történt: ", osszesen)

def eldontes():
    lista = [2, 5, 4, 8, 9, 11, 10, 12]
    
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

def kereses():
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

def kivalasztas():
    lista = [2, 5, 4, 8, 9, 11, 10, 12]

    talalat = False
    index = 0
    while not talalat:
	      if lista[index] % 3 == 0:
		        talalat = True
	      index = index + 1

    print('A hárommal osztható szám indexe a listában: ', index-1)

def szamlalas():
    lista = [12, 5, 4, 8, 9, 11, 10, 12, 6]

    darab = 0
    for szam in lista:
	      if szam % 3 == 0:
		        darab = darab + 1

    print('A listában lévő hárommal osztható számok száma: ', darab)

def szelso():
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

print("1 = osszegzes")
print("2 = eldontes")
print("3 = kereses")
print("4 = kivalaszt")
print("5 = szamlal")
print("6 = szelso")
print("0 = STOP")

valasz = None

while valasz != range(0,6):
    valasz = int(input("mit szeretnel vegrehajtani"))
    if valasz == 1:
        osszegzes()
        break
    elif valasz == 2:
        eldontes()
        break
    elif valasz == 3:
        kereses()
        break
    elif valasz == 4:
        kivalasztas()
        break
    elif valasz == 5:
        szamlalas()
        break
    elif valasz == 6:
        szelso()
        break
    elif valasz == 0:
        print("programvege")
