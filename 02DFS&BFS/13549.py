#수빈은N에 있고, 동생은 K에 있음. 가장 빠른 시간 구하라
#수빈의 위치가 X일 때 
#걷는다면 1초 후에 x-1또는x+1로 이동
#순간이동을하면 0초 후에 2*x위치로 이동
from collections import deque
from sys import maxsize

n, k = map(int, input().split())
dp = [maxsize for _ in range(100001)]
dp[n] = 0
que = deque([n])

while que:
    node = que.popleft()
    if node == k: #도착
        print(dp[node])
        break
    if k < n:
        print(n-k) #1초에 1칸씩 뒤로 가야함
        break
    if 100001 > node*2 and dp[node*2] > dp[node]:
        dp[node*2] = dp[node]
        que.append(node*2)
    if 0 <= node-1 and dp[node-1] > dp[node] + 1: #갱신 가능
        dp[node-1] = dp[node] + 1
        que.append(node-1)
    if 100001 > node+1 and dp[node+1] > dp[node] + 1:
        dp[node+1] = dp[node] + 1
        que.append(node+1)