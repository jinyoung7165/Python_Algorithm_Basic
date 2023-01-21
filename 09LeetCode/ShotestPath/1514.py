#Path with Maximum Probability
#start->end max prob값
#양방향 -> 갔던 길 다시 못가게 visited 체크
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        graph = defaultdict(list)
        for i, node in enumerate(edges):
            u, v = node[0], node[1]
            graph[u].append((v, succProb[i]))
            graph[v].append((u, succProb[i]))
        que = [(-1, start)] #최대힙(-cost)기준 정렬
        visited = set()
        while que:
            cost, cur = heapq.heappop(que)
            if cur == end: return -cost
            if cur in visited: continue
            visited.add(cur)

            for node, next_cost in graph[cur]:
                if node not in visited:
                    heapq.heappush(que, (-abs(cost*next_cost), node))
        return 0