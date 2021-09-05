phone_book = ["119", "97674223", "1195524421"]


def solution(phone_book):
    answer = False
    for each in phone_book:
        i = 0
        while i < len(phone_book):
            # print(each)
          #          i = phone_book.index(each)+1
            if(i == len(phone_book)):
                break
            if(each in phone_book[i]):
                answer = False
            i += 1
    return answer


print(solution(phone_book))
