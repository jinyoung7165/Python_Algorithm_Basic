#k대회기출 - 정확한 순위
#학생들의 성적을 비교한 결과가 주어질 때, 성적 순위를 정확히 알 수 있는 학생은 모두 몇 명인지
#학생들의 수 N, 두 학생의 성적을 비교한 횟수 M
#M개의 각 줄에는 두 학생의 성적을 비교한 결과를 나타내는 양의 정수 A와 B=> A번 학생< B번 학생
#각 학생들 간의 비용을 모두 저장.DP
#특정노드가 다른 노드들과 모두 연결 돼있으면 순위를 알 수 있는 노드이다.
INF=int(1e9)
n,m=map(int,input().split()) #노드,간선 수
graph=[[INF]*(n+1) for _ in range(n+1)]
for a in range(1,n+1):#자기자신은 0으로
    for b in range(1,n+1):
        if a==b:
            graph[a][b]=0

for _ in range(m):#간선에 대한 정보 입력
    a,b=map(int,input().split())
    graph[a][b]=1 #a->b 방향으로 연결

for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b]=min(graph[a][b],graph[a][k]+graph[k][b]) #INF 대신 경유해서 연결 비용 저장

count,result=0,0
for i in range(1,n+1): #i학생과 다른 학생들 간의 비교
    for j in range(1,n+1):
        if graph[i][j] != INF or graph[j][i] != INF: #두 학생 사이 아무런 방향의 연결이 있으면 도달 가능
            count+= 1  #i학생에 대한 비교 수
    if count==n: #모든 학생과 연결돼 있으면 이 학생은 순위를 알 수 있는 것
        result+=1 #순위를 알 수 있는 학생 수 증가
print(result)       