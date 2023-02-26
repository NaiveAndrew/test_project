number_tickets = int(input("Введите количество билетов: "))
age = []
counter = 1
while number_tickets > 0:
    age.append(int(input(f"Введите возраст для билета {counter}: ")))
    counter += 1
    number_tickets -= 1
amount = 0
for a in age:
    if a < 18:
        pass
    elif 18 <= a < 25:
        amount += 990
    else:
        amount += 1390

if len(age)>3:
    amount = int(amount/100*90)
    print (f"Сумма к оплате с учетом скидки 10%: {amount}")
else:
    print(f"Сумма к оплате: {amount}")