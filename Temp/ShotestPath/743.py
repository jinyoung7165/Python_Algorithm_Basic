#Network Delay Time
#모든 노드가 신호를 받을 수 있는 최장 시간
#다익스트라(bfs, heapq)
import collections
import heapq


def networkDelayTime(self, times, N, K): #k:출발노드
    graph = collections.defaultdict(list)
    for u, v, w in times: #출발,도착,시간
        graph[u].append((v,w))
    Q = [(0,K)] #소요시간, 정점
    dist = collections.defaultdict(int)
    
    while Q: #우선순위 큐 최솟값 기준으로 최단 경로 삽입
        time, node = heapq.heappop(Q)
        if node not in dist:
            dist[node] = time
            for v, w in graph[node]:
                alt = time + w
                heapq.heappush(Q, (alt, v))
    if len(dist) == N:
        return max(dist.values())
    return -1 #모든 정점까지 도달 불가능 
    