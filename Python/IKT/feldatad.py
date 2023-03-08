employers = []

def beolvas():
    f = open("Meta/nevek.txt", "r")
    i = 0
    while i < 8:
        employers.append(f.readline())
        i += 1
    f.close()
    
def jogsi():
    for item in employers:
        x = item.split(";")
        if x[0] == "true":
            print(x[0])

def harminc():
    for item in employers:
        x =item.split(";")
        if x[0] > "30":
            print(x[0])

def dolgozonagy():
    for item in employers:
        x = item.split(";")
        if x[0][0].isupper():
            print(x[0])

def dolgozok():
    for item in employers:
        print(item)

def felvetel():
    file = open("Meta/nevek.txt", "a")
    file.writelines("\nHock;38;true;")
    file.close

def fajlkiiras():
    file = open("Meta/writenames.txt", "w")
    file.writelines(employers)
    file.close()

def nevszam():
    print(len(employers))

beolvas()
jogsi()
harminc()
dolgozonagy()
dolgozok()
felvetel()
fajlkiiras()
nevszam()
