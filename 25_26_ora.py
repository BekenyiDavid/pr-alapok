"""
list = ["alma", "banan", "cseresznye"]
print(lista)
"""
################################
"""
list1 = ["alma", "banan", "cseresznye"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
"""
################################
"""
list = ["abc", 34, True, 40, "ferfi"]
print(lista)
"""
################################
"""
list = ["alma", "banan", "cseresznye"]
print(type(list))
"""
################################
"""
lista = list(("alma", "banan", "cseresznye"))
print(lista)
"""
################################
"""
list = ["alma", "banan", "cseresznye"]
print(list[1])
"""
################################
"""
list = ["alma", "banan", "cseresznye"]
print(list[-1])
"""
################################
"""
list = ["alma-0", "banan-1", "cseresznye-2", "narancs-3", "kivi-4", "szolo-5", "mango-6"]
print(list[2:5])
print(list[2:6])
"""
################################
"""
list = ["alma-0", "banan-1", "cseresznye-2", "narancs-3", "kivi-4", "szolo-5", "mango-6"]
print(list[:4])
"""
################################
"""
list = ["alma-0", "banan-1", "cseresznye-2", "narancs-3", "kivi-4", "szolo-5", "mango-6"]
print(list[2:])
"""
################################
"""
list = ["alma-0", "banan-1", "cseresznye-2", "narancs-3", "kivi-4", "szolo-5", "mango-6"]
print(list[-4:-1])
"""
################################
"""
list = ["alma-0", "banan-1", "cseresznye-2", "narancs-3", "kivi-4", "szolo-5", "mango-6"]
if "banan-1" in list:
    print("A banan bennevan a listaban")
"""
################################
"""
list = ["alma-0", "banan-1", "cseresznye-2", "narancs-3", "kivi-4", "szolo-5", "mango-6"]
if "banan" not in list:
    print("A banan nincs benne a listaban")
"""
################################
"""
list = ["alma", "banan", "cseresznye"]
list[1] = "kivi"
print(list)
"""
################################
"""
list = ["alma-0", "banan-1", "cseresznye-2", "narancs-3", "kivi-4", "szolo-5", "mango-6"]
list[1:3] = ["korte", "szilva"]
print(list)
"""
################################
"""
list = ["alma-0", "banan-1", "cseresznye-2", "narancs-3", "kivi-4", "szolo-5", "mango-6"]
list[1:3] = ["korte"]
print(list)
"""
################################
"""
list = ["alma-0", "banan-1", "cseresznye-2", "narancs-3", "kivi-4", "szolo-5", "mango-6"]
list.insert(2, "korte")
print(list)
"""
################################

list = ["alma", "banan", "cseresznye"]
list.append("korte")
print(list)