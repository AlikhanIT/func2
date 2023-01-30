class Student:
  def __init__(self, name, age, gpa, adviser, email):
    self.name = name
    self.age = age
    self.gpa = gpa
    self.adviser = adviser
    self.email = email

students = [
    Student("Dimash", 19, 3.7, "Abdygalym", "dimash@gmail.com"),
    Student("Ilyas", 19, 3.1, "Abdygalym", "ilyas@gmail.com"),
    Student("Islam", 19, 3.61, "Asem", "islam@gmail.com"),
    Student("Batyr", 20, 3.15, "Asem", "batyr@gmail.com"),
]

a = str(input("Введите имя ",))

def find_person(students, a):
  for student in students:
    if student.name == a:
      return student
  return None

result = find_person(students, a);

if result:
  print(f"Имя студента {result.name}") # Вывод имени студента
  print(f"Возраст студента {result.age}") # Вывод возраста студента
  print(f"GPA студента {result.gpa}") # Вывод GPA студента
  print(f"Эдвайзер студента {result.adviser}") # Вывод эдвайзера студента
  print(f"Почта студента {result.email}") # Вывод почты студента
else:
  print(f"Студент по имени {a} отсутствует в базе данных")

print("Добавление нового студента")
name = str(input("Введите имя студента ",))
age = str(input("Введите возраст студента ",))
gpa = str(input("Введите GPA студента ",))
adviser = str(input("Введите эдвайзера студента ",))
email = str(input("Введите почту студента ",))

newStudent = Student(name, age, gpa, adviser, email)
students.append(newStudent)

for student in students:
    print(f"Имя студента {student.name}")  # Вывод имени студента
    print(f"Возраст студента {student.age}")  # Вывод возраста студента
    print(f"GPA студента {student.gpa}")  # Вывод GPA студента
    print(f"Эдвайзер студента {student.adviser}")  # Вывод эдвайзера студента
    print(f"Почта студента {student.email}")  # Вывод почты студента
    print(f"\n")