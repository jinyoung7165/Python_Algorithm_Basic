#트리의 부모 찾기
import collections
import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline
n = int(input())
graph = collections.defaultdict(list)

for i in range(n-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [0] * (n+1)

def dfs(node): #부모->자식
    for i in graph[node]:
        if visited[i] == 0: #방문하지 않았을 때: 자식
            visited[i] = node 
            dfs(i) #자식의 자식 탐색
        
dfs(1) #1이 루트이기 때문에 이것만 호출해도 다 탐색 가능

for i in range(2, n+1):
    print(visited[i])