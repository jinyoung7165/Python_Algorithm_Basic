#Redundant Connection-> 무방향 그래프. cycle 만드는 마지막 간선 찾아라
#multiple answers ->return the answer that occurs last in the input.
#union find 로 바꾸기 O(n)
class Solution(object):
    def findRedundantConnection(self, edges):
        graph = collections.defaultdict(list)
        result = []
        def dfs(u, v): #u->v 이동 가능하면 true
            if u not in visited:
                visited.add(u)
                if u == v: return True #연결된 unit일 때
                for next in graph[u]:
                    if dfs(next, v): return True
            return False
        
        # 두 노드 전에 이미 나왔고, 서로 연결된 unit일 때 result에 추가
        for x, y in edges:
            visited = set()
            if x in graph and y in graph and dfs(x, y):
                result.append([x,y])
            graph[x].append(y)
            graph[y].append(x)
        return result.pop() if result else []