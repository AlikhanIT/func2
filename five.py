import random
import math


# class school_student:
#   def __init__(self, name, subject):
#     self.name = name
#     self.subject = subject
#
# school_students = []
# count_of_students = int(input("Сколько учащихся вы хотите добавить",))
#
# i = 0
#
# while(i < count_of_students):
#   name = str(input(f"Имя ученика №{i + 1}",))
#   subject = str(input(f"Предмет ученика №{i + 1}",))
#   newStudent = school_student(name, subject)
#   school_students.append(newStudent)
#   i+=1
#
# school_students.sort(key=lambda x: x.name)
# subjects = []
# for student in school_students:
#     if(student.subject not in subjects):
#         subjects.append(student.subject)
#
# print("\n")
#
# for sub in subjects:
#     print(sub, end=" ")
#     for student in school_students:
#         if(student.subject == sub):
#             print(student.name, end=" ")
#     print("\n")





# class school_student:
#   def __init__(self, name, subject, grades):
#     self.name = name
#     self.subject = subject
#     self.grades = grades
#
# school_students = [
#   school_student("Alikhan", ["Math", "Science", "Russian", "Algorhytms"], [100,100,100,100]),
#   school_student("Darina", ["Math", "Science", "Russian", "Algorhytms"], [90,90,90,90]),
#   school_student("Ernur", ["Math", "Science", "Russian", "Algorhytms"], [80,80,80,80]),
#   school_student("Dias", ["Math", "Science", "Russian", "Algorhytms"], [70,70,70,70]),
#   school_student("Elaman", ["Math", "Science", "Russian", "Algorhytms"], [60,60,60,60])
# ]
# count_of_students = len(school_students)
# i = 0
#
# school_students.sort(key=lambda x: x.name)
#
# while(i < count_of_students):
#   print(f"№{i+1} {school_students[i].name}")
#   i+=1
#
# selectedSubject = int(input(("Выберите ученика которого хотите увидеть"),))
#
# print("\n")
#
# print(school_students[selectedSubject - 1].name)
# print("\n")
# for i in range(0, len(school_students[selectedSubject - 1].subject)):
#   print(school_students[selectedSubject - 1].subject[i], end=" ")
#   print(school_students[selectedSubject - 1].grades[i])





# intput = int(input(("Введите значение листа"),))
# list_of_digits = []
#
# while(intput != 0):
#   list_of_digits.append(intput)
#   intput = int(input(("Введите значение листа"), ))
#
# list_of_digits.sort(reverse=True)
#
# for digit in list_of_digits:
#   print(digit)






winTicket = []

i = 0

while(i < 6):
  winTicket.append(random.randint(1, 49))
  i = i + 1

winTicket.sort()

winTicket = "".join(str(x) for x in winTicket)

print(f"Выиграшный билет {winTicket}")
print("\n")
print("\n")
print("\n")

my_ticket = []
ticket_count = 0

while(my_ticket != winTicket):
  my_ticket = []
  i = 0

  while (i < 6):
    my_ticket.append(random.randint(1, 49))
    i = i + 1

  my_ticket.sort()

  my_ticket = "".join(str(x) for x in my_ticket)
  print(f"Мой билет {my_ticket}")
  print("\n")
  ticket_count = ticket_count + 1

print("Выигрышный билет и твой совпали")
print(f"Выигрышный билет {winTicket}")
print(f"Tвой совпали {my_ticket}")
print(f"Было разыграно {ticket_count} билетов")
print(f"Ваш шанс победы составил {((1 / ticket_count) * 100)} процентов")





# def isSorted(array, sorts, sortsReversed):
#   length = len(array)
#
#   coin = 0
#
#   for i in range(0, length):
#     if array[i] == sorts[i]:
#       coin = coin + 1
#
#   if coin == 6:
#     return True
#
#   for i in range(0, length):
#     if array[i] == sortsReversed[i]:
#       coin = coin + 1
#
#   if coin == 6:
#     return True
#   else:
#     return False
#
#
# list_of_digit = []
# sorts = []
# sortsReversed = []
#
# digit = int(input(("Введите числа"),))
# list_of_digit.append(digit)
# sorts.append(digit)
# sortsReversed.append(digit)
#
# i = 1
#
# while(i < 5):
#   digit = int(input(("Введите числа"), ))
#   list_of_digit.append(digit)
#   sorts.append(digit)
#   sortsReversed.append(digit)
#   i = i + 1
#
# sorts.sort()
# sortsReversed.sort(reverse=True)
#
# print(isSorted(list_of_digit, sorts, sortsReversed))