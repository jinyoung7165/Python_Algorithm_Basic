#Cheapest Flights Within K Stops
import collections
import heapq

def findCheapestPrice(self, n, flights, src, dst, k):
    graph = collections.defaultdict(list)
    for u, v, w in flights:
        graph[u].append([v, w])
    k = 0
    visit = {}
    Q = [(0, src, 0)] #가격, 정점, 갔던 경유지 수
    while Q: #우선순위 큐 최솟값 기준으로 최소 비용 판별
        price, node, k = heapq.heappop(Q)
        if node == dst: #목적지 도착
            return price
        if node not in visit or visit[node] > k:
            visit[node] = k
            for v, w in graph[node]:
                if k <= K:
                    alt = price + w
                    heapq.heappush(Q, (alt, v, k + 1))
    return -1