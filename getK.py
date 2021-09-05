array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]


def solution(array, commands):
    answer = []
    for i in commands:
        sec_array = array
        new_ary = sec_array[i[0]-1:i[1]]
        # print(new_ary)
        new_ary.sort()
        answer.append(new_ary[i[2]-1])

    return answer


print(solution(array, commands))
