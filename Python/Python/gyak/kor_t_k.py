import random

kor_01 = range(5, (2, 6))

    # objektum tesztelése
print(kor_01)
print(type(kor_01))
print(isinstance(kor_01, range))

    # terulet nevű metódus hívása
print(kor_01.terulet())
  

korok = []
for _ in range(5):
    kor = range(random.randint(0, 10))
    korok.append(kor)

for kor in korok:
    kor.info()
    
print(kor_01.terulet())