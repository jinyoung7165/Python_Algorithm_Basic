#특정한 최단 경로
#방향성 없는 그래프 1->N 최단 거리로 이동
#임의로 주어진 두 정점은 반드시 통과해야함
#한번 이동했던 정점,간선 재방문 가능, but최단경로!

import collections
import heapq
from sys import maxsize, stdin
input = stdin.readline

n, e = map(int, input().split()) #정점 수, 간선 수
graph = collections.defaultdict(list)
for i in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b,c)) #a,b사이에는 간선이 최대1개 존재
    graph[b].append((a,c)) #양방향
    
v1, v2 = map(int, input().split()) #반드시 거쳐야 하는 정점

def Dijkstra(start):
    dp = [maxsize for _ in range(n+1)] #냅다 [maxsize]*n+1보다 메모리효율 굳, 빠름
    dp[start] = 0 ####중요!!!!!!!!!!!!!!!!!
    que = [(0, start)] #cost, 시작점
      
    while que:
        cost, node = heapq.heappop(que)
        
        if dp[node] < cost: continue #이미 최솟값이면 pass

        for v, c in graph[node]: #자식 방문
            newsum = cost + c
            if dp[v] > newsum:
                dp[v] = newsum #갱신
                heapq.heappush(que,(newsum,v))
            
    return dp            

one_dp = Dijkstra(1)
v1_dp = Dijkstra(v1)
v2_dp = Dijkstra(v2)

result = min(one_dp[v1]+v1_dp[v2]+v2_dp[n], \
    one_dp[v2]+v2_dp[v1]+v1_dp[n])

print(result if result < maxsize else -1)