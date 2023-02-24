s = []
s = [0, 'hello', (1, 'a')]
# допустим, у нас есть список, содержащий первые 4 буквы латинского алфавита
letters = ['a', 'b', 'c', 'd']
print (letters)
# с помощью метода append() мы добавляем ещё один элемент в список
letters.append('e')

print(letters)
# ['a', 'b', 'c', 'd', 'e']
print(letters[1])
# b
print(letters[0])
# a

L = ["а", "б", "в", 1, 2, 3, 4]
print (L[ 1:4 ])
print (L[ ::3 ])
print (L[ -4::-1 ])
print (L[ -1:-4:-1 ])

#Функция map(function, list)
# имеем список с числами с плавающей точкой
L = [3.3, 4.4, 5.5, 6.6]

# печатаем сам объект map
print(map(round, L)) # к каждому элементу применяем функцию округления
# <map object at 0x7fd7e86eb6a0>

# и результат его преобразования в список
print(list(map(round, L)))
# [3, 4, 6, 7]

L = ['3.3', '4.4', '5.5', '6.6']

print (list (map ( float , L)))

string = input("Введите числа через пробелы:")

list_of_strings = string.split() # список строковых представлений чисел
list_of_numbers = list(map(int, list_of_strings)) # список чисел

print("Сумма каждого третьего числа в списке:",sum(list_of_numbers[::3])) # sum() вычисляет сумму элементов списка