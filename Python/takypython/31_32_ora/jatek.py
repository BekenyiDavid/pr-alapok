import random
szam = random.randrange(0, 5)
e = 5
tip = int(input("szamot: "))

while e == 0:
    
    if tip > szam:
        print("kisebb")
        e -= 1
        continue

    elif tip < szam:
        print("nagyobb")
        e -= 1
        continue

    else:
        print("kys")
        break