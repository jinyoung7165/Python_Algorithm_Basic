#Cheapest Flights Within K Stops
import heapq

def findCheapestPrice(n: int, flights, src: int, dst: int, k: int):
    
    graph = [[] * n for _ in range(n)]
    for a, b, c in flights:
        graph[a].append((c, b))
    
    INF = int(1e9)
    num_move_list = [INF] * n #경유 수 리스트

    q = []
    
    heapq.heappush(q, (0, src, 0)) #가격, 시작점, 경유수

    while q:
        cost, u, num_move = heapq.heappop(q) #누적 가격이 낮은 간선부터 택함

        if u == dst: #도착 지점이면 답을 구한 것
            return cost

        if num_move >= num_move_list[u]: #이전보다 더 많이 경유해왔으면 탈락
            continue

        if num_move >= k + 1: #더 이상 이동 못하면 탈락
            continue

        num_move_list[u] = num_move #이전보다 덜 경유해왔으면 경유 수 갱신

        for c, v in graph[u]: #이 노드를 거쳐서 누적 경로를 heapq에 삽입
            heapq.heappush(q, (cost+c, v, num_move+1))

    return -1


#print(findCheapestPrice(4, [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]],0,3,1))
print(findCheapestPrice(4,[[0,1,1],[0,2,5],[1,2,1],[2,3,1]],0,3,1)) 
# K제한 없으면3이지만, K=1이므로 6나와야함