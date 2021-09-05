priorities = [1, 1, 9, 1, 1, 1]
location = 0


def solution(priorities, location):
    cnt = 0
    max_num = max(priorities)
    while True:
        for i in range(len(priorities)):
            if(priorities[i] == max_num):
                priorities[i] = 0
                cnt += 1
                if(i == location):
                    return cnt
            max_num = max(priorities)


print(solution(priorities, location))
