L = ['a', 'b', 'c']
print(id(L))

L.append('d')
print(id(L))

a = 5
b = 3+2

print (id(a))
print (id(b))
#Значение Id одинаковые потому что число 5 хранится в определенной ячейке памяти

list_1 = ['a', 'b', 'c']
list_2 = list_1
list_3 = list(list_1)
print(list_1)
print(list_2)
print(list_3)

print(list_1 is list_2)
print(list_1 is list_3) #false потому что list_3 указывает на другой объект в памяти из-за строки 16