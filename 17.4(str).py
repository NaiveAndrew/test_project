s1 = 'hello' # используя апострофы
s2 = "hola" # используя кавычки
s3 = '''Привет!
        Хорошего дня!''' # используя тройные "апострофы" или тройные кавычки
s = "Hello!"

print(s[0])
# H
print(s[4])
# o
print(s[1:4])
# ell
print(s[::2])
# Hlo
print(s[-1])
# !
print(s[-3:-1])
# lo
#Встроенная функция len() позволяет узнать длину строки:
print(len(s))
#Метод find(substr), определённый для строк, позволяет находить символы и подстроки:
print(s.find('e')) # возвращает индекс
# 1
print(s.find('o!')) # в случае подстроки возвращает индекс первого символа
# 4
print(s.isdigit()) # строка состоит из цифр?
# False

print(s.isalpha()) # строка состоит из букв?
# False

print(s.isalnum()) # строка состоит из цифр и букв?
# False
print(s.upper())
# HELLO!

print(s.lower())
# hello!

print(s.capitalize())
# Hello!