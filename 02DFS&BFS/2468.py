#백준 2468 - 안전영역
#물에 잠기지 않는 안전영역이 최대 몇 개인지
#높이정보: N*N 배열. 각 원소는 해당 지점의 높이
#높이가 x이하인 인접한 침수 지점들이 경계선이 되어 안 잠긴 지역들이 뭉탱이로 갈라진다
#비의 양에 따라 안정영역 수가 달라짐
#높이 정보가 주어졌을 때 안전영역의 최대 개수를 구하라
import sys
import copy
sys.setrecursionlimit(10**6) #재귀 깊이 설정 (10만 -> 100만)
input = sys.stdin.readline

graph, temp = [], []
n = int(input())
for _ in range(n): #높이 정보
    graph.append(list(map(int,input().split())))
graph_min = min(map(min,graph))
graph_max = max(map(max,graph))  #2차원 배열에서 최솟값, 최댓값 구할 때 map 쓰면 편리

d = [[0,1],[1,0],[0,-1],[-1,0]]
def dfs(x,y,height):
    graph[x][y] = -1 #방문처리
    for i in range(4): #다음 방향
        dx = x+d[i][0]
        dy = y+d[i][1]
        if 0<=dx<n and 0<=dy<n and graph[dx][dy] > height: #인접한 침수되지 않은 곳으로 이동
            dfs(dx,dy,height)

max_count = 1 #최대 안전영역 수. 비가 안 내리면 전체가 하나의 안전영역이므로 0 대신 1부터 시작.
temp = copy.deepcopy(graph)

for height in range(graph_min,graph_max):
    #height보다 크면 인접한 지점들 찾으러
    count = 0 #height별 안전영역 최대 개수
    for i in range(n):
        for j in range(n):
            if graph[i][j] > height:
                dfs(i,j,height)
                count+=1
    if count > max_count:
        max_count = count
    graph = copy.deepcopy(temp)

print(max_count)