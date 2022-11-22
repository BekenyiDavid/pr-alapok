""""
print("Hello")
print('Hello')


a = "Hello"
print(a)
"""
#################################################
"""
a = ""Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.""
print(a)
"""
#################################################
"""
a = "Hello, World!"
print(a[a])
print(a[12])

#a
# b =10
# b
"""
#################################################
"""
a = "hello world!asdfsdgake"


print(a[len(a)-1])
print("VEGE")
print("az utolso", len(a)-1)
"""
#################################################
"""
for x in "banana":

  print(x)

for x in "banana":

  print(x,end='')
"""
#################################################
"""
a = "abcdefghijklmnop"

szamlalo = 1
for x in a:
    if szamlalo % 2 == 0:
        print(a[szamlalo-1], end="")
    szamlalo = szamlalo+1
"""
#################################################
"""
a = "Hello, World!"

print(len(a))


txt = "The best things in life are freae!"

print("free" in txt)
"""
#################################################
"""
txt = "The best things in life are free!"

if "expensive" not in txt:

  print("No, 'expensive' is NOT present.")
"""
#################################################
"""
b = "Hello, World!"

print(b[2:5])
"""
#################################################
"""
b = "Hello, World!"

print(b[:5])
"""
#################################################
"""
b = "hello, world"

print(b[1:5])
"""
#################################################
"""
c = "H" +b[1:5]
print(c)
"""
#################################################
"""
b = "Hello, World!"

print(b[2:])
"""
#################################################
"""
b = "Hello, World!"

print(b[-5:-2]) # orl
"""
#################################################ű
"""
a = "Hello, World!"

print(a.upper())
"""
#################################################
"""
a =" Hello world!"
nagybetu = a.upper()

print(nagybetu)
"""
#################################################
"""
a = "Hello, World!"

print(a.lower())
"""
#################################################
"""
a = " Hello, World! "
b = a.strip()

a.strip()
print(len(b))
"""
#################################################
"""
a = "Jello, World!"

print(a.replace("J", "H"))
"""
#################################################
"""
a = "Hello, World!, alma, a, fa, alatt, nyari, piros, almaaaaa"

print(a.split(","))
lista = a.split(",")
print(lista[7])
"""
#################################################
"""
a = "44;341;223;333;54544"
a.split(";")
lista = a.split(";")
print(lista[3])
"""
#################################################
"""
a = "Hello"
b = "World"
c = a + b
print(c)
"""
#################################################
"""
age = 36
txt = "My name is John, I am " + age
print(txt)
"""
#################################################
"""
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."

print(myorder.format(quantity, itemno, price))
"""
#################################################
"""
txt = "We are the so-called \"Vikings\" from the north."
print(txt)
"""
#################################################
"""
print("almaafaalatt", end="\n\n\n")
print("íbfiab",  end="\t")
print("dfaBFADBA")
"""
#################################################
"""
szam = 0
while szam != 100:
  szam += 1
  print(szam)
"""
#################################################

szam = 0
while True:
    szam += 1
    print(szam)
