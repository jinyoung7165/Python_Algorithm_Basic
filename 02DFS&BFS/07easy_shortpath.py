#백준 - 14940 쉬운 최단거리
#모든 지점 대해 목표지점까지의 최단 거리
#0은 갈 수 없는 땅, 1은 갈 수 있는 땅, 2는 목표지점
#원래 갈 수 없는 땅은 0출력, 도달할 수 없는 위치는 -1출력
#최단거리 문제기 때문에 해당 노드와 이어진 4방향 노드(bfs) 중 1이면서 도착지까지 최소비용인 노드를 선택
from sys import stdin
from collections import deque
input=stdin.readline
n,m=map(int,input().split())
graph=[]
visited=[[False]*m for _ in range(n)]
result=[[-1]*m for _ in range(n)]
d=[[0,-1],[-1,0],[0,1],[1,0]] #좌,상,우,하
que=deque()
for i in range(n):
    graph.append(list(map(int,input().split())))
for i in range(n):
    for j in range(m):
        if graph[i][j]==2:#도착지 저장
            que.append([i,j]) #도착지에서부터 출발
            result[i][j]=0
            visited[i][j]=True
        elif graph[i][j]==0:#갈 수 없는 땅
            result[i][j]=0

def bfs():
    while que:
        x,y=que.popleft()#현재 위치
        for i in range(4):#사방으로 이동
            nx,ny=x+d[i][0],y+d[i][1]
            if (0<=nx<n) and (0<=ny<m) and graph[nx][ny]==1 and not visited[nx][ny]:#갈 수 있는 땅
                visited[nx][ny]=True
                que.append([nx,ny])
                result[nx][ny]=result[x][y]+1 #그 전 누적+1
bfs()
for i in range(n):
    print(" ".join(map(str,result[i]))) #각 원소 사이에 공백 넣어 출력


