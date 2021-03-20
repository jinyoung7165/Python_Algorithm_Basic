from collections import deque

n,m,k,x=map(int,input().split()) #도시 수, 도로 수, 최단거리, 시작노드
lenlist=[0]*(n+1) #출발노드로부터 해당 노드와의 거리를 기록
graph=[[]for _ in range(n+1)] #각 도시에 대한 2차원 리스트 입력
for i in range(m):
    a,b=map(int,input().split())
    graph[a].append(b) #a번 노드는 b와 연결
visited=[False]*(n+1)#0부터 n번 노드까지

que=deque([x])
visited[x]=True #현재 노드를 방문 처리
while que: #큐가 빌 때까지 반복
    v=que.popleft() #맨 앞에서 원소 뽑아 출력
    for i in graph[v]: #이 노드와 연결된 단일 거리의 노드들 확인
        if not visited[i]:
            que.append(i) #방문하지 않은 원소를 큐에 삽입
            visited[i]=True
            lenlist[i]=lenlist[v]+1 #이전에 방문한 노드보다 거리+1
result=False
for i in range(1,n+1):
    if(k==lenlist[i]):
        print(i)
        result=True  #해당 최단거리의 노드 발견함
if not result: print(-1)

