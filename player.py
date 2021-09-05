participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]


def solution(participant, completion):
    p = {}
    ind = 0
    result = ''
    for val in participant:
     #   print(1)
        p[ind] = val
        ind += 1
    # print(p)
    ind = 0
    # print(list(p.values()))
    for i in list(p.values()):
        # print(i)
        if (i in completion):
            completion.remove(p[ind])
            del p[ind]
        ind += 1
    for i in p:
        result = p[i]
    return result


#solution(participant, completion)
print(solution(participant, completion))
