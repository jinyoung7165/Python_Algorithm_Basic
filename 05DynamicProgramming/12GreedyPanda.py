#백준 1937 - 욕심쟁이 판다
#n*n대나무 숲. 대나무 먹고 이전보다 더 대나무가 많은 칸으로 이동
#출발지점을 어디로 정하냐에 따라 판다의 최대 이동 블록 달라진. 최대 이동 블록 수 구하라
#방문순서가 다음 방문에게 영향을 끼치는 BFS문제처럼 보이지만, 시간초과 난다
#따라서 Backtracking(DFS+promise)로 풀자..
import sys
sys.setrecursionlimit(1000000) #dfs 깊이때문에 달아줘야함

n=int(input())
forest=[]
dp=[]    # 각 칸에서 출발했을 때 이동 수

dx=[1,-1,0,0]
dy=[0,0,1,-1]

for i in range(n):
    forest.append(list(map(int, input().split())))
    dp.append([0]*n)

def dfs(x,y): # 정보가 없을 경우에만 수행. 이미 있으면 그 값 이용
    if dp[x][y]>0:
        return dp[x][y]

    dp[x][y]=1 # 일단 현재 자리 = 1칸
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if (0<=nx<n and 0<=ny<n and forest[x][y]<forest[nx][ny]): #상하좌우 중 이동가능하고 promise 만족할 때
            # 상하좌우로 이동했을 때 가장 큰 이동 수 저장
            dp[x][y]=max(dp[x][y], dfs(nx,ny)+1) # 현재의 이동 수, 다음 위치로 이동(+1)+다음 위치에서부터 시작 비교
    
    return dp[x][y]
   
count=0
for j in range(n): #각 칸에서 출발(같은 열부터 탐색)
    for i in range(n):
        count=max(count, dfs(i,j))  #모든 칸의 이동 수 중 최대 count에 저장

print(count)
                

