ary = [5, 10, 66, 77, 54, 32, 11, 15]
sorted_ary = []
while ary:
    sorted_ary.append(min(ary))
    ary.pop(ary.index(min(ary)))

print(sorted_ary)
