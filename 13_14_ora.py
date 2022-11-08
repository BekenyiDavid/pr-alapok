# 1 hoanpja ugyan az
"""
szam1 = int(input("kerek egy egesz szamot"))
szam2 = int(input("kerek egy masik szamot"))

if szam1 > szam2:
    print("Az elso szam nagyobb mint a masodik")

if szam1 < szam2:
    print("a masodik szam a nagyobb")

if szam1 == szam2:
    print("a ket szam megegyezik")
"""
# vegre valami "uj"
"""
szam1 = int(input("kerek egy egesz szamot"))
szam2 = int(input("kerek egy masik szamot"))

if szam1 > szam2:
    print("Az elso szam nagyobb mint a masodik")

elif szam1 < szam2:
    print("a masodik szam a nagyobb")

elif szam1 == szam2:
    print("a ket szam megegyezik")
"""

"""
szam1 = int(input("kerek egy egesz szamot"))
szam2 = int(input("kerek egy masik szamot"))

if szam1 > szam2:
    print("Az elso szam nagyobb mint a masodik")

elif szam1 < szam2:
    print("a masodik szam a nagyobb")

else:
    print("a ket szam megegyezik")
"""

"""
x = None
print(x)
print(type(x))

if x:
    print("do you think None is true?")
else x is False:
    print("do you think None is false?")
else:
    print("None is not true, or false, none is just none")
"""

"""
jegy = input("kerek egy osztalyzatot")

if jegy == "5":
    print("Jeles")
elif jegy == "4":
    print("jo")
elif jegy == "3":
    print("kozepes")
elif jegy == "2":
    print("elegseges")
elif jegy == "1":
    print("elegtelen")
else:
    print("Nem ervenyes osztalyzat")
"""
# na vajon  haladunk tovabb????
"""
szam = int(input("Egy pozitiv egesz szam"))

if szam % 2 == 0:
    print(" a szam paros")
else:
    print("a szam paratlan")
"""
#random
"""
import random

gondolt_szam = random.randint(1,6)
tipp = int(input("gondoltam egyszamra"))
if tipp == gondolt_szam:
    print("eltalaltad")
else:
    print("nem")
"""

import random
szam = random.randint(1,1001)

print(szam)

if szam <= 500 and not(szam % 2 == 0):
    print("suuuu")
else:
    print("a szam nem felel meg")