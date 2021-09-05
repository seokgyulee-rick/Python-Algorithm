# def f(n):
#     if(n <= 1):
#         return n
#     else:
#         return n + f(n-1)


# n = 100
# print(f(n))
def f(n):
    if(n >= 100):
        return n
    else:
        return n + f(n+1)


n = 1
print(f(n))
