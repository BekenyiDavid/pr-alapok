#1.1
"""
szo = str(input("szo: "))

print(szo.upper())
"""
#1.2
"""
list = ["alma", 'korte', "barack"]

list2 = [szo.upper() for szo in list]

print(list)
print(list2)
"""
#1.3
"""
list = ["alma", 'korte', "barack"]

list2 = [szo.upper() for szo in list if len(szo) > 3]

print(list)
print(list2)
"""

#1.4
"""
list = ['alma', 'korte', 'barack']

list2 = [szo.swapcase() for szo in list]

print(list)
print(list2)
"""
#2.1
"""
et = list(range(-3, 5))

ek = [2 * x - 3 for x in et]

print('Ertelemzesi tartomany:', et)
print('Ertek keszlet:', ek)
"""
#2.2
"""
et = list(range(-3, 5))

ek = [2 * x - 3 for x in et if x >= 0]

print('Ertelemzesi tartomany:', et)
print('Ertek keszlet:', ek)
"""
####################################
#1.1
"""
paletta = ['kék', 'piros', 'fehér', 'fekete', 'zöld', 'sárga', 'barna', 'piros', 'fehér', 'szürke']

szin = input('Adj meg egy színt!\t')
if szin in paletta:
	print('A megadott szín szerepel a listában.')
else:
	print('A megadott szín nem szerepel a listában.')

print('A lista színei:')
for szin in paletta:
	print(szin, end=', ')
"""
#1.2
"""
paletta = ['kék', 'piros', 'fehér', 'fekete', 'zöld', 'sárga', 'barna', 'piros', 'fehér', 'szürke']

szin = input('Adj meg egy színt!\t')
if szin in paletta:
    print('A', szin, len([arnyalat for arnyalat in paletta if arnyalat == szin]), '-szer/szor szerepel a listában:', ', '.join(paletta))
else:
	print('A megadott szín nem szerepel a listában.')

print('A lista színei:')
for szin in paletta:
	print(szin, end=', ')
"""

