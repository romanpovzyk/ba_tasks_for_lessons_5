import random

i = 0
list1 = []
list2 = []

while i < 10:
    number1 = random.randint(0, 10)
    list1.append(number1)
    number2 = random.randint(0, 10)
    list2.append(number2)
    i += 1

print(f"У першому списку — {list1}\n"
      f"У другому списку — {list2}\n"
      f"Спільні числа у них — {set(list1).intersection(list2)}")