# d = {1: 2, 2: 4, 3: 9}
# print(d)
# e = d.copy()
# print(e)
# print(d.items())
# print(d.keys())
# print(d.popitem())
# print(d)
# d.pop(1)
# print(d)




# dict = {"Kazakhstan": "Oral", "Russia": "Volga", "Egypt": "Nile", "Brazil": "Amazon", "India": "Gang"}
#
# print("Введите сколько рек вы хотите проверить(на английском)")
# n = int(input())
# rivers = []
# i = 0
# while i < n:
#     river = str(input(f"Введите реку номер {i+1}",))
#     rivers.append(river)
#     i+=1
#
# for j in range(0, n):
#     t = ""
#     for key in dict:
#         if (dict[key].lower() == rivers[j].lower()):
#             t = "есть"
#             break
#         else:
#             t = "нет"
#     print(f"{rivers[j]}: {t}")
#
# dict["Uzbekistan"] = "Amudaria"
# print(dict.items())



# print("Введите ваши комментарии")
# comments = {}
# i = 0
# j = str(input(f"Комментатор№{i+1}",))
# comments[f"Комментатор№{i+1}"] = j
# i+=1
# while len(j) != 0:
#     comments[f"Комментатор№{i}"] = j
#     j = str(input(f"Комментатор№{i + 1}", ))
#     i+=1
#
# print(comments.items())
# print(len(comments))




# numbers = {}
#
# count_of_numbers = int(input("Сколько номеров вы хотите ввести?",))
#
# i = 0
#
# while i < count_of_numbers:
#     number = str(input(f"Введите номер телефона в формате: 88005553535 Имя №{i + 1}",))
#     value = number.split(" ")[0]
#     key = number.split(" ")[1]
#     numbers[key] = value
#     i+=1
#
# search = str(input(f"Введите имя номера который вы хотите найти:",))
#
# t = True
#
# for key in numbers:
#     t = True
#     if(key == search):
#         print(f"{search}: {numbers[key]}")
#         t = False
#         break
#
# if t == True:
#     print("Нет в телефонной книге")



n = int(input())

vacations = {}

for i in range(n):
    name, day, month = input().split()
    if month in vacations:
        vacations[month].append(name)
    else:
        vacations[month] = [name]

month = str(input())

dict = {
    "январь": "января",
    "февраль": "февраля",
    "март": "марта",
    "аперель": "апреля",
    "май": "мая",
    "июнь": "июня",
    "июль": "июля",
    "август": "августа",
    "сентябрь": "сентября",
    "октябрь": "октября",
    "ноябрь": "ноября",
    "декабрь": "декабря"
}
month = dict[month]
print(vacations)
if month in vacations:
    print(" ".join(vacations[month]))
else:
    print()
