#Merge k sorted lists
#k개의 정렬된 리스트를 1개의 정렬된 리스트로 병합해라
#Priority Queue -> python 내장모듈인 heapq 간단하게 import 해서 최소힙
#최대힙하려면 heappush할때 값에 -붙이면 됨 heappush(힙, (-값, 값))해서 힙[1]읽어오면 됨
import heapq
result = []
def mergeLists(lists = [[1,4,5], [1,3,4], [2,6]]):
    heap = []
    
    for i in range(len(lists)): #각 리스트별로 루트를 최소힙에 저장
        if lists[i]:
            heapq.heappush(heap, (lists[i][0], i, lists[i][1:]))
    
    while heap:
        node = heapq.heappop(heap)
        idx = node[1] #몇번째 리스트인지
        result.append(node[0])
        
        if node[2]:
            heapq.heappush(heap, (node[2][0], idx, node[2][1:]))


mergeLists()

print(result)