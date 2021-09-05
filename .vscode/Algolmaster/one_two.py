# 숫자의 크기 - 1 부터 시작해서 for 문 돌려서 brute force로 모든 경우의 수 찾기

T = int(input())
cnt = 0
ary = []
for i in range(T):
    num = int(input())
    ary.append(num)

print("ary = ")
print(ary)


def cal(length, num, combi, order, ans):

    print("printing : " + str(length) + " " + str(num) +
          " " + str(combi) + " " + str(order))
    global cnt
    print("cnt = " + str(cnt))

    if(order == length):

        sum = 0
        for i in combi:
            sum += i
        if(sum == ans):
            cnt += 1
            return 'correct'
    else:
        combi.append(num)
        for i in range(9):
            val = cal(length, i+1, combi.copy(), order+1, ans)
            if(val == 'correct'):
                print('break!')
                break


final_answer = []
for i in range(len(ary)):
    cnt = 0
    s = ary[i]-1
    while s > 1:

        for j in range(9):
            combi = [j+1]
            for k in range(9):
                cal(s, k+1, combi.copy(), 1, ary[i])
        s -= 1
    final_answer.append(cnt+1)


print("answer " + str(final_answer))
