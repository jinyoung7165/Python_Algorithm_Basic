#Find the Town Judge
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
    #trust[i] = [ai, bi] a가 b를 믿는다
    #아무도 믿지 않는데 모두에게 신임받는 사람의 idx 출력
        graph = defaultdict(list)
        out = defaultdict(int)
        def dfs(node):
            for i in graph[node]:
                out[i] += 1

        for x, y in trust:
            graph[y].append(x)
        flag = -1
        for i in range(1, n+1):
            if len(graph[i]) != n-1: continue
            for j in graph[i]:
                dfs(j)
            if out[i] == 0: flag = i
        return flag
#공간 복잡도 줄여보자. trusted=n-1만큼. trust는 0. trust할 때마다 1을 빼자
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        graph = [0] * n+1
        for x, y in trust:
            graph[y] += 1
            graph[x] -= 1
        
        for i in range(1, n+1):
            if graph[i] == n-1:
                return i
        return -1