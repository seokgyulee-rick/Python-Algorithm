n = 5
lost = [2, 3, 4]
reserve = [1, 2, 3]


# 4
def solution(n, lost, reserve):
    # lost 를 최대한 줄이고
    # 그걸 n에서 뺀다.
    lost.sort()
    lost_cnt = len(lost)
    for i in lost:
        if(i in reserve):
            reserve.remove(i)
            lost_cnt -= 1
        elif(i-1 in reserve):
            reserve.remove(i-1)
            lost_cnt -= 1
        elif(i+1 in reserve):
            reserve.remove(i+1)
            lost_cnt -= 1

    answer = n - lost_cnt

    return answer


print(solution(n, lost, reserve))
