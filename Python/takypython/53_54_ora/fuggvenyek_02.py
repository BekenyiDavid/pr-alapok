# Lower case the string:
"""
txt = "Hello my FRIENDS"

x = txt.lower()

print(x)
"""

# Upper case the string:
"""
txt = "Hello my FRIENDS"

x = txt.upper()

print(x)
"""

# Capitalz the first latter
"""
txt = "Hello my FRIENDS"

x = txt.capitalize()

print(x)
"""

# Check if the string ends with a punctuation sign (.):
"""
txt = "Hello, welcome to my world."

x = txt.endswith(".")

print(x)
"""

# Search for a word in the text:
"""
txt = "Hello, welcome to my world."

x = txt.find("welcome")

print(x)
"""

# Check if all the characters in the text are alphanumeric:
"""
txt = "Company12"

x = txt.isalnum()

print(x)
"""

# Check if all the characters in the text are letters:
"""
txt = "CompanyX"

x = txt.isalpha()

print(x)
"""

# Check if all the characters in the text are in lower case:
"""
txt = "hello world!"

x = txt.islower()

print(x)
"""
# Join all items in a tuple into a string, using a hash character as separator:
"""
myTuple = ("John", "Peter", "Vicky")

x = "#".join(myTuple)

print(x)
"""

# replace a word in a text
"""
txt = "I like bananas"

x = txt.replace("bananas", "apples")

print(x)
"""

#Where in the text is the last occurrence of the string "casa"?:
"""
txt = "Mi casa, su casa."

x = txt.rfind("casa")

print(x)
"""

#Remove any white spaces at the end of the string:
"""
txt = "     banana     "

x = txt.rstrip()

print("of all fruits", x, "is my favorite")
"""

#Check if the string starts with "Hello":
"""
txt = "Hello, welcome to my world."

x = txt.startswith("Hello")

print(x)
"""

# Remove spaces at the beginning and at the end of the string:
"""
txt = "     banana     "

x = txt.strip()

print("of all fruits", x, "is my favorite")
"""

# Make the lower case letters upper case and the upper case letters lower case:
"""
txt = "Hello My Name Is PETER"

x = txt.swapcase()

print(x)
"""

# Make the first letter in each word upper case:
"""
txt = "Welcome to my world"

x = txt.title()

print(x)
"""

#Print the word "banana", taking up the space of 20 characters, with "banana" in the middle:
"""
txt = "banana"

x = txt.center(20)

print(x)
"""