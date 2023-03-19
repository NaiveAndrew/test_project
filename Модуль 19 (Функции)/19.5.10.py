def mirror(a, res=0):
    if a == 0:
        return res
    else:
        return mirror(a // 10, res * 10 + a % 10)

number = 967435261
print(mirror(number))