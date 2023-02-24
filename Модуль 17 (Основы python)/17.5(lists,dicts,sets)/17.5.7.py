string = input("Введите числа через пробелы:")

list_of_strings = string.split() # список строковых представлений чисел
list_of_numbers = list(map(int, list_of_strings)) # список чисел
# Меняем местами первый и последний элементы списка:
list_of_numbers[0],list_of_numbers[-1]=list_of_numbers[-1],list_of_numbers[0]
list_of_numbers.append(sum(list_of_numbers)) #Добавляем в конец сумму списка

print (list_of_numbers)
print("Сумма всех чисел в списке:",list_of_numbers[-1])
# sum() вычисляет сумму элементов списка