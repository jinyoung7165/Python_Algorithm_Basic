#1:이동 가능, 0:불가
#(1,1)->(n,m)으로 이동할 때 지나야하는 최소 칸 수
#시작 칸수와 도착 칸수도 센다
from sys import stdin
from collections import deque
input = stdin.readline
n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(int(x) for x in input().rstrip()))
def bfs(i,j):
    d = [[0,1],[1,0],[0,-1],[-1,0]]
    que = deque()
    que.append((i,j))

    while que:
        x, y = que.popleft()
        if x == n-1 and y == m-1:
            return graph[n-1][m-1]

        for i in range(4):
            dx, dy = x + d[i][0], y + d[i][1]
            if 0 <= dx < n and 0 <= dy < m and graph[dx][dy] == 1 and (dx+dy)>0:
                que.append((dx, dy))
                graph[dx][dy] = graph[x][y] + 1
print(bfs(0,0))