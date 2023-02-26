a = "foo"
b = "bar"

print(1 and a or b)

a = ""
b = "bar"

print(1 and a or b)

a = 4
b = "text"

#a = 0
#b = ""
# пусть a и b - переменные, которые мы хотим проверить
if a and b :
    print("Обе переменные истинные")
    print(a,b)
elif a or b :
    print("Одна из переменных истинная")
    print( a or b ) # печать значения одной переменной, которая является истинной
else:
    print ("Обе переменные ложные")
