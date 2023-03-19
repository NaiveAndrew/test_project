#Дано натуральное число N. Вычислите сумму его цифр.
def sum_digit(n):
   if n < 10:
       return n
   else:
       return n % 10 + sum_digit(n // 10)

print (sum_digit(9))
print(sum_digit(11634926))
