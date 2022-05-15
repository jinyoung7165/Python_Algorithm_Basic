#연속합
#n개의 정수로 이뤄진 수열, 연속된 몇 개의 수를 선택해 합 중 최대.
from sys import stdin
input = stdin.readline
n = int(input())
arr = list(map(int, input().split()))

dp = [0]*n
dp[0] = arr[0]

for i in range(1, n):
    dp[i] = max(arr[i], dp[i-1]+arr[i])
    

print(max(dp))