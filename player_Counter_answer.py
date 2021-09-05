from collections import Counter
participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]


def solution(participant, completion):
    answer = Counter(participant) - Counter(completion)
    return answer


#solution(participant, completion)
print(solution(participant, completion))
