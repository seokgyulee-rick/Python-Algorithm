def pibo(x):
    if (x == 0 or x == 1):
        return 1
    else:
        return pibo(x-1) + pibo(x-2)


print(pibo(5))
print(pibo(6))
print(pibo(7))
print(pibo(8))
