#모든 노드에서 모든 노드까지.경유점 기억 DP.O(N3)
#간선의 개수가 많으면 다익스트라 써야함
#D(k)[i][j]=D(k-1)[i][j]
#D(k)[i][j]=D(k-1)[i][k]+D(k-1)[k][j]
INF=int(1e9)
n=int(input()) #노드 수
m=int(input()) #간선 수
graph=[[INF]*(n+1) for _ in range(n+1)]
#자기자신으로 가는 비용은 0
for a in range(1,n+1):
    for b in range(n+1):
        if a==b:
            graph[a][b]=0
for _ in range(m):#간선 정보
    a,b,c=map(int,input().split())
    graph[a][b]=c #a->b 비용:c

for k in range(1,n+1):#플로이드 알고리즘 수행
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b]=min(graph[a][b],graph[a][k]+graph[k][b])

for a in range(1,n+1):#결과 출력
    for b in range(1,n+1):
        if graph[a][b]==INF:
            print("INFINITY",end='')
        else:
            print(graph[a][b],end='')
    print()