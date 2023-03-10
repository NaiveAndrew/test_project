#Создайте скрипт, который будет в input() принимать строки, их необходимо будет конвертировать
# в числа, добавьте try-except, чтобы строки могли быть сконвертированы в числа.

#В случае удачного выполнения скрипта пусть выведется: «Вы ввели правильное число».

#В конце скрипта обязательно должна быть надпись «Выход из программы».

try:
    i = int(input('Введите число:\t'))
except ValueError as e:
    print('Вы ввели неправильное число')
else:
    print(f'Вы ввели {i}')
finally:
    print('Выход из программы')