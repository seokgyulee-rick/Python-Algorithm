numbers = [3, 30, 34, 5, 9]


def solution(numbers):
    ary = []
    for i in numbers:
        while i != 0:
            ary.append(i % 10)
            i = i/10

        ary.sort()

    answer = ''.join(ary)
    return answer


print(solution(numbers))
