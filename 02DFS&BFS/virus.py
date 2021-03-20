'''
0은 빈 칸, 1은 벽, 2는 바이러스가 있는 곳
바이러스는 상하좌우로 인접한 빈 칸으로 모두 퍼져나갈 수 있다
벽을 3개 세운 뒤, 바이러스가 퍼질 수 없는 곳을 안전 영역
dfs
'''
from itertools import combinations
from collections import deque
n,m=map(int,input().split())
graph=[]
avail=[] #벽 넣을 수 있는 공간
virus_start=[] #초기바이러스 위치

for _ in range(n):
    graph.append(list(map(int,input().split())))
for i in range(n):
    for j in range(m):
        if graph[i][j]==0:
            avail.append((i,j))
        if graph[i][j]==2:
            virus_start.append((i,j))
def dfs(x,y):
    if x<=-1 or x>=n or y<=-1 or y>=m:  #주어진 범위를 벗어나면 즉시종료
        return False
    if graph[x][y]==0:
        graph[x][y]=2 #방문 처리해서 감염
        que.append((x,y))
        dfs(x-1,y) #상하좌우 호출
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False

maxx=0
block=list(combinations(avail,3)) #벽 세 개 조합
que=deque()
for i in range(len(block)):  # [((),(),()),  ((),(),()),     ((),(),())]
    for j in range(3): #벽 세 개 세울 것  ((),(),())
        a,b=block[i][j]
        graph[a][b]=1 #벽 세우기
        que.append((a,b))
    result=0

    for k in range(len(virus_start)):
        x,y=virus_start[k]
        dfs(x-1,y) #상하좌우 호출
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
    for p in range(n):
        for j in range(m):
            if graph[p][j]==0:
                result+=1
    maxx=max(result,maxx)
    while que:
        a,b=que.popleft()
        graph[a][b]=0 #원상태로

print(maxx)