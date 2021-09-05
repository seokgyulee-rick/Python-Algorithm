# 1번 수포자가 찍는 방식: 1, 2, 3, 4, 5,/ 1, 2, 3, 4, 5,/ ...
# 2번 수포자가 찍는 방식: 2/, 1, 2/, 3, 2/, 4, 2/, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
# 3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2,/ 4, 4, 5, 5,// 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...


answers = [1, 2, 3, 1, 2]


def solution(answers):
    answer_ary = [0, 0, 0]
    for i in range(len(answers)):
        if(answers[i] == (i % 6 + 1)):
            answer_ary[0] += 1

        if(i % 2 == 0 and answers[i] == 2):
            answer_ary[1] += 1
        elif(i % 8 == 5 and answers[i] == (i % 5 - 1)):
            answer_ary[1] += 1
        elif(i % 8 == 7 and answers[i] == (i % 5 - 2)):
            answer_ary[1] += 1
        elif(i % 8 == 1 and answers[i] == 1):
            answer_ary[1] += 1
        elif(i % 8 == 3 and answers[i] == 3):
            answer_ary[1] += 1

        if((i % 10 == 0 or i % 10 == 1) and answers[i] == 3):
            answer_ary[2] += 1
        elif((i % 10 == 2 or i % 10 == 3) and answers[i] == 1):
            answer_ary[2] += 1
        elif((i % 10 == 4 or i % 10 == 5) and answers[i] == 2):
            answer_ary[2] += 1
        elif((i % 10 == 6 or i % 10 == 7) and answers[i] == 4):
            answer_ary[2] += 1
        elif((i % 10 == 8 or i % 10 == 9) and answers[i] == 5):
            answer_ary[2] += 1
    print(answer_ary)
    max_num = max(answer_ary)

    answer = [i+1 for i in range(len(answer_ary)) if(answer_ary[i]) == max_num]
    answer.sort()
    return answer


print(solution(answers))
