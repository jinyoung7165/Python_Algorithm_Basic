import sys
from collections import defaultdict
from collections import deque

input = sys.stdin.readline

def main():
    n, m, v = map(int, input().split())

    graph = defaultdict(list)
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    for node in list(graph):
        graph[node] = sorted(graph[node])
        
        
    def dfs(v, visited = [v]):
        
        for node in graph[v]: #자식들
            if node not in visited:
                visited.append(node)
                dfs(node, visited)
        return visited
        
    def bfs(v):
        que = deque([])
        que.append(v)
        visited = [v]
        
        while que:
            a = que.popleft()
            for node in graph[a]:
                if node not in visited: 
                    visited.append(node)
                    que.append(node)
        return visited
                    
    print(*dfs(v))
    print(*bfs(v))

if __name__ == '__main__':
    main()
    