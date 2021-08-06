#다익스트라.Greedy.단일노드 출발.전체 노드 수가 5000개 이하일 때
from sys import stdin
input=stdin.readline
INF=int(1e9)
n,m=map(int(input()).split()) #노드수,간선수
start=int(input())#시작노드
graph=[[] for i in range(n+1)] #각 노드 연결 정보
visited=[False]*(n+1)
distance=[INF]*(n+1) #최단거리 테이블
for _ in range(m):#모든 간선 정보
    a,b,c=map(int,input().split())#출발,도착,비용
    graph[a].append((b,c))#a에서 b로 가는 비용이 c
def get_min_node():#distance테이블에서 방문하지 않은 노드 중 최단의 노드 반환
    min=INF
    index=0 #가장 최단의 노드
    for i in range(1,n+1):
        if distance[i]<min and not visited[i]:
            min=distance[i]
            index=i
    return index
def dijkstra(start):
    distance[start]=0
    visited[start]=True
    for j in graph[start]:
        distance[j[0]]=j[1] #start와 연결된 노드j[0]들의 비용j[1]
    for i in range(n-1):#시작노드 제외 n-1번 반복
        now=get_min_node()#현재가장 최단 거리 짧은 노드 꺼내 방문처리
        visited[now]=True
        for j in graph[now]:#현재 노드(거쳐서)와 연결된 노드들 확인
            cost=distance[now]+j[1] #현재 노드 거친 비용결과
            if cost<distance[j[0]]: #안 거치는 것보다 비용 적으면 교체
                distance[[j[0]]]=cost
dijkstra(start)

for i in range(1,n+1):#모든 노드로 가기 위한 최단 거리출력
    if distance[i]==INF:#이어져 있지 않음
        print("INFINITY")
    else:
        print(distance[i])