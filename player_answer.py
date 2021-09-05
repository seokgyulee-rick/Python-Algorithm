# 시간 초과
participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]


def solution(participant, completion):
    participant.sort()
    completion.sort()

    ary = list(zip(participant, completion))
    answer = ''
    for i in ary:
        #print(i[0] + i[1])
        if(i[0] != i[1]):
            return i[0]
    return participant.pop()


#solution(participant, completion)
print(solution(participant, completion))
