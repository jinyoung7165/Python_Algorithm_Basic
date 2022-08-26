#연결 요소의 개수
#방향 없는그래프가 주어졌을 때, 연결 요소 개수
import collections
import sys

sys.setrecursionlimit(1000000)
input = sys.stdin.readline
n, m = map(int, input().split()) #정점, 간선
graph = collections.defaultdict(list)
visited = [False] * n
count = 0

for i in range(m):
    u,v = map(int, input().split())
    graph[u-1].append(v-1)
    graph[v-1].append(u-1)

def dfs(node):
    if not visited[node]:
        visited[node] = True
        for i in graph[node]:
            if not visited[i]: dfs(i)
        return True
    
    return False
          
for i in range(n):
    if dfs(i) == True:
        count += 1
        
print(count)