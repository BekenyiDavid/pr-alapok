bloggers = []

def beolvas():
    f = open("Meta/Block.txt", "r")
    i = 0
    f.readline()
    while i < 5:
        bloggers.append(f.readline())
        i += 1
    f.close()
    

    def kiirat():
        for x in bloggers:
            print(x)
        print(f"A lista {i-1} soros")
    kiirat()

def age():
    ages = []
    for item in bloggers:
        x = item.split(";")
        ages.append(x[2])

    sum = 0
    rep = 0
    for x in ages:
        sum = sum + int(x)
        rep += 1

    atlag = sum / rep
    print(f"Az eletkorok atlaga: {atlag}")


def szelsoert():
    ages = []
    for item in bloggers:
        x = item.split(";")
        ages.append(x[2])

    kis = min(ages)
    nagy = max(ages)
    print(f"A legfiatalabb {kis} eves")
    print(f"A legidosebb {nagy} eves")

def story():
    for item in bloggers:
        x = item.split(";")
        if x[3] == "":
            print("VAN")

def harom():
    for item in bloggers:
        x = item.split(";")
        if x[0] > "3":
            print(x[3])

beolvas()
age()
szelsoert()
story()
harom()