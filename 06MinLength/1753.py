#최단 경로
#주어진 시작점에서 모든 정점으로의 최단경로(정점 간 여러 경로 가능)
from collections import defaultdict
import heapq
from sys import maxsize, stdin
input = stdin.readline
v, e = map(int, input().split()) #정점 수, 간선 수
start = int(input()) #시작 정점

graph = defaultdict(list)
dp = [maxsize for _ in range(v+1)]
for _ in range(e):
    src, dist, cost = map(int, input().split())
    graph[src].append((dist, cost))

que = [(0, start)] #cost, 시작점
dp[start] = 0

while que:
    cost, node = heapq.heappop(que)
    
    if dp[node] < cost: continue #이미 최솟값이면 pass
    
    for u, c in graph[node]: #이 노드 경유해서 갈 수 있는 간선
        newsum = cost + c
        if dp[u] > newsum:
            dp[u] = newsum
            heapq.heappush(que, (newsum, u))

for i in dp[1:]:
    print("INF" if i == maxsize else i)