#Path with Maximum Probability
from heapq import heappush, heappop
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        graph = self.build_graph(edges, succProb)
        seen = set()
        
        max_heap = [(-1, start)]
        
        while max_heap:
            prob, cur = heappop(max_heap)
			seen.add(cur)
            if cur == end:
                return -prob
            for neigh, p in graph.get(cur, []):
                if not neigh in seen:
                    new_prob = -1 * abs(prob*p)
                    heappush(max_heap, (new_prob, neigh))
					
		# No path from start to end
        return 0
    
    def build_graph(self, edges, succProb):
        graph = {}
        for i in range(len(edges)):
            cur_edge = edges[i]
            cur_prob = succProb[i]
            graph.setdefault(cur_edge[0], []).append((cur_edge[1], cur_prob))
            graph.setdefault(cur_edge[1], []).append((cur_edge[0], cur_prob))
        return graph