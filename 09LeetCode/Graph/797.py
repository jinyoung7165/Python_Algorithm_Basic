# All Paths From Source to Target
# DFS <-> DP 생각해보기
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        @cache
        def f(i):
            if i == n-1:
                return [[n-1]]
            return [[i] + p for c in graph[i] for p in f(c)]
        return f(0)