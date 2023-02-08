szam1 = int(input("Kerem az elso szomot 1-100 kozott"))
szam2 = int(input("Kerem az elso szomot 1-100 kozott"))

kulonbseg1 = szam1 - szam2
kulonbseg2 = szam2 - szam1

if szam1 == szam2 :
    print("A két szam megegyezik")

if szam1 != szam2:
    print("Nem egyezik!")

if szam1 > szam2:
    print(szam1,  "a nagyobb", kulonbseg1, "-al/el" )
    
if szam1 < szam2:
    print(szam2,  "a nagyobb", kulonbseg2, "-al/el" )