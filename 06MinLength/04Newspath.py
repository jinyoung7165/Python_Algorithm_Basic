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
            cost=dist+i[1]
            if cost<distance[[i[0]]]:#현재노드 거쳐 더 짧아지면
                distance[i[0]]=cost #갱신 후 후보로 넣을 거임
                heapq.heappush(q,(cost,i[0]))#제일 cost작은 순으로 정렬
n,m,start=map(int(input()).split()) #노드수,간선수
graph=[[] for i in range(n+1)] #각 노드 연결 정보
distance=[INF]*(n+1) #최단거리 테이블
for _ in range(m):#모든 간선 정보
    a,b,c=map(int,input().split())#출발,도착,비용
    graph[a].append((b,c))#a에서 b로 가는 비용이 c
dijkstra(start)

count=0 #도달할 수 있는 노드 개수
max_distance=0 #도달할 수 있는 노드 중, 가장 멀리있는 노드와의 최단거리
for d in distance:
    if d!=1e9: #도달 가능
        count+=1
        max_distance=max(max_distance,d)

print(count-1,max_distance) #시작노드 제외