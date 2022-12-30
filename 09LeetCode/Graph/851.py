#Loud and Rich
#richer = [[a,b]] a>b 부자
#quiet[i] i번째 사람의 quiet정도
#output[i] i번째 사람 이상의 재력 가진 사람 중 "가장 작은 quiet"가지는 사람
class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        graph = [[] for _ in range(n)]
        result = []
        for x, y in richer:
            graph[y].append(x) #y->x(더 rich한 쪽)
        
        def dfs(node): #현재 노드의 인덱스
            if not graph[node]: return node #out간선 더 이상 없으면 자신이 가장 rich
            
            min_quiet = node
            quietness = quiet[node]
            for next_node in graph[node]: #자기보다 rich한 사람
                candidate = dfs(next_node)
                if quietness > quiet[candidate]: #현재보다 quiet작으면 기록
                    min_quiet = candidate
                    quietness =  quiet[candidate]
            return min_quiet #rich한 사람 중 가장 작은 rich

        for i in range(n):
            result.append(dfs(i))
        
        return result
    
#시간 초과 해결  
class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        graph = [[] for _ in range(n)]
        for x, y in richer:
            graph[y].append(x) #y->x(더 rich한 쪽)
        
        result = [-1] * n
        def dfs(node):
            #least quiet person in this subtree
            if result[node] == -1: #아직 기록되지 않음
                result[node] = node #일단 자기자신. 현재 노드에 대한 min을 즉시 result[node]에 기록
                for child in graph[node]:
                    candidate = dfs(child)
                    if quiet[candidate] < quiet[result[node]]:
                        result[node] = candidate
            return result[node]#이미 기록된 노드는 탐색하지 않고 바로 리턴(여러 노드가 하나의 노드를 가리킬 수 있기 때문)

        for i in range(n):
            result[i] = dfs(i)
        return result