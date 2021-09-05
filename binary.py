# x = int(input('2진수로 바꿀 숫자를 입력하세요 : '))
# result = ''
# while True:
#     if x % 2 == 0:
#         result += '0'
#     else:
#         result += '1'
#     x = x // 2
#     if x == 1:
#         result += str(x)
#         print(result[:: -1])
#         break

def getBinary(x):
    if (x < 2):
        return str(x)
    else:
        return(str(getBinary(x//2)) + str(x % 2))


print(getBinary(11))
