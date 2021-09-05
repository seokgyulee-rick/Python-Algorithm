
def cal(num):
    if(num == 1):
        return 1
    elif(num == 2):
        return 2
    elif(num == 3):
        return 4
    else:
        return cal(num-1) + cal(num-2) + cal(num-3)


T = int(input())
ary = []
for i in range(T):
    input_num = int(input())
    ary.append(cal(input_num))

print(ary)
