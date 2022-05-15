#동전 2
#동전 n종류로 k가치를 만들 때 필요한 동전의 최소 개수
from sys import maxsize
n, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]

dp = [maxsize]*(k+1)
dp[0] = 0

for coin in arr:
    for i in range(1, k+1):
        if i >= coin: dp[i] = min(dp[i-coin] + 1, dp[i])

if(dp[k] == maxsize): print(-1)
else: print(dp[k])