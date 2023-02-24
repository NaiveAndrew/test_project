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

#Форматирование строк
age = 25

my_age = "I'm %d years old" % (age) # в шаблоне присутствует специальный символ %d

print(my_age)
# I'm 25 years old

#Форматирование даты
day = 14
month = 2
year = 2012

print("%d.%02d.%d" % (day, month, year))
# 14.02.2012
print("%d-%02d-%d" % (year, month, day))
# 2012-02-14
print("%d/%d/%d" % (year, day, month))
# 2012/14/2

#Форматирование времени
hours = 15
minutes = 53
seconds = 44
print("%d:%d:%d" % (hours, minutes, seconds))