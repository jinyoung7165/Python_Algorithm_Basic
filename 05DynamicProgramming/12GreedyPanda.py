#백준 1937 - 욕심쟁이 판다
#n*n대나무 숲. 대나무 먹고 이전보다 더 대나무가 많은 칸으로 이동
#출발지점을 어디로 정하냐에 따라 판다의 최대 이동 블록 달라진. 최대 이동 블록 수 구하라
#방문순서가 다음 방문에게 영향을 끼치는 BFS문제처럼 보이지만, 시간초과 난다
#따라서 Backtracking(DFS+promise)로 풀자..
from sys import setrecursionlimit,stdin 
setrecursionlimit(10**9)
input=stdin.readline

n=int(input().rstrip())
forest=[] #map
visited = [[-1] * n for _ in range(n)]
dp=[[-1 for _ in range(n)]for _ in range(n)] #각 노드로부터 출발했을 때 이동 블록 수
d=[[1,0],[0,1],[-1,0],[0,-1]]
result=0 #최대 이동 블록

for i in range(n):
    forest.append(list(map(int, input().rstrip().split()))) #map

def dfs(x,y): #현재 좌표부터 출발
    if visited[x][y]<0: #방문하지 않았을 때
        visited[x][y]=0 #방문 처리
        for i in range(4):
            nx,ny=x+d[i][0],y+d[i][1] #다음 좌표
            if 0<=nx<n and 0<=ny<n and forest[x][y]<forest[nx][ny]:#맵 안에 있고, promise만족하면
                visited[x][y]=max(visited[x][y],dfs(nx,ny))  #???여기부터 return까지 이해안됨
        visited[x][y]+=1
    return visited[x][y]
        
for i in range(n): #(i,j)를 출발점으로 했을 때 블록 이동 수 구하기
    for j in range(n):
        result=max(result,dfs(i,j))

print(result)
                

