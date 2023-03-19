def equal(N,S):
    if S < 0:
        return False
    Nsum= 0
    for n in str(N):
        Nsum += int(n)
    if Nsum == S:
        return True
    else:
        return False

print (equal(12345,15))