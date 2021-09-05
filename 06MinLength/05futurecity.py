#미래 도시에는 1번~n번 회사. 특정 회사끼리는 도로를 통해 연결
#연결된 회사는 양방향으로 이동 가능.1만큼의 시간
#A는 1번 회사에서 출발해 K번 방문 후 X번으로 가려한다
#최소 시간을 계산
#시간제한 1초.M최대 100. =>플로이드 워셜O(n3)로 풀 수 있다. 1초는 10^8
# 1번->X 최단거리 + X->K 최단거리
INF=int(1e9)
n,m=map(int,input().split())
graph=[[INF]*(n+1) for _ in range(n+1)]
#자기자신으로 가는 비용은 0으로 초기화
for a in range(1,n+1):
    for b in range(1,n+1):
        if a==b:
            graph[a][b]=0
for _ in range(m):
    a,b=map(int,input().split()) #a-b 연결
    graph[a][b]=1 #a-b 비용 1
    graph[b][a]=1

x,k=map(int,input().split()) #거쳐 갈 노드 x와 최종 목적지 노드k를 입력받기

for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b]=min(graph[a][b],graph[a][k]+graph[k][b])
distance=graph[1][k]+graph[k][x] #1->k->x 최단거리
if distance >=INF:
    print("-1")
else:
    print(distance)
