per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input("Введите сумму вклада: "))
deposit = []
for v in per_cent.values():
    value = money/100*v
    deposit.append(round(value,2))

print ("Максимальная сумма, которую вы можете заработать -",max(deposit))