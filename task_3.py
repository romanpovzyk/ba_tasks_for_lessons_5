i = 0
list1 = []
list2 = []

while i < 100:
    list1.append(i+1)
    if (i + 1) % 7 == 0 and (i + 1) % 5 != 0:
        list2.append(i + 1)
    i += 1

print(list2)