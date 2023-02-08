nev = input("kereszt nev: ")
kor = int(input("hany eves vagy: "))

if kor < 1:
    print(f"Keresztneve: {nev} \nA kora alapjan {kor} {nev} csecse mo" )

elif kor < 6:
    print(f"Keresztneve: {nev} \nA kora alapjan {kor} {nev} puja" )

elif kor < 12:
    print(f"Keresztneve: {nev} \nA kora alapjan {kor} {nev} puja" )

elif kor < 16:
    print(f"Keresztneve: {nev} \nA kora alapjan {kor} {nev} puja+" )

elif kor < 25:
    print(f"Keresztneve: {nev} \nA kora alapjan {kor} {nev} pujaro" )

elif kor < 65:
    print(f"Keresztneve: {nev} \nA kora alapjan {kor} {nev} cosanostra" )

else:
    print(f"Keresztneve: {nev} \nA kora alapjan {kor} {nev} nyugger" )