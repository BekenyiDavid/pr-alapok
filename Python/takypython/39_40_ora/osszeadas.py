"""
szamoklista = [3, 21, 7, 63, 9, 27]
print(max(szamoklista))
print(min(szamoklista))
"""
"""
szamoklista = [3, 21, 7, 63, 9, 27]

def szelsoertek():
    min = szamoklista[0]
    max = szamoklista[0]

    for szam in szamoklista:
        if szam < min:
            min = szam
        if szam > max:
            max = szam

    print(f"A legkisebb szam a {min}")
    print(f"A legnagyobb szam {max}")
szelsoertek()
"""

#osszegzes tetele van 1 sorozat ez a sorozat egy lista es kivamycsiak vagyunk hogy kiszamolja a sorozat osszeget
"""
szamoklista = [3, 21, 7, 63, 9, 27]

osszeg = 0

for reszosszeg in szamoklista:
    osszeg = osszeg + reszosszeg

print(osszeg) 
"""

# A lista elemeinek atlaganak kiszamitasa
"""
szamoklista = [3, 21, 7, 63, 9, 27]
atlag = None
osszeg= 0
hossz = len(szamoklista)
for reszosszeg in szamoklista:
    osszeg = osszeg + reszosszeg

atlag = osszeg / hossz
print(f"Az lista atlaga : {atlag}")
"""
