from random import randint
from random import randrange

# list1 = []
#
# length = int(input("Введите размер листа ", ))
#
# i = 0
#
# while (i < length):
#     print(f"Элемент №{i + 1}")
#     list1.append(int(input( )))
#     i+=1
#
# list2 = lst = [randint(-50, 50) for _ in range(randrange(10, 20))]
# print(list2)
# for i in enumerate(list1):
#     print(i)
#
# for i in range(1, 20, 5):
#     print(i)

# print(f"Первая задача")
#
# a = int(input("Введите A ",))
# b = int(input("Введите B ",))
#
# while (a > b):
#     print(f"А должно быть меньше или равно В")
#     a = int(input("Введите A ", ))
#     b = int(input("Введите B ", ))
#
# for i in range(a, b + 1):
#     print(i)

# print(f"Вторая задача")
#
# a = int(input("Введите A ",))
# b = int(input("Введите B ",))
#
# if (a < b):
#     for i in range(a, b + 1):
#         print(i)
# else:
#     for i in range(a, b + 1, -1):
#         print(i)

print(f"Третья задача")

a = int(input("Введите A ",))
b = int(input("Введите B ",))

while (a <= b):
    print(f"А должно быть больше В")
    a = int(input("Введите A ", ))
    b = int(input("Введите B ", ))
d = a % 2 + a + 1
for i in range(d - 2, b - 1, -2):
    print(i)

# print(f"Четвертая задача")
#
# n = int(input("Введите количество карт ",))
# expectedSum = (n + 1) * n // 2
# actualSum = 0
# for i in range(n - 1):
#     actualSum += int(input())
# print(f"Пропущенное число это {expectedSum - actualSum}")