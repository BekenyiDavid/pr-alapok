# utalom a ciagynokat
"""
idei_ev = 2022
print(type(idei_ev))
print("az ide ev:" , idei_ev, sep="--->")
felhasznalo_kora = input("hany eves vagy?")
print(type(felhasznalo_kora))
print("te most", felhasznalo_kora, "eves vagy.")
felhasznalo_kora = int(felhasznalo_kora)
szuletesi_ev = idei_ev - felhasznalo_kora
print("ekkor szulettel:", szuletesi_ev, ".", sep="")
"""
# meg azt5 mogyak hogy nincsen ciganybaró
from pickletools import read_int4

gondolt_szam = 4
tipp= input("gondoltam egy szamra. Tippeld meg! ")
tipp = int(tipp)
if tipp == gondolt_szam:
    print("ciganykiraj")
if tipp <= gondolt_szam:
    print("nagyobb")
if tipp >= gondolt_szam:
    print("kisebb")