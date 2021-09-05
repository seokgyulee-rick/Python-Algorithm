
def recurEachNum(x):
    global sum
    if(len(x) == 0):
        return 0
    else:
        return int(x[0]) + recurEachNum(x[1:])


print(recurEachNum('2231'))
