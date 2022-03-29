#백준 12015 가장 긴 증가하는 부분 수열 길이 출력
#수열 A = {10,20,10,30,20,50}일 때
#가장 긴 증가부분은 {10,20,30,50}이고 길이는 4
#DP로 풀면,O(n^2). dp[i]: i번째의 LIS길이. 현재 원소를 이전 원소들 모두와 비교해서 dp[i] = max(dp[i], dp[j]+1)
#BS로 풀면 O(NlogN). dp[i]: 길이가 i인 LIS를 만들 수 있는 원소 중 제일 작은 값 
from sys import stdin
from bisect import bisect_left
input = stdin.readline

def bs():
    n = int(input())
    arr = [int(x) for x in input().split()]

    dp = [0]
    for obj in arr:
        if dp[-1] < obj: #현재원소가 LIS의 가장 마지막 원소보다 크면 걍 붙여라
            dp.append(obj) 
        else:
            idx = bisect_left(dp, obj) #LIS에 obj가 들어갈 수 있는 가장 왼쪽 위치
            dp[idx] = obj #대치를 해도 LIS의 길이는 변하지 않음
    print(len(dp)-1)

bs()