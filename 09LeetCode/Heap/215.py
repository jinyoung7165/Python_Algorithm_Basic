#kth largest element in array
#정렬되지 않은 배열에서 k번째 큰 요소
#[3,2,3,1,2,4,5,5,6], k=4 -> 4
import heapq


def findKthLargest(nums, k):
    heap = list()
    for n in nums:
        heapq.heappush(heap, -n) #최대힙
    
    for _ in range(1, k): #k개만큼 제일 큰 원소들 빼라
        heapq.heappop(heap)
        
    return -heapq.heappop(heap)

def findKthLargest(nums, k):
    heapq.heapify(nums)
    
    for _ in range(len(nums) - k): #k개 남기고 작은 애들 빼라
        heapq.heappop(nums)
        
    return heapq.heappop(nums)

def findKthLargest(nums, k):
    return heapq.nlargest(k, nums)[-1] #k번째만큼 큰 값이 순서대로 리스트로 리턴. 가장 마지막 원소가 k번째 값

def findKthLargest(nums, k): #추가.삭제가 빈번할 때는 힙큐, 고정일 때는 정렬이 제일 빠르다
    return sorted(nums, reverse=True)[k-1] #큰값부터 정렬