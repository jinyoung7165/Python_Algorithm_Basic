#Find the City With the Smallest Number of Neighbors at a Threshold Distance
#전체 노드를 출발지로 고려해야 할 때, i->i 비용이 0이라는 것 이용해 heapq에 삽입
class Solution: #제일 빠름
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        #비용 distanceThreshold안에 갈 수 있는 도착지 수가 최소인 출발지 중 번호 최대
        graph = defaultdict(list)
        result = -1
        for u, v, c in edges:
            if c > distanceThreshold: continue
            graph[u].append((v,c))
            graph[v].append((u,c))
        min_num = float('inf') #이전 출발지로부터 갈 수 있는 도착지 수
        for i in range(n): #i로부터 출발
            visited = set()
            que = []
            heapq.heappush(que, (0, i)) #i->i 비용 0 !!!!!!!!!!!!!!!!!!!!!!!1
            while que:
                cost, cur = heapq.heappop(que)
                if cost > distanceThreshold: break
                if cur in visited: continue
                visited.add(cur)
                for node, next_cost in graph[cur]:
                    if node in visited: continue
                    if next_cost + cost <= distanceThreshold:
                        heapq.heappush(que, (next_cost + cost, node))
            if min_num >= len(visited):
                min_num = len(visited)
                result = i
        return result

#메모리 효율 제일 좋음. dp. 플로이드워셜
class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], dt: int) -> int:
        dist = [[int(1e9)] * n for i in range(n)]
        
        for i, j, d in edges:
            dist[i][j] = dist[j][i] = d
        
        for i in range(n): #i->i 비용 0 추가
            dist[i][i] = 0
            
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]) #k거쳐 i->j 비교

        city_res = [[] for i in range(n)]
        city_min_cnt = int(1e9)
        
        for i in range(n):
            for j in range(n):
                if dist[i][j] <= dt: #모두 탐색해 가능한 비용이 나오면 각 출발지별 도착지 배열에 삽입
                    city_res[i].append(j)
                
            if len(city_res[i]):
                city_min_cnt = min(len(city_res[i]), city_min_cnt)
        
        res = []
        for i in range(n):
            if len(city_res[i]) == city_min_cnt:
                 res.append(i)
                
        return max(res)