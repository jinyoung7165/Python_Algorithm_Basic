#Find the City With the Smallest Number of Neighbors at a Threshold Distance
class Solution:
    def findTheCity(self, count: int, edges: List[List[int]], cap: int) -> int:
        memo = collections.defaultdict(list)
        for i,j,z in edges:
            memo[i] += (j,z),
            memo[j] += (i,z),
        self.ans, self.minCity = -1, float('inf')
        def bfs(n):
            seen = {n:-1}
            q = collections.deque([(0, n)])
            while q:
                t, cur = q.popleft()
                for i,j in memo[cur]:
                    if (i not in seen or t + j < seen[i]) and t + j <= cap:
                        seen[i] = t + j
                        q += (t + j, i),
            total = len(seen)
            if total < self.minCity or total == self.minCity and n > self.ans:
                self.minCity, self.ans = total, n 
        for i in range(count):
            bfs(i)
        return self.ans