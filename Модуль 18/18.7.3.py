def print_ladder(n):
    result = "*"
    while n > 0:
        print (result)
        n -=1
        result = result +"*"

print_ladder(4)