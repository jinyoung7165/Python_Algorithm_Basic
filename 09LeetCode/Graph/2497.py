#Maximum Star Sum of a Graph
#A star graph is a subgraph of the given graph having a center node containing 0 or more neighbors. 
# = subset of edges of the given graph such that there exists a common node for all edges.
class Solution:
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:
        center_vals = defaultdict(list) #해당 center에 대한 결과

        if k == 0: return max(vals)

        for u, v in edges:
            if vals[v] > 0: #중심으로부터 1단계만 보면 됨(양수면 플러스)
                heapq.heappush(center_vals[u], vals[v])
                if len(center_vals[u]) > k: #최대 k개의 간선만 포함 가능
                    heapq.heappop(center_vals[u]) #제일 작은 거 뺌
            if vals[u] > 0:
                heapq.heappush(center_vals[v], vals[u])
                if len(center_vals[v]) > k:
                    heapq.heappop(center_vals[v])
        max_result = -float('inf')
        for i in range(len(vals)): #edges = [] 대비
            center_vals[i].append(vals[i]) #노드 자신 더함
            if sum(center_vals[i]) > max_result: 
                max_result = sum(center_vals[i])
        return max_result