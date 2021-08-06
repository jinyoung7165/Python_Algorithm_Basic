#다익스트라.Greedy.단일노드 출발.최소heap사용.최단노드 꺼낼때W(logN).총nlog(n)
from sys import stdin
import heapq
input=stdin.readline
INF=int(1e9)
n,m=map(int(input()).split()) #노드수,간선수
start=int(input())#시작노드
graph=[[] for i in range(n+1)] #각 노드 연결 정보
#visited=[False]*(n+1) 방문처리표 사용x
distance=[INF]*(n+1) #최단거리 테이블
for _ in range(m):#모든 간선 정보
    a,b,c=map(int,input().split())#출발,도착,비용
    graph[a].append((b,c))#a에서 b로 가는 비용이 c
def dijkstra(start):
    q=[] #큐.(최단경로,노드)저장
    heapq.heappush(q,(0,start))#최단경로0,시작노드 큐에 삽입
    distance[start]=0
    while q:#큐가 빌 때까지
        dist,now=heapq.heappop(q)#가장 최단경로,노드 꺼냄
        if distance[now]<dist:#이미 방문처리된 노드라면 무시
            continue
        for i in graph[now]:#현재 노드와 연결된 노드(i[0])들 확인
            cost=dist+i[1]
            if cost<distance[[i[0]]]:#현재노드 거쳐 더 짧아지면
                distance[i[0]]=cost #갱신 후 후보로 넣을 거임
                heapq.heappush(q,(cost,i[0]))#제일 cost작은 순으로 정렬
dijkstra(start)
for i in range(1,n+1):#모든 노드로 가기 위한 최단 거리출력
    if distance[i]==INF:#이어져 있지 않음
        print("INFINITY")
    else:
        print(distance[i])