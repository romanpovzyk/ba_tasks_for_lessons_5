import random

i = 0
max = 0
list = []

while i < 10:
    number = random.randint(0, 100)
    list.append(number)
    print(f"№{i} у цьому списку — {list[i]}")
    if max < list[i]:
        max = list[i]
    i += 1

print(f"Найбільше число у цьому списку — {max}")