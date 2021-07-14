#백준 16234 - 인구 이동
#나라 1*1 크기
#r행 c열 국가의 인구는 A[r][c]
#인접한 나라 인구차 L명 이상, R명 이하면 하루동안 국경선 개방
#위 조건 만족하는 모든 국경선 열리면 인구이동 시작
#연합국 총 인구//연합국 수
#각 나라의 인구수가 주어졌을 때 인구이동이 몇 번 발생하는지
from collections import deque
N,L,R=map(int,input().split())#땅크기 N,L명 이상,R명 이하
graph=[] #N*N
move=False
count=0 #인구이동 횟수
for _ in range(N):#각 나라 인구수
    graph.append(list(map(int,input().split())))
dd=[(-1,0),(0,1),(0,-1),(1,0)]

def bfs(x,y,visited,graph):
    global move
    sum=graph[x][y] #초기 인구수(국가 1개일 때)
    un_count=1 #현재 연합한 국가 수
    que=deque()
    que.append((x,y)) #현재 국가 좌표
    visited[x][y]=True #방문처리
    united=[] #각 노드와 연결된 국가들의 좌표 저장
    united.append((x,y)) #첫번째 연합국
    while que: #한 뭉텅이의 연합국 단위
        ux,uy=que.popleft() #연합국의 좌표
        for k in range(4):
            nx,ny=ux+dd[k][0],uy+dd[k][1] #비교할 좌표
            if 0<=nx<=N-1 and 0<=ny<=N-1:#원소 존재
                if visited[nx][ny]==False and L<=abs(graph[nx][ny]-graph[ux][uy])<=R:#연합 가능
                    visited[nx][ny]=True
                    united.append((nx,ny)) #연합국의 좌표 저장
                    un_count+=1
                    sum+=graph[nx][ny]
                    que.append((nx,ny))
    population=sum//un_count #연합국에 속한 국가의 각 인구수
    if un_count>1:#국가끼리 연합을 맺었으면
        move=True
        for x,y in united:#연합국에 속한 국가들의 인구 재조정
            graph[x][y]=population
while True:
    move=False
    visited=[[False]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                bfs(i,j,visited,graph)
    if move:
        count+=1 #인구이동 횟수 증가
    else:#아무 연합도 발생하지 않았으면 인구이동 끝난 것
        break
print(count)
