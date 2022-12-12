#Loud and Rich
#richer = [[a,b]] a>b 부자
#quiet[i] i번째 사람의 quiet정도
#output[i] i번째 사람 이상의 재력 가진 사람 중 가장 작은 quiet가지는 사람
class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        graph = [[] for _ in range(n)]
        result = [[] for _ in range(n)]
        for x, y in richer:
            graph[y].append(x) #y->x(더 rich한 쪽)
        
        def dfs(node): #현재 노드의 인덱스
            if not graph[node]: return node #더 이상 없으면 자기자신
            #min_quiet = node #자기자신
            minimum = node
            for neighbour in graph[node]:
                candidate = dfs(neighbour)
                if quiet[minimum] > quiet[candidate]:
                    minimum = candidate 
            return minimum  
            

        for i in range(n):
            result.append(dfs(i))
        
        return result