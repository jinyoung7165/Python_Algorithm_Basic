#K closest points to origin(0,0) 유클리드 거리
#거리 값이 작은 순대로 k개 추출 : 우선순위큐!!!!heapq
import heapq


def kClosest(self, points, k):
    heap = []
    for (x,y) in points:
        dist = x**2 + y**2
        heapq.heappush(heap, (dist, x, y))
    
    result = []
    for _ in range(k):
        (dist, x, y) = heapq.heappop(heap)
        result.append((x, y))
    return result