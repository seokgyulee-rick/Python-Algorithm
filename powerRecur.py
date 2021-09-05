
def f(n, e):
    if(e <= 0):
        return 1
    else:
        return n*f(n, e-1)


print(f(2, 6))
