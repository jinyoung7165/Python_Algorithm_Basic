#외판원순회
#1-N도시. 출발지->N개 도시 모두 거쳐 원해의 도시로 돌아옴
#한 번 갔던 도시 재방문 안됨
#W[i][j] = i->j도시 비용(양의 정수). W[i][i]는 항상 0
#i->j 길 없으면 W[i][j]=0
from sys import maxsize, stdin

input = stdin.readline
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
mincost = maxsize
visited = [False for _ in range(n)] #방문 여부(not in 보다 비교연산이 나음)

def dfs(depth, idx, cost): #깊이, 탐색할 노드의 인덱스, 누적 비용
    global mincost
    if cost >= mincost: return  #볼 거 없다
    if depth == n-1: #마지막 도시->시작 도시 갈 수 있으면 비용 갱신
        if graph[idx][0] != 0:
            mincost = min(mincost, cost + graph[idx][0])
        return
    
    for i in range(1, n): #방문한 적 없을 때
        if not visited[i] and graph[idx][i] != 0:
            visited[i] = True
            dfs(depth + 1, i, cost + graph[idx][i])
            visited[i] = False
    
dfs(0, 0, 0)

print(mincost)