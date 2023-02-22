"""
szam = int(input("5-10 kozoztt"))
while not 5 <= szam <= 10:
    szam = int(input("helytelen eretek, megegyszer"))

print("rendben")
"""
################################
"""
szam = int(input("5-10 kozoztt"))

while not 5 <= szam <= 10:
    szam = int(input("helytelen eretek, megegyszer"))
    if szam % 2 == 0:
        print("rendben")
"""
################################

szo = None
szoveg = ""
while szo != "":
    szo = input("Adj meg szavakat, kilepes ENTER")
print(szo+szoveg)
print("VEGE")