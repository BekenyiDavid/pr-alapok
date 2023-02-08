print('Ez a program kiszámolja az átlagodat.')
print('Ha már nem akarsz több jegyet megadni, írj 0-át!')
print('--------------------------------------------')

darab = 0
osszeg = 0

erdemjegy = int(input('Add meg az első érdemjegyet: '))

while erdemjegy != 0:
    darab = darab + 1
    osszeg = osszeg + erdemjegy
    erdemjegy = int(input("Add meg a kovetkezo erdemjegyet!!!!!!!!!!"))

if darab != 0:
    print(f"A jegyeid atlaga : {osszeg / darab}")
else:
    print("Nem adtal meg egy jegyet sem!")