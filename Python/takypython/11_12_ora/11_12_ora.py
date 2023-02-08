#feladat1
""""
gondolt_szam = 4
tipp= int(input("gondoltam egy szamra. Tippeld meg! "))
if tipp == gondolt_szam:
    print("SUUWI")
print("pápá")
"""
#feladat2
"""
gondolt_szam = 4
tipp = int(input("Gondoltam egy szamra. Tippeld meg!"))

if tipp == gondolt_szam:
    print("Ugyes!")
    print("Grat")
else:
    print("Hosszan gondolgoztal rajta?")
    print("Nem erte meg.")
print("Papa")
"""

from xml.sax import SAXNotRecognizedException


szam1 = int(input("Kerek egy sazmot!"))
szam2 = int(input("Kereke egy masik szamot!"))

if szam1 == szam2:
    print("A ket szam megegyezik")

if szam1 != szam2:
    print("A ket szam kuolonbozo")
if szam1 < szam2 :
    print("Az elso szam a kisebb")
if szam1 >= szam2:
    print("nagyobb vagy egyenlo")
print("Program vege")