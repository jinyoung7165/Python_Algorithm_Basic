from itertools import combinations
from collections import deque
n=int(input()) #n*n크기의 맵
graph=[]
avail=[] #장애물 넣을 수 있는 공간
t_start=[] #초기선생님 위치
#모든 학생들을 감시로부터 피하게 할 수 있는지
for _ in range(n):
    graph.append(list(input().split()))
for i in range(n):
    for j in range(n):
        if graph[i][j]=='X':
            avail.append((i,j))
        if graph[i][j]=='T':
            t_start.append((i,j))

cannot=0 #감시 못피하면 1이 됨
def dfs(x,y):
    global cannot
    if x<=-1 or x>=n or y<=-1 or y>=n:  #주어진 범위를 벗어나면 즉시종료
        return 0
    if graph[x][y]=='X':
        graph[x][y]='T' #방문 처리해서 선생님의 감시 지정
        que.append((x,y))
        return 1
    if graph[x][y]=='S':#감시 못 피함
        cannot=1
        return 1
    return 0

block=list(combinations(avail,3)) #벽 세 개 조합
que=deque()
for i in range(len(block)):  # [((),(),()),  ((),(),()),     ((),(),())]
    for j in range(3): #벽 세 개 세울 것  ((),(),())
        a,b=block[i][j]
        graph[a][b]='O' #장애물 세우기
        que.append((a,b))

    for k in range(len(t_start)):
        x,y=t_start[k]
        dfs(x-1,y) #상하좌우 호출
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)

    while que:
        a,b=que.popleft()
        graph[a][b]='X' #원상태로

if cannot==1:print("NO")
else:print("YES")