#백준 1012 - 유기농 배추
#지렁이 있으면 배추의 해충 보호, 다른 지렁이는 인접한 배추로 이동 가능(상하좌우)
#서로 인접한 배추 '몇 군데'인지 조사하면 필요한 지렁이 수 알 수 있음 -> 뭉탱이를 세라
#0은 땅, 1은 배추가 있는 땅
#순서 상관없이 연결된 곳 찾으면 되니까 DFS로 푼다
#T:테스트 수, M,N,K:밭 가로세로,배추 개수
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6) #재귀 깊이 설정 (10만 -> 100만)
d = [[0,1],[1,0],[0,-1],[-1,0]]
def dfs(x,y):
    graph[x][y] = -1 #방문처리
    for i in range(4): #다음 방향
        dx = x+d[i][0]
        dy = y+d[i][1]
        if 0<=dx<n and 0<=dy<m and graph[dx][dy] == 1: #인접한 배추면 이동
            dfs(dx,dy)
    
T = int(input())
for _ in range(T):
    m,n,k = map(int,input().split())
    graph = [[0]*m for _ in range(n)]

    for _ in range(k): #배추의 위치
        i,j = map(int,input().split())
        graph[j][i] = 1
    
    count = 0 #인접한 뭉탱이 수
    
    for i in range(n): #세로
        for j in range(m): #가로
            if graph[i][j]>0: #배추
                dfs(i,j) #인접한 배추 있는지 확인
                count+=1
    print(count)
