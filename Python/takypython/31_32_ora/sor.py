list = [7, 8, 6, 2, 15, 1, 13, 5, 9, 11, 12, 3, 4]
print(list)
lr = len(list)
for i in range(lr):
    for j in range(0, i):
        if list[j] > list[j+1]:
            tmp = list[j+1]
            list[j+1] = list[j]
            list[j] = tmp
    print(f"{list} i = {i} j = {j}")
