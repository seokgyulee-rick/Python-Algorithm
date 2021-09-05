import sys
from typing import ChainMap

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    '''
        이 부분에 여러분의 알고리즘 구현이 들어갑니다.
    
    K = int(input()) # 배터리 량
    N = int(input()) # 정류장 갯수
    M = int(input()) # 충전기 갯수 
    '''
    K, N, M = map(int,input().split())
    
    listCharge = list(map(int, input().strip().split()))
    
print("#" + str(test_case))
    #print(chargeAry)
    
    # ///////////////////////////////////////////////////////////////////////////////////
