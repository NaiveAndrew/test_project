print(not True)
# False

print(not False)
# True

# можно проверить, находится ли число 1 в промежутке (0,4)
cond1 = 0 < 1
cond2 = 1 < 4

print(cond1 and cond2)
# True

# или, например, содержат ли две строки один и тот же символ
cond3 = 't' in "python"
cond4 = 't' in "django"

print(cond3 and cond4)
# False

# к слову, логические выражения можно сразу объединять в одно целое
print(('t' in "python") or ('t' in "django"))
# True

print (not True or (True and not True))

print(not
    False
    and
    True
    or
    False
    and
    not
    True)

def is_leap_year(x):
    return (x % 400 == 0) or (( x % 4 == 0) and ( x % 100 != 0))

print (is_leap_year(2000))
print (is_leap_year(1900))
print (is_leap_year(1999))
print (is_leap_year(2020))