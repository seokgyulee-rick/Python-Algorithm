# 시간 초과
participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]


def solution(participant, completion):
    #answer = participant.copy()
    for i in completion:
        j = 0
        parti_len = len(participant)
        while j < parti_len:
            if(participant[j] == i):
                del participant[j]
                break
            j += 1

    return participant


#solution(participant, completion)
print(solution(participant, completion))
