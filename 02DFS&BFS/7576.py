#백준 7576 - 토마토
#0:토마토, 1:익은 토마토, -1:없음
#토마토가 모두 익을 때까지의 최소 날짜 출력
#이미 토마토가 모두 익어있는 경우 0
#모든 토마토가 익지 못하는 상황이면 -1 출력
from sys import stdin
from collections import deque
input = stdin.readline

m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited=[[False]*m for _ in range(n)]
d = [[0,1], [1,0], [0,-1], [-1,0]]
que = deque() #익은 토마토들
unripe, count = 0, 0
for i in range(n): #익은 토마토들의 위치 저장
    for j in range(m):
        if graph[i][j] == 1: 
            que.append([i,j,i,j])
            visited[i][j] = True #방문 처리
        elif graph[i][j] == 0:
            unripe += 1
if len(que) == 0: #익지 못한다
    print(-1)
    exit()
elif unripe == 0: #모든 토마토가 익어 있다
    print(0)
    exit()
    
while que:
    y, x, py, px = que.popleft() #현재 위치, 과거 위치
    graph[y][x] = graph[py][px]+1 #며칠 째에 익었는지
    
    for i in range(4):
        dx, dy = x + d[i][0], y + d[i][1]
        if 0 <= dx < m and  0 <= dy < n and graph[dy][dx] == 0 and visited[dy][dx] == False: #방문안한 토마토일 때
            que.append([dy,dx,y,x]) #익어라
            visited[dy][dx] = True #방문 처리
            unripe -= 1
    if graph[y][x] > count:
        count = graph[y][x]         
   
if unripe == 0: 
    print(count-2) #처음부터 익어있던 토마토:1
else:
    print(-1)

