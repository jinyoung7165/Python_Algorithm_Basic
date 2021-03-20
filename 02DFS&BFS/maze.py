'''
n x m 크기의 미로. 현재 위치는 (1,1). 미로의 출구는 (n,m)
한 번에 한 칸만 이동 가능. 괴물이 있는 부분은 0. 괴물이 없는 부분은 1
탈출을 위한 최소 칸의 수?(시작 칸과 마지막 칸 포함)
<BFS>
가장 가까운 노드부터 방문.상하좌우 노드 간의 거리는 1
110
010
011  1은 방문할 수 있는 노드
상하좌우 탐색하며 새로 방문하는 노드 값을 이동 거리로 바꿈
'''
from collections import deque
def bfs(x,y):
    que=deque()
    que.append((x,y))
    while que: #큐가 빌 때까지 반복
        x,y=que.popleft() #현재 위치
        for i in range(4): #상하좌우 위치 확인
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            if graph[nx][ny]==0:#벽인 경우 무시
                continue
            if graph[nx][ny]==1:#해당 노드를 처음 방문하는 경우에만 최단 거리 기록
                graph[nx][ny]=graph[x][y]+1
                que.append((nx,ny))
    return graph[n-1][m-1] #가장 오른쪽 아래까지의 최단 거리 반환

n,m=map(int,input().split())
graph=[] #2차원 리스트 입력
for i in range(n):
    graph.append(list(map(int,input())))
dx=[-1,1,0,0] #상하좌우
dy=[0,0,-1,1]
print(bfs(0,0))
