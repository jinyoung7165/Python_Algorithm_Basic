#n개의 도시.x->y 방향성 통로가 있어야 전보가능
#c도시에서 최대한 많은 도시로 메시지 보내려고할 때,
#메시지를 받는 도시의 개수와 모두 메시지를 받는데까지 걸리는 시간
#단일출발점.다익스트라
#연결된 도시 수와 가장 먼 도시까지의 비용 출력
import heapq
import sys
input=sys.stdin.readline
INF=int(1e9)
def dijkstra(start):
    q=[]
    heapq.heappush(q,(0,start)) #최단거리,시작노드
    distance[start]=0
    while q:#큐가 비어있지 않다면
        dist,now=heapq.heappop(q)
        if distance[now]<dist:
            continue  #58분
        for i in graph[now]:
            const=dist+i[1]
