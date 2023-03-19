# a = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
# b = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
# print(len(a))
# print("Конкатенация (сложение строк)")
# a = a + b
# print(len(a))
# print("Повторение строки")
# a = a * 3
# print(len(a))
# print("Обращение по индексу")
# print(a[10])
# print("Извлечение среза")
# print(a[20: 55: 3])
# print("Длина строки")
# print(len(a))
# print("Поиск подстроки в строке. Возвращает номер первого вхождения или -1")
# print(a.find("sed do eiusmod tempor", 0, -1))
# print("Поиск подстроки в строке. Возвращает номер последнего вхождения или -1")
# print(a.rfind("sed do eiusmod tempor", 0, -1))
# print("Замена шаблона на замену. maxcount ограничивает количество замен")
# print(a.replace("sed do eiusmod tempor", "замена"))
# print("Разбиение строки по разделителю")
# a = a.split(" ")
# print(a)
# print("Сборка строки из списка с разделителем S")
# a = " ".join(a)
# print(a)



# class school_student:
#   def __init__(self, name, clas):
#     self.name = name
#     self.clas = clas
#
# school_students = []
# count_of_students = int(input("Сколько учащихся вы хотите добавить",))
#
# i = 0
#
# while(i < count_of_students):
#   name = str(input(f"Имя ученика №{i + 1}",))
#   clas = int(input(f"Класс ученика №{i + 1}",))
#   newStudent = school_student(name, clas)
#   school_students.append(newStudent)
#   i+=1
#
# school_students.sort(key=lambda x: x.clas)
# for student in school_students:
#     print(f"Имя учащегося {student.name}")  # Вывод имени студента
#     print(f"Класс учащегося {student.clas}")  # Вывод возраста студента
#     print(f"\n")



# a = str(input("Введите строку",))
# b = "".join(a.split(" "))
# low = 0
# high = 0
#
# for i in range(0, len(b)):
#   if(b[i].islower()):
#     low +=1
#   else:
#     high+=1
#
# if(low >= high):
#   a = a.lower()
# else:
#   a = a.upper();
#
# print(a)



# a = str(input("Введите первое число",))
# b = str(input("Введите второе число",))
#
# while(not a.isdigit() or not b.isdigit()):
#   a = str(input("Введите первое число", ))
#   b = str(input("Введите второе число", ))
#
# print(int(a) + int(b))
