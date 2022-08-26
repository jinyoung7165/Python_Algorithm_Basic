#최소 비용 구하기
#N개의 도시(1-n). 두 도시 간 이동 버스 M개
#A->B 도시 버스 비용 최소화
#queue로 모든 간선의 누적 비교하면 -> 메모리 많이 잡아 먹음
#메모리 아끼려면 모든 노드에 대한 누적최소비용 저장해서 활용=> DP
#메모리 128MB제한
#heapq에 이미 추가된 불필요한 값이 다시 추가되어memory 에러가 난다.
#dist dict를 만들어?
# 거리가 갱신될 때만 거리를 갱신하고 넣어야 합니다.
import collections
from sys import maxsize, stdin
import heapq

input = stdin.readline

n = int(input()) #도시 개수
m = int(input()) #버스 개수
graph = collections.defaultdict(list) #[[] for i in range(n + 1)]
dp = [maxsize for _ in range(n+1)] #출발지는 하나 -> 누적 최소 비용을 1차원 배열에

for i in range(m):
    u, v, c = map(int, input().split()) #출발, 도착, 가격
    graph[u].append((v, c))
    
src, dest = map(int, input().split()) #시작점, 종점
que = [(0, src)] #가격, 시작점

while que: #0에서 각 노드까지의 누적 최소 비용
    cost, u = heapq.heappop(que) #누적 가격이 낮은 간선부터 택함
    if dp[u] < cost:#이미 최솟값이면 pass
        continue
    
    for v, c in graph[u]: #여기서 갈 수 있는 간선들
        sumcost = cost + c #이 노드를 경유했을 때 가격
        if sumcost < dp[v]: #경유한 게 더 싸면 갱신 가능
            dp[v] = sumcost
            heapq.heappush(que, (sumcost, v))
            
print(dp[dest])