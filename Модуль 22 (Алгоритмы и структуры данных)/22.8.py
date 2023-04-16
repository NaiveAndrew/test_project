import math
D = math.factorial(100)
def count_digits(n):
    # Проверяем, что n - целое неотрицательное число
    if not isinstance(n, int) or n < 0:
        return None
    # Если n равно нулю, то возвращаем 1
    if n == 0:
        return 1
    # Инициализируем счетчик цифр
    count = 0
    # Пока n не равно нулю, делим его на 10 и увеличиваем счетчик
    while n > 0:
        n //= 10
        count += 1
    # Возвращаем счетчик цифр
    return count

# Тестируем функцию на числе 100
print(count_digits(D)) # Должно вывести 3