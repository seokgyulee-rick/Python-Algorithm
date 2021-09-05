ary = [5, 10, 66, 77, 54, 32, 11, 15]
sorted_ary = []


def findIndex(sorted_ary, num):
    for i in range(len(sorted_ary)):
        if (num < sorted_ary[i]):
            return i
    return len(sorted_ary)


while ary:
    num = ary.pop(0)
    i = findIndex(sorted_ary, num)
    sorted_ary.insert(i, num)

print(sorted_ary)
