from sys import stdin
from collections import deque
input = stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
d = [[0,1],[1,0],[-1,0],[0,-1]]
size, count, s_x, s_y = 2, 0, -1, -1

for i in range(n):
    for j in range(n):
        if graph[i][j] == 9: #상어 위치
            s_x, s_y = i, j
            graph[i][j] = 0 #자기 자신 못 먹음

        
def bfs(x, y):
    global size #현재 상어 크기
    visited = [[False]*n for _ in range(n)]
    visited[x][y] = True #현재 위치 방문처리!!!
    q = deque()
    q.append([x, y, 0])  #현재 위치, 시간
    fish = [] #여기서부터 출발해서 먹을 수 있는 물고기들
    level = None # 몇 레벨의 노드에서 fish나왔는지 
    flag = False #level이 변했을 때 어차피 더 깊은 레벨들만 남았기 때문에 break하기 위함
    while q:
        i,j,t = q.popleft() 
        for k in range(4):
            dj, di = j + d[k][0], i + d[k][1]
            if 0 <= dj < n and 0 <= di < n and not visited[di][dj]:#이동 가능
                visited[di][dj] = True #이동
                if graph[di][dj] != 0 and graph[di][dj] < size: #먹을 수 있음
                    fish.append((t+1, di, dj)) #시간, 위, 왼 오름차순 정렬을 위함
                    q.append([di,dj,t+1]) #이동

                    if not level: level = t+1 #처음으로 fish가 나온 노드의 레벨
                    elif level != t+1:
                        flag = True
                        break #fish 노드의 레벨이 바꼈을 때
                        
                elif graph[di][dj] == size or graph[di][dj] == 0: #이동만 가능
                    q.append([di,dj,t+1]) 
        if flag: break 
    fish.sort() #시간, 위, 왼 오름차순 정렬
    if fish:
        return [fish[0][1], fish[0][2], fish[0][0]] #x,y,time
    else:
        return []
 
    
answer = 0 #더이상 못 먹을 때까지의 총 시간
while True:
    fish_eat = bfs(s_x, s_y) #해당 노드로부터 출발 시 먹기 가능한 가장 가까운 물고기
    if fish_eat: #존재할 때
        x, y, time = fish_eat #좌표, 시간
        graph[x][y] = 0 #먹음
        count += 1 #먹은 수 증가
        answer += time #전체 시간 증가
        
        if count == size: #사이즈업
            size += 1
            count = 0
        s_x, s_y = x, y
    else:
        break
            
print(answer)         