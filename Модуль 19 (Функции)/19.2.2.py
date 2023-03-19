def mul(*nums):
    p = 1
    for n in nums:
        p *= n

    return p


print(mul())  # 0
print(mul(1))  # 1
print(mul(1, 2))  # 3
print(mul(1, 2, 3))  # 6