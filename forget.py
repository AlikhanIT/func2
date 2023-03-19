# Функция добавления элемента в список
def add_to_list(lst, item):
    lst.append(item)

# Функция удаления элемента из списка
def remove_from_list(lst, item):
    if item in lst:
        lst.remove(item)

# Функция сортировки списка
def sort_list(lst):
    lst.sort()

# Функция поиска элемента в списке
def search_list(lst, item):
    if item in lst:
        return lst.index(item)
    else:
        return -1

# Функция вывода списка на экран
def print_list(lst):
    print("Список:")
    for item in lst:
        print(item)

# Создание пустого списка
my_list = []

# Добавление элементов в список
add_to_list(my_list, "яблоко")
add_to_list(my_list, "банан")
add_to_list(my_list, "апельсин")

# Вывод списка на экран
print_list(my_list)

# Удаление элемента из списка
remove_from_list(my_list, "банан")

# Вывод списка на экран
print_list(my_list)

# Сортировка списка
sort_list(my_list)

# Вывод списка на экран
print_list(my_list)

# Поиск элемента в списке
index = search_list(my_list, "яблоко")
if index != -1:
    print("Элемент найден на позиции", index)
else:
    print("Элемент не найден")