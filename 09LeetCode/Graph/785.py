#Is Graph Bipartite?
#무방향 그래프
#각 노드가 연결된 노드들 list주어짐
#이분 그래프면 true 리턴
# 인접한 정점끼리 서로 다른 색으로 칠해서 모든 정점을 두 가지 색으로만 칠할 수 있는 그래프
# BFS, DFS로 탐색하면서 정점을 방문할 때마다 두 가지 색 중 하나를 칠한다.
# 다음 정점을 방문하면서 자신과 인접한 정점은 자신과 다른 색으로 칠한다.
# 탐색을 진행할 때 자신과 인접한 정점의 색이 자신과 동일하면 이분 그래프가 아니다.
# 모든 정점을 다 방문했는데 위와 같은 경우가 없다면 이분 그래프이다.
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        queue = collections.deque()
        colors = [-1] * n

        for i in range(n):
            if colors[i] == -1: #방문하지 않은 노드
                colors[i] = 1 #color는 1또는 0
                queue.append(i)
                while queue:
                    node = queue.popleft()
                    for next in graph[node]:
                        if colors[next] == -1: #방문하지 않음
                            colors[next] = 1-colors[node] #현재 노드와 반대 color
                            queue.append(next)
                        elif colors[next] == colors[node]:
                            return False
        return True