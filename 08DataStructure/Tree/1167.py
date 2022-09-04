#백준 1167 트리의 지름
from sys import stdin, setrecursionlimit
input = stdin.readline
setrecursionlimit(1000000)
#임의의 노드에서 제일 먼 노드 -> 해당 노드로부터 모든 노드까지의 최댓값
n = int(input()) #노드 수

graph = [[] for _ in range(n+1)]

for i in range(n):
    given = list(map(int, input().split()))
    for j in range(1, len(given)-2, 2):
        graph[given[0]].append((given[j], given[j+1]))

result = 0
visit = [False for _ in range(n+1)]
maxnode = 1
def dfs(node, cost):
    global result, maxnode
    flag = False
    visit[node] = True
    for u, c in graph[node]:
        if visit[u] == False:
            flag = True
            dfs(u, cost + c)
    if flag == False: #더 내려가지 않았다 -> 리프
        if result < cost:
            maxnode = node #최장 노드 갱신
            result = cost
        
dfs(1, 0)
visit = [False for _ in range(n+1)]
dfs(maxnode, 0)

print(result)