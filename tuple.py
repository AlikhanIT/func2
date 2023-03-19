import random

# my_tuple = ('adwise', 'english', 'somesay', 'algs', 'rmp', 'int', 'test')
#
# for word in my_tuple:
#     print(word)
#
# print("\n")
#
# my_sorted_tuple = sorted(my_tuple)
#
# for word in my_sorted_tuple:
#     print(word)
#
# print(my_tuple[0:3])
#
# print(len(my_tuple[0:3]))
# print(my_tuple.index("algs"))
# print(my_sorted_tuple.index("algs"))
#
# del my_tuple




# test = []
# test2 = []
# for i in range(0, 10):
#     test.append(random.randint(0,5))
#     test2.append(random.randint(-5,0))
#
# first_tuple = tuple(test)
# second_tuple = tuple(test2)
#
# print(first_tuple)
# print(second_tuple)
#
# third_tuple = first_tuple + second_tuple
#
# print(third_tuple)
# print(third_tuple.count(0))



# tuple = (42, (3.14, (1 + 2j, ('Hello world!', ()))) )
# print(tuple[1][1][0])



# categories = ["Транспорт", "Еда"]
#
# expenses = {}
#
# days = ["Понедельник", "Вторник"]
#
# for category in categories:
#     expenses[category] = []
#     print(f"Введите затраты для категории '{category}', для дня недели:")
#     for day in days:
#         expense = float(input(f"{day}: "))
#         expenses[category].append(expense)
#
# print(expenses)
# i = 0
# for day in days:
#     sum = 0
#     for category in categories:
#         sum += expenses[category][i]
#     print(f"{day}: {sum}")
#     i+=1



i = 0
students = []

while i < 3:
    students.append(str(input(f"Введите фамилию студента номер {i+1}",)))
    i+=1

students_tuple = tuple(students)

for word in students_tuple:
    if "ов" in str(word):
        print(word)